# Publica el sitio en GitHub y activa GitHub Pages
# Requisito: cargar un token con permisos "repo" en la variable GH_TOKEN
#
#   $env:GH_TOKEN = "ghp_..."
#   powershell -ExecutionPolicy Bypass -File publicar_github.ps1
#
# El token NO se guarda en el repo ni en el remote.

param(
    [string]$RepoName = "frigzone-web",
    [switch]$Pages = $true
)

$ErrorActionPreference = "Stop"

$token = $env:GH_TOKEN
if (-not $token) { $token = [Environment]::GetEnvironmentVariable("GH_TOKEN", "User") }
if (-not $token) { $token = [Environment]::GetEnvironmentVariable("GH_TOKEN", "Machine") }
if (-not $token) {
    Write-Host ""
    Write-Host "Falta el token de GitHub." -ForegroundColor Yellow
    Write-Host "1. Entra a https://github.com/settings/tokens"
    Write-Host "2. Generate new token (classic) con scope 'repo'"
    Write-Host "3. En PowerShell:  `$env:GH_TOKEN = `"ghp_tu_token`""
    Write-Host "4. Volve a ejecutar este script."
    Write-Host ""
    Read-Host "Enter para salir"
    exit 1
}

# Detectar proyecto y git
$proyecto = $null
foreach ($c in @((Join-Path $PSScriptRoot "sitio-web"), (Join-Path $PSScriptRoot "frigzone-web"), $PSScriptRoot)) {
    if (Test-Path (Join-Path $c "index.html")) { $proyecto = $c; break }
}
if (-not $proyecto) { throw "No encontre el proyecto (index.html)" }

$git = "C:\Users\Familia\Documents\deepseek-harness\default-workspace\_tools\mingit\cmd\git.exe"
if (-not (Test-Path $git)) {
    $git = (Get-Command git -ErrorAction SilentlyContinue).Source
}
if (-not $git) { throw "No encontre git.exe" }

$headers = @{
    Authorization          = "Bearer $token"
    Accept                 = "application/vnd.github+json"
    "User-Agent"           = "frigzone-deploy"
    "X-GitHub-Api-Version" = "2022-11-28"
}

Write-Host "Verificando token..." -ForegroundColor Cyan
$user = Invoke-RestMethod -Uri "https://api.github.com/user" -Headers $headers
Write-Host "Usuario: $($user.login)" -ForegroundColor Green

Write-Host "Creando repositorio $RepoName..." -ForegroundColor Cyan
$body = @{
    name        = $RepoName
    private     = $false
    description = "Sitio web de Frig Zone - refrigeracion y climatizacion en CABA"
    has_issues  = $true
} | ConvertTo-Json

try {
    Invoke-RestMethod -Method Post -Uri "https://api.github.com/user/repos" -Headers $headers -Body $body -ContentType "application/json" | Out-Null
    Write-Host "Repositorio creado." -ForegroundColor Green
} catch {
    Write-Host "El repo ya existe o no se pudo crear. Sigo con el push." -ForegroundColor Yellow
}

Write-Host "Configurando remote..." -ForegroundColor Cyan
& $git -C $proyecto remote remove origin 2>$null
& $git -C $proyecto remote add origin "https://github.com/$($user.login)/$RepoName.git"

Write-Host "Subiendo main..." -ForegroundColor Cyan
& $git -C $proyecto -c "http.extraheader=AUTHORIZATION: bearer $token" push -u origin main

if ($LastExitCode -ne 0) {
    Write-Host "El push fallo. Revisa el token y los permisos." -ForegroundColor Red
    Read-Host "Enter para salir"
    exit 1
}

$repoUrl = "https://github.com/$($user.login)/$RepoName"
Write-Host "Repo: $repoUrl" -ForegroundColor Green

if ($Pages) {
    Write-Host "Activando GitHub Pages..." -ForegroundColor Cyan
    $pagesBody = @{ source = @{ branch = "main"; path = "/" } } | ConvertTo-Json
    try {
        Invoke-RestMethod -Method Post -Uri "https://api.github.com/repos/$($user.login)/$RepoName/pages" -Headers $headers -Body $pagesBody -ContentType "application/json" | Out-Null
        Write-Host "Pages activado." -ForegroundColor Green
    } catch {
        Write-Host "No se pudo activar Pages por API. Hacelo a mano: Settings > Pages > Deploy from branch > main / root." -ForegroundColor Yellow
    }
    Start-Sleep -Seconds 3
    Write-Host "Sitio (tarda 1-2 minutos): https://$($user.login).github.io/$RepoName/" -ForegroundColor Cyan
}

Write-Host ""
Write-Host "Listo." -ForegroundColor Green
Read-Host "Enter para salir"
