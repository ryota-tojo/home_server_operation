# ライブラリ
from datetime import datetime
from dateutil.relativedelta import relativedelta

# 処理
def is_valid_date(value: str, format_: str = "%Y%m%d") -> bool:
   try:
      datetime.strptime(value, format_)
      return True
   except ValueError:
      return False

def get_year(date_str: str, format_: str = "%Y%m") -> int:
   dt = datetime.strptime(date_str, format_)
   return dt.year

def get_month(date_str: str, format_: str = "%Y%m") -> int:
   dt = datetime.strptime(date_str, format_)
   return dt.month

def get_two_months_ago(datetime_: datetime) -> datetime:
   return datetime_ - relativedelta(months=2)

def get_one_year_and_one_months_ago(datetime_: datetime) -> datetime:
   return datetime_ - relativedelta(years=1,months=1)