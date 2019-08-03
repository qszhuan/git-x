param(
[Parameter(Mandatory)]
[ValidateSet('pypi', 'test')]
[string] $where
)

if($where -eq 'pypi'){
    $url = "https://pypi.org/legacy/"
}
if($where -eq 'test'){
    $url = "https://test.pypi.org/legacy/"
}

twine upload dist/*.whl  --repository-url=$url