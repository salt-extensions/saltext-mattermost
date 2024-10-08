"""
Library for interacting with Mattermost Incoming Webhooks
"""

import http.client
import logging
import urllib.parse

import salt.utils.http
from salt.version import __version__

log = logging.getLogger(__name__)


def query(hook=None, api_url=None, data=None):
    """
    Mattermost object method function to construct and execute on the API URL.

    :param api_url:     The Mattermost API URL
    :param hook:        The Mattermost hook.
    :param data:        The data to be sent for POST method.
    :return:            The json response from the API call or False.
    """
    method = "POST"

    ret = {"message": "", "res": True}

    base_url = urllib.parse.urljoin(api_url, "/hooks/")
    url = urllib.parse.urljoin(base_url, str(hook))

    result = salt.utils.http.query(url, method, data=data, decode=True, status=True)

    if result.get("status", None) == http.client.OK:
        ret["message"] = f"Message posted {data} correctly"
        return ret
    if result.get("status", None) == http.client.NO_CONTENT:
        return True
    log.debug(url)
    log.debug(data)
    log.debug(result)
    if "dict" in result:
        _result = result["dict"]
        if "error" in _result:
            ret["message"] = result["error"]
            ret["res"] = False
            return ret
        ret["message"] = "Message not posted"
    else:
        ret["message"] = "invalid_auth"
        ret["res"] = False
    return ret
