import pytest

import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
grand_parentdir = os.path.dirname(parentdir)
sys.path.append(grand_parentdir)

@pytest.fixture
def mock_subprocess_call(monkeypatch):
    pass

def test_start(mock_subprocess_call):
    url = 'https://github.com'
    #start(url)