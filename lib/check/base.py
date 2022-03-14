import asyncio
import logging

DEFAULT_TIMEOUT = 10


class Base:
    interval = 300
    required = False

    @classmethod
    async def run(cls, data, asset_config=None):
        try:
            # If asset_id is needed in future; uncomment next line:
            # asset_id = data['hostUuid']
            config = data['hostConfig']['probeConfig']['httpProbe']
            URI = config['URI']  # TODO uri in capital letters?
            timeout = config.get('timeout', DEFAULT_TIMEOUT)
            ssl = config.get('ssl', False)
            interval = data.get('checkConfig', {}).get('metaConfig', {}).get(
                'checkInterval')
            assert interval is None or isinstance(interval, int)
        except Exception as e:
            logging.error(f'invalid check configuration: `{e}`')
            return

        try:
            state_data = cls.get_data(URI, ssl, timeout)
        except asyncio.TimeoutError:
            raise Exception('Check timed out.')
        except Exception as e:
            raise Exception(f'Check error: {e.__class__.__name__}: {e}')
        else:
            return state_data

    @classmethod
    async def get_data(cls, URI, ssl, timeout):
        data = None
        try:
            data = await cls.run_check(URI, ssl, timeout)
        except Exception as err:
            logging.exception(f'HTTP error: `{err}`\n')
            raise

        try:
            state = cls.get_result(data)
        except Exception:
            logging.exception('HTTP parse error\n')
            raise

        return state

    @staticmethod
    async def run_check(URI, ssl, timeout):
        pass

    @staticmethod
    def on_item(itm):
        return itm

    @classmethod
    def get_result(cls, data):
        itm = cls.on_item(data)
        state = {}
        state[cls.type_name] = {}
        name = itm['name']
        state[cls.type_name][name] = itm
        return state
