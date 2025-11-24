# ライブラリ
import json

# 共通部品
from projects.src.common.utils import logger as log


# 処理
def create(param_key_list, param_value_list, br = True):
    print(f"param_key_list={param_key_list}")
    print(f"param_value_list={param_value_list}")
    if len(param_key_list) != len(param_value_list):
        log.general(__file__, "INFO",
                    f"jsonパラメータの作成に失敗しています(キー、値の数が不一致) param_key_list=count({len(param_key_list)}), param_value_list=count({len(param_value_list)})")
        return json.dumps(
            {},
            ensure_ascii=False,
            separators=(",", ":")
        )

    param_dict = {key: value for key, value in zip(param_key_list, param_value_list)}

    if br:
        return json.dumps(param_dict, ensure_ascii=False, indent=2)

    return json.dumps(
        param_dict,
        ensure_ascii=False,
        separators=(",", ":")
    )
