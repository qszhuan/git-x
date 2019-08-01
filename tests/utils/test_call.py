import pytest

import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
grand_parentdir = os.path.dirname(parentdir)
sys.path.append(grand_parentdir)
import mock
from utils import call

def test_call():
    command = 'ls'
    with mock.patch('subprocess.call') as mock_call:
        mock_call.return_value = 0
        call(command)
        expected = 'ls'
        mock_call.assert_called_once_with(expected)