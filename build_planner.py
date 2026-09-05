import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.colors import HexColor

# Setup colors
COLOR_PEACH = HexColor("#F4C4B5")
COLOR_BLUSH = HexColor("#F9D3D3")
COLOR_GOLD = HexColor("#C5A059")
COLOR_CREAM = HexColor("#FDFBF7")
COLOR_ROSE = HexColor("#B87375")
COLOR_DARK_TEXT = HexColor("#4A403F")
COLOR_LIGHT_BOX = HexColor("#FFFFFF")
COLOR_DIVIDER = HexColor("#E8D8D8")

# Setup page size
PAGE_WIDTH = 768
PAGE_HEIGHT = 1024

def draw_background(c):
    c.setFillColor(COLOR_CREAM)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, stroke=0, fill=1)

def draw_tabs(c):
    # Right side tabs
    tabs = [
        ("Home", "index_page", PAGE_HEIGHT - 100),
        ("Daily", "daily_page", PAGE_HEIGHT - 200),
        ("Weekly", "weekly_page", PAGE_HEIGHT - 300),
    ]

    for label, dest, y_pos in tabs:
        # Draw tab shape
        c.setFillColor(COLOR_BLUSH)
        c.setStrokeColor(COLOR_GOLD)
        c.setLineWidth(1)
        # A simple rounded rect for tab
        tab_w = 40
        tab_h = 80
        c.roundRect(PAGE_WIDTH - 20, y_pos - tab_h/2, tab_w, tab_h, 10, stroke=1, fill=1)

        # Add text
        c.saveState()
        c.translate(PAGE_WIDTH - 5, y_pos)
        c.rotate(270)
        c.setFillColor(COLOR_DARK_TEXT)
        c.setFont("Helvetica", 12)
        c.drawCentredString(0, 0, label)
        c.restoreState()

        # Add link
        # rect format: (x1, y1, x2, y2)
        rect = (PAGE_WIDTH - 20, y_pos - tab_h/2, PAGE_WIDTH + 20, y_pos + tab_h/2)
        c.linkAbsolute("", dest, rect)

def draw_cover(c):
    c.bookmarkPage("cover_page")
    draw_background(c)

    # Decorative organic shapes
    c.setFillColor(COLOR_PEACH)
    c.circle(PAGE_WIDTH * 0.2, PAGE_HEIGHT * 0.8, 150, stroke=0, fill=1)
    c.setFillColor(COLOR_BLUSH)
    c.circle(PAGE_WIDTH * 0.8, PAGE_HEIGHT * 0.2, 200, stroke=0, fill=1)

    # Elegant border
    c.setStrokeColor(COLOR_GOLD)
    c.setLineWidth(2)
    c.rect(50, 50, PAGE_WIDTH - 100, PAGE_HEIGHT - 100)
    c.rect(55, 55, PAGE_WIDTH - 110, PAGE_HEIGHT - 110)

    # Floral/line art element (simple placeholder via lines/bezier)
    c.setStrokeColor(COLOR_ROSE)
    c.setLineWidth(1.5)
    c.bezier(PAGE_WIDTH*0.5, PAGE_HEIGHT*0.6,
             PAGE_WIDTH*0.6, PAGE_HEIGHT*0.7,
             PAGE_WIDTH*0.4, PAGE_HEIGHT*0.8,
             PAGE_WIDTH*0.5, PAGE_HEIGHT*0.9)
    # small leaves
    c.circle(PAGE_WIDTH*0.53, PAGE_HEIGHT*0.75, 5, stroke=1, fill=0)
    c.circle(PAGE_WIDTH*0.47, PAGE_HEIGHT*0.85, 5, stroke=1, fill=0)

    # Title text
    c.setFillColor(COLOR_DARK_TEXT)
    c.setFont("Helvetica-Bold", 48)
    c.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT / 2 + 50, "Scripture Writing Planner")

    # Subtitle text
    c.setFont("Helvetica", 24)
    c.setFillColor(COLOR_ROSE)
    c.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT / 2 - 20, "A Daily Journey in the Word")

    c.showPage()

def draw_index(c):
    c.bookmarkPage("index_page")
    draw_background(c)
    draw_tabs(c)

    c.setFillColor(COLOR_DARK_TEXT)
    c.setFont("Helvetica-Bold", 36)
    c.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 100, "Index")

    # Add beautiful dividers
    c.setStrokeColor(COLOR_GOLD)
    c.setLineWidth(1)
    c.line(PAGE_WIDTH/2 - 100, PAGE_HEIGHT - 120, PAGE_WIDTH/2 + 100, PAGE_HEIGHT - 120)

    sections = [
        ("Daily Layout", "daily_page"),
        ("Weekly Layout", "weekly_page")
    ]

    y = PAGE_HEIGHT - 250
    for title, dest in sections:
        # Button shape
        c.setFillColor(COLOR_LIGHT_BOX)
        c.setStrokeColor(COLOR_PEACH)
        c.roundRect(PAGE_WIDTH/2 - 150, y, 300, 60, 15, stroke=1, fill=1)

        c.setFillColor(COLOR_DARK_TEXT)
        c.setFont("Helvetica", 20)
        c.drawCentredString(PAGE_WIDTH / 2, y + 22, title)

        rect = (PAGE_WIDTH/2 - 150, y, PAGE_WIDTH/2 + 150, y + 60)
        c.linkAbsolute("", dest, rect)

        y -= 100

    c.showPage()

