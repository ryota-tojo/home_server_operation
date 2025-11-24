from datetime import datetime
from pathlib import Path

def start(process_file_fullpath, log_level = "INFO"):
    process_file_path = delete_project_root(process_file_fullpath)
    print(f"{time_stamp()}[{log_level}] {process_file_path} - 処理開始")
    return

def general(process_file_fullpath, log_level = "INFO", text = ""):
    process_file_path = delete_project_root(process_file_fullpath)
    print(f"{time_stamp()}[{log_level}] {process_file_path} - {text}")
    return

def end(process_file_fullpath, log_level = "INFO"):
    process_file_path = delete_project_root(process_file_fullpath)
    print(f"{time_stamp()}[{log_level}] {process_file_path} - 処理終了")
    return

def time_stamp(format ="%Y-%m-%d_%H:%M:%S "):
    return datetime.now().strftime(format)

def delete_project_root(path):
    current_file = Path(__file__).resolve()
    project_root = current_file.parents[3]
    return str(path).replace(str(project_root), "")
