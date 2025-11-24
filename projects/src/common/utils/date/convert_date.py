# ライブラリ
from datetime import datetime


# 処理
def to_date_for_yyyymm(yyyymm):
    dt = datetime.strptime(yyyymm, "%Y%m")
    return dt.date()
