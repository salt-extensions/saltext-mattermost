import pytest
import salt.modules.test as testmod
import saltext.mattermost.modules.mattermost_mod as mattermost_module
import saltext.mattermost.states.mattermost_mod as mattermost_state


@pytest.fixture
def configure_loader_modules():
    return {
        mattermost_module: {
            "__salt__": {
                "test.echo": testmod.echo,
            },
        },
        mattermost_state: {
            "__salt__": {
                "mattermost.example_function": mattermost_module.example_function,
            },
        },
    }


def test_replace_this_this_with_something_meaningful():
    echo_str = "Echoed!"
    expected = {
        "name": echo_str,
        "changes": {},
        "result": True,
        "comment": f"The 'mattermost.example_function' returned: '{echo_str}'",
    }
    assert mattermost_state.exampled(echo_str) == expected
