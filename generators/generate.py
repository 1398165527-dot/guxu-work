#!/usr/bin/env python3
import argparse, json, html
from pathlib import Path

def esc(x): return html.escape(str(x or ''))
def facts(p):
    return [e for e in p.get('experiences',[]) if e.get('situation') or e.get('action') or e.get('result')]
def build_report(p):
    s=p['student']; ds=p.get('directions',[]); c=p['competition']; task=p.get('task',{})
    ex=facts(p)
    evidence=''.join(f'<li><b>情境：</b>{esc(e.get("situation"))}<br><b>行动：</b>{esc(e.get("action"))}<br><b>结果：</b>{esc(e.get("result"))}<br><b>他人反馈：</b>{esc(e.get("feedback") or "待补证据")}</li>' for e in ex)
    direction=''.join(f'<article><h3>{esc(d.get("name"))}</h3><p>{esc(d.get("reason"))}</p><p><b>已有证据</b> {esc("；".join(d.get("evidence",[])))}</p><p class="pending"><b>待验证</b> {esc("；".join(d.get("unknowns",[])))}</p></article>' for d in ds)
    actions=''.join(f'<tr><td>{esc(a.get("time"))}</td><td>{esc(a.get("action"))}</td><td>{esc(a.get("evidence"))}</td></tr>' for a in c.get('actions',[]))
    return f'''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><title>{esc(s.get("name"))}的职业规划报告</title><style>body{{font-family:system-ui,"Noto Sans SC";max-width:960px;margin:0 auto;padding:40px;color:#173d37;background:#f7f6f0;line-height:1.7}}header,section,article{{background:white;border:1px solid #d4e0d7;border-radius:18px;padding:24px;margin:18px 0}}h1{{font-size:42px}}h2{{border-bottom:2px solid #b8df62;padding-bottom:8px}}.pending{{color:#966a18}}table{{width:100%;border-collapse:collapse}}td{{border-bottom:1px solid #d4e0d7;padding:10px}}</style><header><p>谷序 · 学生职业规划个人报告</p><h1>{esc(s.get("name"))}</h1><p>{esc(s.get("school"))} · {esc(s.get("major"))} · {esc(s.get("year"))}</p></header><section><h2>一、报告说明</h2><p>本报告依据学生提供的经历和回答生成。事实、推断和待验证内容分别标记，不能替代学校指导或当年度赛事通知。</p></section><section><h2>二、优势证据</h2><ul>{evidence or '<li class="pending">尚未提供真实经历，需补充。</li>'}</ul></section><section><h2>三、职业方向假设</h2>{direction or '<p class="pending">尚未形成方向假设。</p>'}</section><section><h2>四、真实任务</h2><h3>{esc(task.get("title") or "待设计")}</h3><p>{esc(task.get("brief") or "请先选择一个目标职业并设计可观察任务。")}</p><p><b>观察信号：</b>{esc("；".join(task.get("signals",[])))}</p><p><b>复盘：</b>{esc(task.get("reflection") or "完成后记录投入感、困难、结果和他人反馈。")}</p></section><section><h2>五、比赛方向草案</h2><p><b>目标职业：</b>{esc(c.get("targetCareer"))}</p><p><b>赛道：</b>{esc(c.get("track"))}</p><p><b>参赛目标：</b>{esc(c.get("goal"))}</p><table><tr><th>时间</th><th>行动</th><th>证据</th></tr>{actions}</table></section><section><h2>六、待补证据</h2><p>补充真实数据、作品链接、他人反馈、岗位信息和当年度赛事要求后再提交正式材料。</p></section></html>'''
def build_slides(p):
    s=p['student']; c=p['competition']; ds=p.get('directions',[])
    pages=[('封面',f'{s.get("name")}的职业规划探索'),('我的基本信息',f'{s.get("school")}｜{s.get("major")}｜{s.get("year")}'),('我正在探索的问题','我想知道自己适合怎样的工作，以及如何把优势变成可验证的行动。'),('优势证据', '；'.join(e.get('action','') for e in facts(p)) or '待补充真实经历'),('职业方向假设','；'.join(d.get('name','') for d in ds) or '待形成'),('目标职业',c.get('targetCareer','待确定')),('行动计划','；'.join(a.get('action','') for a in c.get('actions',[])) or '待制定'),('待验证问题','哪些任务让我更投入？哪些能力需要补齐？哪些职业信息还没有核验？'),('答辩提醒','每个结论都要回到真实经历、真实任务和可检查的证据。')]
    return [{'page':i+1,'title':t,'body':b,'speaker_notes':'请结合学生真实经历补充，不要替学生编造事实。','interaction':'请学生记录或分享一个具体例子。'} for i,(t,b) in enumerate(pages)]
def build_doc(p):
    s=p['student']; c=p['competition']; ex=facts(p)
    return f'''# {s.get("name")}职业规划大赛提交文档草稿\n\n## 一、基本信息\n- 学校：{s.get("school")}\n- 专业：{s.get("major")}\n- 年级：{s.get("year")}\n\n## 二、职业目标\n目标职业：{c.get("targetCareer")}\n\n参赛方向：{c.get("track")}\n\n参赛目标：{c.get("goal")}\n\n## 三、个人优势证据\n''' + ''.join(f'\n### 经历 {i}\n- 情境：{e.get("situation")}\n- 行动：{e.get("action")}\n- 结果：{e.get("result")}\n- 反馈：{e.get("feedback") or "待补证据"}\n' for i,e in enumerate(ex,1)) + '''\n## 四、行动计划\n''' + ''.join(f'\n- {a.get("time")}：{a.get("action")}。证据：{a.get("evidence")}\n' for a in c.get('actions',[])) + '''\n\n## 五、风险与备选路径\n- 需要补充岗位真实信息和行业访谈。\n- 需要用真实任务验证方向适配度。\n- 需要根据当年度官方通知复核赛道、材料和时间。\n\n## 六、答辩问题\n1. 你为什么选择这个职业目标？\n2. 哪段真实经历能证明你的优势？\n3. 如果目标路径受阻，你的备选行动是什么？\n'''
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('input'); ap.add_argument('--out',default='generated-output'); a=ap.parse_args(); p=json.loads(Path(a.input).read_text(encoding='utf-8')); out=Path(a.out); out.mkdir(parents=True,exist_ok=True); (out/'report.html').write_text(build_report(p),encoding='utf-8'); (out/'slides.json').write_text(json.dumps(build_slides(p),ensure_ascii=False,indent=2),encoding='utf-8'); (out/'competition-document.md').write_text(build_doc(p),encoding='utf-8'); print(f'generated {out}')
if __name__=='__main__': main()
