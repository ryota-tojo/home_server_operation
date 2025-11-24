from dotenv import load_dotenv
import os

load_dotenv()

# ==============================================
# Docker関連設定
# ==============================================
DOCKER_CONTAINER_HOME=os.getenv("DOCKER_CONTAINER_HOME", "").split(",")


# ==============================================
# ngrok関連設定
# ==============================================
NGROK_PORT = os.getenv("NGROK_PORT")
NGROK_URL_LOGIN = os.getenv("NGROK_URL_LOGIN")
NGROK_URL_LOGIN_PARAM = os.getenv("NGROK_URL_LOGIN_PARAM")
NGROK_LINE_SEND_FLAG = os.getenv("NGROK_LINE_SEND_FLAG")


# ==============================================
# google関連設定
# ==============================================
G_SPRED_HOME_DB_SHEET_KEY = os.getenv("G_SPRED_HOME_DB_SHEET_KEY")
G_SPRED_HOME_DB_SHEET_NAME = os.getenv("G_SPRED_HOME_DB_SHEET_NAME")
G_SPRED_HOME_DB_KEY_NGROK_URL = os.getenv("G_SPRED_HOME_DB_KEY_NGROK_URL")
G_SPRED_HOME_DB_KEY_NGROK_URL_ACCESS_ERROR_FLAG = os.getenv("G_SPRED_HOME_DB_KEY_NGROK_URL_ACCESS_ERROR_FLAG")


# ==============================================
# LINE関連設定
# ==============================================
LINE_ACCESS_TOKEN_FOR_TEST = os.getenv("LINE_ACCESS_TOKEN_FOR_TEST")
LINE_SEND_ID_FOR_TEST = os.getenv("LINE_SEND_ID_FOR_TEST")
LINE_ACCESS_TOKEN_FOR_HOME_ADMIN = os.getenv("LINE_ACCESS_TOKEN_FOR_HOME_ADMIN")
LINE_SEND_ID_FOR_HOME_ADMIN = os.getenv("LINE_SEND_ID_FOR_HOME_ADMIN")
LINE_ACCESS_TOKEN_FOR_HOME = os.getenv("LINE_ACCESS_TOKEN_FOR_HOME")
LINE_SEND_ID_FOR_HOME = os.getenv("LINE_SEND_ID_FOR_HOME")

