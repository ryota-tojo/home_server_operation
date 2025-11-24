# ライブラリ
import os
from future.backports.datetime import datetime

# 共通部品
from projects.src.common.utils import logger as log
from projects.src.common.utils import param
from projects.src.common.utils.date import get_date as gdate
from projects.src.tools.log.rotate.parts import date as parts_date
from projects.src.tools.log.rotate.parts import dir as parts_dir

# 処理概要
## 処理日の1年1ヶ月以前のタイムスタンプを持つファイルを削除する
def main(base_date, target_dir):
    # datetime_(datetime)：処理日を指定
    # from_dir(Path)：対象ファイルが存在するディレクトリを指定
    # to_dir(Path)：アーカイブ先のディレクトリを指定
    # zip_dir_label(str)：zip化する際のファイル名を指定（ファイル名：{zip_dir_label}_{ログファイルのタイムスタンプ以前の部分}_{yyyymm(処理日2か月前).zip}）

    param_key = ["base_date","target_dir"]
    param_value = [str(base_date),str(target_dir)]
    value_params = param.create(param_key,param_value)

    log.general(__file__,"INFO",f"対象ファイルを削除します param={value_params}")

    # ログディレクトリから最も古いタイムスタンプを取得する（※スタート）
    start_yyyymm = parts_dir.get_oldest_timestamp(target_dir)
    if start_yyyymm == "":
        log.general(__file__,"INFO",f"対象ディレクトリのファイルからタイムスタンプを取得できませんでした dir={target_dir}")
        log.general(__file__,"INFO",f"削除終了")
        return False
    start_dt = datetime.strptime(start_yyyymm, "%Y%m")

    # base_dateの1年1ヶ月以前の年月を取得する（※エンド）
    end_dt = parts_date.get_one_year_and_one_months_ago(base_date)

    if start_dt > end_dt:
        log.general(__file__,"INFO",f"削除対象のファイルが存在しませんでした dir={target_dir}")
        log.general(__file__,"INFO",f"削除終了")
        return

    # スタート～エンドをループ
    log.general(__file__,"INFO",f"start_date={start_dt}")
    log.general(__file__,"INFO",f"end_date={end_dt}")

    current = start_dt
    while current <= end_dt:
        # 削除する
        remove(current, target_dir)

        # 次の月に進める
        if current.month == 12:
            current = current.replace(year=current.year+1, month=1)
        else:
            current = current.replace(month=current.month+1)

    log.general(__file__,"INFO",f"削除完了")
    return True

# 処理概要
## 処理日のタイムスタンプを持つファイルを削除する
def remove(datetime_, target_dir):
    # datetime_(datetime)：処理日を指定
    # target_dir(Path)：対象ファイルが存在するディレクトリを指定

    # アーカイブ対象年月変換
    remove_date = gdate.get_date(datetime_,"%Y%m")

    # 処理対象ログファイル取得
    ## 条件
    ## ・拡張子：.zip
    zip_files = [f for f in target_dir.iterdir() if f.is_file() and f.suffix == ".zip" and remove_date in f.name]

    # アーカイブファイルをループ
    log.general(__file__,"INFO",f"処理対象 timestamp={remove_date}")

    for f in zip_files:
        # 存在すれば削除
        if f.exists():
            os.remove(f)
            log.general(__file__,"INFO",f"  -> 削除 file_name={f.name}")
