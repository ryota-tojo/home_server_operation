# ライブラリ
from dateutil.relativedelta import relativedelta

# 共通部品


# 処理
def get_date(datetime_, format_="%Y%m%d", year_=0, month_=0, day_=0):
    two_months_ago = datetime_ - relativedelta(years=year_, months=month_, days=day_)
    return two_months_ago.strftime(format_)
