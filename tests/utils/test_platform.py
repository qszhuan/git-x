import pytest
import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
grand_parentdir = os.path.dirname(parentdir)
sys.path.append(grand_parentdir)

from utils import *

def test_is_windows(monkeypatch):
    mock =  'win32'
    monkeypatch.setattr(sys, 'platform', mock)
    assert Platform.is_windows() == True
    assert Platform.is_mac() == False
    assert Platform.is_linux() == False
    assert Platform.is_cygwin() == False

def test_is_mac(monkeypatch):
    mock =  'darwin'
    monkeypatch.setattr(sys, 'platform', mock)
    assert Platform.is_windows() == False
    assert Platform.is_mac() == True
    assert Platform.is_linux() == False
    assert Platform.is_cygwin() == False

def test_is_linux(monkeypatch):
    mock =  'linux'
    monkeypatch.setattr(sys, 'platform', mock)
    assert Platform.is_windows() == False
    assert Platform.is_mac() == False
    assert Platform.is_linux() == True
    assert Platform.is_cygwin() == False

def test_is_cygwin(monkeypatch):
    mock =  'cygwin'
    monkeypatch.setattr(sys, 'platform', mock)
    assert Platform.is_windows() == False
    assert Platform.is_mac() == False
    assert Platform.is_linux() == False
    assert Platform.is_cygwin() == True
