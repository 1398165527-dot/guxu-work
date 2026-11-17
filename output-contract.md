# 谷序 Skill 输出协议

输入必须是 `student-profile.json`，或由对话问答逐步填充的同名对象。生成器必须输出：

1. `report.html`：学生个人职业规划报告，含事实、推断、待验证证据和行动计划。
2. `slides.json`：可导入演示工具的页面数组，每页包含 `title`、`body`、`speaker_notes`、`interaction`。
3. `competition-document.md`：职业规划大赛提交文档草稿，含目标、职业理解、优势证据、行动计划、风险与答辩问题。

生成器不得补写学生没有提供的奖项、经历、数据、机构或结果。所有推断必须标注为“推断”，所有空缺必须进入“待补证据”。
