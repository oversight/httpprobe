from collections import namedtuple


def http_response(name, payload, response_time, status_code, certificate=None):
        HTTPResponse = namedtuple(
            'HTTPResponse',
            ['certificate', 'name', 'payload', 'response_time', 'status_code'])
        return HTTPResponse(
            certificate, name, payload, response_time, status_code)