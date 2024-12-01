from fpdf import FPDF


def main():
    name = input("Name: ")
    pdf(name)


def pdf(name):
    pdf = FPDF("p", "pt", "a4")
    pdf.add_page()

    pdf.set_text_color(0, 0, 0)
    pdf.set_font("helvetica", "B", size=40)
    pdf.cell(0, 40, "", new_x="LMARGIN", new_y="NEXT", align="C")  # empty box
    pdf.cell(0, None, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")

    pdf.image("shirtificate.png", x="C", y=192, w=525, h=524)

    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", size=20)
    pdf.cell(0, 256, "", new_x="LMARGIN", new_y="NEXT", align="C")  # empty box
    pdf.cell(0, None, f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")


main()
