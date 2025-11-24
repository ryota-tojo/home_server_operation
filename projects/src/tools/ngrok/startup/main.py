# ライブラリ
import sys
from pathlib import Path

# 設定
from projects.conf import config

# 共通部品
from projects.src.common.utils import logger as log
from projects.src.common.ngrok.ngrok import create
from projects.src.common.google import spread_sheet
from projects.src.common.line.line import send_line as line
from projects.src.common.utils import get_path as gpath

# 処理
log.start(__file__)

# 親フォルダ取得
current_file = Path(__file__)
parent_folder = current_file.parent

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

# ngrokURL生成
ngrok_url = f"{create(config.NGROK_PORT)}/{config.NGROK_URL_LOGIN}{config.NGROK_URL_LOGIN_PARAM}"

# スプレッドシート連携
send_sheet_ngrok_url_result = spread_sheet.insert(
    f"{gpath.spread_sheet_auth_dir()}\\home_database\\auth.json",
    config.G_SPRED_HOME_DB_SHEET_KEY,
    config.G_SPRED_HOME_DB_SHEET_NAME,
    config.G_SPRED_HOME_DB_KEY_NGROK_URL,
    ngrok_url
)

# LINE通知
line_msg = f"【ngrokURL 発行通知】\n{log.time_stamp('%Y/%m/%d %H:%M:%S ')}\n{ngrok_url}"
if config.NGROK_LINE_SEND_FLAG:
    send_line_flag = line(config.LINE_ACCESS_TOKEN_FOR_HOME, config.LINE_SEND_ID_FOR_HOME, line_msg)
else:
    print(line_msg)

log.end(__file__)