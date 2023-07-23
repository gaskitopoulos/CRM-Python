from PyPDF2 import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm


packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=letter)
can.setFont('Helvetica', 10)
can.drawString(170, 680, "ΟΝΟΜΑΤΕΠΩΝΥΜΟ")
can.drawString(400, 680, "ΚΑΤΗΓΟΡΙΑ ΠΕΛΑΤΗ")
can.drawString(85, 663, "ΔΙΕΥΘΥΝΣΗ")
can.drawString(335, 663, "ΤΚ")
can.drawString(430, 663, "ΠΟΛΗ")
can.drawString(115, 646, "ΑΔΤ")
can.drawString(258, 646, "ΑΦΜ")
can.drawString(372, 646, "ΔΟΥ")
can.drawString(497, 646, "ΙΔΙΟΤΗΤΑ")
can.drawString(85, 628, "ΣΤΑΘΕΡΟ")
can.drawString(256, 628, "ΚΙΝΗΤΟ")
can.drawString(376, 628, "EMAIL")
can.drawString(84, 530, "ΔΙΕΥΘΥΝΣΗ ΑΛΛΗΛΟΓΡΑΦΙΑΣ")
can.drawString(335, 530, "ΤΚ ΑΛΛ")
can.drawString(427, 530, "ΠΟΛΗ ΑΛΛ")
can.drawString(310, 474, "Γ1...")
can.drawString(480, 474, "ΧΑΜΗΛΗ ΤΑΣΗ")
can.drawString(83, 457, "ΔΙΕΥΘΥΝΣΗ ΠΑΡΟΧΗΣ")
can.drawString(335, 457, "ΤΚ ΠΑΡ")
can.drawString(503, 457, "ΠΟΛΗ ΠΑΡ")
can.drawString(427, 392, "ΕΓΓΥΗΣΗ")
can.setFillColorRGB(255,255,255)
can.rect(22, 388, 300, 15, stroke=0, fill=1)
can.setFillColorRGB(0,0,0)
can.drawString(36, 392, "ΠΡΟΓΡΑΜΜΑ")
can.setFont('Helvetica', 8)
can.drawString(226, 80, "ΘΕΣΣΑΛΟΝΙΚΗ ΗΜΕΡΟΜΗΝΙΑ")
can.setFont('Helvetica', 6)
can.drawString(460, 130, "HSH***")
can.setFont('Helvetica', 10)
can.setFillColorRGB(255,255,255)
can.rect(285, 512, 290, 10, stroke=0, fill=1)
can.setFillColorRGB(0,0,0)
can.drawString(29, 513, "X")
can.drawString(300, 513, "example@gmail.com")
can.save()

#move to the beginning of the StringIO buffer
packet.seek(0)

# create a new PDF with Reportlab
new_pdf = PdfReader(packet)
# read your existing PDF
existing_pdf = PdfReader(open("aitisi.pdf", "rb"))
output = PdfWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.pages[0]
page.merge_page(new_pdf.pages[0])
output.add_page(page)
# finally, write "output" to a real file
output_stream = open("final.pdf", "wb")
output.write(output_stream)
output_stream.close()
