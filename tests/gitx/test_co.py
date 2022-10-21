import mock

from gitx import Gitx


@mock.patch('gitx.call', return_value=0)
def test_co(mock_call):
    Gitx().co("master")
    mock_call.assert_called_once_with('git checkout master')


@mock.patch('gitx.call', return_value=0)
def test_co_create_if_not_exist(mock_call):
    Gitx().co("master", create_if_not_existed=True)
    mock_call.assert_called_once_with('git checkout -b master')


@mock.patch('gitx.call', return_value=0)
def test_co_create_if_not_exist_with_start_point(mock_call):
    Gitx().co("master", 'c1ff877', create_if_not_existed=True)
    mock_call.assert_called_once_with('git checkout -b master c1ff877')


@mock.patch('gitx.call', return_value=0)
def test_co_ignore_start_point_if_not_create_new(mock_call):
    Gitx().co("master", 'c1ff877', create_if_not_existed=False)
    mock_call.assert_called_once_with('git checkout master')


@mock.patch('gitx.popen')
@mock.patch('gitx.call', return_value=0)
def test_co_with_partial_local_branch_name_but_unique(mock_call, mock_popen):
    mock_popen.side_effect = lambda x: 'abc\n  click\n* master\n' if x == 'git branch' else (
        'origin/HEAD -> origin/master \n origin/master \n' if x == 'git branch -r' else 0)
    branch = Gitx().co("ab")
    mock_call.assert_called_once_with('git checkout abc')
    assert branch == 'abc'

@mock.patch('gitx.popen')
@mock.patch('gitx.call', return_value=0)
def test_co_with_partial_remote_branch_name_but_unique(mock_call, mock_popen):
    mock_popen.side_effect = lambda x: 'abc\n  click\n* master\n' if x == 'git branch' else (
        'origin/HEAD -> origin/master \n origin/master \n origin/test' if x == 'git branch -r' else 0)
    branch = Gitx().co("tes")
    mock_call.assert_called_once_with('git checkout test')
    assert branch == 'test'


@mock.patch('gitx.popen')
@mock.patch('gitx.call', return_value=0)
def test_co_with_exactly_matched_branch_name_forcely(mock_call, mock_popen):
    mock_popen.side_effect = lambda x: 'abc\n  click\n* master\n master2\n' if x == 'git branch' else (
        'origin/HEAD -> origin/master \n origin/master \n' if x == 'git branch -r' else 0)
    Gitx().co("master", force=True)
    mock_call.assert_called_once_with('git checkout master')


@mock.patch('gitx.print_prompt', return_value=0)
@mock.patch('gitx.popen')
@mock.patch('gitx.call', return_value=0)
def test_co_with_partial_branch_name_but_not_unique(mock_call, mock_popen, _):
    mock_popen.side_effect = lambda x: 'abc\n  click\n* master\n' if x == 'git branch' else (
        'origin/HEAD -> origin/master \n origin/master \n' if x == 'git branch -r' else 0)
    Gitx().co("a")
    mock_call.assert_called_once_with('git checkout abc')


@mock.patch('gitx.print_prompt', return_value=1)
@mock.patch('gitx.popen')
@mock.patch('gitx.call', return_value=0)
def test_co_with_partial_branch_name_but_not_unique_2(mock_call, mock_popen, _):
    mock_popen.side_effect = lambda x: 'abc\n  click\n* master\n' if x == 'git branch' else (
        '  origin/HEAD -> origin/master \n origin/master \n' if x == 'git branch -r' else 0)
    Gitx().co("a")
    mock_call.assert_called_once_with('git checkout master')

@mock.patch('gitx.print_prompt', return_value=1)
@mock.patch('gitx.popen')
@mock.patch('gitx.call', return_value=0)
def test_co_with_dot_as_the_branch_name(mock_call, mock_popen, _):
    mock_popen.side_effect = lambda x: 'a.b.c\n  click\n* master\n' if x == 'git branch' else (
        'origin/HEAD -> origin/master \n origin/master \n' if x == 'git branch -r' else 0)
    Gitx().co(".")
    mock_call.assert_called_once_with('git checkout .')