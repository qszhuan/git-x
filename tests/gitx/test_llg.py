import pytest

import mock
from gitx import Gitx
import utils

def test_llg_with_5_by_default():
    with mock.patch('gitx.call') as mock_call:
        mock_call.return_value = 0
        Gitx().llg()
        expected = 'git log --oneline -n {}'.format(5)
        mock_call.assert_called_once_with(expected)

def test_llg_with_n():
    with mock.patch('gitx.call') as mock_call:
        mock_call.return_value = 0
        n=10
        Gitx().llg(n)
        expected = 'git log --oneline -n {}'.format(n)
        mock_call.assert_called_once_with(expected)

def test_llg_with_negative():
    with pytest.raises(Exception) as e:
        n=-1
        Gitx().llg(n)
        expected = 'The commit count must be greater than zero.'
        assert e == expected