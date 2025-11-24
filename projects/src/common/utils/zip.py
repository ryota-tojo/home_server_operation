# ライブラリ
import shutil
import os
import time
from subprocess import run, DEVNULL

# 共通部品
from projects.src.common.utils import get_path as gpath
from projects.src.common.utils import logger as log
from projects.src.common.utils import param


# フォルダサイズの取得
def get_dir_size(path = '.'):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total

# ファイルサイズの取得
def get_file_size(path = '.'):
    return os.path.getsize(path)

# zip化
def make_zip(zipfile_name,target_dir,output_dir):
    # 【引数】
    # zipfile_name = 作成するzipファイル名
    # target_dir = 圧縮対象のディレクトリ
    # output_dir = 圧縮先のディレクトリ

    param_key = ["zipfile_name", "target_dir", "output_dir"]
    param_value = [zipfile_name, target_dir, output_dir]
    params = param.create(param_key, param_value)
    log.general(__file__, "INFO", f"フォルダをzip化します param={params}")

    # 圧縮ファイル出力
    try:
        shutil.make_archive(f'{output_dir}/{zipfile_name}', 'zip', root_dir = target_dir)
        log.general(__file__, "INFO", f"  -> 処理成功")
        return True
    except Exception as e:
        log.general(__file__, "ERROR", f"  -> 処理失敗 error={e}")
        return False


def make_7zip(zipfile_name,target_dir,output_dir,password="",compress=0):

    zip7file = f"{gpath.application_dir()}\\7-Zip\\7z.exe"

    if password == "":
        password_value = ""
    else:
        password_value = "********"

    param_key = ["zip7file","zipfile_name", "target_dir", "output_dir","password","compress"]
    param_value = [zip7file,zipfile_name, target_dir, output_dir,password_value,compress]
    params = param.create(param_key, param_value)
    log.general(__file__, "INFO", f"フォルダをzip化します param={params}")

    # 7zip実行ファイルの存在チェック
    if not os.path.exists(zip7file):
        log.general(__file__, "ERROR", f"7zip.exeが存在しません zip7file={zip7file}")
        return False

    # ファイル名作成
    zip_name = f"{zipfile_name}.zip"

    # 圧縮ファイルパス(保存フォルダ\\ファイル名)
    latest_file = f"{output_dir}\\{zip_name}"

    # 圧縮対象フォルダパス
    src_dir = f"{target_dir}\\*"

    # 圧縮率に設定できない値が指定されている場合は未圧縮に設定
    if compress !=0 and compress !=1 and compress !=3 and compress !=5 and compress !=7 and compress !=9:
        # 【圧縮率】
        # 0 (no compression 無圧縮、非圧縮),
        # 1 (Fastest),
        # 3 (Fast),
        # 5 (Normal),
        # 7 (Maximum),
        # 9 (Ultra 超圧縮)
        compress=0

    # コマンドの引数リスト作成
    if password == "":
        args = (
            zip7file, # 7z.exe
            "a", # a (Add) command
            latest_file, # 圧縮後のファイル
            src_dir, # 圧縮対象フォルダ
            f"-mx={compress}" # zipの圧縮率
        )
    else:
        args = (
            zip7file, # 7z.exe
            "a", # a (Add) command
            f"-p{password}",
            latest_file, # 圧縮後のファイル
            src_dir, # 圧縮対象フォルダ
            f"-mx={compress}" # zipの圧縮率
        )

    print(f"圧縮実行: {args}")
    # 圧縮実行
    cp = run(args, stdout=DEVNULL)

    # 7z.exe エラーの場合
    if cp.returncode != 0:
        time.sleep(0.5)
        log.general(__file__, "ERROR", f"  -> 処理失敗 return_code={cp.returncode}")
        return False

    else:
        time.sleep(0.5)
        log.general(__file__, "INFO", f"  -> 処理成功")
        return True
