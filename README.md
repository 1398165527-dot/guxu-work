# 谷序职业规划 Skill

这是一个对话式输入、文件化输出的学生职业规划 Skill。学生回答结构化问题后，将回答整理成 `student-profile.json`，运行生成器即可得到 HTML 个人报告、PPT 页面数据和职业规划大赛提交文档草稿。

## 运行

```bash
python3 generators/generate.py examples/student-profile.json --out generated-output
```

## 结果

- `report.html` 可直接用浏览器打开
- `slides.json` 是页面数据，每页含标题、正文、讲师备注和互动指令
- `competition-document.md` 可继续审阅并导出为 Word/PDF

## 对话问答顺序

身份与阶段 → 真实经历 → 优势证据 → 职业方向假设 → 真实任务 → 目标职业与赛道 → 行动计划 → 风险与待补证据。

生成器不会自动补写学生没有提供的奖项、数据、经历或结果。赛事细则须按当年度官方通知复核。

## 直接问答生成

```bash
python3 generators/interactive.py
```

程序会逐项询问学生信息、真实经历、方向假设、真实任务和比赛行动，并在 `generated-output/` 中生成个人报告、PPT 页面数据、参赛文档和保存后的 `student-profile.json`。
