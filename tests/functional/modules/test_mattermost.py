import pytest

pytestmark = [
    pytest.mark.requires_salt_modules("mattermost.example_function"),
]


@pytest.fixture
def mattermost(modules):
    return modules.mattermost


def test_replace_this_this_with_something_meaningful(mattermost):
    echo_str = "Echoed!"
    res = mattermost.example_function(echo_str)
    assert res == echo_str
