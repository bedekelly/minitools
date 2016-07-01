import requests

def url_replacer(url, replace=None):
    """A pointless function for testing which gets a URL, then (depending
    on the arguments passed to it) can replace a given substring of the
    response content with another substring."""
    response = requests.get(url)
    if replace:
        return response.content.replace(*replace)
    else:
        return response.content
