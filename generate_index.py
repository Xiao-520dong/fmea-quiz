import os
import glob
import re

def extract_day_number(filename):
    match = re.search(r'Day(\d+)', filename)
    if match:
        return int(match.group(1))
    return 999

def extract_title(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()
    m = re.search(r'<title>(.*?)</title>', c)
    return m.group(1) if m else os.path.basename(filepath)

os.chdir('/home/node/.openclaw/workspace-fmea-expert/fmea-quiz')
html_files = glob.glob('output/Day*.html')
html_files.sort(key=extract_day_number)

modules = [
    ("第一阶段：第 1 章 引言与项目规划（5T法 & 七步法总览）", 1, 10),
    ("第二阶段：第 2 章 设计 FMEA (DFMEA) 七步法全流程精讲", 11, 37),
    ("第三阶段：第 3 章 过程 FMEA (PFMEA) 七步法全流程精讲", 38, 55),
    ("第四阶段：第 4 章 监视及系统响应的补充 FMEA (FMEA-MSR)", 56, 69),
    ("第五阶段：附件 A & B 标准表格视图与分步实操填写提示", 70, 77),
    ("第六阶段：附件 C S/O/D、S/F/M 与 AP 评分表逐级深度拆解", 78, 85),
    ("第七阶段：附件 D~H 特殊特性、软件 FMEA、新旧版变更对比与总复盘", 86, 100),
    ("第八阶段：【番外实战篇】FMEA 与 CP/8D/防错/SPC/MSA/DRBFM 综合联动", 101, 120)
]

sections_html = ""
for mod_title, d_start, d_end in modules:
    sections_html += f'<h2>{mod_title}（Day {d_start:03d} - Day {d_end:03d}）</h2>\n<ul>\n'
    for f in html_files:
        d_num = extract_day_number(f)
        if d_start <= d_num <= d_end:
            title = extract_title(f)
            sections_html += f'  <li><a href="{f}">{title}</a></li>\n'
    sections_html += '</ul>\n'

index_content = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AIAG & VDA FMEA 手册 120天精讲课程目录</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans SC", sans-serif; line-height: 1.6; padding: 30px 20px; max-width: 900px; margin: 0 auto; color: #2d3748; background: #f7fafc; }}
        .container {{ background: #fff; padding: 35px; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.06); }}
        h1 {{ color: #1a202c; border-bottom: 3px solid #667eea; padding-bottom: 12px; margin-top: 0; }}
        h2 {{ color: #2b6cb0; font-size: 18px; margin-top: 28px; border-left: 4px solid #4299e1; padding-left: 10px; background: #ebf8ff; padding: 8px 12px; border-radius: 0 8px 8px 0; }}
        ul {{ list-style-type: none; padding: 0; display: grid; grid-template-columns: 1fr; gap: 8px; }}
        li {{ padding: 10px 14px; background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; transition: all 0.2s; }}
        li:hover {{ background-color: #edf2f7; border-color: #cbd5e0; transform: translateX(4px); }}
        a {{ text-decoration: none; color: #2d3748; font-weight: 500; display: block; }}
        a:hover {{ color: #3182ce; }}
        .badge {{ display: inline-block; background: #667eea; color: #fff; font-size: 13px; padding: 4px 12px; border-radius: 12px; margin-bottom: 15px; }}
        .manual-card {{
            display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px;
            background: linear-gradient(135deg, #ebf8ff 0%, #e6fffa 100%);
            border: 1.5px solid #90cdf4; border-radius: 12px; padding: 16px 20px; margin: 15px 0 25px 0;
            box-shadow: 0 2px 10px rgba(66, 153, 225, 0.08);
        }}
        .manual-info {{ display: flex; align-items: center; gap: 12px; }}
        .manual-icon {{ font-size: 28px; background: #fff; width: 48px; height: 48px; border-radius: 10px; display: flex; align-items: center; justify-content: center; box-shadow: 0 2px 6px rgba(0,0,0,0.05); }}
        .manual-title {{ font-weight: 700; font-size: 16px; color: #2b6cb0; margin-bottom: 2px; }}
        .manual-desc {{ font-size: 13px; color: #4a5568; }}
        .manual-btns {{ display: flex; gap: 10px; }}
        .btn-pdf {{
            display: inline-block; padding: 8px 16px; border-radius: 8px; font-size: 14px; font-weight: 600;
            text-decoration: none !important; transition: all 0.2s;
        }}
        .btn-pdf.view {{ background: #3182ce; color: #fff !important; box-shadow: 0 2px 6px rgba(49, 130, 206, 0.3); }}
        .btn-pdf.view:hover {{ background: #2b6cb0; transform: translateY(-1px); }}
        .btn-pdf.dl {{ background: #fff; color: #2b6cb0 !important; border: 1px solid #90cdf4; }}
        .btn-pdf.dl:hover {{ background: #ebf8ff; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📘 AIAG & VDA FMEA 手册 120天精讲课程目录</h1>
        <div class="badge">共 {len(html_files)} 期课件 | 239页原书逐节精讲 (Day 001-100) + 质量工具联动实战番外 (Day 101-120)</div>
        <div class="manual-card">
            <div class="manual-info">
                <div class="manual-icon">📕</div>
                <div>
                    <div class="manual-title">《AIAG & VDA FMEA 手册》原版教材（中文第一版 · 共239页）</div>
                    <div class="manual-desc">本课程唯一权威事实来源，支持在线翻阅原书页面与高清下载对照学习（PDF, 18MB）</div>
                </div>
            </div>
            <div class="manual-btns">
                <a href="source/AIAG_VDA_FMEA.pdf" target="_blank" class="btn-pdf view">📖 在线阅读原手册</a>
                <a href="source/AIAG_VDA_FMEA.pdf" download="AIAG_VDA_FMEA_手册原版.pdf" class="btn-pdf dl">⬇️ 下载 PDF</a>
            </div>
        </div>
        {sections_html}
    </div>
</body>
</html>
"""
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_content)
print(f"index.html generated successfully with {len(html_files)} items.")
