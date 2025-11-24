# ライブラリ
from pathlib import Path
import os

# 共通部品
from projects.src.common.utils import logger as log


# 処理
def project_root(path_object = True):
    current_file = Path(__file__).resolve()
    path = current_file.parents[3]
    if path_object:
        return path
    return str(path)

def project_env(path_object = True):
    path = f"{project_root()}\\conf\\.env"
    if not os.path.isfile(path):
        log.general(__file__,"ERROR",f"存在しないファイルです path={path}")
        return ""
    if path_object:
        return Path(path)
    return path

def log_dir(path_object = True):
    path = f"{project_root()}\\call\\_log"
    if not os.path.isdir(path):
        log.general(__file__,"ERROR",f"存在しないディレクトリです path={path}")
        return ""
    if path_object:
        return Path(path)
    return path

def log_archives_dir(path_object = True):
    path = f"{log_dir()}\\archives"
    if not os.path.isdir(path):
        log.general(__file__,"ERROR",f"存在しないディレクトリです path={path}")
        return ""
    if path_object:
        return Path(path)
    return path

def application_dir(path_object = True):
    path = f"{project_root()}\\application"
    if not os.path.isdir(path):
        log.general(__file__,"ERROR",f"存在しないディレクトリです path={path}")
        return ""
    if path_object:
        return Path(path)
    return path

def spread_sheet_auth_dir(path_object = True):
    path = f"{project_root()}\\src\\conf\\google\\spread_sheet\\auth"
    if not os.path.isdir(path):
        log.general(__file__,"ERROR",f"存在しないディレクトリです path={path}")
        return ""
    if path_object:
        return Path(path)
    return path

print(project_root())