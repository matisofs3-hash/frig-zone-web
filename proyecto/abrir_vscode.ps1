# Abre el proyecto en VS Code
# Uso: doble clic o powershell -ExecutionPolicy Bypass -File abrir_vscode.ps1

$ErrorActionPreference = "Stop"

$candidatos = @(
    (Join-Path $PSScriptRoot "sitio-web"),
    (Join-Path $PSScriptRoot "frigzone-web"),
    $PSScriptRoot
)

$proyecto = $null
foreach ($c in $candidatos) {
    if (Test-Path (Join-Path $c "index.html")) { $proyecto = $c; break }
}

if (-not $proyecto) {
    Write-Host "No encontre index.html cerca de este script." -ForegroundColor Red
    Read-Host "Enter para salir"
    exit 1
}

$code = "C:\Users\Familia\AppData\Local\Programs\Microsoft VS Code\Code.exe"
if (-not (Test-Path $code)) {
    Write-Host "No encuentro VS Code en $code" -ForegroundColor Red
    Read-Host "Enter para salir"
    exit 1
}

Write-Host "Abriendo: $proyecto" -ForegroundColor Cyan
Start-Process -FilePath $code -ArgumentList "--new-window", "`"$proyecto`""
Write-Host "Listo. Si no se abrio, abri VS Code y usa Archivo > Abrir carpeta." -ForegroundColor Green
Start-Sleep -Seconds 2
