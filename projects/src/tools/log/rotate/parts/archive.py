# ライブラリ
import os
import shutil
from future.backports.datetime import datetime

# 共通部品
from projects.src.common.utils import logger as log
from projects.src.common.utils import param
from projects.src.common.utils.date import get_date as gdate
from projects.src.tools.log.rotate.parts import date as parts_date
from projects.src.tools.log.rotate.parts import dir as parts_dir
from projects.src.common.utils import zip

# 処理概要
## 処理月の2ヶ月前以前のタイムスタンプを持つファイルをアーカイブディレクトリに移動しzip化する
def main(base_date, from_dir, to_dir, zip_dir_label):
    # base_date(datetime)：処理日を指定
    # from_dir(Path)：対象ファイルが存在するディレクトリを指定
    # to_dir(Path)：アーカイブ先のディレクトリを指定
    # zip_dir_label(str)：zip化する際のファイル名を指定（ファイル名：{zip_dir_label}_{ログファイルのタイムスタンプ以前の部分}_{yyyymm(処理日2か月前).zip}）

    print(base_date)
    print(from_dir)
    print(to_dir)
    print(zip_dir_label)

    param_key = ["base_date","from_dir","to_dir","zip_dir_label"]
    param_value = [str(base_date),str(from_dir),str(to_dir),zip_dir_label]
    value_params = param.create(param_key,param_value)

    log.general(__file__,"INFO",f"対象ファイルをアーカイブします param={value_params}")

    # ログディレクトリから最も古いタイムスタンプを取得する（※スタート）
    start_yyyymm = parts_dir.get_oldest_timestamp(from_dir)
    if start_yyyymm == "":
        log.general(__file__,"INFO",f"対象ディレクトリのファイルからタイムスタンプを取得できませんでした dir={from_dir}")
        log.general(__file__,"INFO",f"アーカイブ終了")
        return False
    start_dt = datetime.strptime(start_yyyymm, "%Y%m")

    # base_dateの2ヶ月前の年月を取得する（※エンド）
    end_dt = parts_date.get_two_months_ago(base_date)

    if start_dt > end_dt:
        log.general(__file__,"INFO",f"アーカイブ対象のファイルが存在しませんでした dir={from_dir}")
        log.general(__file__,"INFO",f"アーカイブ終了")
        return False

    # スタート～エンドをループ
    log.general(__file__,"INFO",f"start_date={start_dt}")
    log.general(__file__,"INFO",f"end_date={end_dt}")

    current = start_dt
    while current <= end_dt:
        # アーカイブする
        archive(current, from_dir, to_dir, zip_dir_label)

        # 次の月に進める
        if current.month == 12:
            current = current.replace(year=current.year+1, month=1)
        else:
            current = current.replace(month=current.month+1)

    log.general(__file__,"INFO",f"アーカイブ完了")
    return True

## 処理月のタイムスタンプを持つファイルをアーカイブディレクトリに移動しzip化する
def archive(base_date, from_dir, to_dir, zip_dir_label):

    # アーカイブ対象年月変換
    archive_yyyymm = gdate.get_date(base_date,"%Y%m")

    # 処理対象ログファイル取得
    ## 条件
    ## ・拡張子：.log
    log_files = [f for f in from_dir.iterdir() if f.is_file() and f.suffix == ".log" and archive_yyyymm in f.name]

    # logファイル名からtool名取得
    tmp_tool_names = []
    for f in log_files:
        tmp_tool_names.append(f.name.rsplit('_', 1)[0])
    tool_names = list(set(tmp_tool_names))

    # tool名ごとにループ
    for tool_name in tool_names:

        log.general(__file__,"INFO",f"処理対象 target_name={tool_name} timestamp={archive_yyyymm}")

        # 圧縮対象ディレクトリパス作成
        if zip_dir_label == "":
            zip_dir_name = f"{tool_name}_{archive_yyyymm}"
        else:
            zip_dir_name = f"{zip_dir_label}_{tool_name}_{archive_yyyymm}"
        zip_target_dir = f"{str(to_dir)}/{zip_dir_name}"

        # 圧縮対象ディレクトリが存在しない場合は作成
        if not os.path.isdir(zip_target_dir):
            os.mkdir(zip_target_dir)
            log.general(__file__,"INFO",f"アーカイブディレクトリを作成しました dir_name={zip_target_dir}")

        # アーカイブに対象ファイルを移動
        for f in log_files:
            if tool_name in f.name:
                shutil.move(f, f"{zip_target_dir}/{f.name}")
                log.general(__file__,"INFO",f"  -> アーカイブ file_name={f.name}")

        # zip化
        zip.make_7zip(zip_dir_name,zip_target_dir,to_dir,"",3)

        # zip元のディレクトリ削除
        shutil.rmtree(zip_target_dir)
        log.general(__file__,"INFO",f"対象ディレクトリ削除 path={zip_target_dir}")

