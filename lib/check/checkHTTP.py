import aiohttp
import asyncio

from .base import Base
from .utils import http_response


class CheckHTTP(Base):

    required = True
    type_name = 'http'

    @staticmethod
    async def run_check(uri, verify_ssl, timeout):
        start = asyncio.get_event_loop().time()
        aiohttp_timeout = aiohttp.ClientTimeout(total=timeout)
        if verify_ssl:
            verify_ssl = None  # None for default SSL check
        async with aiohttp.ClientSession(timeout=aiohttp_timeout) as session:
            async with session.get(uri, ssl=verify_ssl) as response:
                payload = None
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
        return {
            'name': itm.name,  # (str)
            'payload': itm.payload,  # (str)
            'responseTime': itm.response_time,  # (float, seconds)
            'statusCode': itm.status_code,  # (int, for example 200)
        }
