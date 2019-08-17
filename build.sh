
echo "Clean ..."
rm -rf build
rm -rf dist/git*.whl

echo "Build package ..."
python setup.py bdist_wheel

echo "install ..."
a="$(ls dist/*.whl)"
pip install "${a}" --upgrade
