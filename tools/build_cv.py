"""Build an English academic CV using embedded Computer Modern Unicode fonts."""
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether, Table,
    TableStyle, Flowable,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets' / 'CV.pdf'
FONT_DIR = ROOT / 'assets' / 'fonts' / 'cmu'
for name, filename in [('CMU', 'cmunrm.ttf'), ('CMU-Bold', 'cmunbx.ttf'),
                       ('CMU-Italic', 'cmunti.ttf'), ('CMU-BoldItalic', 'cmunbi.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(FONT_DIR / filename)))
pdfmetrics.registerFontFamily('CMU', normal='CMU', bold='CMU-Bold', italic='CMU-Italic', boldItalic='CMU-BoldItalic')
INK = colors.HexColor('#171717')
GRAY = colors.HexColor('#555555')
LINK = '#263f8e'
PAGE_W, PAGE_H = A4
MARGIN = 39.685
WIDTH = PAGE_W - 2 * MARGIN
BASE = dict(fontName='CMU', fontSize=10.9, leading=13.6, textColor=INK)
styles = {
    'body': ParagraphStyle('body', **BASE, spaceAfter=5),
    'name': ParagraphStyle('name', fontName='CMU-Bold', fontSize=16, leading=20, alignment=TA_CENTER, spaceAfter=4),
    'subtitle': ParagraphStyle('subtitle', **BASE, alignment=TA_CENTER, spaceAfter=10),
    'contact': ParagraphStyle('contact', **(BASE | dict(fontSize=9.9, leading=13.3))),
    'right': ParagraphStyle('right', **(BASE | dict(fontSize=9.9, leading=13.3)), alignment=TA_RIGHT),
    'detail': ParagraphStyle('detail', fontName='CMU-Italic', fontSize=9.6, leading=12.6, textColor=INK, spaceAfter=3),
    'date': ParagraphStyle('date', fontName='CMU-Italic', fontSize=9.4, leading=13.6, alignment=TA_RIGHT, textColor=INK),
    'entry': ParagraphStyle('entry', **(BASE | dict(fontName='CMU-Bold'))),
    'bullet': ParagraphStyle('bullet', **BASE, leftIndent=10, firstLineIndent=-10, spaceAfter=5),
    'pub': ParagraphStyle('pub', **BASE, leftIndent=16, firstLineIndent=-16, spaceAfter=12),
    'subhead': ParagraphStyle('subhead', fontName='CMU-Italic', fontSize=10.5, leading=14, textColor=GRAY, spaceAfter=7, spaceBefore=4),
}

def para(text, style='body'):
    return Paragraph(text, styles[style])

def link(label, url):
    return f'<link href="{escape(url, {chr(34): "&quot;"})}" color="{LINK}">{escape(label)}</link>'

class Section(Flowable):
    """Small capitals and a thin rule, as in the reference academic CV."""
    def __init__(self, title):
        super().__init__()
        self.title = title
        self.height = 29
        self.keepWithNext = True
    def wrap(self, availWidth, availHeight):
        self.width = availWidth
        return availWidth, self.height
    def draw(self):
        c = self.canv
        c.setFillColor(INK)
        x = 0
        for word in self.title.split(' '):
            for i, char in enumerate(word):
                size = 12 if i == 0 else 9.6
                c.setFont('CMU-Bold', size)
                c.drawString(x, 10, char.upper())
                x += pdfmetrics.stringWidth(char.upper(), 'CMU-Bold', size)
            x += 3.3
        c.setStrokeColor(INK)
        c.setLineWidth(.4)
        c.line(0, 5.5, self.width, 5.5)

story = []
def add(text, style='body'):
    story.append(para(text, style))
def section(title):
    story.append(Section(title))
def entry(title, dates, detail=None, body=None):
    table = Table([[para(title, 'entry'), para(dates, 'date')]], colWidths=[WIDTH-155,155])
    table.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'), ('LEFTPADDING',(0,0),(-1,-1),0),
        ('RIGHTPADDING',(0,0),(-1,-1),0), ('TOPPADDING',(0,0),(-1,-1),0), ('BOTTOMPADDING',(0,0),(-1,-1),2)]))
    elements = [table]
    if detail:
        elements.append(para(detail, 'detail'))
    if body:
        elements.append(para(body))
    story.append(KeepTogether(elements))

add('Zishuo Zhao', 'name')
add('Alibaba Holding', 'subtitle')
contact = Table([[para('Alibaba Group Holding Limited<br/>Hangzhou, China', 'contact'),
    para(link('zhaozsh@alumni.sysu.edu.cn','mailto:zhaozsh@alumni.sysu.edu.cn')+'<br/>'+link('hebaomian.github.io','https://hebaomian.github.io/'), 'right')],
    [para('LLM Agents &amp; Reinforcement Learning', 'contact'),
    para(link('Google Scholar','https://scholar.google.com/citations?user=PjFPF9MAAAAJ&hl=en')+' &nbsp; | &nbsp; '+link('GitHub','https://github.com/Hebaomian'), 'right')]], colWidths=[WIDTH/2]*2)
contact.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0)]))
story.append(contact)

section('Research Interests')
add('My research focuses on <b>large language model agents and reinforcement learning</b>, particularly learning from multi-turn interactions, preference alignment, reasoning, and tool use.')
for text in [
    '<b>Agentic reinforcement learning:</b> Multi-turn preference learning, turn-level credit assignment, and alignment for LLM agents.',
    '<b>Natural language processing:</b> Source-free domain adaptation for question answering and aspect-based sentiment analysis.',
    '<b>Multimodal learning:</b> Cross-modal retrieval, multimodal graph learning, and vision-language applications.',
]:
    add('• '+text, 'bullet')

