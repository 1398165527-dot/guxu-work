# 推荐 GitHub 仓库结构

仓库根目录建议直接使用 `guxu-career-skill/` 的内容，而不是把整个交付包上传到 Skill 仓库。学生隐私样例只使用 `examples/student-profile.json` 中的虚拟数据。

## 发布前检查

- 运行 `python3 generators/generate.py examples/student-profile.json --out generated-example`
- 检查 HTML、页面 JSON 和 Markdown 文档均生成
- 检查所有规则性内容保留官方核验提示
- 检查仓库没有 Token、授权码、手机号和真实学生资料
- 建立 GitHub Release `v0.1.0`
