# ライブラリ

# 共通部品

# 固有部品
from projects.src.tools.log.rotate.parts import date


def get_oldest_timestamp(path):
    #  ディレクトリの中のファイルから最も古いタイムスタンプを取得

    files = [f for f in path.iterdir() if f.is_file()]

    tmp_timestamps = []
    for f in files:
        ts = f.stem.split('_')[-1][:6]
        if date.is_valid_date(ts, "%Y%m"):
            tmp_timestamps.append(ts)

    if not tmp_timestamps:
        return ""

    return min(list(set(tmp_timestamps)))
