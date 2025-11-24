# 共通部品
from projects.src.common.utils import logger as log
from projects.src.common.docker import docker

# 設定
from projects.conf import config

# 処理
log.start(__file__)

for container in config.DOCKER_CONTAINER_HOME:
    docker.start_windows(container)

log.end(__file__)
