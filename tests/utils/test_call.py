import pytest

import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
grand_parentdir = os.path.dirname(parentdir)
sys.path.append(grand_parentdir)
import mock
from utils import call


def test_start(mock_platform, extected_command):
        url = 'https://github.com'
        with mock.patch('subprocess.call') as mock_call:
            mock_call.return_value = 0
            start(url)
            expected = '{} {}'.format(extected_command, url)
            subprocess.call.assert_called_once_with(expected)