from pathlib import Path

from docx import Document
from docx.shared import Inches
from pptx import Presentation
from pptx.util import Inches as PtInches
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "docs"
SCREENSHOT_DIR = DOCS_DIR / "screenshots"
DOCS_DIR.mkdir(parents=True, exist_ok=True)
SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)


def make_placeholder(path: Path, label: str) -> None:
    img = Image.new("RGB", (1200, 675), color=(245, 245, 245))
    draw = ImageDraw.Draw(img)
    text = f"{label}"
    font = None
    try:
        font = ImageFont.truetype("arial.ttf", 42)
    except Exception:
        font = ImageFont.load_default()
    try:
        text_w, text_h = font.getsize(text)
    except Exception:
        bbox = draw.textbbox((0, 0), text, font=font)
        text_w, text_h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(((1200 - text_w) / 2, (675 - text_h) / 2), text, fill=(70, 70, 70), font=font)
    img.save(path)


login_screenshot = SCREENSHOT_DIR / "login.png"
dashboard_screenshot = SCREENSHOT_DIR / "dashboard.png"
for screenshot_path, label in [(login_screenshot, "Login Screenshot"), (dashboard_screenshot, "Dashboard Screenshot")]:
    if not screenshot_path.exists():
        make_placeholder(screenshot_path, label)

# Create Word document
writeup = Document()
writeup.add_heading("Unique Academy Student Attendance System", level=1)
writeup.add_paragraph(
    "This document presents the Unique Academy Student Attendance System, a Laravel-based application adapted for student attendance tracking, scheduling, late-time monitoring, and reporting."
)

writeup.add_heading("Project Overview", level=2)
writeup.add_paragraph(
    "The system was customized for Unique Academy and NACTVET NTA Level 5 ICT. It replaces generic clone branding with a student-focused attendance workflow and a simplified dashboard for academic administration."
)

writeup.add_heading("Core Features", level=2)
features = [
    "Student attendance recording with on-time and late tracking.",
    "Schedule management with subject and teacher details.",
    "Attendance review with search and date-based filtering.",
    "Late-time monitoring and attendance summary cards.",
    "Role-based access for admin and staff users.",
    "Clean branding for the Unique Academy portal.",
]
for item in features:
    writeup.add_paragraph(item, style="List Bullet")

writeup.add_heading("Raspberry Pi Database Hosting Plan", level=2)
writeup.add_paragraph(
    "The database can be hosted on a Raspberry Pi using MariaDB, which is lightweight and suitable for a small academic project deployment."
)
plan_items = [
    "Install MariaDB on the Raspberry Pi and create a database named unique_academy.",
    "Create a dedicated database user and grant access to the attendance schema.",
    "Update the Laravel .env file with the Raspberry Pi IP address, database name, username, and password.",
    "Ensure the Pi is reachable on the local network and port 3306 is open for the application server.",
    "Run php artisan migrate and test the login and attendance workflow against the remote database.",
]
for item in plan_items:
    writeup.add_paragraph(item, style="List Bullet")

writeup.add_paragraph("Example .env values:")
writeup.add_paragraph(
    "DB_CONNECTION=mysql\nDB_HOST=192.168.1.50\nDB_PORT=3306\nDB_DATABASE=unique_academy\nDB_USERNAME=unique_app\nDB_PASSWORD=StrongPassword123",
    style="Intense Quote",
)

writeup.add_heading("Implementation Highlights", level=2)
items = [
    "Added student_class and contact_phone fields for student records.",
    "Extended schedule management with subject_name and teacher_name fields.",
    "Updated the dashboard layout to focus on attendance metrics.",
    "Refined the UI title and branding for a more professional presentation.",
    "Prepared documentation assets for reports, presentations, and project delivery.",
]
for item in items:
    writeup.add_paragraph(item, style="List Number")

writeup.add_heading("Setup Instructions", level=2)
writeup.add_paragraph(
    "1. Copy .env.example to .env and configure the database.\n2. Run composer install.\n3. Run php artisan key:generate.\n4. Run php artisan migrate.\n5. Start the Laravel server and verify the system."
)

