from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether

OUT = "output/pdf/JobHub_ChatGPT_Handoff.pdf"

navy = colors.HexColor("#172033")
blue = colors.HexColor("#2563EB")
slate = colors.HexColor("#475467")
light = colors.HexColor("#F1F5F9")
line = colors.HexColor("#D0D5DD")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="CoverTitle", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=29, leading=34, textColor=navy, alignment=TA_CENTER, spaceAfter=12))
styles.add(ParagraphStyle(name="CoverSub", parent=styles["BodyText"], fontSize=12, leading=18, textColor=slate, alignment=TA_CENTER))
styles.add(ParagraphStyle(name="H1Custom", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=19, leading=24, textColor=navy, spaceBefore=6, spaceAfter=10))
styles.add(ParagraphStyle(name="H2Custom", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=13, leading=17, textColor=blue, spaceBefore=12, spaceAfter=5))
styles.add(ParagraphStyle(name="BodyCustom", parent=styles["BodyText"], fontName="Helvetica", fontSize=10, leading=15, textColor=navy, spaceAfter=7))
styles.add(ParagraphStyle(name="Prompt", parent=styles["BodyText"], fontName="Courier", fontSize=8.4, leading=12.5, backColor=light, borderColor=line, borderWidth=0.5, borderPadding=10, textColor=navy, spaceAfter=8))

def p(text, style="BodyCustom"):
    return Paragraph(text, styles[style])

def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(line)
    canvas.line(45, 40, A4[0] - 45, 40)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(slate)
    canvas.drawString(45, 27, "JobHub learning-project handoff")
    canvas.drawRightString(A4[0] - 45, 27, f"Page {doc.page}")
    canvas.restoreState()

doc = SimpleDocTemplate(OUT, pagesize=A4, rightMargin=45, leftMargin=45, topMargin=48, bottomMargin=55)
story = []

story += [Spacer(1, 1.2 * inch), p("JobHub", "CoverTitle"), p("Full-stack learning project - handoff prompt for a new ChatGPT conversation", "CoverSub"), Spacer(1, .45 * inch)]
story += [p("Purpose", "H2Custom"), p("This document preserves the learner's goals, teaching preferences, project state, and the work completed through Day 2. Paste the continuation prompt on the final page into a new normal ChatGPT chat.")]
story += [Spacer(1, .25 * inch), p("Current project", "H2Custom"), p("A JobHub job portal is being built from an empty repository. It will eventually use Python, Django, Django REST Framework, PostgreSQL, React, and deployment tools. The project is deliberately being built feature by feature, not learned as a separate theoretical study plan.")]
story.append(PageBreak())

story += [p("Learner profile and teaching rules", "H1Custom")]
rules = [
    ["Learner", "Knows Python basics, SQL, and HTML. Needs practical, beginner-friendly explanations while building."],
    ["Goal", "Build a production-style JobHub job portal in 30 days, while understanding how every added feature works."],
    ["Teaching method", "For each day: build one visible feature, explain what was added, explain the underlying concept, explain where it is used in real applications, then give a small edit/exercise."],
    ["Pacing", "Do not give a separate study plan. Do not dump a large amount of code. Progress day by day and explain terms in simple English."],
    ["Git habit", "Every day ends with: git status, git add -A, git commit -m with a meaningful message, and git push."],
    ["Important", "The learner wants to perform Git actions personally. Guide them with exact commands and explain what each command means."],
]
table = Table([[p(a), p(b)] for a, b in rules], colWidths=[1.35 * inch, 5.8 * inch])
table.setStyle(TableStyle([("BACKGROUND", (0, 0), (0, -1), light), ("GRID", (0, 0), (-1, -1), .4, line), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8), ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
story += [table]
story += [p("How to explain", "H2Custom"), p("Use simple language. Before using a technical word such as browser, server, API, database, component, or responsive design, briefly define it. When presenting code, explain the meaningful lines and why they are useful. Do not assume the learner understands; ask for a small confirmation or change after each feature.")]
story.append(PageBreak())

story += [p("Project and repository state", "H1Custom")]
story += [p("Repository: https://github.com/BalliMahesh/python_fullstack"), p("The remote GitHub branch is main. The learner's local branch was renamed from master to main, then connected to origin/main. Future pushes should work with just <font name='Courier'>git push</font> after running the one-time branch commands.")]
story += [p("Current project files", "H2Custom")]
files = [
    ["frontend/index.html", "JobHub landing page: navigation, hero area, search form, featured jobs, and how-it-works section."],
    ["frontend/styles.css", "Shared styles for the landing page and Job Details page. Original green palette remains; do not change colors unless the learner asks again."],
    ["frontend/job-details.html", "New Day 2 Job Details page."],
    ["readme.md", "Brief project notes."],
]
file_table = Table([[p(a), p(b)] for a, b in files], colWidths=[2.0 * inch, 5.15 * inch])
file_table.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.white), ("GRID", (0, 0), (-1, -1), .4, line), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8), ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
story += [file_table]
story += [p("Git history and cleanup", "H2Custom"), p("Day 1 was committed as <font name='Courier'>feat: add JobHub landing page</font> and pushed. Existing starter files, index.html and hello.py, were deleted by the learner. The empty duplicate README filename issue was resolved. Day 2 changes have been created but should be reviewed by the learner and then committed and pushed by the learner.")]
story.append(PageBreak())

