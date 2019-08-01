if(Test-Path "build"){
    write-host "Clean build dir........." -f green
    rm -Recurse -Force build
    rm -Force dist/gity*.whl
}

write-host "Build package............." -f green
python .\setup.py bdist_wheel 
write-host "Install package..........." -f green

$whl = Get-Item dist/gity*.whl | Select-Object -first 1 -ExpandProperty Name
pip install .\dist\$whl --upgrade