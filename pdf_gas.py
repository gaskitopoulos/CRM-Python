from PyPDF2 import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm


packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=letter)
can.setFont('Helvetica', 10)
can.drawString(170, 699, "ΟΝΟΜΑΤΕΠΩΝΥΜΟ")
can.drawString(458, 699, "ΚΑΤΗΓΟΡΙΑ ΠΕΛΑΤΗ")
can.drawString(82, 683, "ΔΙΕΥΘΥΝΣΗ")
can.drawString(318, 683, "ΤΚ")
can.drawString(440, 683, "ΠΟΛΗ")
can.drawString(115, 666, "ΑΔΤ")
can.drawString(232, 666, "ΑΦΜ")
can.drawString(342, 666, "ΔΟΥ")
can.drawString(469, 666, "ΙΔΙΟΤΗΤΑ")
can.drawString(82, 649, "ΣΤΑΘΕΡΟ")
can.setFont('Helvetica', 6)
can.drawString(136, 620, "ΝΟΜΙΜΟΣ ΕΚΠΡΟΣΩΠΟΣ")
can.setFont('Helvetica', 10)
can.drawString(330, 620, "ΑΔΤ ΝΟΜ ΕΚΠ")
can.drawString(230, 649, "ΚΙΝΗΤΟ")
can.drawString(380, 649, "EMAIL")
can.drawString(82, 539, "ΔΙΕΥΘΥΝΣΗ ΑΛΛΗΛΟΓΡΑΦΙΑΣ")
can.drawString(319, 539, "ΤΚ ΑΛΛ")
can.drawString(439, 539, "ΠΟΛΗ ΑΛΛ")
can.drawString(122, 488, "ΔΙΕΥΘΥΝΣΗ ΠΑΡΟΧΗΣ")
can.drawString(371, 488, "ΔΗΜΟΣ")
can.drawString(142, 473, "ΟΙΚΙΑΚΟΣ")
can.drawString(146, 458, "T2")
can.drawString(470, 443, "ΕΓΓΥΗΣΗ")
can.drawString(320, 473, "ΘΕΡΜΑΝΣΗ ΖΕΣΤΟ ΝΕΡΟ")
can.drawString(320, 457, "25000")
can.drawString(128, 425, "ΤΥΠΟΣ ΕΝΕΡΓΟΠΟΙΗΣΗΣ")
can.setFillColorRGB(255,255,255)
can.rect(103, 440, 50, 11, stroke=0, fill=1)
can.setFillColorRGB(0,0,0)
can.drawString(110, 443, "ΝΑΙ")
can.setFont('Helvetica', 8)
can.drawString(226, 50, "ΘΕΣΣΑΛΟΝΙΚΗ ΗΜΕΡΟΜΗΝΙΑ")
can.setFont('Helvetica', 6)
can.drawString(460, 87, "HSH***")
can.setFont('Helvetica', 10)
can.setFillColorRGB(255,255,255)
can.rect(278, 522, 295, 10, stroke=0, fill=1)
can.setFillColorRGB(0,0,0)
can.drawString(23, 524, "X")
can.drawString(300, 525, "example@gmail.com")
can.save()

#move to the beginning of the StringIO buffer
packet.seek(0)

# create a new PDF with Reportlab
new_pdf = PdfReader(packet)
# read your existing PDF
existing_pdf = PdfReader(open("aitisi_gas.pdf", "rb"))
output = PdfWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.pages[0]
page.merge_page(new_pdf.pages[0])
output.add_page(page)
# finally, write "output" to a real file
output_stream = open("final_gas.pdf", "wb")
output.write(output_stream)
output_stream.close()
