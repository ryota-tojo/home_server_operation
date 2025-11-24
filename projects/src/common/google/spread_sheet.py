import gspread
from oauth2client.service_account import ServiceAccountCredentials
from projects.src.common.utils import logger as log
from projects.src.common.utils import param


def get(auth_file, spread_sheet_key, sheet_name, db_key):
    all_param_key = ["auth_file","spread_sheet_key","sheet_name","key"]
    all_param_value = [auth_file, spread_sheet_key, sheet_name, db_key]
    all_params = param.create(all_param_key, all_param_value)

    log.general(__file__, "INFO", f"スプレッドシートから値を取得します param={all_params}")

    try:
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"
        ]

        credentials = ServiceAccountCredentials.from_json_keyfile_name(auth_file, scope)
        gc = gspread.authorize(credentials)

        spreadsheet = gc.open_by_key(spread_sheet_key)
        worksheet = spreadsheet.worksheet(sheet_name)

        a_values = worksheet.col_values(1)  # A列

        for i, value in enumerate(a_values, start=1):
            if value == db_key:
                db_value = worksheet.cell(i, 2).value  # B列の値
                log.general(__file__, "INFO", f"値の取得に成功しました key={db_key}, value={db_value}")
                return db_value

        log.general(__file__, "ERROR", f"値の取得に失敗しました：キーが存在しません key={db_key}")
        return None

    except gspread.SpreadsheetNotFound:
        log.general(__file__,"ERROR",f"スプレッドシートが見つかりません spread_sheet_key={spread_sheet_key}")
    except gspread.WorksheetNotFound:
        log.general(__file__,"ERROR",f"シートが見つかりません sheet_name={sheet_name}")
    except FileNotFoundError:
        log.general(__file__,"ERROR",f"認証ファイルが見つかりません auth_file={auth_file}")
    except Exception as e:
        log.general(__file__,"ERROR",f"例外が発生 error={e}")

    return None

def insert(auth_file, spread_sheet_key, sheet_name, db_key, db_value):
    all_param_key = ["auth_file","spread_sheet_key","sheet_name","key","value"]
    all_param_value = [auth_file,spread_sheet_key,sheet_name,db_key,db_value]
    all_params = param.create(all_param_key,all_param_value)
    param_key = ["key","value"]
    param_value = [db_key,db_value]
    value_params = param.create(param_key,param_value)

    log.general(__file__,"INFO",f"スプレッドシートに値を連携します param={all_params}")
    try:
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"
        ]
        credentials = ServiceAccountCredentials.from_json_keyfile_name(auth_file, scope)
        gc = gspread.authorize(credentials)

        spreadsheet = gc.open_by_key(spread_sheet_key)
        worksheet = spreadsheet.worksheet(sheet_name)

        a_values = worksheet.col_values(1)
        for i, value in enumerate(a_values, start=1):
            if value == db_key:
                worksheet.update_cell(i, 2, db_value)
                log.general(__file__,"INFO",f"値の連携に成功しました param={value_params}")
                return True  # 成功
        log.general(__file__,"ERROR",f"値の連携に失敗しました：キーが存在しません key={db_key}")
        return False

    except gspread.SpreadsheetNotFound:
        log.general(__file__,"ERROR",f"値の連携に失敗しました：スプレッドシートが見つかりません spread_sheet_key={spread_sheet_key}")
    except gspread.WorksheetNotFound:
        log.general(__file__,"ERROR",f"値の連携に失敗しました：シートが見つかりません sheet_name={sheet_name}")
    except FileNotFoundError:
        log.general(__file__,"ERROR",f"値の連携に失敗しました：認証ファイルが見つかりません auth_file={auth_file}")
    except Exception as e:
        log.general(__file__,"ERROR",f"値の連携に失敗しました：例外 error={e}")
    return False