section('Education')
entry('Sun Yat-sen University', 'Sep 2021 - Jun 2024',
      "Master's degree in Intelligent Control", 'School of Intelligent Systems Engineering, Shenzhen, China')
story.append(Spacer(1,3))
entry('Sun Yat-sen University', 'Sep 2017 - Jun 2021',
      "Bachelor's degree in Computational Materials", 'School of Materials, Guangzhou, China')

section('Professional Experience')
entry('Alibaba Holding', 'Aug 3, 2026 - Present', 'Alibaba Group Holding Limited')
story.append(Spacer(1,7))
entry('Alibaba International', 'Jul 2024 - Jul 3, 2026', 'LLM Agents &amp; Reinforcement Learning')
for text in [
    '<b>Customer service agents:</b> Contributed to AliExpress pre-sales and after-sales agents, including planner-reasoner architectures, tool calling, reward evaluation, and alignment with DPO and GRPO.',
    '<b>Multimodal review:</b> Worked on image-based review with multimodal models, OCR, image classification, and preference alignment.',
    '<b>Voice agents:</b> Worked on Lazada inbound and ICBU outbound voice agents, covering planning, knowledge grounding, interruption handling, and order understanding.',
]:
    add('• '+text, 'bullet')
story.append(Spacer(1,7))
entry('Alibaba International', 'Dec 2023 - Feb 2024', 'Research Intern',
    'Explored RLHF and DPO for customer service language models, reinforcement learning frameworks, and automated model evaluation.')
story.append(Spacer(1,7))
entry('Tencent AI Lab', 'May 2023 - Oct 2023', 'Research Intern',
    'Worked on LLM role-playing, game commentary, and report generation. Participated in research on PPO-based methods for extending model input context.')

story.append(PageBreak())
section('Publications')
add('Preprints', 'subhead')
publications = [
    ('Turn-level Multiscale Density Ratio Estimation for LLM Agents',
     'Zishuo Zhao, Kai Chen, Ao Li, Yuan Liu', 'arXiv:2609.16760, 2026', 'https://arxiv.org/abs/2609.16760'),
    ('FLEX-CLIP: Feature-Level GEneration Network Enhanced CLIP for X-shot Cross-modal Retrieval',
     'Jingyou Xie, Jiayi Kuang, Zhenzhou Lin, Jiarui Ouyang, Zishuo Zhao, Ying Shen',
     'arXiv:2411.17454, 2024', 'https://arxiv.org/abs/2411.17454'),
]
conference = [
    ('Source-free Domain Adaptation for Aspect-based Sentiment Analysis',
     'Zishuo Zhao, Ziyang Ma, Zhenzhou Lin, Jingyou Xie, Yinghui Li, Ying Shen',
     'LREC-COLING 2024, pp. 15076-15086', 'https://aclanthology.org/2024.lrec-main.1310/'),
    ('Source-Free Unsupervised Domain Adaptation for Question Answering',
     'Zishuo Zhao, Yuexiang Xie, Jingyou Xie, Zhenzhou Lin, Yaliang Li, Ying Shen',
     'IEEE ICASSP 2023, pp. 1-5', None),
    ('Hierarchical Type Enhanced Negative Sampling for Knowledge Graph Embedding',
     'Zhenzhou Lin, Zishuo Zhao, Jingyou Xie, Ying Shen',
     'ACM SIGIR 2023, pp. 2047-2051', 'https://doi.org/10.1145/3539618.3591996'),
    ('Multimodal Graph Learning for Cross-Modal Retrieval',
     'Jingyou Xie, Zishuo Zhao, Zhenzhou Lin, Ying Shen',
     'SIAM SDM 2023, pp. 145-153', 'https://doi.org/10.1137/1.9781611977653.ch17'),
]

def paper(item, number):
    title, authors, venue, url = item
    authors = escape(authors).replace('Zishuo Zhao','<b>Zishuo Zhao</b>')
    title = escape(title)
    if url:
        title = f'<link href="{escape(url)}" color="{LINK}">{title}</link>'
    add(f'[{number}] {authors}.<br/>{title}.<br/><i>{escape(venue)}.</i>', 'pub')
for i, item in enumerate(publications, 1):
    paper(item, i)
add('Conference Papers', 'subhead')
for i, item in enumerate(conference, 3):
    paper(item, i)
section('Technical Skills')
add('<b>Programming and frameworks:</b> Python, verl.<br/>'
    '<b>Methods:</b> DPO, GRPO, RLHF, LLM agent development, and multimodal learning.<br/>'
    '<b>Languages:</b> English (CET-6, CET-4).')

def footer(canvas, doc):
    canvas.setFillColor(GRAY)
    canvas.setFont('CMU', 9)
    canvas.drawCentredString(PAGE_W/2, 24, 'Last updated: October 20, 2026')
    canvas.drawRightString(PAGE_W-MARGIN, 24, str(doc.page))
    if doc.page > 1:
        canvas.setFont('CMU-Italic',9)
        canvas.drawString(MARGIN, PAGE_H-24, 'Zishuo Zhao')
        canvas.drawRightString(PAGE_W-MARGIN,PAGE_H-24,'Curriculum Vitae')

OUT.parent.mkdir(parents=True, exist_ok=True)
doc = SimpleDocTemplate(str(OUT), pagesize=A4, rightMargin=MARGIN-6,leftMargin=MARGIN-6,
    topMargin=24,bottomMargin=42,title='Zishuo Zhao - Curriculum Vitae',author='Zishuo Zhao',
    subject='English academic curriculum vitae')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print(OUT)
