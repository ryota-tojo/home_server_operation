# ライブラリ
from linebot import LineBotApi
from linebot.models import TextSendMessage

# 共通部品
from projects.src.common.utils import logger as log
from projects.src.common.utils import param


def send_line(access_token, send_id, msg_text):
    param_key = ["access_token", "send_id"]
    param_value = [access_token, send_id]
    params = param.create(param_key, param_value)
    log.general(__file__, "INFO", f"メッセージをLINEに連携します param={params}")

    try:
        line_bot_api = LineBotApi(access_token)
        message = TextSendMessage(text=msg_text)
        line_bot_api.push_message(send_id, message)
        log.general(__file__, "INFO", f"メッセージを連携しました")
        return True

    except Exception as e:
        log.general(__file__, "ERROR", f"メッセージの連携に失敗しました error={e}")
        return False
