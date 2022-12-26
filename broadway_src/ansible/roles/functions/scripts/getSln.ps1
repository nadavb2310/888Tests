$file = Get-ChildItem "$env:WORKSPACE\$env:slnLocation" | Where-Object {$_.Name -match "^$env:slnPattern$"}
If ($file.Name -eq $null){
    Write-Host "The requested file pattern was not found."
    return "ERROR"
}
return $file.Name