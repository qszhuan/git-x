if(Test-Path "build"){
    write-host "Clean build dir........." -f green
    rm -Recurse -Force build
}

write-host "Build package............." -f green
python .\setup.py bdist_wheel 
write-host "Install package..........." -f green
pip install .\dist\Gity-1.0.0.dev0-py2.py3-none-any.whl --upgrade