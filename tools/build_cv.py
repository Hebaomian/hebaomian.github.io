"""Generate the public English CV; the original private resume stays local."""
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "CV.pdf"
PURPLE = colors.HexColor("#70509a")
INK = colors.HexColor("#332d3b")
MUTED = colors.HexColor("#746c7c")
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="NameCV", fontName="Helvetica-Bold", fontSize=25, leading=30, textColor=INK, spaceAfter=5))
styles.add(ParagraphStyle(name="SubtitleCV", fontName="Helvetica", fontSize=10, leading=15, textColor=PURPLE, spaceAfter=7))
styles.add(ParagraphStyle(name="ContactCV", fontName="Helvetica", fontSize=8.5, leading=13, textColor=MUTED, spaceAfter=15))
styles.add(ParagraphStyle(name="SectionCV", fontName="Helvetica-Bold", fontSize=12, leading=16, textColor=PURPLE, spaceBefore=14, spaceAfter=7))
styles.add(ParagraphStyle(name="TitleCV", fontName="Helvetica-Bold", fontSize=10, leading=14, textColor=INK, spaceAfter=3))
styles.add(ParagraphStyle(name="BodyCV", fontName="Helvetica", fontSize=9, leading=13.4, textColor=INK, spaceAfter=6))
styles.add(ParagraphStyle(name="MetaCV", fontName="Helvetica", fontSize=8.2, leading=12.1, textColor=MUTED, spaceAfter=5))
styles.add(ParagraphStyle(name="BulletCV", fontName="Helvetica", fontSize=8.8, leading=13, leftIndent=10, firstLineIndent=-8, textColor=INK, spaceAfter=4))

story = []
def p(text, kind="BodyCV"):
    return Paragraph(text, styles[kind])
def add(text, kind="BodyCV"):
    story.append(p(text, kind))
def section(title):
    add(title, "SectionCV")
def entry(title, meta, body=None):
    content = [p(title, "TitleCV"), p(meta, "MetaCV")]
    if body:
        content.append(p(body))
    story.append(KeepTogether(content))

add("Zishuo Zhao", "NameCV")
add("LLM Agents | Reinforcement Learning | NLP | Multimodal Learning", "SubtitleCV")
add('Alibaba International | Hangzhou, China<br/>'
    '<link href="mailto:zhaozsh@alumni.sysu.edu.cn" color="#70509a">zhaozsh@alumni.sysu.edu.cn</link> '
    '| <link href="https://github.com/Hebaomian" color="#70509a">GitHub: Hebaomian</link> '
    '| <link href="https://scholar.google.com/citations?user=PjFPF9MAAAAJ&amp;hl=en" color="#70509a">Google Scholar</link>', "ContactCV")
section("Research Interests")
add("Large language model agents and reinforcement learning, with an emphasis on multi-turn preference learning, turn-level alignment, planning, reasoning, and tool use. Additional interests include source-free domain adaptation and multimodal retrieval.")
section("Experience")
entry("Alibaba International", "LLM Agents &amp; Reinforcement Learning | Jul 2024 - Present")
for text in [
    "<b>Customer service agents:</b> Contributed to AliExpress pre-sales and after-sales agents, including planner-reasoner architectures, tool calling, reward evaluation, and preference alignment using DPO and GRPO.",
    "<b>Multimodal review:</b> Contributed to image-based review workflows using multimodal models, OCR, image classification, and preference alignment.",
    "<b>Voice agents:</b> Worked on Lazada inbound customer service and ICBU outbound voice agents, including planning, knowledge grounding, interruption handling, and order understanding.",
    "<b>Agent learning:</b> First-author work on Turn-level Multiscale Density Ratio Estimation for LLM Agents (arXiv:2609.16760).",
]:
    add("- " + text, "BulletCV")