writeup.add_heading("Screenshots", level=2)
writeup.add_paragraph("The following screenshots capture the login page and the attendance dashboard used for the project documentation.")
writeup.add_picture(str(login_screenshot), width=Inches(6.0))
writeup.add_paragraph()
writeup.add_picture(str(dashboard_screenshot), width=Inches(6.0))

writeup_path = DOCS_DIR / "Unique_Academy_Attendance_System_Writeup.docx"
writeup.save(writeup_path)

# Create PowerPoint
presentation = Presentation()
layout_title = presentation.slide_layouts[0]
layout_content = presentation.slide_layouts[1]
layout_two_content = presentation.slide_layouts[3] if len(presentation.slide_layouts) > 3 else presentation.slide_layouts[1]

slide = presentation.slides.add_slide(layout_title)
title = slide.shapes.title
subtitle = slide.placeholders[1]
title.text = "Unique Academy Student Attendance System"
subtitle.text = "Laravel project for student attendance, scheduling, and reporting."


def body_placeholder(slide):
    for shape in slide.shapes:
        if shape.is_placeholder and shape.placeholder_format.idx != 0:
            return shape.text_frame
    raise ValueError("No body placeholder found")

slide = presentation.slides.add_slide(layout_content)
title = slide.shapes.title
body = body_placeholder(slide)
body.text = "Project Objective"
for bullet in [
    "Adapt an existing attendance system for Unique Academy.",
    "Remove clone branding and add student-focused features.",
    "Deliver a practical solution for attendance management and reporting.",
]:
    p = body.add_paragraph()
    p.text = bullet
    p.level = 0

slide = presentation.slides.add_slide(layout_content)
title = slide.shapes.title
body = body_placeholder(slide)
body.text = "Key Features"
for bullet in [
    "Student attendance recording with on-time and late status.",
    "Schedule entries that include subject and teacher details.",
    "Attendance dashboard with search and date filtering.",
    "Role-based admin and staff access.",
]:
    p = body.add_paragraph()
    p.text = bullet
    p.level = 0

slide = presentation.slides.add_slide(layout_content)
title = slide.shapes.title
body = body_placeholder(slide)
body.text = "Raspberry Pi Database Hosting"
for bullet in [
    "Use MariaDB on a Raspberry Pi for the project database.",
    "Create a dedicated database and user for the Laravel application.",
    "Point the app to the Pi IP address in the Laravel environment file.",
    "Test the connection and run migrations from the application server.",
]:
    p = body.add_paragraph()
    p.text = bullet
    p.level = 0

slide = presentation.slides.add_slide(layout_two_content)
title = slide.shapes.title
body = body_placeholder(slide)
body.text = "Implementation Highlights"
for bullet in [
    "New student_class and contact_phone fields added.",
    "Attendance summary cards show total, on-time, late, and percentage.",
    "The UI was cleaned and branded for Unique Academy.",
    "Project documentation and presentation assets were generated.",
]:
    p = body.add_paragraph()
    p.text = bullet
    p.level = 0

slide = presentation.slides.add_slide(layout_content)
title = slide.shapes.title
body = body_placeholder(slide)
body.text = "Screenshots"
for bullet in [
    "Login screen captured from the running application.",
    "Dashboard view captured after authentication.",
]:
    p = body.add_paragraph()
    p.text = bullet
    p.level = 0

slide = presentation.slides.add_slide(layout_content)
title = slide.shapes.title
body = body_placeholder(slide)
body.text = "Thank You"
for bullet in [
    "Unique Academy Student Attendance System",
    "Prepared for NACTVET NTA Level 5 ICT.",
]:
    p = body.add_paragraph()
    p.text = bullet
    p.level = 0

pptx_path = DOCS_DIR / "Unique_Academy_Attendance_System_Presentation.pptx"
presentation.save(pptx_path)

print(f"Generated: {writeup_path}")
print(f"Generated: {pptx_path}")
print(f"Login screenshot: {login_screenshot}")
print(f"Dashboard screenshot: {dashboard_screenshot}")
