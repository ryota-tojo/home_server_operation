# ライブラリ
from datetime import datetime

# 共通部品
from projects.src.common.utils import get_path as gpath
from projects.src.common.utils import logger as log

# 固有処理部品
from projects.src.tools.log.rotate.parts import archive
from projects.src.tools.log.rotate.parts import remove

# 処理
log.start(__file__)

# 処理日を取得
datetime_ = datetime.now()

# アーカイブ
archive.main(datetime_,gpath.log_dir(),gpath.log_archives_dir(),"")

# 削除
remove.main(datetime_,gpath.log_archives_dir())

log.end(__file__)


