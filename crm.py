import pymysql
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PyPDF2 import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
from datetime import date
from datetime import *
from tkcalendar import Calendar

def newContactForm():
    menu_frame.forget()
    lbl_title.config(text="ΔΗΜΙΟΥΡΓΙΑ ΝΕΑΣ ΕΠΑΦΗΣ")
    form_frame.pack()
    lbl_fullname=tk.Label(master=form_frame,text="Ονοματεπώνυμο",width=20,font="ARIAL 13").grid(row=0,column=0)
    lbl_address=tk.Label(master=form_frame,text="Διεύθυνση",width=20,font="ARIAL 13").grid(row=1,column=0)
    lbl_zip_code=tk.Label(master=form_frame,text="Ταχ/κός Κώδικας",width=20,font="ARIAL 13").grid(row=2,column=0)
    lbl_city=tk.Label(master=form_frame,text="Πόλη",width=20,font="ARIAL 13").grid(row=3,column=0)
    lbl_afm=tk.Label(master=form_frame,text="ΑΦΜ",width=20,font="ARIAL 13").grid(row=4,column=0)
    lbl_adt=tk.Label(master=form_frame,text="ΑΔΤ",width=20,font="ARIAL 13").grid(row=5,column=0)
    lbl_doy=tk.Label(master=form_frame,text="ΔΟΥ",width=20,font="ARIAL 13").grid(row=6,column=0)
    lbl_idiotita=tk.Label(master=form_frame,text="Ιδιότητα",width=20,font="ARIAL 13").grid(row=7,column=0)
    lbl_mobile=tk.Label(master=form_frame,text="Κινητό",width=20,font="ARIAL 13").grid(row=8,column=0)
    lbl_phone=tk.Label(master=form_frame,text="Σταθερό",width=20,font="ARIAL 13").grid(row=9,column=0)
    lbl_email=tk.Label(master=form_frame,text="Email",width=20,font="ARIAL 13").grid(row=10,column=0)

    global list_entry_contact,var
    list_entry_contact=[]
    var=IntVar()

    for i in range(11):
        if i!=7:
            list_entry_contact.append(tk.Entry(master=form_frame,width=40))
            list_entry_contact[i].grid(row=i,column=1)
        else:
            list_entry_contact.append("blank")
            radio_frame=tk.Frame(master=form_frame)
            radio_frame.grid(row=7,column=1)
            r1=tk.Radiobutton(master=radio_frame,text="Ιδιοκτήτης",variable=var,value=1).grid(row=0,column=0)
            r2=tk.Radiobutton(master=radio_frame,text="Ενοικιαστής",variable=var,value=2).grid(row=0,column=1)
            r3=tk.Radiobutton(master=radio_frame,text="Διαχειριστής",variable=var,value=3).grid(row=0,column=2)


    for i in range(11,14,1):
        label=tk.Label(master=form_frame,text="",width=20,font="ARIAL 13").grid(row=i,column=0)
        label=tk.Label(master=form_frame,text="",width=20,font="ARIAL 13").grid(row=i,column=1)
    saveButton=tk.Button(master=form_frame,text="Καταχώρηση",command=saveContact).grid(row=14,column=0,columnspan=2,sticky="se",padx=10)

