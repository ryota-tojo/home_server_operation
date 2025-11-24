# ライブラリ
import sys

# 共通部品
from projects.src.common.utils import logger as log
from projects.src.common.google import spread_sheet
from projects.src.common.ngrok.ngrok import stop
from projects.src.common.utils import get_path as gpath

# 設定
from projects.conf import config

# 処理
log.start(__file__)

# スプレッドシート連携 - エラー連携フラグ取得
ngrok_url_access_error_send_flag = spread_sheet.get(
    f"{gpath.spread_sheet_auth_dir()}\\home_database\\auth.json",
    config.G_SPRED_HOME_DB_SHEET_KEY,
    config.G_SPRED_HOME_DB_SHEET_NAME,
    config.G_SPRED_HOME_DB_KEY_NGROK_URL_ACCESS_ERROR_FLAG
)

if ngrok_url_access_error_send_flag == "FALSE":
    log.general(__file__, "INFO", f"ngrokURLが有効のため処理をスキップします")
    sys.exit()

stop()

log.end(__file__)
