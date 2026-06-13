from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from xml.sax.saxutils import escape

root = Path(__file__).resolve().parents[1]
out = root / 'word_revision' / 'output'
out.mkdir(parents=True, exist_ok=True)

files = [
    root / 'word_revision' / 'part1.md',
    root / 'word_revision' / 'sections' / '2.1.md',
    root / 'word_revision' / 'sections' / '2.2.md',
    root / '最终稿' / '13-2.3案例调研.md',
    root / '最终稿' / '14-2.4设计定位.md',
    root / 'word_revision' / 'sections' / '3.1.md',
    root / '最终稿' / '16-3.2数据收集.md',
    root / 'word_revision' / 'sections' / '3.3.md',
    root / '最终稿' / '18-3.4数据集制作.md',
    root / '最终稿' / '19-4.1字体系统设计.md',
    root / '最终稿' / '20-4.2色彩系统设计.md',
    root / '最终稿' / '21-4.3标志系统设计.md',
    root / '最终稿' / '22-4.4版式设计.md',
    root / '最终稿' / '23-4.5效果图制作.md',
    root / '最终稿' / '24-4.6设计优化.md',
    root / '最终稿' / '25-5.1网页交互设计.md',
    root / '最终稿' / '26-5.2展板设计.md',
    root / '最终稿' / '27-5.3实物制作与展示.md',
    root / '最终稿' / '28-结论与展望.md',
    root / '最终稿' / '29-致谢.md',
    root / '最终稿' / '30-参考文献.md'
]

text = '\n\n'.join(p.read_text(encoding='utf-8') for p in files if p.exists())
text = text.replace('# 2.1 总体方案', '# 第2章 设计方案与构思\n\n## 2.1 总体方案', 1)
text = text.replace('# 3.1 叙事框架搭建', '# 第3章 设计制作流程\n\n## 3.1 叙事框架搭建', 1)
text = text.replace('# 4.1 字体系统设计', '# 第4章 设计制作\n\n## 4.1 字体系统设计', 1)
text = text.replace('# 5.1 网页交互设计', '# 第5章 延展设计\n\n## 5.1 网页交互设计', 1)

paragraphs = []
for line in text.splitlines():
    s = line.strip().replace('**','').replace('`','')
    if not s or s.startswith('```') or s.startswith('---'):
        continue
    level = 0
    while level < len(s) and s[level] == '#':
        level += 1
    if level:
        s = s[level:].strip()
    paragraphs.append((level, s))


def p_xml(level, value):
    style = ''
    if level == 1:
        style = '<w:pStyle w:val="Heading1"/><w:pageBreakBefore/>'
    elif level == 2:
        style = '<w:pStyle w:val="Heading2"/>'
    elif level >= 3:
        style = '<w:pStyle w:val="Heading3"/>'
    else:
        style = '<w:ind w:firstLineChars="200"/>'
    return '<w:p><w:pPr>' + style + '<w:spacing w:line="360" w:lineRule="auto"/></w:pPr><w:r><w:t xml:space="preserve">' + escape(value) + '</w:t></w:r></w:p>'

body = ''.join(p_xml(level, value) for level, value in paragraphs)
body += '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1701"/></w:sectPr>'

doc = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body>' + body + '</w:body></w:document>'

styles = Path(root / 'word_revision' / 'styles.xml').read_text(encoding='utf-8')
with ZipFile(out / 'revised.docx', 'w', ZIP_DEFLATED) as z:
    z.writestr('[Content_Types].xml', Path(root / 'word_revision' / 'content_types.xml').read_text(encoding='utf-8'))
    z.writestr('_rels/.rels', Path(root / 'word_revision' / 'package_rels.xml').read_text(encoding='utf-8'))
    z.writestr('word/document.xml', doc)
    z.writestr('word/styles.xml', styles)
    z.writestr('word/_rels/document.xml.rels', Path(root / 'word_revision' / 'document_rels.xml').read_text(encoding='utf-8'))
