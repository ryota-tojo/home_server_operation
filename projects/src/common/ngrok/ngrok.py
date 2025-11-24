# ライブラリ
import subprocess
import os
import sys
import time
import shutil

# 共通部品
from projects.src.common.utils.logger import time_stamp as ts
from projects.src.common.utils.file_control import get_file_to_target_row as get_file
from projects.src.common.utils import get_path as gpath
from projects.src.common.utils import logger as log


# 設定ファイル
from projects.src.common.ngrok.conf import ngrok_conf

def create(port):
    log.general(__file__,"INFO",f"ngrokURLを生成します port={port}")

    # 実行中ファイルの親ディレクトリ取得
    exe_file = os.path.abspath(__file__)
    working_dir = os.path.abspath(os.path.join(exe_file, os.pardir))

    # ngrok.exeまでのパスを取得
    ngrok_app_path=f"{gpath.application_dir(False)}\\ngrok"

    ngrok_path = os.path.join(ngrok_app_path, "ngrok.exe")
    log.general(__file__,"INFO",f"ngrok.exeファイルパス path={ngrok_path}")

    try:

        # ngrok強制終了
        log.general(__file__,"INFO",f"ngrok強制終了中...")
        subprocess.run(
            f'powershell -Command "Get-Process | Where-Object {{$_.Path -eq \'{ngrok_path}\'}} | Stop-Process -Force"',
            shell=True
        )
        log.general(__file__,"INFO",f"ngrokを強制終了しました")

        # ログディレクトリ作成
        logdir_path = f"{working_dir}\\{ngrok_conf.LOG_DIR}"
        log.general(__file__,"INFO",f"ログディレクトリを作成します path={logdir_path}")
        if not os.path.isdir(logdir_path):
            os.makedirs(logdir_path)
            log.general(__file__,"INFO",f"ログディレクトリを作成しました path={logdir_path}")
        else:
            shutil.rmtree(logdir_path)
            log.general(__file__,"INFO",f"ログディレクトリを削除しました path={logdir_path}")
            os.makedirs(logdir_path)
            log.general(__file__,"INFO",f"ログディレクトリを作成しました path={logdir_path}")
        logfile_path = f"{logdir_path}{ngrok_conf.LOG_FILE}"

        # ngrokをバッググラウンドで実行
        log.general(__file__,"INFO",f"ngrok起動中...")
        cmd = f'"{ngrok_path}" http {port} --log=stdout > .\\{ngrok_conf.LOG_DIR}{ngrok_conf.LOG_FILE} 2>&1'
        process = subprocess.Popen(cmd, shell=True, cwd=working_dir)

        # ngrok起動エラー検知
        time.sleep(5)
        if process.poll() is not None:
            error_code = get_file(logfile_path, ngrok_conf.ERROR_WORD)
            log.general(__file__,"ERROR",f"ngrokの起動に失敗しました error_code={error_code}, log={logfile_path}")
            log.general(__file__,"INFO",f"処理を強制終了します")
            sys.exit()

        # urlが出力されるまで待機
        log.general(__file__,"INFO",f"ngrokURL取得中...")
        time.sleep(1)
        found_line = get_file(logfile_path, ngrok_conf.TARGET_WORD)

        # TARGET_WORD を含む行を確認
        if not found_line or not found_line.strip():
            log.general(__file__,"ERROR",f"ngrokURLの取得に失敗しました")
            log.general(__file__,"INFO",f"処理を強制終了します")
            sys.exit()

        parts = found_line.split(" ")
        url_parts = [p for p in parts if p.startswith("url")]
        ngrok_url = url_parts[0].replace("url=","")

        log.general(__file__,"INFO",f"ngrokURLを取得しました url={ngrok_url}")
        return ngrok_url

    except Exception as e:
        log.general(__file__,"ERROR",f"例外エラーが発生しました error={e}")
        log.general(__file__,"INFO",f"処理を強制終了します")
        sys.exit()


def stop():
    try:
        print(ts() + "処理開始")

        # ngrok.exeまでのパスを取得
        ngrok_app_path=f"{gpath.application_dir(False)}\\ngrok"

        ngrok_path = os.path.join(ngrok_app_path, "ngrok.exe")
        log.general(__file__,"INFO",f"ngrok.exeファイルパス path={ngrok_path}")

        # ngrok強制終了
        log.general(__file__,"INFO",f"ngrok強制終了中...")
        subprocess.run(
            f'powershell -Command "Get-Process | Where-Object {{$_.Path -eq \'{ngrok_path}\'}} | Stop-Process -Force"',
            shell=True
        )
        log.general(__file__,"INFO",f"ngrokを強制終了しました")

    except Exception as e:
        log.general(__file__,"ERROR",f"例外エラーが発生しました error={e}")
        log.general(__file__,"INFO",f"処理を強制終了します")
        sys.exit()