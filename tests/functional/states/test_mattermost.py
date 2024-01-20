import pytest

pytestmark = [
    pytest.mark.requires_salt_states("mattermost.exampled"),
]


@pytest.fixture
def mattermost(states):
    return states.mattermost


def test_replace_this_this_with_something_meaningful(mattermost):
    echo_str = "Echoed!"
    ret = mattermost.exampled(echo_str)
    assert ret.result
    assert not ret.changes
    assert echo_str in ret.comment
