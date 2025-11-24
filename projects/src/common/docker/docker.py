import subprocess
from projects.src.common.utils import logger as log
from projects.src.common.utils import param

# wsl
def start_wsl(container, distro="Ubuntu-22.04"):
    param_key = ["executor","distro_option","distro","cli","action","container_name"]
    cmd = ["wsl", "-d", distro, "docker", "start", container]
    params = param.create(param_key,cmd)

    log.general(__file__,"INFO",f"WSLのコンテナを起動します param={params}")
    return start_result_msg(container,docker_cmd_exec(cmd))

def stop_wsl(container, distro="Ubuntu-22.04"):
    param_key = ["executor","distro_option","distro","cli","action","container_name"]
    cmd = ["wsl", "-d", distro, "docker", "stop", container]
    params = param.create(param_key,cmd)

    log.general(__file__,"INFO",f"WSLのコンテナを停止します param={params}")
    return stop_result_msg(container,docker_cmd_exec(cmd))

# windows
def start_windows(container):
    param_key = ["cli","action","container_name"]
    cmd = ["docker", "start", container]
    params = param.create(param_key,cmd)

    log.general(__file__,"INFO",f"Windowsのコンテナを起動します param={params}")
    return start_result_msg(container,docker_cmd_exec(cmd))

def stop_windows(container):
    param_key = ["cli","action","container_name"]
    cmd = ["docker", "stop", container]
    params = param.create(param_key,cmd)

    log.general(__file__,"INFO",f"Windowsのコンテナを停止します param={params}")
    return stop_result_msg(container,docker_cmd_exec(cmd))


# 共通
# --- Dockerコマンド実行
def docker_cmd_exec(cmd):
    log.general(__file__,"INFO",f"コマンド実行 - {cmd}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    return docker_run_result_check(result)

# --- Dockerコマンド実行結果判定
def docker_run_result_check(result):
    if result.returncode == 0:
        return True
    log.general(__file__,"ERROR",f"stderr: {result.stderr.strip()}")
    return False

# --- コンテナ起動時のメッセージ出力
def start_result_msg(container, check):
    if check:
        log.general(__file__,"INFO",f"コンテナ[{container}]を起動しました")
        return check
    log.general(__file__,"ERROR",f"コンテナ[{container}]の起動に失敗しました")
    return False

# --- コンテナ停止時のメッセージ出力
def stop_result_msg(container, check):
    if check:
        log.general(__file__,"INFO",f"コンテナ[{container}]を起動しました")
        return check
    log.general(__file__,"ERROR",f"コンテナ[{container}]の起動に失敗しました")
    return False