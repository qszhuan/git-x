import pytest

import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
grand_parentdir = os.path.dirname(parentdir)
sys.path.append(grand_parentdir)
import mock
import gitx


def test_git_a():
    pass