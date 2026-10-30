# GitHub Actions 定时任务模板（合规自用）

一个最小可用的定时任务骨架：每天定时跑一次脚本，也支持在网页上手动触发测试。

## 文件结构

```
你的仓库/
├─ .github/workflows/scheduled-task.yml   # 定时任务定义
├─ scripts/task.py                        # 真正干活的脚本（换成你的逻辑）
└─ requirements.txt                       # 依赖（可选）
```

## 三步用起来

1. 把 `.github/workflows/scheduled-task.yml` 和 `scripts/task.py` 放进你的仓库，提交到**默认分支**（定时任务只在默认分支生效）。
2. 网页上进入 Actions → 左侧选 **Scheduled Task** → **Run workflow**，勾住 `dry_run` 先演练一次，确认日志正常。
3. 确认无误后取消勾选再跑一次真实执行；之后 cron 到点会自动跑，不用再点。

## 关键注意点

| 事项 | 说明 |
|---|---|
| 时区 | cron 用 **UTC**，北京时间 = UTC + 8。每天 08:00 北京 → `0 0 * * *` |
| 生效分支 | 只在**默认分支**上生效 |
| 延迟 | 高峰期可能延迟几分钟到十几分钟，不适合秒级准点 |
| 60 天规则 | 仓库连续 60 天无活动，定时任务会被自动停用，需要去 Actions 页点 Enable |
| 密钥 | 一律放 Settings → Secrets and variables → Actions，不要在 yml 里写明文 |
| 权限 | 顶部 `permissions` 用最小权限，需要提交产物时才加 `contents: write` |

## 常见报错

| 日志关键词 | 原因 | 处理 |
|---|---|---|
| `Invalid workflow file` | YAML 语法错，常见是多写了 `timezone:` | GitHub 不支持 cron 的 timezone 参数，删掉只留 `cron:` |
| `Resource not accessible by integration` | 权限不足 | 在 `permissions` 里加对应权限 |
| 工作流列表里找不到 | 文件路径不对或有语法错 | 确认路径是 `.github/workflows/xxx.yml` |
| 定时没触发 | 不在默认分支 / 被自动停用 / 仓库长期无提交 | 检查分支，去 Actions 点 Enable，提交一次空改动 |