story.append(Spacer(1, 8))
entry("Alibaba International", "Research Intern | Dec 2023 - Feb 2024", "Explored RLHF and DPO for customer service language models, reinforcement learning frameworks, and automated model evaluation.")
story.append(Spacer(1, 6))
entry("Tencent AI Lab", "Research Intern | May 2023 - Oct 2023", "Worked on LLM role-playing, real-time game commentary, and report generation. Participated in research on PPO-based methods for extending model input context.")
section("Education")
entry("Sun Yat-sen University", "Master's degree in Intelligent Control | Sep 2021 - Jun 2024", "School of Intelligent Systems Engineering | Shenzhen, China")
story.append(Spacer(1, 4))
entry("Sun Yat-sen University", "Bachelor's degree in Computational Materials | Sep 2017 - Jun 2021", "School of Materials | Guangzhou, China")

story.append(PageBreak())
add("Zishuo Zhao", "NameCV")
add("Publications &amp; Research", "SubtitleCV")
section("Preprints")
publications = [
    ("Turn-level Multiscale Density Ratio Estimation for LLM Agents", "Zishuo Zhao, Kai Chen, Ao Li, Yuan Liu", "arXiv:2609.16760, 2026", "https://arxiv.org/abs/2609.16760"),
    ("FLEX-CLIP: Feature-Level GEneration Network Enhanced CLIP for X-shot Cross-modal Retrieval", "Jingyou Xie, Jiayi Kuang, Zhenzhou Lin, Jiarui Ouyang, Zishuo Zhao, Ying Shen", "arXiv:2411.17454, 2024", "https://arxiv.org/abs/2411.17454"),
]
conference = [
    ("Source-free Domain Adaptation for Aspect-based Sentiment Analysis", "Zishuo Zhao, Ziyang Ma, Zhenzhou Lin, Jingyou Xie, Yinghui Li, Ying Shen", "LREC-COLING 2024, pp. 15076-15086", "https://aclanthology.org/2024.lrec-main.1310/"),
    ("Source-Free Unsupervised Domain Adaptation for Question Answering", "Zishuo Zhao, Yuexiang Xie, Jingyou Xie, Zhenzhou Lin, Yaliang Li, Ying Shen", "ICASSP 2023, pp. 1-5", None),
    ("Hierarchical Type Enhanced Negative Sampling for Knowledge Graph Embedding", "Zhenzhou Lin, Zishuo Zhao, Jingyou Xie, Ying Shen", "SIGIR 2023, pp. 2047-2051", "https://doi.org/10.1145/3539618.3591996"),
    ("Multimodal Graph Learning for Cross-Modal Retrieval", "Jingyou Xie, Zishuo Zhao, Zhenzhou Lin, Ying Shen", "SDM 2023, pp. 145-153", "https://doi.org/10.1137/1.9781611977653.ch17"),
]
def paper(item):
    title, authors, venue, url = item
    title = escape(title)
    if url:
        title = f'<link href="{escape(url)}" color="#533574">{title}</link>'
    authors = escape(authors).replace("Zishuo Zhao", "<b>Zishuo Zhao</b>")
    story.append(KeepTogether([p(title, "TitleCV"), p(authors, "BodyCV"), p(escape(venue), "MetaCV"), Spacer(1, 9)]))
for item in publications:
    paper(item)
section("Conference Papers")
for item in conference:
    paper(item)
section("Skills")
add("<b>Programming &amp; frameworks:</b> Python, verl<br/><b>Methods:</b> DPO, GRPO, RLHF, LLM agent development, multimodal learning<br/><b>Languages:</b> English (CET-6, CET-4)")

def footer(canvas, doc):
    width, height = A4
    canvas.setStrokeColor(colors.HexColor("#dfd4e9"))
    canvas.setLineWidth(0.6)
    canvas.line(44, 34, width-44, 34)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(MUTED)
    canvas.drawString(44, 22, "Zishuo Zhao | Public English CV | October 2026")
    canvas.drawRightString(width-44, 22, str(doc.page))

doc = SimpleDocTemplate(str(OUT), pagesize=A4, rightMargin=44, leftMargin=44, topMargin=35, bottomMargin=48,
    title="Zishuo Zhao - Curriculum Vitae", author="Zishuo Zhao", subject="Public English curriculum vitae")
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUT)
