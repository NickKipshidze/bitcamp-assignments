from fpdf import FPDF

shirt_text = input("Name: ")
shirt_image = "./shirtificate.png"

document = FPDF(orientation="portrait")

document.add_page()
document.set_font("Arial", size=64)

document.cell(0, 75, txt="CS50 Shirtificate", align="C")
document.image(shirt_image, x=0, y=85, w=210)

document.set_font("Arial", size=32)
document.set_text_color((255, 255, 255))
document.cell(-190, 300, txt=shirt_text, align="C")

document.output("shirtificate.pdf")