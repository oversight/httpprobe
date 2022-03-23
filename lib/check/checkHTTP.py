import aiohttp
import asyncio

from .base import Base
from .utils import http_response


class CheckHTTP(Base):

    required = True
    type_name = 'http'

    @staticmethod
    async def run_check(uri, verify_ssl, with_payload, timeout):
        start = asyncio.get_event_loop().time()
        aiohttp_timeout = aiohttp.ClientTimeout(total=timeout)
        if verify_ssl:
            verify_ssl = None  # None for default SSL check
        async with aiohttp.ClientSession(timeout=aiohttp_timeout) as session:
            async with session.get(uri, ssl=verify_ssl) as response:
                payload = None
                if with_payload:
                    try:
                        payload = await response.text('UTF-8')  # str
                    except UnicodeDecodeError:
                        payload = '<BLOB>'

                return http_response(
                    name=uri,
                    payload=payload,
                    response_time=asyncio.get_event_loop().time() - start,
                    status_code=response.status
                )

    @staticmethod
    def on_item(itm):
        data = {
            'name': itm.name,  # (str)
            'responseTime': itm.response_time,  # (float, seconds)
            'statusCode': itm.status_code,  # (int, for example 200)
        }

        if isinstance(itm.payload, str):
            data['payload'] = itm.payload

        return data
