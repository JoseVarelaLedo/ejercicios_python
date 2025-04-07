from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


def create_canvas(doc_title):
    cv = canvas.Canvas(f"{doc_title}.pdf", pagesize=A4)
    return cv


def draw_header(cv, nombre_cliente):
    cv.setFont("Courier", 30)
    cv.drawString(50, 780, "Factura")
    cv.setFont("Courier", 20)
    cv.drawString(50, 750, nombre_cliente)


def draw_logo(cv):
    logo = ImageReader('logo.jpg')
    cv.drawImage(logo, 400, 685, mask='auto')

def draw_lines(cv):
    cv.line(50,700, 50, 50)
    cv.line(350, 700, 350, 50)
    cv.line(420, 700, 420, 50)
    cv.line(480, 700, 480, 50)
    cv.line(540, 700, 540, 50)
    cv.line(50, 700, 540, 700)
    cv.line(50, 50, 540, 50)

def draw_concepts(cv, conceptos):
    y_pos = 650
    y_offset = -20
    for concepto in conceptos:
        cv.drawString(55, y_pos, f"{concepto[0]:15}{concepto[1]:15}{concepto[2]:4}€{concepto[1]*concepto[2]:4}€")
        y_pos+=y_offset

def save_canvas(cv):
    cv.save()