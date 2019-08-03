import pytest
import mock
from utils import call

def test_call():
    command = 'ls'
    with mock.patch('subprocess.call') as mock_call:
        mock_call.return_value = 0
        call(command)
        expected = 'ls'
        mock_call.assert_called_once_with(expected)