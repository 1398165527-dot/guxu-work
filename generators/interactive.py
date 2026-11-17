#!/usr/bin/env python3
import json
from pathlib import Path
from generate import build_report, build_slides, build_doc

def ask(label, required=True):
    while True:
        value=input(label+'：').strip()
        if value or not required:return value
        print('这一项需要填写。')

def run(out='generated-output'):
    print('谷序职业规划探索开始。请尽量使用真实经历，暂时不知道的内容可以填写“待补”。')
    profile={'student':{},'experiences':[],'directions':[],'competition':{'actions':[]},'task':{}}
    s=profile['student']; s['name']=ask('姓名或昵称'); s['school']=ask('学校'); s['major']=ask('专业'); s['year']=ask('年级'); s['contact']=ask('联系方式',False)
    print('\n请填写一段真实经历。')
    e={'situation':ask('当时是什么情境'),'action':ask('你具体做了什么'),'result':ask('结果是什么'),'feedback':ask('他人如何反馈',False),'energy':ask('其中哪一部分让你比较投入',False)}
    profile['experiences'].append(e)
    for i in range(2):
        more=input('是否再添加一段经历？输入 y 继续，直接回车跳过：').strip().lower()
        if more!='y':break
        profile['experiences'].append({'situation':ask('情境'),'action':ask('行动'),'result':ask('结果'),'feedback':ask('他人反馈',False),'energy':ask('投入部分',False)})
    print('\n请填写一个职业方向假设。')
    d={'name':ask('可能的职业或方向'),'reason':ask('为什么想到它'),'evidence':[ask('支持这个方向的一条真实证据')],'unknowns':[ask('还不知道或需要验证什么')]}
    profile['directions'].append(d)
    t=profile['task']; t['title']=ask('真实任务名称'); t['brief']=ask('任务要完成什么'); t['signals']=[ask('任务中要观察的信号')]; t['reflection']='完成后记录投入感、困难、结果和他人反馈。'
    c=profile['competition']; c['targetCareer']=ask('目标职业'); c['track']=ask('参赛赛道（不确定可写待核验）'); c['goal']=ask('参赛目标')
    print('\n至少填写一项行动计划。')
    c['actions'].append({'time':ask('行动时间'),'action':ask('具体行动'),'evidence':ask('完成后留下什么证据')})
    outp=Path(out); outp.mkdir(parents=True,exist_ok=True); (outp/'student-profile.json').write_text(json.dumps(profile,ensure_ascii=False,indent=2),encoding='utf-8'); (outp/'report.html').write_text(build_report(profile),encoding='utf-8'); (outp/'slides.json').write_text(json.dumps(build_slides(profile),ensure_ascii=False,indent=2),encoding='utf-8'); (outp/'competition-document.md').write_text(build_doc(profile),encoding='utf-8'); print(f'已生成：{outp}/report.html、{outp}/slides.json、{outp}/competition-document.md')
if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser(); ap.add_argument('--out',default='generated-output'); args=ap.parse_args(); run(args.out)
