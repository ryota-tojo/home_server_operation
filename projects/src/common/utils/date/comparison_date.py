# ライブラリ


# 処理
def is_less_than_or_equal_for_date(target_datetime, source_datetime):
    # 対象日が比較日以下かどうかを判定
    # target_datetime：対象日
    # source_datetime：比較日
    return target_datetime <= source_datetime


def is_less_than_for_date(target_datetime, source_datetime):
    # 対象日が比較日より前かどうかを判定
    # target_datetime：対象日
    # source_datetime：比較日
    return target_datetime < source_datetime
