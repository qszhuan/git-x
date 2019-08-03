from gitx import Gitx
import mock

@mock.patch('gitx.call', return_value=0)
def test_st(mock_call):
    Gitx().st()
    mock_call.assert_called_once_with('git status')