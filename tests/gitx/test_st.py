from gitx import Gitx
import mock

def test_st():
    with mock.patch('gitx.call') as mock_call:
        mock_call.return_value = 0 
        Gitx().st()
        mock_call.assert_called_once_with('git status')