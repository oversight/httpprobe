from collections import namedtuple

from urllib.parse import urlparse


def http_response(name, payload, response_time, status_code):
    HTTPResponse = namedtuple(
        'HTTPResponse',
        ['name', 'payload', 'response_time', 'status_code'])
    return HTTPResponse(name, payload, response_time, status_code)


def check_config(uri):
    o = urlparse(uri)
    if o.scheme not in ('http', 'https'):
        raise Exception(f'uri should start with "http" or "https", got: {uri}')
