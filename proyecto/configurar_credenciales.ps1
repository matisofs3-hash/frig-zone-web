# Guarda las credenciales como variables de USUARIO (no en el repo)
# Uso: powershell -ExecutionPolicy Bypass -File configurar_credenciales.ps1
#
# Los tokens quedan en el registro de tu usuario. No se escriben en el proyecto.
# Para borrarlos:
#   [Environment]::SetEnvironmentVariable("GH_TOKEN", $null, "User")

$ErrorActionPreference = "Stop"

function Leer-Secreto($prompt) {
    $s = Read-Host $prompt -AsSecureString
    if ($s.Length -eq 0) { return $null }
    return [System.Net.NetworkCredential]::new("", $s).Password
}

Write-Host ""
Write-Host "=== Credenciales de Frig Zone ===" -ForegroundColor Cyan
Write-Host "Enter para omitir cada una. No se muestran en pantalla." -ForegroundColor DarkGray
Write-Host ""

$gh = Leer-Secreto "Token de GitHub (scope repo o fine-grained)"
if ($gh) {
    [Environment]::SetEnvironmentVariable("GH_TOKEN", $gh, "User")
    Write-Host "  GH_TOKEN guardado." -ForegroundColor Green
}

$fb = Leer-Secreto "Token de pagina de Facebook (pages_manage_posts)"
if ($fb) {
    [Environment]::SetEnvironmentVariable("FB_TOKEN", $fb, "User")
    Write-Host "  FB_TOKEN guardado." -ForegroundColor Green
}

$page = Read-Host "ID de la pagina de Facebook (solo numeros)"
if ($page) {
    [Environment]::SetEnvironmentVariable("FB_PAGE_ID", $page, "User")
    Write-Host "  FB_PAGE_ID guardado." -ForegroundColor Green
}

Write-Host ""
Write-Host "Listo. Cerrá y volvé a abrir PowerShell para que las tome." -ForegroundColor Cyan
Write-Host "Después avisame y ejecuto la publicación." -ForegroundColor Cyan
Read-Host "Enter para salir"
