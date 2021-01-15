from tkinter import*
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import Databasehotel
import datetime
import time
import tkinter
from datetime import datetime,timedelta
import random

#frontend

class Hotel:
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Database Management System")
        self.root.geometry("1250x600+0+0")
       
        MainFrame = Frame(self.root)
        MainFrame.grid()
        TopFrame = Frame(MainFrame, bd=10, width=1350, height=550, padx=2, relief=RIDGE)
        TopFrame.pack(side=TOP)
        
        LeftFrame = Frame(TopFrame, bd=5, width=400, height=550,relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        
        RightFrame = Frame(TopFrame, bd=5, width=820, height=550,relief=RIDGE)
        RightFrame.pack(side=RIGHT)

        RightFrame1 = Frame(RightFrame, bd=5, width=800, height=50, padx=10, relief=RIDGE)
        RightFrame1.grid(row=0,column=0)
        RightFrame2 = Frame(RightFrame, bd=5, width=800, height=100, padx=3, relief=RIDGE)
        RightFrame2.grid(row=1,column=0)
        RightFrame3 = Frame(RightFrame, bd=5, width=800, height=400, padx=4, relief=RIDGE)
        RightFrame3.grid(row=3,column=0)

        BottomFrame = Frame(MainFrame, bd=10, width=1350, height=150, padx=2, relief=RIDGE)
        BottomFrame.pack(side=BOTTOM)
        
        global hd
        CusID = StringVar()
        Firstname = StringVar()
        Lastname = StringVar()
        Address = StringVar()
        Mobile = StringVar()
        Email = StringVar()
        DoB = StringVar()
        Nationality = StringVar()
        ProveOfID = StringVar()
        DateIn = StringVar()
        DateOut = StringVar()
        RoomType = StringVar()
        RoomNo = StringVar()
        RoomExtNo = StringVar()
        TotalCost = StringVar()
        SubTotal = StringVar()
        PaidTax = StringVar()
        Meal = StringVar()
        Gender = StringVar()
        TotalDays = StringVar()
        DateIn.set(time.strftime("%d/%m/%Y"))
        DateOut.set(time.strftime("%d/%m/%Y"))

        x = random.randint(1190,8746)
        randomRef = str(x)
        CusID.set("Hotel"+ randomRef)

        def iExit():
            iExit = tkinter.messagebox.askyesno("Hotel Database Management System","Confim if you want to exit")
            if iExit > 0:
                root.destroy()
                return
        def Reset():

            Meal.set("")   
            ProveOfID.set("") 
            RoomType.set("")
            TotalDays.set("")
            RoomExtNo.set("")
            RoomNo.set("") 
            TotalCost.set("")
            self.txtFirstname.delete(0,END)
            self.txtLastname.delete(0,END)
            self.txtAddress.delete(0,END)
            self.txtMobile.delete(0,END)
            self.txtPaidTax.delete(0,END)
            self.txtSubTotal.delete(0,END)
            self.txtTotalCost.delete(0,END)
            self.txtNationality.delete(0,END)
            self.txtEmail.delete(0,END)
            self.txtDoB.delete(0,END)
            self.txtTotalDays.delete(0,END)
            DateIn.set(time.strftime("%d/%m/%Y"))
            DateOut.set(time.strftime("%d/%m/%Y"))


            x = random.randint(1190,8746)
            randomRef = str(x)
            CusID.set("Hotel"+ randomRef)
        
        def HotelRec():
            global hd
            searchHdb = lstHotel.curselection()[0]
            hd = lstHotel.get(searchHdb)
            self.txtcusID.delete(0,END)
            self.txtcusID.insert(END,hb[1])
            self.txtFirstname.delete(0,END)
            self.txtFirstname.insert(END,hb[2])
            self.txtLastname.delete(0,END)
            self.txtLastname.insert(END,hb[3])
            self.cboProveOfID.delete(0,END)
            self.cboProveOfID.insert(END,hb[4])
            self.txtNationality.delete(0,END)
            self.txtNationality.insert(END,hb[5])
            self.txtEmail.delete(0,END)
            self.txtEmail.insert(END,hb[6])
            self.txtAddress.delete(0,END)
            self.txtAddress.insert(END,hb[7])
            self.txtMobile.delete(0,END)
            self.txtMobile.insert(END,hb[8])
            self.txtDateIn.delete(0,END)
            self.txtDateIn.insert(END,hb[9])
            self.txtDateOut.delete(0,END)
            self.txtDateOut.insert(END,hb[10])

        def TotalCostandAddDate():
            addDate()
            InDate = DateIn.get
            OutDate = DateOut.get
            Indate = datetime.strptime(InDate,"%d/%m/%y")
            Outdate = datetime.strptime(OutDate,"%d/%m/%y")
            TotalDays.set(abs((OutDate - InDate).days))
            
            if (meal.get() == "Dinner" and RoomType.get() == "single"):

                q1 = float(17)
                q2 = float(34)
                q3 = float (TotalDays.get())
                q4 = float (q1 + q2)
                q5 = float (q3 +q4)
                Tax = "#" + str('%.2f'%((q5) * 0.09))
                ST = "#" + str('%.2f'%((q5))
                TT = "#" + str('%.2f'%(q5 + ((q5) * 0.09))
                PaidTax.st(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT) 
            elif(meal.get() == "Breakfast" and RoomType.get() == "Double"):

                q1 = float(35)
                q2 = float(43)
                q3 = float (TotalDays.get())
                q4 = float (q1 + q2)
                q5 = float (q3 +q4)
                Tax = "#" + str('%.2f'%((q5) * 0.09))
                ST  = "#" + str('%.2f'%((q5))
                TT = "#" + str('%.2f'%(q5 + ((q5) * 0.09))
                PaidTax.st(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif(meal.get() == "Breakfast" and RoomType.get() == "Family"):

                q1 = float(45)
                q2 = float(63)
                q3 = float (TotalDays.get())
                q4 = float (q1 + q2)
                q5 = float (q3 +q4)
                Tax = "#" + str('%.2f'%((q5) * 0.09))
                ST  = "#" + str('%.2f'%((q5)))
                TT = "#" + str('%.2f'%(q5 + ((q5) * 0.09)))
                PaidTax.st(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif(meal.get() == "Lunch" and RoomType.get() == "Family"):

                q1 = float(45)
                q2 = float(63)
                q3 = float (TotalDays.get())
                q4 = float (q1 + q2)
                q5 = float (q3 +q4)
                Tax = "#" + str('%.2f'%((q5) * 0.09)))
                ST  = "#" + str('%.2f'%((q5)))
                TT = "#" + str('%.2f'%(q5 + ((q5) * 0.09)))
                PaidTax.st(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT) 

            elif(meal.get() == "Dinner" and RoomType.get() == "Single"):

                q1 = float(45)
                q2 = float(63)
                q3 = float (TotalDays.get())
                q4 = float (q1 + q2)
                q5 = float (q3 +q4)
                Tax = "#" + str('%.2f'%((q5) * 0.09)))
                ST  = "#" + str('%.2f'%((q5)))
                TT = "#" + str('%.2f'%(q5 + ((q5) * 0.09)))
                PaidTax.st(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)


        def DisplayDate():
            lstHotel.delete(0,END)
            for row in Databasehotel.viewData():
                lstHotel.insert(END,row,str(""))  

        def addDate():
            if (len(CusID.get())!=0):
                Databasehotel.addHotel(CusID.get(),Firstname.get(),Lastname.get(),Address.get(), Mobile.get(),Nationality.get(),ProveOfID.get(),DateIn.get(),DateOut.get(),Email.get())
                lstHotel.delete(0,END)
                lstHotel.insert(END, (CusID.get(),Firstname.get(),Lastname.get(),Address.get(), Mobile.get(),Nationality.get(),ProveOfID.get(),DateIn.get(),DateOut.get(),Email.get())
        



        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
        
        self.cusID = Label(LeftFrame, font=('arial',12,'bold'), text="Customer Ref:", padx=1)
        self.cusID.grid(row=0,column=0, sticky=W)
        self.txtcusID=Entry(LeftFrame, font=('arial' ,12, 'bold'), width=18, textvariable=CusID)
        self.txtcusID.grid(row=0,column=1, pady=3, padx=20)
        
        self.TotalCost = Label(RightFrame3, font=('arial', 12,'bold'),text="Total Cost:",padx=2,pady=2)
        self.TotalCost.grid(row=3,column=0, sticky=W)
        self.txtTotalCost=Entry(RightFrame3, font=('arial' ,12, 'bold'), width=76, textvariable=TotalCost)
        self.txtTotalCost.grid(row=3,column=1, pady=3, padx=20)

        self.Firstname = Label(LeftFrame, font=('arial',12,'bold'), text="Firstname:", padx=1)
        self.Firstname.grid(row=1,column=0, sticky=W)
        self.txtFirstname=Entry(LeftFrame, font=('arial' ,12, 'bold'), width=18, textvariable=Firstname)
        self.txtFirstname.grid(row=1,column=1, pady=3, padx=20)

        self.Lastname = Label(LeftFrame, font=('arial',12,'bold'), text="Lastname:", padx=1)
        self.Lastname.grid(row=2,column=0, sticky=W)
        self.txtLastname=Entry(LeftFrame, font=('arial' ,12, 'bold'), width=18,textvariable=Lastname)
        self.txtLastname.grid(row=2,column=1, pady=3, padx=20)

        self.Address = Label(LeftFrame, font=('arial',12,'bold'), text="Address:", padx=1)
        self.Address.grid(row=4,column=0, sticky=W)
        self.txtAddress=Entry(LeftFrame, font=('arial' ,12, 'bold'), width=18, textvariable=Address)
        self.txtAddress.grid(row=4,column=1, pady=3, padx=20)

        self.Email = Label(LeftFrame, font=('arial',12,'bold'), text="Email:", padx=1)
        self.Email.grid(row=5,column=0, sticky=W)
        self.txtEmail=Entry(LeftFrame, font=('arial' ,12, 'bold'), width=18, textvariable=Email)
        self.txtEmail.grid(row=5,column=1, pady=3, padx=20)

        self.DoB = Label(LeftFrame, font=('arial',12,'bold'), text="Date of Birth:", padx=1)
        self.DoB.grid(row=6,column=0, sticky=W)
        self.txtDoB=Entry(LeftFrame, font=('arial' ,12, 'bold'), width=18, textvariable=DoB)
        self.txtDoB.grid(row=6,column=1, pady=3, padx=20)

        self.Nationality = Label(LeftFrame, font=('arial',12,'bold'), text="Nationality:", padx=1)
        self.Nationality.grid(row=7,column=0, sticky=W)
        self.txtNationality=Entry(LeftFrame, font=('arial' ,12, 'bold'), width=18, textvariable=Nationality)
        self.txtNationality.grid(row=7,column=1, pady=3, padx=20)

        self.mobile = Label(LeftFrame, font=('arial',12,'bold'), text="Mobile:", padx=1)
        self.mobile.grid(row=8,column=0, sticky=W)
        self.txtMobile=Entry(LeftFrame, font=('arial' ,12, 'bold'), width=18, textvariable=Mobile)
        self.txtMobile.grid(row=8,column=1, pady=3, padx=20)

        self.DateIn = Label(LeftFrame, font=('arial',12,'bold'), text="Check In Date:", padx=1)
        self.DateIn.grid(row=9,column=0, sticky=W)
        self.txtDateIn=Entry(LeftFrame, font=('arial' ,12, 'bold'), width=18, textvariable=DateIn)
        self.txtDateIn.grid(row=9,column=1, pady=3, padx=20)

        self.DateOut = Label(LeftFrame, font=('arial',12,'bold'), text="Check out Date:", padx=1)
        self.DateOut.grid(row=10,column=0, sticky=W)
        self.txtDateOut=Entry(LeftFrame, font=('arial' ,12, 'bold'), width=18, textvariable=DateOut)
        self.txtDateOut.grid(row=10,column=1, pady=3, padx=20)

        self.ProveOfID = Label(LeftFrame, font=('arial', 12,'bold'),text="Type of ID:",padx=2,pady=2)
        self.ProveOfID.grid(row=11,column=0, sticky=W)
        self.cboProveOfID=ttk.Combobox(LeftFrame, textvariable=ProveOfID, state='readonly', font=('arial',12,'bold'),width=18)
        self.cboProveOfID ['value'] = ('','Pilot Licence','Driving Licence', 'Student ID','Passport')
        self.cboProveOfID.current(0)
        self.cboProveOfID.grid(row=11,column=1,pady=3,padx=2)

        self.Meal = Label(LeftFrame, font=('arial', 12,'bold'),text="Meal:",padx=2,pady=2)
        self.Meal.grid(row=12,column=0, sticky=W)
        self.cboMeal=ttk.Combobox(LeftFrame, textvariable=Meal, state='readonly', font=('arial',12,'bold'),width=18)
        self.cboMeal ['value'] = ('','Breakfast','Brunch', 'Lunch','Dinner')
        self.cboMeal.current(0)
        self.cboMeal.grid(row=12,column=1,pady=3,padx=2)

        self.RoomType = Label(LeftFrame, font=('arial', 12,'bold'),text="Room Type:",padx=2,pady=2)
        self.RoomType.grid(row=13,column=0, sticky=W)
        self.cboRoomType=ttk.Combobox(LeftFrame, textvariable=RoomType, state='readonly', font=('arial',12,'bold'),width=18)
        self.cboRoomType ['value'] = ('','Single','Double', 'Family')
        self.cboRoomType.current(0)
        self.cboRoomType.grid(row=13,column=1,pady=3,padx=2)

        self.RoomNo = Label(LeftFrame, font=('arial', 12,'bold'),text="Room No:",padx=2,pady=2)
        self.RoomNo.grid(row=14,column=0, sticky=W)
        self.cboRoomNo=ttk.Combobox(LeftFrame, textvariable=RoomNo, state='readonly', font=('arial',12,'bold'),width=18)
        self.cboRoomNo ['value'] = ('','001','002', '003','004','005','007','008')
        self.cboRoomNo.current(0)
        self.cboRoomNo.grid(row=14,column=1,pady=3,padx=2)

        self.RoomExtNo = Label(LeftFrame, font=('arial', 12,'bold'),text="Room Ext. No:",padx=2,pady=2)
        self.RoomExtNo.grid(row=15,column=0, sticky=W)
        self.cboRoomExtNo=ttk.Combobox(LeftFrame, textvariable=RoomExtNo, state='readonly', font=('arial',12,'bold'),width=18)
        self.cboRoomExtNo ['value'] = ('','100','101', '102','103','104','105','106','107','108')
        self.cboRoomExtNo.current(0)
        self.cboRoomExtNo.grid(row=15,column=1,pady=3,padx=2)

        #========================================Widget==============================================================


        self.Label = Label(RightFrame1,font=('arial',12,'bold'),padx=6,pady=10,
        text="Customer Ref\tFirstname \tLastname \tAddress\tMobile\tNationality\tProveOfID\tDateIn\tDateOut\t\tEmail")
        self.Label.grid(row=0,column=0, columnspan=17)

        scrollbar = Scrollbar(RightFrame2)
        scrollbar.grid(row=0,column=0,sticky='ns')
        lstHotel = Listbox(RightFrame2, width=103,height=14,font=('arial',10,'bold'),yscrollcommand=scrollbar.set)
        lstHotel.bind('<<ListboxSelect>>',HotelRec)
        lstHotel.grid(row=0,column=0,padx=7,sticky='nsew')
        scrollbar.config(command = lstHotel.xview) 

        #=======================================Widget=================================================================
        
        self.TotalDays = Label(RightFrame3, font=('arial', 12,'bold'),text="No of Days:",padx=2,pady=2)
        self.TotalDays.grid(row=0,column=0, sticky=W)
        self.txtTotalDays = Entry(RightFrame3, font=('arial' ,12, 'bold'), width=76, textvariableTotalDays)
        self.txtTotalDays .grid(row=0,column=1, pady=3, padx=20)

        self.PaidTax =Label(RightFrame3, font=('arial', 12,'bold'),text="Paid Tax:",padx=2,pady=2)
        self.PaidTax.grid(row=1,column=0, sticky=W)
        self.txtPaidTax = Entry(RightFrame3, font=('arial' ,12, 'bold'), width=76)
        self.txtPaidTax.grid(row=1,column=1, pady=3, padx=20)

        self.Subtotal = Label(RightFrame3, font=('arial', 12,'bold'),text="Subtotal:",padx=2,pady=2)
        self.Subtotal.grid(row=2,column=0, sticky=W)
        self.txtSubTotal = Entry(RightFrame3, font=('arial' ,12, 'bold'), width=76)
        self.txtSubTotal.grid(row=2,column=1, pady=3, padx=20)

        self.TotalCost = Label(RightFrame3, font=('arial', 12,'bold'),text="Total Cost:",padx=2,pady=2)
        self.TotalCost.grid(row=3,column=0, sticky=W)
        self.txtTotalCost  = Entry(RightFrame3, font=('arial' ,12, 'bold'), width=76)
        self.txtTotalCost.grid(row=3,column=1, pady=3, padx=20)

        #=======================================Widget Button======================================================================
        
        
        self.btnTotalandAddData = Button(BottomFrame, bd=4, font=('arial',16,'bold'),
        width=13, height=2, text="AddNew/Total", command=TotalCostandAddDate).grid(row=0, column=0, padx=4, pady=1)

        self.btnDisplay = Button(BottomFrame, bd=4, font=('arial',16,'bold'),
        width=13, height=2, text="Display",command=DisplayDate).grid(row=0, column=1, padx=4, pady=1)

        self.btnUpdate = Button(BottomFrame, bd=4, font=('arial',16,'bold'), 
        width=13, height=2, text="Update",command=UpdateData).grid(row=0, column=2, padx=4, pady=1)

        self.btnDelete = Button(BottomFrame, bd=4, font=('arial',16,'bold'),
        width=13, height=2, text="Delete",command=DeleteData).grid(row=0, column=3, padx=4, pady=1)

        self.btnSearch = Button(BottomFrame, bd=4, font=('arial',16,'bold'),
        width=13, height=2, text="Search",command=SearchDatabase).grid(row=0, column=4, padx=4, pady=1)

        self.btnReset = Button(BottomFrame, bd=4, font=('arial',16,'bold'),
        width=13, height=2, text="Reset", command=Reset).grid(row=0, column=5, padx=4, pady=1)

        self.btnExit = Button(BottomFrame, bd=4,font=('arial',16,'bold'),
        width=13, height=2, text="Exit", command=iExit).grid(row=0, column=6, padx=4, pady=1)

if __name__=='__main__':
    root = Tk()
    application = Hotel(root)
    root.mainloop()