def saveContact():
    user_input = messagebox.askquestion('Confirm','Είστε σίγουρος;')
    if user_input=='yes':
        #global fullname,address,zipcode,city,adt,doy,idiotita,mobile,phone,email,temp_idiotita
        fullname=list_entry_contact[0].get().upper()
        address=list_entry_contact[1].get().upper()
        zipcode=list_entry_contact[2].get()
        city=list_entry_contact[3].get().upper()
        afm=str(list_entry_contact[4].get())
        adt=list_entry_contact[5].get()
        doy=list_entry_contact[6].get().upper()
        mobile=list_entry_contact[8].get()
        phone=list_entry_contact[9].get()
        email=list_entry_contact[10].get()
        temp_idiotita=var.get()
       
        if temp_idiotita==1:
            idiotita="ΙΔΙΟΚΤΗΤΗΣ"
        elif temp_idiotita==2:
            idiotita="ΕΝΟΙΚΙΑΣΤΗΣ"
        else:
            idiotita="ΔΙΑΧΕΙΡΙΣΤΗΣ"

        cursor.execute("INSERT INTO επαφές(Ονοματεπώνυμο,Διεύθυνση,ΑΦΜ,ΑΔΤ,Κινητό,Σταθερό,Πόλη,ΤΚ,email,ΔΟΥ,Ιδιότητα_Πελάτη) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(fullname,address,afm,adt,mobile,phone,city,zipcode,email,doy,idiotita))
        connection.commit()
        messagebox.showinfo("Success","Όλα καλά!")
        addSupply(afm)

def newCompanyForm():
    menu_frame.forget()
    lbl_title.config(text="ΔΗΜΙΟΥΡΓΙΑ ΝΕΑΣ ΕΤΑΙΡΕΙΑΣ")
    form_Company_frame.pack()
    global entries,varRadio
    varRadio=IntVar()
    labels=[]
    entries=[]
    texts=["Επωνυμία Εταιρείας","Διεύθυνση","ΤΚ","Πόλη","ΑΦΜ","ΔΟΥ","Ιδιότητα","Σταθερό","Κινητό","Email","Νόμιμος Εκπρόσωπος","ΑΔΤ Εκπροσώπου"]
    for i in range(14):
        if i<12:
            labels.append(tk.Label(master=form_Company_frame,text=texts[i],width=20,font="ARIAL 13"))
            labels[i].grid(row=i,column=0)
            if i!=6:
                entries.append(tk.Entry(master=form_Company_frame,width=40))
                entries[i].grid(row=i,column=1)
            else:
                entries.append("nothing")
                radio_frame=tk.Frame(master=form_Company_frame)
                radio_frame.grid(row=i,column=1)
                r1=tk.Radiobutton(master=radio_frame,text="Ιδιοκτήτης",variable=varRadio,value=1).grid(row=0,column=0)
                r2=tk.Radiobutton(master=radio_frame,text="Ενοικιαστής",variable=varRadio,value=2).grid(row=0,column=1)
                r3=tk.Radiobutton(master=radio_frame,text="Διαχειριστής",variable=varRadio,value=3).grid(row=0,column=2)
        else:
            label=tk.Label(master=form_Company_frame,text="",width=20,font="ARIAL 13").grid(row=i,column=0)
            label=tk.Label(master=form_Company_frame,text="",width=20,font="ARIAL 13").grid(row=i,column=1)

    saveCompanyButton=tk.Button(master=form_Company_frame,text="Καταχώρηση",command=saveCompany).grid(row=14,column=0,columnspan=2,sticky="se",padx=10)


def saveCompany():
    list_toSave=[]
    for i in range(12):
        if i!=6:
            list_toSave.append(entries[i].get())
        else:
            if varRadio.get()==1:
                list_toSave.append("ΙΔΙΟΚΤΗΤΗΣ")
            elif varRadio.get()==2:
                list_toSave.append("ΕΝΟΙΚΙΑΣΤΗΣ")
            else:
                list_toSave.append("ΔΙΑΧΕΙΡΙΣΤΗΣ")

    
    afm=str(entries[4].get())
    cursor.execute("INSERT INTO εταιρείες(Επωνυμία,Διεύθυνση,ΤΚ,Πόλη,ΑΦΜ,ΔΟΥ,Ιδιότητα,Σταθερό,Κινητό,email,Νόμιμος_Εκπρόσωπος,ΑΔΤ_Εκπροσώπου) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(list_toSave[0],list_toSave[1],list_toSave[2],list_toSave[3],list_toSave[4],list_toSave[5],list_toSave[6],list_toSave[7],list_toSave[8],list_toSave[9],list_toSave[10],list_toSave[11]))
    connection.commit()
    messagebox.showinfo("Success","Όλα καλά!")
    addSupply(afm)          
    


   
def addSupply(afm):
    form_frame.forget()
    menu_frame.forget()
    form_Company_frame.forget()
    frame.forget()
    lbl_title.config(text="ΚΑΤΑΧΩΡΗΣΗ ΑΙΤΗΣΗΣ")
    button_frame.pack()
    button_power=tk.Button(master=button_frame,width=30,height=2,text="Προσθήκη Αίτησης Ρεύματος",command=lambda: addSupplyPower(afm))
    button_power.grid(row=0,column=0)
    lbl_blank=tk.Label(master=button_frame,width=30,text="")
    lbl_blank.grid(row=0,column=1)
    button_gas=tk.Button(master=button_frame,width=30,height=2,text="Προσθήκη Αίτησης Αερίου",command=lambda: addSupplyGas(afm))
    button_gas.grid(row=0,column=2)

def addSupplyPower(afm):
    button_frame.forget()
    lbl_title.config(text="ΚΑΤΑΧΩΡΗΣΗ ΑΙΤΗΣΗΣ ΡΕΥΜΑΤΟΣ")
   
    form_power_frame.pack()
    address_frame.pack()
   
    ship_address_frame=tk.Frame(master=address_frame,padx=10)
    ship_address_frame.grid(row=0,column=0)
    lbl_title_ship=tk.Label(master=ship_address_frame,text="Πληροφορίες Αλληλογραφίας",font="ARIAL 15",pady=5).grid(row=0,column=0,columnspan=2)
    lbl_ship1=tk.Label(master=ship_address_frame,text="Διεύθυνση").grid(row=1,column=0)
    lbl_ship2=tk.Label(master=ship_address_frame,text="Ταχ/κός Κώδικας").grid(row=2,column=0)
    lbl_ship3=tk.Label(master=ship_address_frame,text="Πόλη").grid(row=3,column=0)
   
    supply_address_frame=tk.Frame(master=address_frame,padx=10)
    supply_address_frame.grid(row=0,column=1)
    lbl_title_supply=tk.Label(master=supply_address_frame,text="Πληροφορίες παροχής",font="ARIAL 15",pady=5).grid(row=0,column=0,columnspan=2)
    lbl_supply1=tk.Label(master=supply_address_frame,text="Διεύθυνση").grid(row=1,column=0)
    lbl_supply2=tk.Label(master=supply_address_frame,text="Ταχ/κός Κώδικας").grid(row=2,column=0)
    lbl_supply3=tk.Label(master=supply_address_frame,text="Πόλη").grid(row=3,column=0)

    global list_entry_supply_power
    list_entry_supply_power=[]
    for i in range(1,7,1):
        if i<4:
           list_entry_supply_power.append(tk.Entry(master=ship_address_frame))
           list_entry_supply_power[i-1].grid(row=i,column=1)
        else:
            list_entry_supply_power.append(tk.Entry(master=supply_address_frame))
            list_entry_supply_power[i-1].grid(row=i-3,column=1)


    form_power_frame2.pack()

    options=[["Γ1","Γ1Ν","Γ21","Γ22","Γ23"],["50","70","350"],["POWER HOME NOW","POWER HOME BASIC","POWER BUSINESS BASIC"],["ΑΛ. ΠΑΡΟΧΟΥ","ΕΠΑΝΑΣΥΝΔΕΣΗ","ΔΙΑΔΟΧΗ","ΝΕΑ ΣΥΝΔΕΣΗ","ΑΝΑΝΕΩΣΗ"],["Ναι","Όχι"],["Ναι","Όχι"],["006","008","016","017","018","019"],["LDA","HSH","CC"],["ΙΔΙΩΤΗΣ","ΑΤΟΜΙΚΗ ΕΠΙΧΕΙΡΗΣΗ","ΕΤΑΙΡΙΚΗ ΕΠΙΧΕΙΡΗΣΗ","ΚΟΙΝΟΧΡΗΣΤΟΙ ΧΩΡΟΙ"]]
    labeltexts=["Κατηγορία Τιμολόγησης","Εγγύηση","Πρόγραμμα","Τύπος Ενεργοποίσης","Ebill","Πάγια Εντολή","Κωδικός Πωλητή","Λίστα","Κατηγορία Πελάτη"]

    global clicked,text_RDV
    
    clicked1=StringVar()
    clicked2=StringVar()
    clicked3=StringVar()
    clicked4=StringVar()
    clicked5=StringVar()
    clicked6=StringVar()
    clicked7=StringVar()
    clicked8=StringVar()
    clicked9=StringVar()
    clicked=[clicked1,clicked2,clicked3,clicked4,clicked5,clicked6,clicked7,clicked8,clicked9]


    dropMenus=[]
    for i in range(9):
        clicked[i].set("---")
        label=tk.Label(master=form_power_frame2,text=labeltexts[i]).grid(row=i+1,column=0)
        dropMenus.append(tk.OptionMenu(form_power_frame2,clicked[i],*options[i]))
        dropMenus[i].config(width=32)
        dropMenus[i].grid(row=i+1,column=1)

    label_RDV=tk.Label(master=form_power_frame2,text="Σχόλια ραντεβού").grid(row=10,column=0)
    text_RDV=tk.Text(master=form_power_frame2,width=32,height=8)
    text_RDV.grid(row=10,column=1,rowspan=2)

    

    buttonSaveSupplyPower.config(text="Καταχώρηση",command=lambda: saveSupplyPower(afm),state=NORMAL)
    buttonSaveSupplyPower.pack()

def saveSupplyPower(afm):
    buttonSaveSupplyPower.config(state=DISABLED)
    address_ship=list_entry_supply_power[0].get()
    tk_ship=list_entry_supply_power[1].get()
    city_ship=list_entry_supply_power[2].get()
    address_supply=list_entry_supply_power[3].get()
    tk_supply=list_entry_supply_power[4].get()
    city_supply=list_entry_supply_power[5].get()
    kat_timologisis=clicked[0].get()
    eggyisi=clicked[1].get()
    programma=clicked[2].get()
    typos_energ=clicked[3].get()
    ebill=clicked[4].get()
    pagia=clicked[5].get()
    agent_no=clicked[6].get()
    code_list=clicked[7].get()
    kat_pelati=clicked[8].get()
    sxolia=text_RDV.get("1.0","end-1c")
    power_or_gas="ΡΕΥΜΑ"

    two_digits_AFM=afm[0]+afm[1]
    
    if afm[0] in etairika_AFM or two_digits_AFM in etairika_AFM: 
        cursor.execute("SELECT Κωδικός_Εταιρείας FROM εταιρείες WHERE ΑΦΜ='{}';".format(afm))
        result=cursor.fetchall()
        for x in result:
            contact_id=x[0]
            break
    else:
        cursor.execute("SELECT Κωδικός_Επαφής FROM επαφές WHERE ΑΦΜ='{}';".format(afm))
        result=cursor.fetchall()
        for x in result:
            contact_id=x[0]
            break

    cursor.execute("INSERT INTO αιτήσεις(Διεύθυνση_Αλλ,Διεύθυνση_Παροχής,Κωδικός_Επαφής,Ρεύμα_Αέριο,Κατηγορία_Τιμολόγησης,Εγγύηση,Πρόγραμμα,Τύπος_Ενεργοποίησης,ΤΚ_Αλλ,Πόλη_Αλλ,ΤΚ_Παροχής,Πόλη_Παροχής,ebill,Κωδικός_Πωλητή,Λίστα,Πάγια_εντολή,Κατηγορία_Πελάτη,Σχόλια_Ραντεβού) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(address_ship,address_supply,contact_id,power_or_gas,kat_timologisis,eggyisi,programma,typos_energ,tk_ship,city_ship,tk_supply,city_supply,ebill,agent_no,code_list,pagia,kat_pelati,sxolia))
    connection.commit()
    messagebox.showinfo("Success","Όλα καλά!")
    frameToPDF.pack()
    buttonToPDF.config(text="Δημιουργία PDF",state=NORMAL,command=lambda: powerToPDF(afm,address_ship,tk_ship,city_ship,address_supply,tk_supply,city_supply,
                                                                   kat_timologisis,eggyisi,programma,typos_energ,ebill,pagia,agent_no,code_list,kat_pelati))
    buttonToPDF.pack()

def powerToPDF(afm,address_ship,tk_ship,city_ship,address_supply,tk_supply,city_supply,kat_timologisis,eggyisi,programma,typos_energ,ebill,pagia,agent_no,code_list,kat_pelati):
    two_digits_AFM=afm[0]+afm[1]
    if afm[0] not in etairika_AFM and two_digits_AFM not in etairika_AFM:
        cursor.execute("SELECT Ονοματεπώνυμο,Διεύθυνση,ΤΚ,Πόλη,ΑΔΤ,ΔΟΥ,Ιδιότητα_Πελάτη,Σταθερό,Κινητό,email FROM επαφές WHERE ΑΦΜ='{}'".format(afm))
        result=cursor.fetchall()
        list_contact=[]
        for x in result:
            for i in range(len(x)):
                list_contact.append(x[i])
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFont('Helvetica', 10)
        if len(list_contact[0])>20:
            can.setFont('Helvetica', 6)
        can.drawString(170, 680, list_contact[0])
        can.setFont('Helvetica', 10)
        can.drawString(400, 680, kat_pelati)
        can.drawString(85, 663, list_contact[1])
        can.drawString(335, 663, list_contact[2])
        can.drawString(430, 663, list_contact[3])
        can.drawString(115, 646, list_contact[4])
        can.drawString(258, 646, afm)
        if len(list_contact[5])>12:
            can.setFont('Helvetica', 8)
        can.drawString(372, 646, list_contact[5])
        can.setFont('Helvetica', 10)
        can.drawString(497, 646, list_contact[6])
        can.drawString(85, 628, list_contact[7])
        can.drawString(256, 628, list_contact[8])
        can.drawString(376, 628, list_contact[9])
        can.drawString(84, 530, address_ship)
        can.drawString(335, 530, tk_ship)
        can.drawString(427, 530, city_ship)
        can.drawString(310, 474, kat_timologisis)
        can.drawString(480, 474, "ΧΑΜΗΛΗ ΤΑΣΗ")
        can.drawString(83, 457, address_supply)
        can.drawString(335, 457, tk_supply)
        if len(city_supply)>11:
            can.setFont('Helvetica', 8)
        elif len(city_supply)>17:
            can.setFont('Helvetica', 6)
        can.drawString(503, 457, city_supply)
        can.setFont('Helvetica', 10)
        can.drawString(427, 392, eggyisi)
        can.setFillColorRGB(255,255,255)
        can.rect(22, 388, 300, 15, stroke=0, fill=1)
        can.setFillColorRGB(0,0,0)
        can.drawString(25, 392, programma)
        can.setFont('Helvetica', 8)
        place_date="ΘΕΣΣΑΛΟΝΙΚΗ"+"  "+dateNow()
        can.drawString(226, 80, place_date)
        can.setFont('Helvetica', 6)
        can.drawString(460, 130, str(code_list+agent_no))
        can.setFont('Helvetica', 10)
        can.setFillColorRGB(255,255,255)
        can.rect(285, 512, 290, 10, stroke=0, fill=1)
        can.setFillColorRGB(0,0,0)
        if ebill=="Ναι":
            can.drawString(29, 513, "X")
            can.drawString(300, 513, list_contact[9])
        can.drawString(496, 423, typos_energ)
        can.save()
    else:
        cursor.execute("SELECT * FROM εταιρείες WHERE ΑΦΜ='{}'".format(afm))
        result=cursor.fetchall()
        list_contact=[]
        for x in result:
            for i in range(1,len(x)):
                list_contact.append(x[i])
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFont('Helvetica', 10)
        if len(list_contact[0])>24 and len(list_contact[0])<35:
            can.setFont('Helvetica', 8)
        elif len(list_contact[0])>34 and len(list_contact[0])<45:
            can.setFont('Helvetica', 6)
        elif len(list_contact[0])>44:
            can.setFont('Helvetica', 4)
        can.drawString(170, 680, list_contact[0])
        can.setFont('Helvetica', 10)
        can.drawString(400, 680, kat_pelati)
        can.drawString(85, 663, list_contact[1])
        can.drawString(335, 663, list_contact[2])
        can.drawString(430, 663, list_contact[3])
        can.drawString(258, 646, list_contact[4])
        if len(list_contact[5])>12:
            can.setFont('Helvetica', 8)
        elif len(list_contact[5])>19:
            can.setFont('Helvetica', 6)
        can.drawString(372, 646, list_contact[5])
        can.setFont('Helvetica', 10)
        can.drawString(497, 646, list_contact[6])
        can.drawString(85, 628, list_contact[7])
        can.drawString(256, 628, list_contact[8])
        can.drawString(376, 628, list_contact[9])
        can.setFont('Helvetica', 5)
        can.drawString(138, 597, list_contact[10])
        can.setFont('Helvetica', 10)
        can.drawString(310, 597, list_contact[11])
        can.drawString(84, 530, address_ship)
        can.drawString(335, 530, tk_ship)
        can.drawString(427, 530, city_ship)
        can.drawString(310, 474, kat_timologisis)
        can.drawString(480, 474, "ΧΑΜΗΛΗ ΤΑΣΗ")
        can.drawString(83, 457, address_supply)
        can.drawString(335, 457, tk_supply)
        if len(city_supply)>11:
            can.setFont('Helvetica', 8)
        elif len(city_supply)>17:
            can.setFont('Helvetica', 6)
        can.drawString(503, 457, city_supply)
        can.setFont('Helvetica', 10)
        can.drawString(427, 392, eggyisi)
        can.setFillColorRGB(255,255,255)
        can.rect(22, 388, 300, 15, stroke=0, fill=1)
        can.setFillColorRGB(0,0,0)
        can.drawString(25, 392, programma)
        can.setFont('Helvetica', 8)
        place_date="ΘΕΣΣΑΛΟΝΙΚΗ"+"  "+dateNow()
        can.drawString(226, 80, place_date)
        can.setFont('Helvetica', 8)
        can.drawString(460, 130, str(code_list+agent_no))
        can.setFont('Helvetica', 10)
        can.setFillColorRGB(255,255,255)
        can.rect(285, 512, 290, 10, stroke=0, fill=1)
        can.setFillColorRGB(0,0,0)
        if ebill=="Ναι":
            can.drawString(29, 513, "X")
            can.drawString(300, 513, list_contact[9])
        can.drawString(496, 423, typos_energ)
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
    messagebox.showinfo("Επιβεβαίωση","Η αίτηση είναι έτοιμη για εκτύπωση")
    buttonToPDF.config(state=DISABLED)
    menu()
   

def dateNow():
    today=str(date.today())
    day=today[8:10]
    month=today[5:7]
    year=today[0:4]
    return day+"/"+month+"/"+year

def addSupplyGas(afm):
    button_frame.forget()
    lbl_title.config(text="ΚΑΤΑΧΩΡΗΣΗ ΑΙΤΗΣΗΣ ΑΕΡΙΟΥ")
    buttonSaveSupplyGas.config(state=NORMAL)

    form_gas_frame.pack()
    address_gas_frame.pack()
    form_gas_frame2.pack()

    ship_address_frame=tk.Frame(master=address_gas_frame,padx=10)
    ship_address_frame.grid(row=0,column=0)
    lbl_title_ship=tk.Label(master=ship_address_frame,text="Πληροφορίες Αλληλογραφίας",font="ARIAL 15",pady=5).grid(row=0,column=0,columnspan=2)
    lbl_ship1=tk.Label(master=ship_address_frame,text="Διεύθυνση").grid(row=1,column=0)
    lbl_ship2=tk.Label(master=ship_address_frame,text="Ταχ/κός Κώδικας").grid(row=2,column=0)
    lbl_ship3=tk.Label(master=ship_address_frame,text="Πόλη").grid(row=3,column=0)
   
    supply_address_frame=tk.Frame(master=address_gas_frame,padx=10)
    supply_address_frame.grid(row=0,column=1)
    lbl_title_supply=tk.Label(master=supply_address_frame,text="Πληροφορίες παροχής",font="ARIAL 15",pady=5).grid(row=0,column=0,columnspan=2)
    lbl_supply1=tk.Label(master=supply_address_frame,text="Διεύθυνση").grid(row=1,column=0)
    lbl_supply2=tk.Label(master=supply_address_frame,text="Ταχ/κός Κώδικας").grid(row=2,column=0)
    lbl_supply3=tk.Label(master=supply_address_frame,text="Δήμος").grid(row=3,column=0)

    global list_entry_supply_gas
    list_entry_supply_gas=[]
    for i in range(1,7,1):
        if i<4:
           list_entry_supply_gas.append(tk.Entry(master=ship_address_frame))
           list_entry_supply_gas[i-1].grid(row=i,column=1)
        else:
            list_entry_supply_gas.append(tk.Entry(master=supply_address_frame))
            list_entry_supply_gas[i-1].grid(row=i-3,column=1)

    options=[["T2","T3"],["GAS HOME NOW","GAS HOME EASY","GAS HOME PLUS","GAS HOME STAR","GAS BUSINESS EASY 1","GAS BUSINESS EASY 2"],["ΑΛΛΑΓΗ ΠΑΡΟΧΟΥ","ΕΠΑΝΑΣΥΝΔΕΣΗ","ΔΙΑΔΟΧΗ","ΠΡΩΤΗ ΕΓΚΑΤΑΣΤΑΣΗ","ΑΝΑΝΕΩΣΗ"],["Ναι","Όχι"],["Ναι","Όχι"],["006","008","016","017","018","019"],["LDA","HSH","CC"],["ΝΑΙ","ΟΧΙ"],["ΟΙΚΙΑΚΟΣ","ΚΕΝΤΡΙΚΟΣ","ΕΜΠΟΡΙΚΟΣ"],["ΙΔΙΩΤΗΣ","ΑΤΟΜΙΚΗ ΕΠΙΧΕΙΡΗΣΗ","ΕΤΑΙΡΙΚΗ ΕΠΙΧΕΙΡΗΣΗ","ΚΟΙΝΟΧΡΗΣΤΟΙ ΧΩΡΟΙ"]]
    labeltexts=["Κατηγορία Τιμολόγησης","Πρόγραμμα","Τύπος Ενεργοποίσης","Ebill","Πάγια Εντολή","Κωδικός Πωλητή","Λίστα","Ενεργή Παροχή","Κατηγορία Καταναλωτή","Κατηγορία Πελάτη"]

    global clicked_gas,entry_eggyisi
    clicked1=StringVar()
    clicked2=StringVar()
    clicked3=StringVar()
    clicked4=StringVar()
    clicked5=StringVar()
    clicked6=StringVar()
    clicked7=StringVar()
    clicked8=StringVar()
    clicked9=StringVar()
    clicked10=StringVar()
    clicked_gas=[clicked1,clicked2,clicked3,clicked4,clicked5,clicked6,clicked7,clicked8,clicked9,clicked10]


    dropMenus=[]
    for i in range(len(clicked_gas)):
        clicked_gas[i].set("---")
        label=tk.Label(master=form_gas_frame2,text=labeltexts[i]).grid(row=i+1,column=0)
        dropMenus.append(tk.OptionMenu(form_gas_frame2,clicked_gas[i],*options[i]))
        dropMenus[i].config(width=25)
        dropMenus[i].grid(row=i+1,column=1)
    label_eggyisi=tk.Label(master=form_gas_frame2,text="Εγγύηση").grid(row=11,column=0)
    entry_eggyisi=tk.Entry(master=form_gas_frame2)
    entry_eggyisi.grid(row=11,column=1)

    buttonSaveSupplyGas.config(text="Καταχώρηση",command=lambda: saveSupplyGas(afm))
    buttonSaveSupplyGas.pack()

   
def saveSupplyGas(afm):
    address_ship=list_entry_supply_gas[0].get()
    tk_ship=list_entry_supply_gas[1].get()
    city_ship=list_entry_supply_gas[2].get()
    address_supply=list_entry_supply_gas[3].get()
    tk_supply=list_entry_supply_gas[4].get()
    city_supply=list_entry_supply_gas[5].get()
    kat_timologisis=clicked_gas[0].get()
    programma=clicked_gas[1].get()
    typos_energ=clicked_gas[2].get()
    ebill=clicked_gas[3].get()
    pagia=clicked_gas[4].get()
    agent_no=clicked_gas[5].get()
    code_list=clicked_gas[6].get()
    energo_or_not=clicked_gas[7].get()
    kat_katanaloti=clicked_gas[8].get()
    kat_pelati=clicked_gas[9].get()
    eggyisi=entry_eggyisi.get()
    power_or_gas="ΑΕΡΙΟ"

    two_digits_AFM=afm[0]+afm[1]
    if afm[0] in etairika_AFM or two_digits_AFM in etairika_AFM: 
        cursor.execute("SELECT Κωδικός_Εταιρείας FROM εταιρείες WHERE ΑΦΜ='{}';".format(afm))
        result=cursor.fetchall()
        for x in result:
            contact_id=x[0]
            break
    else:
        cursor.execute("SELECT Κωδικός_Επαφής FROM επαφές WHERE ΑΦΜ='{}';".format(afm))
        result=cursor.fetchall()
        for x in result:
            contact_id=x[0]
            break
    
        
            
        

    cursor.execute("INSERT INTO αιτήσεις(Διεύθυνση_Αλλ,Διεύθυνση_Παροχής,Κωδικός_Επαφής,Ρεύμα_Αέριο,Κατηγορία_Τιμολόγησης,Εγγύηση,Πρόγραμμα,Τύπος_Ενεργοποίησης,ΤΚ_Αλλ,Πόλη_Αλλ,ΤΚ_Παροχής,Πόλη_Παροχής,ebill,Κωδικός_Πωλητή,Λίστα,Πάγια_εντολή) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(address_ship,address_supply,contact_id,power_or_gas,kat_timologisis,eggyisi,programma,typos_energ,tk_ship,city_ship,tk_supply,city_supply,ebill,agent_no,code_list,pagia))
    connection.commit()
    messagebox.showinfo("Success","Όλα καλά!")

    buttonSaveSupplyGas.config(state=DISABLED)

    frame_buttonGasToPDF.pack()
    buttonGasToPDF.config(command=lambda: gasPDF(address_ship,tk_ship,city_ship,address_supply,city_supply,kat_timologisis,typos_energ,ebill,pagia,agent_no,code_list,eggyisi,afm,energo_or_not,kat_katanaloti,kat_pelati),state=NORMAL)
    buttonGasToPDF.pack()
   

   
def gasPDF(address_ship,tk_ship,city_ship,address_supply,city_supply,kat_timologisis,typos_energ,ebill,pagia,agent_no,code_list,eggyisi,afm,energo_or_not,kat_katanaloti,kat_pelati):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFont('Helvetica', 10)
    two_digits_AFM=afm[0]+afm[1]
    if not(afm[0] in etairika_AFM or two_digits_AFM in etairika_AFM):
        cursor.execute("SELECT Ονοματεπώνυμο,Διεύθυνση,ΤΚ,Πόλη,ΑΔΤ,ΔΟΥ,Ιδιότητα_Πελάτη,Σταθερό,Κινητό,email FROM επαφές WHERE ΑΦΜ='{}'".format(afm))
        result=cursor.fetchall()
        list_contact=[]
        for x in result:
            for i in range(len(x)):
                list_contact.append(x[i])
        can.setFont('Helvetica', 10)
        can.drawString(170, 699, list_contact[0])
        can.drawString(458, 699, kat_pelati)
        can.drawString(82, 683, list_contact[1])
        can.drawString(318, 683, list_contact[2])
        can.drawString(440, 683, list_contact[3])
        can.drawString(115, 666, list_contact[4])
        can.drawString(232, 666, afm)
        can.drawString(342, 666, list_contact[5])
        can.drawString(469, 666, list_contact[6])
        can.drawString(82, 649, list_contact[7])
        can.drawString(230, 649, list_contact[8])
        can.drawString(380, 649, list_contact[9])
    else:
        cursor.execute("SELECT * FROM εταιρείες WHERE ΑΦΜ='{}'".format(afm))
        result=cursor.fetchall()
        list_contact=[]
        for x in result:
            for i in range(1,len(x)):
                list_contact.append(x[i])
        can.drawString(170, 699, list_contact[0])
        can.drawString(458, 699, kat_pelati)
        can.drawString(82, 683, list_contact[1])
        can.drawString(318, 683, list_contact[2])
        can.drawString(440, 683, list_contact[3])
        can.drawString(232, 666, list_contact[4])
        can.setFont('Helvetica', 8)
        can.drawString(342, 666, list_contact[5])
        can.setFont('Helvetica', 10)
        can.drawString(469, 666, list_contact[6])
        can.drawString(82, 649, list_contact[7])
        can.drawString(230, 649, list_contact[8])
        can.drawString(380, 649, list_contact[9])
        can.setFont('Helvetica', 6)
        can.drawString(136, 620, list_contact[10])
        can.setFont('Helvetica', 10)
        can.drawString(330, 620, list_contact[11])

    
    can.drawString(82, 539, address_ship)
    can.drawString(319, 539, tk_ship)
    can.drawString(439, 539, city_ship)
    can.drawString(122, 488, address_supply)
    can.drawString(371, 488, city_supply)
    can.drawString(142, 473, kat_katanaloti)
    can.drawString(146, 458, kat_timologisis)
    can.drawString(470, 443, eggyisi)
    can.drawString(320, 473, "ΘΕΡΜΑΝΣΗ ΖΕΣΤΟ ΝΕΡΟ")
    can.drawString(320, 457, "25000")
    can.drawString(128, 425, typos_energ)
    can.setFillColorRGB(255,255,255)
    can.rect(103, 440, 50, 11, stroke=0, fill=1)
    can.setFillColorRGB(0,0,0)
    can.drawString(110, 443, energo_or_not)
    can.setFont('Helvetica', 8)
    place_date="ΘΕΣΣΑΛΟΝΙΚΗ"+"  "+dateNow()
    can.drawString(226, 50, place_date)
    code_agent_list=code_list+str(agent_no)
    can.drawString(460, 87, code_agent_list)
    can.setFont('Helvetica', 10)
    can.setFillColorRGB(255,255,255)
    can.rect(278, 522, 295, 10, stroke=0, fill=1)
    can.setFillColorRGB(0,0,0)
    if ebill=="Ναι":
        can.drawString(23, 524, "X")
        can.drawString(300, 525, list_contact[9])
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
    buttonGasToPDF.config(state=DISABLED)
        

        
        
   
   


def checkAFM():
    frame_search_AFM.pack()
    lbl_search_AFM=tk.Label(master=frame_search_AFM,width=15,text="Αναζήτηση ΑΦΜ",font="BOLD").grid(row=0,column=0)
    entry_search_AFM=tk.Entry(master=frame_search_AFM,width=15)
    entry_search_AFM.grid(row=1,column=0)
    blank=tk.Label(master=frame_search_AFM,text="",width=10).grid(row=0,column=1)
    button_search=tk.Button(master=frame_search_AFM,text="Αναζήτηση",width=10,command=lambda: searchAFM(entry_search_AFM.get()))
    button_search.grid(row=1,column=1)

def searchAFM(afm):
    cursor.execute("SELECT ΑΦΜ FROM επαφές WHERE ΑΦΜ='{}'".format(afm))
    result=cursor.fetchall()
    cursor.execute("SELECT ΑΦΜ FROM εταιρείες WHERE ΑΦΜ='{}'".format(afm))
    result_company=cursor.fetchall()
    ret=True
    if afm=="":
        messagebox.showinfo("Προσοχή","Κενό ΑΦΜ")
        return
    else:
        if result or result_company:
            messagebox.showinfo("Αναζήτηση ΑΦΜ","Το ΑΦΜ βρέθηκε")
            frame_search_AFM.forget()
            frame.forget()
            return True
        else:
            messagebox.showinfo("Αναζήτηση ΑΦΜ","Το ΑΦΜ δεν βρέθηκε")
            frame_search_AFM.forget()
            frame.forget()
            return False


def addSupplyExistingAFM():
    global button_search,entry_search_AFM
    frame.pack()
    lbl_search_AFM=tk.Label(master=frame,width=15,text="Αναζήτηση ΑΦΜ",font="BOLD").grid(row=0,column=0)
    entry_search_AFM=tk.Entry(master=frame,width=15)
    entry_search_AFM.grid(row=1,column=0)
    blank=tk.Label(master=frame,text="",width=10).grid(row=0,column=1)
    button_search=tk.Button(master=frame,text="Αναζήτηση",width=10,command=buttonExisting)
    button_search.grid(row=1,column=1)

def buttonExisting():
    if searchAFM(entry_search_AFM.get()):
        addSupply(entry_search_AFM.get())
    else:
        menu()

def menu():
    lbl_title.config(text="ΑΡΧΙΚΟ ΜΕΝΟΥ")
    form_Company_frame.forget()
    menu_frame.pack()
    frame.forget()
    frame_search_AFM.forget()
    form_power_frame.forget()
    buttonSaveSupplyPower.forget()
    frame_buttonGasToPDF.forget()
    form_frame.forget()
    form_power_frame2.forget()
    button_frame.forget()
    buttonSaveSupplyGas.forget()
    form_gas_frame.forget()
    form_gas_frame2.forget()
    frameToPDF.forget()
    frame_login.forget()
    frame_admin_search.forget()
    frame_show_supply_admin.forget()
    try:
        frame_to_show.destroy()
        frame_show_data_admin.destroy()
    except:
        print("Exception handled")
    try:
        frame_search.destroy()
        frame_calendar.destroy()
    except:
        print("Exception handled")
    try:
        frame_records.destroy()
    except:
        print("Exception handled")
        

def menuAsk():
    question=messagebox.askquestion("Προσοχή!","Είστε σίγουροι ότι θέλετε να επιστρέψετε στο αρχικό μενού;\nΤα δεδομένα σας δε θα αποθηκευθούν.")
    if question=='yes':
        menu()

def admin_login():
    global entry_login
    frame_login.pack()
    label_login=tk.Label(master=frame_login,text="Password",width=10,padx=10,font="ARIAL 13")
    label_login.grid(row=1,column=0)
    blank_label1=tk.Label(master=frame_login,width=1)
    blank_label1.grid(row=1,column=1)
    entry_login=tk.Entry(master=frame_login,width=10)
    entry_login.grid(row=1,column=2)
    blank_label1=tk.Label(master=frame_login,width=3)
    blank_label1.grid(row=1,column=3)
    button_confirm=tk.Button(master=frame_login,text="Επιβεβαίωση",width=10,command=admin_search).grid(row=1,column=4)

def admin_search():
    global entry_search,clicked_option,options_search
    if entry_login.get()=="1421":
        search_menu()
    else:
        messagebox.showinfo("Προειδοποίηση","Λάθος κωδικός")
        menu()
    

date1="-"
date2="-"
                
def search_menu():
    menu_frame.forget()
    global frame_search,entry_search,calendar1,calendar2,frame_calendar,button_search,button_date,choose_date
    lbl_title.config(text="ΑΝΑΖΗΤΗΣΗ ΠΕΛΑΤΗ-ΑΙΤΗΣΗΣ")
    frame_search=tk.Frame(master=window,pady=30)
    frame_search.pack()
    frame_calendar=tk.Frame(master=window,pady=10)
    entry_search=[]
    label_search_type=["ΟΝΟΜΑ","ΚΙΝΗΤΟ","ΑΦΜ","ΠΩΛΗΤΗΣ","ΗΜΕΡΟΜΗΝΙΑ ΑΠΟ-ΕΩΣ"]
    choose_date=BooleanVar()
    choose_date.set(False)
    for i in range(5):
        if i<4:
            label=tk.Label(master=frame_search,text=label_search_type[i],width=20).grid(row=0,column=i,padx=5)
            entry_search.append(tk.Entry(master=frame_search,width=20))
            entry_search[i].grid(row=1,column=i,padx=5)
        else:
            label=tk.Label(master=frame_search,text=label_search_type[i],width=20).grid(row=0,column=i,columnspan=2,padx=5)
            calendar1 = Calendar(master=frame_calendar, selectmode = 'day',year = int(set_calendar_date(3)), month = int(set_calendar_date(2)),day = int(set_calendar_date(1)))
            calendar2 = Calendar(master=frame_calendar, selectmode = 'day',year = int(set_calendar_date(3)), month = int(set_calendar_date(2)),day = int(set_calendar_date(1)))
            button_date=tk.Button(master=frame_search,text="Επιλογή",width=15,command=show_calendar)
            button_date.grid(row=1,column=i,columnspan=2)

    button_search=tk.Button(master=frame_search,text="Αναζήτηση",width=20,command=search)
    button_search.grid(row=1,column=6,padx=20)

    button_clear=tk.Button(master=frame_search,text="Καθαρισμός",width=20,command=clear_search)
    button_clear.grid(row=1,column=7,padx=20)

def clear_search():
    try:
        frame_calendar.destroy()
    except:
        print("Exception handled")
    try:
        frame_search.destroy()
    except:
        print("Exception handled")
    try:
        frame_records.destroy()
    except:
        print("Exception handled")
    search_menu()
        
    
    
def show_calendar():
    global button_confirm_date
    button_search.config(state=DISABLED)
    frame_calendar.pack()
    calendar1.grid(row=0,column=0,padx=15)
    calendar2.grid(row=0,column=1,padx=15)
    button_confirm_date=tk.Button(master=frame_calendar,text="Επιβεβαίωση ημερομηνίας",width=25,command=confirm_date)
    button_confirm_date.grid(row=1,column=0,columnspan=2,sticky="ns")


    
def confirm_date():
    global date1_final,date2_final
    date1_final=fix_date(str(calendar1.get_date()))
    date2_final=fix_date(str(calendar2.get_date()))
    if date1_final>date2_final:
        messagebox.showinfo("Προσοχή","Η πρώτη ημερομηνία πρέπει να είναι προγενέστερη.")
        return
    choose_date.set(True)
    button_date.destroy()
    label1=tk.Label(master=frame_search,text=date1_final,width=10).grid(row=1,column=4)
    label2=tk.Label(master=frame_search,text=date2_final,width=10).grid(row=1,column=5)
    button_confirm_date.destroy()
    frame_calendar.destroy()
    button_search.config(state=NORMAL)




def fix_date(date):
    splitted=date.split("/")
    final_list=[splitted[1],splitted[0],"20"+splitted[2]]
    for i in range(3):
        if len(final_list[i])==1:
            final_list[i]="0"+final_list[i]
    return final_list[2]+"-"+final_list[1]+"-"+final_list[0]
    

        
        
def set_calendar_date(a):
    today=str(date.today())
    day=today[8:10]
    month=today[5:7]
    year=today[0:4]
    if a==1:
        return day
    elif a==2:
        return month
    else:
        return year
        

def search():
    global frame_records
    fullname=str(entry_search[0].get())
    kinito=str(entry_search[1].get())
    afm=str(entry_search[2].get())
    agent=str(entry_search[3].get())
    temp_data_epafi=[]
    data_epafi=[]
    id_epafis=[]
    data_aitisi=[]
    if fullname or kinito or afm or agent or choose_date.get():
        cursor.execute("SELECT * FROM επαφές WHERE Ονοματεπώνυμο LIKE '%{}%' AND Κινητό LIKE '%{}%' AND ΑΦΜ LIKE '%{}%'".format(fullname,kinito,afm))
        result_epafi=cursor.fetchall()
        cursor.execute("SELECT * FROM εταιρείες WHERE Επωνυμία LIKE '%{}%' AND Κινητό LIKE '%{}%' AND ΑΦΜ LIKE '%{}%'".format(fullname,kinito,afm))
        result_etairia=cursor.fetchall()
        if result_epafi:
            button_search.config(state=DISABLED)
            for x in result_epafi:
                for i in range(len(x)):
                    if i==0:
                        id_epafis.append(x[i])
                        temp_data_epafi.append(x[i])
                    elif i in [1,3,5]:
                        temp_data_epafi.append(x[i])
                y=tuple(temp_data_epafi)
                data_epafi.append(y)
                temp_data_epafi.clear()
                

        if result_etairia:
            button_search.config(state=DISABLED)
            for x in result_etairia:
                for i in range(len(x)):
                    if i==0:
                        id_epafis.append(x[i])
                        temp_data_epafi.append(x[i])
                    elif i in [1,5,9]:
                        temp_data_epafi.append(x[i])
                y=tuple(temp_data_epafi)
                data_epafi.append(y)
                temp_data_epafi.clear()
                    


        if not (result_epafi or result_etairia):
            messagebox.showinfo("Ενημέρωση","Δεν βρέθηκε πελάτης με τα στοιχεία που δώσατε.")
            button_search.config(state=NORMAL)
            return

        tuple_list=tuple(id_epafis)
        if choose_date.get():
            dates=[]
            ultra=[]
            tuple_ultra=tuple(ultra)
            for i in range(len(id_epafis)):
                cursor.execute("SELECT Ημερομηνία FROM αιτήσεις WHERE Κωδικός_Επαφής={}".format(id_epafis[i]))
                result_dates=cursor.fetchall()
                tuple_ultra=tuple_ultra+result_dates
            
            for x in tuple_ultra:
                for i in x:
                    dates.append(x[0])

            if choose_date.get():
                split_date1=date1_final.split("-")
                split_date2=date2_final.split("-")

                final_dates=[]
                for i in range(len(dates)):
                    if date(int(split_date1[0]),int(split_date1[1]),int(split_date1[2]))<=dates[i] and date(int(split_date2[0]),int(split_date2[1]),int(split_date2[2]))>=dates[i]:
                        if not(dates[i] in final_dates):
                            final_dates.append(dates[i])

                tuple_final_dates=tuple(final_dates)


        r=[]

        if not(choose_date.get()):
            for i in range(len(id_epafis)):
                cursor.execute("SELECT Κωδικός_Επαφής,Ημερομηνία,Διεύθυνση_Παροχής,ΤΚ_Παροχής,Πόλη_Παροχής,Πρόγραμμα,Τύπος_Ενεργοποίησης,Λίστα,Κωδικός_Πωλητή,Σχόλια_Ραντεβού FROM αιτήσεις WHERE Κωδικός_Επαφής='{}' AND Κωδικός_Πωλητή LIKE '%{}%' ORDER BY Κωδικός_Επαφής ASC;".format(id_epafis[i],agent))
                result=cursor.fetchall()
                r.append(result)

        else:
            for i in range(len(final_dates)):
                for j in range(len(id_epafis)):
                    cursor.execute("SELECT Κωδικός_Επαφής,Ημερομηνία,Διεύθυνση_Παροχής,ΤΚ_Παροχής,Πόλη_Παροχής,Πρόγραμμα,Τύπος_Ενεργοποίησης,Λίστα,Κωδικός_Πωλητή,Σχόλια_Ραντεβού FROM αιτήσεις WHERE Κωδικός_Επαφής={} AND Ημερομηνία='{}' AND Κωδικός_Πωλητή LIKE '%{}%' ORDER BY Κωδικός_Επαφής ASC;".format(id_epafis[j],final_dates[i],agent))
                    result=cursor.fetchall()
                    r.append(result)


        final=[]
        for x in r:
            for i in range(len(x)):
                final.append([])
                

        counter=-1
        for x in r:
            for i in x:
                for j in data_epafi:
                    if i[0]==j[0]:
                        counter+=1
                        for k in range(1,4,1):
                            final[counter].append(j[k])
                        for z in range(1,10,1):
                            if z==7:
                                final[counter].append(i[z]+i[z+1])
                            elif z==8:
                                continue
                            else:
                                final[counter].append(i[z])


        frame_records=tk.Frame(master=window,pady=30)
        frame_records.pack()
        buttonsRDV=[]
        frame_row=tk.Frame(master=frame_records,highlightbackground="black", highlightthickness=1)
        for i in range(len(final)):
            frame_row.grid(row=i,column=0,sticky="nsew")
            for j in range(len(final[i])+1):
                if j!=0 and j!=len(final[i]):
                    label=tk.Label(master=frame_row,text=str(final[i][j-1]),font="ARIAL 10",padx=5,highlightbackground="black", highlightthickness=1).grid(row=i,column=j,sticky="nsew")
                elif j==len(final[i]):
                    buttonsRDV.append(tk.Button(master=frame_row,text="Info RDV"))
                    buttonsRDV[i].config(command=lambda: show_infoRDV(final[i][j-1]))
                    buttonsRDV[i].grid(row=i,column=j)
                else:
                    label=tk.Label(master=frame_row,text=str(i+1),font="ARIAL 10",padx=5,highlightbackground="black", highlightthickness=1).grid(row=i,column=j,sticky="nsew")
                    
        
    else:
        messagebox.showinfo("Ενημέρωση","Εισάγετε στοιχεία για αναζήτηση")
       


def show_infoRDV(info):
    messagebox.showinfo("Πληροφορίες ραντεβού",info)
    

  
connection = pymysql.connect(host="localhost", user="root",
                             passwd="",database="call")
cursor=connection.cursor()
window=Tk()
window.title("CRM")
window.state("zoomed")
title_frame=tk.Frame(master=window,pady=20)
title_frame.pack()
lbl_title=tk.Label(master=title_frame,text="ΑΡΧΙΚΟ ΜΕΝΟΥ",font="ARIAL 20")
lbl_title.pack()
menu_frame=tk.Frame(master=window,pady=50)
menu_frame.pack()
button_new_contact=tk.Button(master=menu_frame,text="Δημιουργία νέας επαφής",width=30,height=2,command=newContactForm).grid(row=0,column=0)
lblBlank1=tk.Label(master=menu_frame,text="",width=10).grid(row=0,column=1)
button_new_company=tk.Button(master=menu_frame,text="Δημιουργία νέας εταιρείας",width=30,height=2,command=newCompanyForm).grid(row=0,column=2)
lblBlank2=tk.Label(master=menu_frame,text="",width=10).grid(row=0,column=3)
button_addSupplyInExistingContact=tk.Button(master=menu_frame,text="Προσθήκη αίτησης\nσε υπάρχουσα επαφή ή εταιρεία",width=30,height=2,command=addSupplyExistingAFM).grid(row=0,column=4)
lblBlank3=tk.Label(master=menu_frame,text="",width=10).grid(row=0,column=5)
button_checkAFM=tk.Button(master=menu_frame,text="Έλεγχος ΑΦΜ",width=30,height=2,command=checkAFM).grid(row=0,column=6)
frame_search_AFM=tk.Frame(master=window,pady=40)
button_frame=tk.Frame(master=window,pady=50)
frame=tk.Frame(master=window,pady=40)
form_frame=tk.Frame(master=window,pady=20,padx=20,highlightbackground="black", highlightthickness=3)
form_Company_frame=tk.Frame(master=window,pady=20,padx=20,highlightbackground="black", highlightthickness=3)
form_power_frame=tk.Frame(master=window)
form_power_frame2=tk.Frame(master=window,pady=30)
address_frame=tk.Frame(master=form_power_frame)
buttonSaveSupplyPower=tk.Button(master=window)
mainMenu=tk.Button(master=window,command=menuAsk,text="ΕΠΙΣΤΡΟΦΗ ΣΤΟ\nΑΡΧΙΚΟ ΜΕΝΟΥ").place(relx=1,x=0,y=0,anchor=NE)
form_gas_frame=tk.Frame(master=window)
address_gas_frame=tk.Frame(master=form_gas_frame)
form_gas_frame2=tk.Frame(master=window,pady=30)
buttonSaveSupplyGas=tk.Button(master=window)
frameToPDF=tk.Frame(master=window,pady=15)
buttonToPDF=tk.Button(master=frameToPDF)
frame_buttonGasToPDF=tk.Frame(master=window,pady=30)
buttonGasToPDF=tk.Button(master=frame_buttonGasToPDF,text="Δημιουργία PDF")
etairika_AFM=["9","8","09","08"]
frame_admin_login=tk.Frame(master=menu_frame,pady=80)
frame_admin_login.grid(row=1,column=2,columnspan=3,sticky="we")
button_admin_login=tk.Button(master=frame_admin_login,text="Αναζήτηση πελάτη",width=30,height=2,command=admin_login)
button_admin_login.pack()
frame_login=tk.Frame(master=frame_admin_login,pady=30)
frame_admin_search=tk.Frame(master=window,pady=30)
frame_show_data_admin=tk.Frame(master=window,pady=40)
frame_show_supply_admin=tk.Frame(master=window,pady=40)



window.mainloop()
connection.close()
