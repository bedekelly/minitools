import requests
from minitools.mock import Mock
from minitools.patch import patch
from minitools.test import case, tests

from example_module import url_replacer


@case
def test_gets_normal_url(t):
    # Create a mocked 'requests'.
    patched_requests = Mock(spec=requests)

    # Create a mocked 'requests.get'.
    patched_get = Mock(spec=requests.get)
    patched_requests.get = patched_get

    # Create and set a mocked Response to return.
    patched_response = Mock()
    patched_response.content = "Dummy response content!"
    patched_get.return_value = patched_response

    # Patch requests, and check that we get back our dummy content:
    with patch("example_module.urlgetter.requests", patched_requests) as get:
        t.check_equal(url_replacer("dummy.url"), "Dummy response content!")


@case
def test_replaces_url(t):
    # Create a mocked 'requests'
    patched_requests = Mock(spec=requests)

    # Create a mocked 'requests.get'.
    patched_get = Mock(spec=requests.get)
    patched_requests.get = patched_get

    # Create and set a patched response to return.
    patched_response = Mock()
    patched_response.content = "ABC"
    patched_get.return_value = patched_response

    # Patched requests, and check that we get back our *altered* dummy content.
    with patch("example_module.urlgetter.requests", patched_requests):
        result = url_replacer("dummy.url", ("A", "B"))
        t.check_equal(result, "BBC")


@case
def test_raises_for_non_strings(t):
    t.check_raises(lambda: url_replacer(None), BaseException)


tests.run_all()
