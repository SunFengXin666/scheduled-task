"""定时任务示例脚本：把里面的逻辑换成你自己的即可。

运行环境：GitHub Actions (ubuntu-latest, Python 3.12)
"""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

OUTPUT_DIR = Path("output")


def log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc):%Y-%m-%d %H:%M:%S}Z] {msg}", flush=True)


def main() -> int:
    dry_run = os.getenv("DRY_RUN", "false").lower() in {"1", "true", "yes"}
    token = os.getenv("MY_API_TOKEN")

    log(f"dry_run={dry_run}")
    log(f"note={os.getenv('RUN_NOTE', '')!r}")

    if not token:
        # 没有配置 secret 时只提示，不阻断演练
        log("提示：未检测到 MY_API_TOKEN，如果要调用外部接口请先去 Settings -> Secrets 配置")

    OUTPUT_DIR.mkdir(exist_ok=True)

    # ---- 在这里替换成你的真实业务逻辑 ----
    result = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "dry_run": dry_run,
        "status": "ok",
        "items": [],
    }

    if dry_run:
        log("演练模式：不执行实际写操作")
    else:
        log("正式模式：开始执行实际任务")
        # 示例：result["items"] = fetch_your_data(token)

    out_file = OUTPUT_DIR / "result.json"
    out_file.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    log(f"已写出 {out_file}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