story += [p("Completed work", "H1Custom"), p("Day 1 - JobHub landing page", "H2Custom")]
story += [p("Built a static candidate-facing home page. It contains a header/navigation area, a hero heading, a job-search form, three featured job cards, and a how-it-works section. CSS makes the layout adapt to smaller phone screens.")]
story += [p("Concepts explained: HTML provides the structure and content of the page. CSS provides color, spacing, layout, and responsive design. Git saves versions of the project locally. GitHub stores those versions online and is useful as a portfolio.")]
story += [p("Day 2 - Job Details page", "H2Custom")]
story += [p("Built frontend/job-details.html. The first job card on the landing page is now a link to this page. The Job Details page has a back link, job information, role description, responsibilities, requirements, and an Apply button. It uses the same styles.css file and responds to smaller screens.")]
story += [p("Concepts explained: an anchor tag such as <font name='Courier'>&lt;a href='job-details.html'&gt;</font> creates a link. The href attribute tells the browser which file to open. This is the basic browser navigation pattern used in product pages, profile pages, and job portals. Later, Django and PostgreSQL will replace hard-coded job information with data from a database.")]
story += [p("Next learner task", "H2Custom"), p("Ask the learner to open job-details.html, customize company, location, salary, and one responsibility. Then guide them to commit and push the Day 2 feature themselves using the daily Git workflow.")]
story.append(PageBreak())

story += [p("Continuation prompt for a new ChatGPT chat", "H1Custom")]
prompt = """You are my patient practical mentor for a 30-day Python Full Stack project called JobHub, a job portal. I already know Python basics, SQL, and HTML. Do not give me a separate study plan. Teach through building one small working feature per day.\n\nFor every feature: (1) tell me what we are building, (2) help me build it in small steps, (3) explain what we changed, (4) explain the concept in simple English and where it is useful in real projects, (5) give me one small change to try, and (6) finish by teaching me how to commit and push it myself. Define technical words briefly before using them. Do not rush or dump lots of code.\n\nProject status: GitHub repository is https://github.com/BalliMahesh/python_fullstack and the branch is main. The project currently has frontend/index.html, frontend/styles.css, frontend/job-details.html, and readme.md. Do not change the current colors unless I explicitly ask; I want to choose colors later.\n\nDay 1 is complete: I created a static JobHub landing page with navigation, job search form, featured job cards, and responsive CSS. I learned HTML structure, CSS styling, responsive design, Git, commits, and pushing to GitHub.\n\nDay 2 has been coded but I need to learn it and finalize it: frontend/job-details.html is a Job Details page. The first job card in index.html links to it using href='job-details.html'. It has job title, company, location, salary, role description, responsibilities, requirements, a back link, and an Apply button. Explain this page slowly, including how links work, why we use shared CSS, and why this is still static before a database. Then ask me to personalize a few job details. When I confirm, teach me how to run git status, git add -A, git commit -m 'feat: add job details page', and git push.\n\nAfter Day 2 is committed, continue Day 3 by building the next practical JobHub feature. Keep every lesson hands-on and beginner-friendly."""
story += [p(prompt.replace("\n", "<br/>"), "Prompt")]

doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUT)
