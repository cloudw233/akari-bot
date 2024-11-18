import os

import urllib3
from nio import AsyncClient, AsyncClientConfig

from core.config import config
from core.logger import Logger

homeserver = config('matrix_homeserver', cfg_type=str, table_name='bot_matrix')
user = config('matrix_user', cfg_type=str, table_name='bot_matrix')
device_id = config('matrix_device_id', cfg_type=str, secret=True, table_name='bot_matrix_secret')
device_name = config('matrix_device_name', cfg_type=str, secret=True, table_name='bot_matrix_secret')
token = config('matrix_token', cfg_type=str, secret=True, table_name='bot_matrix_secret')
megolm_backup_passphrase = config(
    'matrix_megolm_backup_passphrase',
    cfg_type=str,
    secret=True,
    table_name='bot_matrix_secret')

store_path = os.path.abspath('./matrix_store')
store_path_nio = os.path.join(store_path, 'nio')
store_path_megolm_backup = os.path.join(store_path, 'megolm_backup')

store_path_next_batch = os.path.join(store_path, 'next_batch.txt')

if homeserver and user and device_id and token:
    if not os.path.exists(store_path):
        os.mkdir(store_path)
    if not os.path.exists(store_path_nio):
        os.mkdir(store_path_nio)
    if megolm_backup_passphrase:
        if not os.path.exists(store_path_megolm_backup):
            os.mkdir(store_path_megolm_backup)
        if len(megolm_backup_passphrase) <= 10:
            Logger.warning("matrix_megolm_backup_passphrase is too short. It is insecure.")
    else:
        Logger.warning(
            f"Matrix megolm backup is not setup. It is recommended to set matrix_megolm_backup_passphrase to a unique passphrase.")

    if homeserver.endswith('/'):
        Logger.warning(f"The matrix_homeserver ends with a slash(/), and this may cause M_UNRECOGNIZED error.")
    homeserver_host = urllib3.util.parse_url(homeserver).host
    bot: AsyncClient = AsyncClient(homeserver,
                                   user,
                                   store_path=store_path_nio,
                                   config=AsyncClientConfig(store_sync_tokens=True))
    bot.restore_login(user, device_id, token)
    if bot.olm:
        Logger.info(f"Matrix E2E encryption support is available.")
    else:
        Logger.info(f"Matrix E2E encryption support is not available.")
else:
    bot = False
