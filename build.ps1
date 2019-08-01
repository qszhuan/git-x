param(
    #Install flag
    [switch]$i = $false
)
if(Test-Path "build"){
    write-host "Clean build dir........." -f green
    rm -Recurse -Force build
    rm -Force dist/git*.whl
}

write-host "Build package............." -f green
python .\setup.py bdist_wheel 

if($i){
    write-host "Install package..........." -f green
    $whl = Get-Item dist\git*.whl | Select-Object -first 1 -ExpandProperty Name
    pip install .\dist\$whl --upgrade
}
