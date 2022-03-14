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
        async with aiohttp.ClientSession(
            ssl=verify_ssl,
            timeout=aiohttp_timeout
        ) as session:
            async with session.get(uri) as response:
                payload = None
                try:
                    payload = await response.text('UTF-8')  # str
                except UnicodeDecodeError:
                    payload = await response.read()  # bytes

                return http_response(
                    name=uri,
                    payload=payload,
                    response_time=asyncio.get_event_loop().time() - start,
                    status_code=response.status
                )

    @staticmethod
    def on_item(itm):
        return {
            'name': itm.uri,  # (str)
            'payload': itm.payload,  # (str, if not UTF-8, return BLOB)
            'responseTime': itm.response_time,  # (float, seconds)
            'statusCode': itm.status_code,  # (int, for example 200)
        }