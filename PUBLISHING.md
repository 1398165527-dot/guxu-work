# GitHub 发布说明

## 本地检查

```bash
python3 generators/generate.py examples/student-profile.json --out generated-example
```

检查生成目录包含 `report.html`、`slides.json` 和 `competition-document.md`。

## GitHub 上传

在目标仓库根目录放置 `github-skill/` 下的全部文件。建议仓库包含：

- `SKILL.md`
- `README.md`
- `schemas/`
- `generators/`
- `examples/`
- `templates/`
- `validation/`
- `output-contract.md`

发布前确认没有学生真实隐私信息、授权码、Token、密码或未授权案例。

## 版本规则

首版使用 `v0.1.0`。后续修改学生问答字段、输出格式或生成器行为时，更新版本号并在变更记录中说明兼容影响。
