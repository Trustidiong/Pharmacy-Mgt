from tkinter import *
from tkinter import ttk
#import mysql.connector

from PIL import Image, ImageTk # pip install pillow
class PharmacyManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1350x800+0+0")
        #self.root.config(bg="white")

        lbltitle = Label(self.root, text = "PHARMACY MANAGEMENT SYSTEM", bd=10, relief=RIDGE, bg ="white", fg = "darkgreen", 
                    font=("times new roman", 40, "bold"),padx=2, pady=4)
        lbltitle.pack(side=TOP, fill = X)

        img1 = Image.open("logo.jpg")
        img1.resize((80, 60), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1 = Button(self.root, image=self.photoimg1, borderwidth=0)
        b1.place(x=20, y=10)

#========DATAFRAME=============
        DataFrame = Frame(self.root, bd=5, relief=RIDGE, padx=20)
        DataFrame.place(x=0, y=100, width=1350, height = 380)

        DataFrameLeft = LabelFrame(DataFrame, bd=5, relief=RIDGE, padx=10, text="Medicine Information",fg = "darkgreen", 
                font=("arial", 12, "bold") )
        DataFrameLeft.place(x=0, y=5, width=780, height = 350)

        DataFrameRight = LabelFrame(DataFrame, bd=5, relief=RIDGE, padx=10, text="Medicine Add Department",fg = "darkgreen", 
                font=("arial", 12, "bold") )
        DataFrameRight.place(x=800, y=5, width=500, height = 350)

        #========BUTTOM FRAME===========
        ButtonFrame = Frame(self.root, bd=5, relief=RIDGE, padx=20)
        ButtonFrame.place(x=0, y=480, width=1350, height = 55)

         #========MAIN BUTTOM ===========
        btnAddData = Button(ButtonFrame, text="Add Medicine",bg = "darkgreen", fg="white", font=("arial", 12, "bold") )
        btnAddData.grid(row = 0, column=0)

        btnUpdateMed = Button(ButtonFrame, text="UPDATE", width=12, bg = "darkgreen", fg="white", font=("arial", 12, "bold") )
        btnUpdateMed.grid(row = 0, column=1)

        btnDeleteMed = Button(ButtonFrame, text="DELETE", width=12, bg = "red", fg="white", font=("arial", 12, "bold") )
        btnDeleteMed.grid(row = 0, column=2)

        btnResetMed = Button(ButtonFrame, text="RESET", width=12, bg = "darkgreen", fg="white", font=("arial", 12, "bold") )
        btnResetMed.grid(row = 0, column=3)

        btnEXitMed = Button(ButtonFrame, text="EXIT", width=12, bg = "darkgreen", fg="white", font=("arial", 12, "bold") )
        btnEXitMed.grid(row = 0, column=4)

 #========SEARCH BY ===========
        lblSearch = Label(ButtonFrame, font=("arial", 12, "bold"), text="Search By", bg = "red", fg="white",  padx=2 )
        lblSearch.grid(row = 0, column=5, sticky=W)

        search_cmb = ttk.Combobox(ButtonFrame, width=10,font=("arial", 12, "bold"), state = "readonly")
        search_cmb["values"] = ("Ref", "MedName", "Lot")
        search_cmb.grid(row = 0, column=6)
        search_cmb.current(0)

        txtSearch = Entry(ButtonFrame, bd=3, relief=RIDGE, width=20,font=("arial", 12, "bold") )
        txtSearch.grid(row = 0, column=7)

        btnSearch = Button(ButtonFrame, text="Search", width=10, bg = "darkgreen", fg="white", font=("arial", 12, "bold") )
        btnSearch.grid(row = 0, column=8)

        btnShowAll = Button(ButtonFrame, text="Show All", width=10, bg = "darkgreen", fg="white", font=("arial", 12, "bold") )
        btnShowAll.grid(row = 0, column=9)

#=========== LABELS AND ENTRY============
        lblRefNo = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Reference No:",  padx=2 )
        lblRefNo.grid(row = 0, column=0, sticky=W)

        ref_cmb = ttk.Combobox(DataFrameLeft, width=25,font=("arial", 10, "bold"), state = "readonly")
        ref_cmb["values"] = ("Ref", "MedName", "Lot")
        ref_cmb.grid(row = 0, column=1)
        ref_cmb.current(0)

        lblCompName = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Company Name:",  padx=2, pady=6 )
        lblCompName.grid(row = 1, column=0, sticky=W)

        txtCompName = Entry(DataFrameLeft, width=27,font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE)
        txtCompName.grid(row = 1, column=1)

        lblMedType = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Type of Medicine:",  padx=2 )
        lblMedType.grid(row = 2, column=0, sticky=W)

        cmb_MedType = ttk.Combobox(DataFrameLeft, width=25,font=("arial", 10, "bold"), state = "readonly")
        cmb_MedType["values"] = ("Tablet", "Liquid", "Capsule", "Topical Medicine", "Drops", "Inhales", "Injection")
        cmb_MedType.grid(row = 2, column=1)
        cmb_MedType.current(0)

#================ ADD MEDICINE=======
        lblMedName = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Medicine Name:",  padx=2, pady=6 )
        lblMedName.grid(row = 3, column=0, sticky=W)

        cmb_MedName = ttk.Combobox(DataFrameLeft, width=25,font=("arial", 10, "bold"), state = "readonly")
        cmb_MedName["values"] = ("Nice", "Novel")
        cmb_MedName.grid(row = 3, column=1)
        cmb_MedName.current(0)

        lblLotNo = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Lot No:",  padx=2, pady=6 )
        lblLotNo.grid(row = 4, column=0, sticky=W)

        txtLotNo = Entry(DataFrameLeft, width=27,font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE)
        txtLotNo.grid(row = 4, column=1)

        lblIssueDate = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Issue Date:",  padx=2, pady=6 )
        lblIssueDate.grid(row = 5, column=0, sticky=W)

        txtIssueDate = Entry(DataFrameLeft, width=27,font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE)
        txtIssueDate.grid(row = 5, column=1)

        lblExpDate = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Exp Date:",  padx=2, pady=6 )
        lblExpDate.grid(row = 6, column=0, sticky=W)

        txtExpDate = Entry(DataFrameLeft, width=27,font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE)
        txtExpDate.grid(row = 6, column=1)

        lblUses = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Uses:",  padx=2, pady=6 )
        lblUses.grid(row = 7, column=0, sticky=W)

        txtUses = Entry(DataFrameLeft, width=27,font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE)
        txtUses.grid(row = 7, column=1)

        lblSideEff = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Side Effects:",  padx=2, pady=6 )
        lblSideEff.grid(row = 8, column=0, sticky=W)

        txtSideEff = Entry(DataFrameLeft, width=27,font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE)
        txtSideEff.grid(row = 8, column=1)

        lblPrec = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Precautions & Warning:",  padx=20, pady=6 )
        lblPrec.grid(row = 0, column=2, sticky=W)

        txtPrec = Entry(DataFrameLeft, width=27,font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE)
        txtPrec.grid(row = 0, column=3)

        lblDosage = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Dosage:",  padx=20, pady=6 )
        lblDosage.grid(row = 1, column=2, sticky=W)

        txtDosage = Entry(DataFrameLeft, width=27,font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE)
        txtDosage.grid(row = 1, column=3)

        lblPrice = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Tablet Price:",  padx=20, pady=6 )
        lblPrice.grid(row = 2, column=2, sticky=W)

        txtPrice = Entry(DataFrameLeft, width=27,font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE)
        txtPrice.grid(row = 2, column=3)

        lblQT = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Product QT:",  padx=20, pady=6 )
        lblQT.grid(row = 3, column=2, sticky=W)

        txtQT = Entry(DataFrameLeft, width=27,font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE)
        txtQT.grid(row = 3, column=3)

#==== PHARM PIX =====
        img2 = Image.open("Pharmacy.jpg")
        #img2.resize((300, 200), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        b2 = Button(DataFrameLeft, image=self.photoimg2, borderwidth=0)
        b2.place(x=340, y=130)


#==== DATAFRAME RIGHT =====
        img3 = Image.open("ecg.jpg")
        #img2.resize((300, 200), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        b3 = Button(DataFrameRight, image=self.photoimg3, borderwidth=0)
        b3.place(x=1, y=2)

        img4 = Image.open("a.jpg")
        #img2.resize((300, 200), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b4 = Button(DataFrameRight, image=self.photoimg4, borderwidth=0)
        b4.place(x=285, y=2)


        lblRefNo = Label(DataFrameRight, font=("arial", 10, "bold"), text="Reference No:",  padx=2 )
        lblRefNo.place(x=0, y=90)

        txtRefNo = Entry(DataFrameRight, width=20,font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE)
        txtRefNo.place(x=110, y=90)

        lblMedName = Label(DataFrameRight, font=("arial", 10, "bold"), text="Medicine Name:",  padx=2)
        lblMedName.place(x=0, y=120)

        txtMedName = Entry(DataFrameRight, width=20,font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE)
        txtMedName.place(x=110, y=120)

#================ ADD MEDICINE BUTTONS=======
        sideFrame = Frame(DataFrameRight, bd=4, relief=RIDGE, bg="white")
        sideFrame.place(x=0, y=150, width=290, height=160)

        scX = ttk.Scrollbar(sideFrame, orient=HORIZONTAL)
        scX.pack(side=BOTTOM, fill=X)
        scY = ttk.Scrollbar(sideFrame, orient=VERTICAL)
        scY.pack(side=RIGHT, fill=Y)

        self.medTable = ttk.Treeview(sideFrame, column=("ref", "medname"), xscrollcommand=scX.set, yscrollcommand=scY.set)

        scX.config(command=self.medTable.xview)
        scY.config(command=self.medTable.yview)

        self.medTable.heading("ref", text="Ref")
        self.medTable.heading("medname", text="Medicine Name")

        self.medTable["show"]="headings"
        self.medTable.pack(fill=BOTH, expand=1)

        self.medTable.column("ref", width=100)
        self.medTable.column("medname", width=100)

        downFrame = Frame(DataFrameRight, bd=4, relief=RIDGE, bg="darkgreen")
        downFrame.place(x=330, y=150, width=135, height=160)

        btnAdd = Button(downFrame, text="ADD",bg = "lime", fg="white", font=("arial", 12, "bold"), width=12, pady=4 )
        btnAdd.grid(row = 0, column=0)
        
        btnUpdate = Button(downFrame, text="UPDATE",bg = "purple", fg="white", font=("arial", 12, "bold"), width=12, pady=4 )
        btnUpdate.grid(row = 1, column=0)
        
        btnDelete = Button(downFrame, text="DELETE",bg = "red", fg="white", font=("arial", 12, "bold"), width=12, pady=4 )
        btnDelete.grid(row = 2, column=0)
        
        btnClear = Button(downFrame, text="CLEAR",bg = "orange", fg="white", font=("arial", 12, "bold"), width=12, pady=4 )
        btnClear.grid(row = 3, column=0)

        #=====FRAME DETAILS========
        frameDetails = Frame(self.root, bd=5, relief=RIDGE)
        frameDetails.place(x=0, y=520, width=1350, height=160)

         #=====MAIN TABLE SCROOL BAR========
        tableFrame = Frame(frameDetails, bd=5, relief=RIDGE, padx=20)
        tableFrame.place(x=0, y=1, width=1350, height=150)

        scX = ttk.Scrollbar(tableFrame, orient=HORIZONTAL)
        scX.pack(side=BOTTOM, fill=X)
        scY = ttk.Scrollbar(tableFrame, orient=VERTICAL)
        scY.pack(side=RIGHT, fill=Y)

        self.pharmTable = ttk.Treeview(tableFrame, column=("ref", "companyname", "type", "tabletname", "lotno", "issuedate", 
                        "expdate", "uses", "sideeffect", "warning", "dosage", "price", "productqt",), 
                        xscrollcommand=scX.set, yscrollcommand=scY.set)

        scX.pack(side=BOTTOM, fill=X)
        scY.pack(side=RIGHT, fill=Y)

        scX.config(command=self.pharmTable.xview)
        scY.config(command=self.pharmTable.yview)

        self.pharmTable["show"]="headings"
        

        self.pharmTable.heading("ref", text="Reference No")
        self.pharmTable.heading("companyname", text="Company Name")
        self.pharmTable.heading("type", text="Type of Medicine")
        self.pharmTable.heading("tabletname", text="Tablet Name")
        self.pharmTable.heading("lotno", text="Lot No")
        self.pharmTable.heading("issuedate", text="Issue Date")
        self.pharmTable.heading("expdate", text="Exp Date")
        self.pharmTable.heading("uses", text="Uses")
        self.pharmTable.heading("sideeffect", text="Side Effects")
        self.pharmTable.heading("warning", text="Prec & Warning")
        self.pharmTable.heading("dosage", text="Dosage")
        self.pharmTable.heading("price", text="Price")
        self.pharmTable.heading("productqt", text="Product QT")
        self.pharmTable.pack(fill=BOTH, expand=1)

        self.pharmTable.column("ref", width=100)
        self.pharmTable.column("companyname", width=100)
        self.pharmTable.column("type", width=100)
        self.pharmTable.column("tabletname", width=100)
        self.pharmTable.column("lotno", width=100)
        self.pharmTable.column("issuedate", width=100)
        self.pharmTable.column("expdate", width=100)
        self.pharmTable.column("uses", width=100)
        self.pharmTable.column("sideeffect", width=100)
        self.pharmTable.column("warning", width=100)
        self.pharmTable.column("dosage", width=100)
        self.pharmTable.column("price", width=80)
        self.pharmTable.column("productqt", width=100)

        #============== FUNCTIONS ============



if __name__ == '__main__':
    root = Tk()
    obj = PharmacyManagementSystem(root)
    root.mainloop()