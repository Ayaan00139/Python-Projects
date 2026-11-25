from fpdf import FPDF

name = input("Name: ")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False)
pdf.add_page()

pdf.set_font("helvetica", "B", 40)
pdf.cell(w=0, h=40, txt="CS50 Shirtificate", align="C")

pdf.image("shirtificate.png", x=10, y=70, w=190)

pdf.set_font("helvetica", "B", 24)
pdf.set_text_color(255, 255, 255)
pdf.set_xy(0, 140)
pdf.cell(w=210, h=10, txt=f"{name} took CS50", align="C")

pdf.output("shirtificate.pdf")