def draw_daily(c):
    c.bookmarkPage("daily_page")
    draw_background(c)
    draw_tabs(c)

    # Header
    c.setFillColor(COLOR_DARK_TEXT)
    c.setFont("Helvetica-Bold", 32)
    c.drawString(60, PAGE_HEIGHT - 80, "Daily Scripture")

    # Date box
    c.setFillColor(COLOR_LIGHT_BOX)
    c.setStrokeColor(COLOR_DIVIDER)
    c.setLineWidth(1)
    c.roundRect(PAGE_WIDTH - 250, PAGE_HEIGHT - 90, 150, 40, 10, stroke=1, fill=1)
    c.setFillColor(COLOR_ROSE)
    c.setFont("Helvetica", 14)
    c.drawString(PAGE_WIDTH - 240, PAGE_HEIGHT - 75, "Date:")

    # Gold divider
    c.setStrokeColor(COLOR_GOLD)
    c.line(60, PAGE_HEIGHT - 110, PAGE_WIDTH - 60, PAGE_HEIGHT - 110)

    # Boxes
    c.setFillColor(COLOR_LIGHT_BOX)
    c.setStrokeColor(COLOR_PEACH)

    # Scripture Box
    c.roundRect(60, PAGE_HEIGHT - 350, PAGE_WIDTH - 120, 200, 10, stroke=1, fill=1)
    c.setFillColor(COLOR_ROSE)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(80, PAGE_HEIGHT - 180, "Scripture")

    # Observation Box
    c.setFillColor(COLOR_LIGHT_BOX)
    c.roundRect(60, PAGE_HEIGHT - 600, PAGE_WIDTH - 120, 220, 10, stroke=1, fill=1)
    c.setFillColor(COLOR_ROSE)
    c.drawString(80, PAGE_HEIGHT - 410, "Observation")

    # Application Box
    c.setFillColor(COLOR_LIGHT_BOX)
    c.roundRect(60, PAGE_HEIGHT - 800, PAGE_WIDTH/2 - 70, 170, 10, stroke=1, fill=1)
    c.setFillColor(COLOR_ROSE)
    c.drawString(80, PAGE_HEIGHT - 660, "Application")

    # Prayer Box
    c.setFillColor(COLOR_LIGHT_BOX)
    c.roundRect(PAGE_WIDTH/2 + 10, PAGE_HEIGHT - 800, PAGE_WIDTH/2 - 70, 170, 10, stroke=1, fill=1)
    c.setFillColor(COLOR_ROSE)
    c.drawString(PAGE_WIDTH/2 + 30, PAGE_HEIGHT - 660, "Prayer")

    # Decorative subtle heart
    c.setStrokeColor(COLOR_BLUSH)
    c.setFillColor(COLOR_BLUSH)
    # Simple polygon approximation for heart or just small circle for gentle sparkle
    c.circle(PAGE_WIDTH - 100, 80, 5, stroke=0, fill=1)
    c.circle(PAGE_WIDTH - 115, 95, 3, stroke=0, fill=1)

    c.showPage()

def draw_weekly(c):
    c.bookmarkPage("weekly_page")
    draw_background(c)
    draw_tabs(c)

    c.setFillColor(COLOR_DARK_TEXT)
    c.setFont("Helvetica-Bold", 32)
    c.drawString(60, PAGE_HEIGHT - 80, "Weekly Reflection")

    c.setStrokeColor(COLOR_GOLD)
    c.line(60, PAGE_HEIGHT - 110, PAGE_WIDTH - 60, PAGE_HEIGHT - 110)

    # 7 boxes for days
    box_width = (PAGE_WIDTH - 140) / 2
    box_height = 100

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    c.setFillColor(COLOR_LIGHT_BOX)
    c.setStrokeColor(COLOR_DIVIDER)

    y = PAGE_HEIGHT - 230
    for i in range(4):
        # Left column
        c.setFillColor(COLOR_LIGHT_BOX)
        c.roundRect(60, y, box_width, box_height, 10, stroke=1, fill=1)
        c.setFillColor(COLOR_ROSE)
        c.setFont("Helvetica", 14)
        c.drawString(75, y + box_height - 25, days[i])

        # Right column
        if i + 4 < 7:
            c.setFillColor(COLOR_LIGHT_BOX)
            c.roundRect(60 + box_width + 20, y, box_width, box_height, 10, stroke=1, fill=1)
            c.setFillColor(COLOR_ROSE)
            c.drawString(75 + box_width + 20, y + box_height - 25, days[i+4])
        else:
            # Memory verse box in the empty space
            c.setFillColor(COLOR_PEACH)
            c.roundRect(60 + box_width + 20, y, box_width, box_height, 10, stroke=0, fill=1)
            c.setFillColor(COLOR_DARK_TEXT)
            c.setFont("Helvetica-Bold", 14)
            c.drawString(75 + box_width + 20, y + box_height - 25, "Memory Verse")
            c.setStrokeColor(COLOR_GOLD)
            c.line(75 + box_width + 20, y + box_height - 35, 75 + box_width * 2 - 20, y + box_height - 35)
            c.setStrokeColor(COLOR_DIVIDER) # reset

        y -= (box_height + 20)

    # Note area at bottom
    c.setFillColor(COLOR_LIGHT_BOX)
    c.roundRect(60, 100, PAGE_WIDTH - 120, y - 100, 10, stroke=1, fill=1)
    c.setFillColor(COLOR_ROSE)
    c.drawString(80, y - 30, "Notes")

    c.showPage()


def build_pdf(filename="Scripture_Writing_Planner.pdf"):
    c = canvas.Canvas(filename, pagesize=(PAGE_WIDTH, PAGE_HEIGHT))
    c.setTitle("Scripture Writing Planner")

    draw_cover(c)
    draw_index(c)
    draw_daily(c)
    draw_weekly(c)

    c.save()

if __name__ == "__main__":
    build_pdf()
