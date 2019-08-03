from gitx import Gitx
import mock

def test_p():
    with mock.patch('gitx.call') as mock_call:
        mock_call.return_value = 0 
        Gitx().p()
        mock_call.assert_called_once_with('git pull --rebase')