from tkinter import *
from tkinter import messagebox
import random
import time
import os, shutil

root = Tk()
root.geometry("1350x750+0+0")
root.title("Engineering at Sriracha Coffee Shop")
root.configure(background='cyan')

Tops = Frame(root,width= 1350,height = 100, bd=14, relief="raise")
Tops.pack(side=TOP)


fMainL = Frame(root,width= 900,height = 650, bd=8, relief="raise")
fMainL.pack(side=LEFT)

fMainR = Frame(root,width= 440,height = 650, bd=8, relief="raise")
fMainR.pack(side=RIGHT)

fMLT = Frame(fMainL,width= 900,height = 320, bd=8, relief="raise")
fMLT.pack(side=TOP)

fMLB = Frame(fMainL,width= 900,height = 320, bd=6, relief="raise")
fMLB.pack(side=BOTTOM)

fReceipt = Frame(fMainR,width= 440,height = 450, bd=12, relief="raise")
fReceipt.pack(side=TOP)

fButton = Frame(fMainR,width= 440,height = 240, bd=12, relief="raise")
fButton.pack(side=BOTTOM)

fCoffee = Frame(fMLT,width= 400,height =
                330, bd=16, relief="raise")
fCoffee.pack(side=LEFT)
fCake = Frame(fMLT,width= 400,height = 320, bd=16, relief="raise")
fCake.pack(side=RIGHT)

fCost1 = Frame(fMLB,width= 440,height = 330, bd=14, relief="raise")
fCost1.pack(side=LEFT)
fCost2 = Frame(fMLB,width= 440,height = 320, bd=14, relief="raise")
fCost2.pack(side=RIGHT)

Tops.configure(background='pink')
fMainL.configure(background='blue')
fMainR.configure(background='blue')

lblInfo = Label(Tops,font=('TH Sarabun New',40,'bold'),text = "Engineering at Sriracha Coffee Shop",bg="yellow",bd=10)
lblInfo.grid(row=0,column=0)  

#============================= Function =====================
def qExit():
    qExit= messagebox.askyesno("Quit System!!!", "Do you want to quit?")
    if qExit > 0:
        root.destroy()
        return

def Reset():
    FrameDrinkReset()
    FrameCakeReset()
    FrameCostReset()
    txtReceipt.delete("1.0",END)

def FrameDrinkReset():
    VarLattae.set("0")
    VarEspresso.set("0")
    VarIceLattae.set("0")
    VarValeCoffee.set("0")
    VarCappuccino.set("0")
    VarAfricanCoffee.set("0")
    VarAmericanCoffee.set("0")
    VarIcedCappuccino.set("0")
    E_Lattae.set("0")
    E_Espresso.set("0")
    E_IceLattae.set("0")
    E_ValeCoffee.set("0")
    E_Cappuccino.set("0")
    E_AfricanCoffee.set("0")
    E_AmericanCoffee.set("0")
    E_IcedCappuccino.set("0")
    txtLattae.configure(state = DISABLED)
    txtEspresso.configure(state = DISABLED)
    txtIceLattae.configure(state = DISABLED)
    txtValeCoffee.configure(state = DISABLED)
    txtCappuccino.configure(state = DISABLED)
    txtAfricanCoffee.configure(state = DISABLED)
    txtAmericanCoffee.configure(state = DISABLED)
    txtIcedCappuccino.configure(state = DISABLED)

def FrameCakeReset():
    for x in VarCakeList:    
        x.set("0")

    for x in EntryCakeList:    
        x.set("0")

    txtCake0.configure(state = DISABLED)
    txtCake1.configure(state = DISABLED)
    txtCake2.configure(state = DISABLED)
    txtCake3.configure(state = DISABLED)
    txtCake4.configure(state = DISABLED)
    txtCake5.configure(state = DISABLED)
    txtCake6.configure(state = DISABLED)
    txtCake7.configure(state = DISABLED)
    
def FrameCostReset():
    CostofDrinks.set("")
    CostofCakes.set("")
    ServiceCharge.set("")
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofDrinks.set("")
    CostofCakes.set("")
                 
def chkbutton_value(chkValue,txtLabel,Entry):
    if chkValue.get() == 1:
        txtLabel.configure(state=NORMAL)
    elif chkValue.get() == 0:
        txtLabel.configure(state=DISABLED)
        Entry.set("0")

def CostofItem():    
  
       TotalDrinkCost = 0
       
       CakePriceList = [50,50,50,50,50,50,50,50]
       TotalCakeCost = 0

       for i in range(8):
             TotalCakeCost += int(EntryCakeList[i].get()) * float(CakePriceList[i])

       DrinksPrice = "B", str('%.2f'%(TotalDrinkCost))
       CakesPrice = "B", str('%.2f'%(TotalCakeCost))
       CostofDrinks.set(DrinksPrice)
       CostofCakes.set(CakesPrice)
       SC = "B", str('%.2f'%(1.59))
       ServiceCharge.set(SC)
       print(TotalCakeCost)

       CostPlus = TotalDrinkCost + TotalCakeCost + 1.59
        
       SubTotalofItems = "B", str('%.2f'%(CostPlus))
       SubTotal.set(SubTotalofItems)

       Tax = "B" , str('%.2f'%(CostPlus*0.15))
       PaidTax.set(Tax)
       TT = CostPlus * 0.15
       TC = "B" , str('%.2f'%(CostPlus + TT))
       TotalCost.set(TC)

def Receipt():
    txtReceipt.delete("1.0",END)
    x = random.randint(10908,500876)
    randomRef = str(x)
    ReceiptRef.set("BILL"+randomRef)

    txtReceipt.insert(END,'Receipt Ref:\t\t\t'+ ReceiptRef.get()  + '\t\t' + DateofOrder.get() + "\n")
    txtReceipt.insert(END,'Items\t\t\t\t\t'+ 'Cost of Items \n\n')
    txtReceipt.insert(END,'Lattae\t\t\t\t\t'+ E_Lattae.get() + '\n')
    txtReceipt.insert(END,'Espresso\t\t\t\t\t'+ E_Espresso.get() + '\n')
    txtReceipt.insert(END,'Iced Lattae\t\t\t\t\t'+ E_IceLattae.get() + '\n')
    txtReceipt.insert(END,'Vale Coffee\t\t\t\t\t'+ E_ValeCoffee.get() + '\n')
    txtReceipt.insert(END,'Cappuccino\t\t\t\t\t'+ E_Cappuccino.get() + '\n')
    txtReceipt.insert(END,'African Coffee\t\t\t\t\t'+ E_AfricanCoffee.get() + '\n')
    txtReceipt.insert(END,'American Coffee\t\t\t\t\t'+ E_AmericanCoffee.get() + '\n')
    txtReceipt.insert(END,'Ice Cappuccino\t\t\t\t\t'+ E_IcedCappuccino.get() + '\n')

    # --------------------------------------- #
    for i in range(8) :
        if int(EntryCakeList[i].get()) > 0 :
            txtReceipt.insert(END, file_read[i] +'\t\t\t\t\t'+ EntryCakeList[i].get() + '\n')

    txtReceipt.insert(END,'\nCost of Drinks : \t\t'+ CostofDrinks.get() + '\n')
    txtReceipt.insert(END,'Cost of Cakes : \t\t'+ CostofCakes.get() + '\n')
    txtReceipt.insert(END,'Service Charge : \t\t'+ ServiceCharge.get() + '\n')
        
#====================== Variable Coffee =====================
ReceiptRef = StringVar()
DateofOrder = StringVar()
DateofOrder.set(time.strftime("%d/%m/%Y"))

VarLattae = IntVar()
VarEspresso = IntVar()
VarIceLattae = IntVar()
VarValeCoffee = IntVar()
VarCappuccino = IntVar()
VarAfricanCoffee = IntVar()
VarAmericanCoffee = IntVar()
VarIcedCappuccino = IntVar()

VarLattae.set("0")
VarEspresso.set("0")
VarIceLattae.set("0")
VarValeCoffee.set("0")
VarCappuccino.set("0")
VarAfricanCoffee.set("0")
VarAmericanCoffee.set("0")
VarIcedCappuccino.set("0")

E_Lattae = StringVar()
E_Espresso = StringVar()
E_IceLattae = StringVar()
E_ValeCoffee = StringVar()
E_Cappuccino = StringVar()
E_AfricanCoffee = StringVar()
E_AmericanCoffee = StringVar()
E_IcedCappuccino = StringVar()


E_Lattae.set("0")
E_Espresso.set("0")
E_IceLattae.set("0")
E_ValeCoffee.set("0")
E_Cappuccino.set("0")
E_AfricanCoffee.set("0")
E_AmericanCoffee.set("0")
E_IcedCappuccino.set("0")


#====================== Variable Cake =====================

CakeList = open("CakeList.txt", "r", encoding="utf-8")
file_read = CakeList.readlines()
print(file_read)
CakeList.close()

VarCake0 = IntVar()
VarCake1 = IntVar()
VarCake2 = IntVar()
VarCake3 = IntVar()
VarCake4 = IntVar()
VarCake5 = IntVar()
VarCake6 = IntVar()
VarCake7 = IntVar()


VarCakeList = [VarCake0,VarCake1,VarCake2,VarCake3,
               VarCake4,VarCake5,VarCake6,VarCake7]
print(VarCakeList)
for x in VarCakeList:    
    x.set("0")

EntryCake0 = StringVar()
EntryCake1 = StringVar()
EntryCake2 = StringVar()
EntryCake3 = StringVar()
EntryCake4 = StringVar()
EntryCake5 = StringVar()
EntryCake6 = StringVar()
EntryCake7 = StringVar()

EntryCakeList = [EntryCake0,EntryCake1,EntryCake2,EntryCake3,
                 EntryCake4,EntryCake5,EntryCake6,EntryCake7]

for x in EntryCakeList:    
    x.set("0")
#===============================Variable Calculation =====================
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofDrinks = StringVar()
CostofCakes = StringVar()
ServiceCharge = StringVar()

#==================================== Drink =================================

Drink = open("Drink.txt", "r", encoding="utf-8")
file_read2 = Drink.readlines()
Drink.close()

"""Lattae = Checkbutton(fMLTa, text="Lattae \t",variable = var1,onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',18,'bold')).grid(row= 0, column = 0)"""
Lattae = Checkbutton(fCoffee, text=file_read2[0],variable = VarLattae,onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',16,'bold'),command=lambda:chkbutton_value(VarLattae,txtLattae,E_Lattae)).grid(row= 0, sticky=W)
Espresso = Checkbutton(fCoffee, text=file_read2[1],variable = VarEspresso,onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',16,'bold'),command=lambda:chkbutton_value(VarEspresso,txtEspresso,E_Espresso)).grid(row= 1, sticky=W)
IceLattae = Checkbutton(fCoffee, text=file_read2[2],variable = VarIceLattae,onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',16,'bold'),command=lambda:chkbutton_value(VarIceLattae,txtIceLattae,E_IceLattae)).grid(row= 2, sticky=W)
ValeCoffee = Checkbutton(fCoffee, text=file_read2[3],variable = VarValeCoffee,onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',16,'bold'),command=lambda:chkbutton_value(VarValeCoffee,txtValeCoffee,E_ValeCoffee)).grid(row= 3, sticky=W)
Cappuccino = Checkbutton(fCoffee, text=file_read2[4],variable = VarCappuccino,onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',16,'bold'),command=lambda:chkbutton_value(VarCappuccino,txtCappuccino,E_Cappuccino)).grid(row= 4, sticky=W)
AfricanCoffee = Checkbutton(fCoffee, text=file_read2[5],variable = VarAfricanCoffee,onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',16,'bold'),command=lambda:chkbutton_value(VarAfricanCoffee,txtAfricanCoffee,E_AfricanCoffee)).grid(row= 5, sticky=W)
AmericanCoffee = Checkbutton(fCoffee, text=file_read2[6],variable = VarAmericanCoffee,onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',16,'bold'),command=lambda:chkbutton_value(VarAmericanCoffee,txtAmericanCoffee,E_AmericanCoffee)).grid(row= 6, sticky=W)
IcedCappuccino = Checkbutton(fCoffee, text=file_read2[7],variable = VarIcedCappuccino,onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',16,'bold'),command=lambda:chkbutton_value(VarIcedCappuccino,txtIcedCappuccino,E_IcedCappuccino)).grid(row= 7, sticky=W)


#=======================Enter Widgets for Drink=======================
"""txtLattae = Entry(fMLTa,font=('TH Sarabun New',18,'bold'),bd=8,width=6,justify='left',state = NORMAL)
txtLattae.grid(row=0,column =1)"""
txtLattae = Entry(fCoffee,font=('TH Sarabun New',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Lattae,state = DISABLED)
txtLattae.grid(row=0,column =1)
txtEspresso = Entry(fCoffee,font=('TH Sarabun New',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Espresso,state = DISABLED)
txtEspresso.grid(row=1,column =1)
txtIceLattae = Entry(fCoffee,font=('TH Sarabun New',16,'bold'),bd=8,width=6,justify='left',textvariable=E_IceLattae,state = DISABLED)
txtIceLattae.grid(row=2,column =1)
txtValeCoffee = Entry(fCoffee,font=('TH Sarabun New',16,'bold'),bd=8,width=6,justify='left',textvariable=E_ValeCoffee,state = DISABLED)
txtValeCoffee.grid(row=3,column =1)
txtCappuccino = Entry(fCoffee,font=('TH Sarabun New',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Cappuccino,state = DISABLED)
txtCappuccino.grid(row=4,column =1)
txtAfricanCoffee = Entry(fCoffee,font=('TH Sarabun New',16,'bold'),bd=8,width=6,justify='left',textvariable=E_AfricanCoffee,state = DISABLED)
txtAfricanCoffee.grid(row=5,column =1)
txtAmericanCoffee = Entry(fCoffee,font=('TH Sarabun New',16,'bold'),bd=8,width=6,justify='left',textvariable=E_AmericanCoffee,state = DISABLED)
txtAmericanCoffee.grid(row=6,column =1)
txtIcedCappuccino = Entry(fCoffee,font=('TH Sarabun New',16,'bold'),bd=8,width=6,justify='left',textvariable=E_IcedCappuccino,state = DISABLED)
txtIcedCappuccino.grid(row=7,column =1)

#====================================== Cake ====================================

"""CoffeeCake = Checkbutton(fCake, text="Coffee Cake \t",variable = var9,onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',18,'bold')).grid(row= 0, column=0)"""
Cake0 = Checkbutton(fCake, text=file_read[0],variable = VarCakeList[0] ,onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',16,'bold'),command=lambda:chkbutton_value(VarCakeList[0],txtCake0,EntryCakeList[0])).grid(row= 0, sticky=W)
Cake1 = Checkbutton(fCake, text=file_read[1],variable = VarCakeList[1],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',16,'bold'),command=lambda:chkbutton_value(VarCakeList[1],txtCake1,EntryCakeList[1])).grid(row= 1, sticky=W)

Cake2 = Checkbutton(fCake, text=file_read[2],variable = VarCakeList[2],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',16,'bold'),command=lambda:chkbutton_value(VarCakeList[2],txtCake2,EntryCakeList[2])).grid(row= 2, sticky=W)

Cake3 = Checkbutton(fCake, text=file_read[3],variable = VarCakeList[3],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',16,'bold'),command=lambda:chkbutton_value(VarCakeList[3],txtCake3,EntryCakeList[3])).grid(row= 3, sticky=W)

Cake4 = Checkbutton(fCake, text=file_read[4],variable = VarCakeList[4],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',16,'bold'),command=lambda:chkbutton_value(VarCakeList[4],txtCake4,EntryCakeList[4])).grid(row= 4, sticky=W)

Cake5 = Checkbutton(fCake, text=file_read[5],variable = VarCakeList[5],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',16,'bold'),command=lambda:chkbutton_value(VarCakeList[5],txtCake5,EntryCakeList[5])).grid(row= 5, sticky=W)

Cake6 = Checkbutton(fCake, text=file_read[6],variable = VarCakeList[6],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',16,'bold'),command=lambda:chkbutton_value(VarCakeList[6],txtCake6,EntryCakeList[6])).grid(row= 6, sticky=W)
Cake7 = Checkbutton(fCake, text=file_read[7],variable = VarCakeList[7],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',16,'bold'),command=lambda:chkbutton_value(VarCakeList[7],txtCake7,EntryCakeList[7])).grid(row= 7, sticky=W)

#=======================Enter Widgets for Cake =======================
    
txtCake0 = Entry(fCake,font=('TH Sarabun New',16,'bold'),bd=8,width=6,justify='left',textvariable=EntryCakeList[0],state = DISABLED)
txtCake0.grid(row=0,column =1)
txtCake1 = Entry(fCake,font=('TH Sarabun New',16,'bold'),bd=8,width=6,justify='left',textvariable=EntryCakeList[1],state = DISABLED)
txtCake1.grid(row=1,column =1)
txtCake2 = Entry(fCake,font=('TH Sarabun New',16,'bold'),bd=8,width=6,justify='left',textvariable=EntryCakeList[2],state = DISABLED)
txtCake2.grid(row=2,column =1)
txtCake3 = Entry(fCake,font=('TH Sarabun New',16,'bold'),bd=8,width=6,justify='left',textvariable=EntryCakeList[3],state = DISABLED)
txtCake3.grid(row=3,column =1)
txtCake4 = Entry(fCake,font=('TH Sarabun New',16,'bold'),bd=8,width=6,justify='left',textvariable=EntryCakeList[4],state = DISABLED)
txtCake4.grid(row=4,column =1)
txtCake5 = Entry(fCake,font=('TH Sarabun New',16,'bold'),bd=8,width=6,justify='left',textvariable=EntryCakeList[5],state = DISABLED)
txtCake5.grid(row=5,column =1)
txtCake6 = Entry(fCake,font=('TH Sarabun New',16,'bold'),bd=8,width=6,justify='left',textvariable=EntryCakeList[6],state = DISABLED)
txtCake6.grid(row=6,column =1)
txtCake7 = Entry(fCake,font=('TH Sarabun New',16,'bold'),bd=8,width=6,justify='left',textvariable=EntryCakeList[7],state = DISABLED)
txtCake7.grid(row=7,column =1)
#================================== Receipt Information ===================
lblReceipt = Label(fReceipt,font=('TH Sarabun New',12,'bold'), text="Receipt", bd=2,anchor='w')
lblReceipt.grid(row=0,column=0, sticky=W)
txtReceipt = Text(fReceipt,font=('TH Sarabun New',11,'bold'), bd=8,width=59,height=22,bg="white")
txtReceipt.grid(row=1,column=0)
#=================================== Cost Items Information============
lblCostofDrinks = Label(fCost1,font=('TH Sarabun New',16,'bold'),text="Cost of Drinks",bd=8)
lblCostofDrinks.grid(row=0,column=0,sticky=W)
txtCostofDrinks=Entry(fCost1,font=('TH Sarabun New',16,'bold'),bd=8,justify='left',
                      textvariable=CostofDrinks)
txtCostofDrinks.grid(row=0,column=1,sticky=W)

lblCostofCakes = Label(fCost1,font=('TH Sarabun New',16,'bold'),text="Cost of Cakes",bd=8)
lblCostofCakes.grid(row=1,column=0,sticky=W)
txtCostofCakes=Entry(fCost1,font=('TH Sarabun New',16,'bold'),bd=8,justify='left',
                     textvariable=CostofCakes)
txtCostofCakes.grid(row=1,column=1,sticky=W)

lblServiceCharge = Label(fCost1,font=('TH Sarabun New',16,'bold'),text="Service Charge",bd=8)
lblServiceCharge.grid(row=2,column=0,sticky=W)
txtServiceCharge=Entry(fCost1,font=('TH Sarabun New',16,'bold'),bd=8,justify='left',
                       textvariable=ServiceCharge)
txtServiceCharge.grid(row=2,column=1,sticky=W)

#=========================== Payment Information========================
lblPaidTax = Label(fCost2,font=('TH Sarabun New',16,'bold'),text="Paid Tax",bd=8)
lblPaidTax.grid(row=0,column=0,sticky=W)
txtPaidTax=Entry(fCost2,font=('TH Sarabun New',16,'bold'),bd=8,justify='left',
                 textvariable=PaidTax)
txtPaidTax.grid(row=0,column=1,sticky=W)

lblSubTotal = Label(fCost2,font=('TH Sarabun New',16,'bold'),text="Sub Total",bd=8)
lblSubTotal.grid(row=1,column=0,sticky=W)
txtSubTotal=Entry(fCost2,font=('TH Sarabun New',16,'bold'),bd=8,justify='left',
                  textvariable=SubTotal)
txtSubTotal.grid(row=1,column=1,sticky=W)

lblTotalCost = Label(fCost2,font=('TH Sarabun New',16,'bold'),text="Total",bd=8)
lblTotalCost.grid(row=2,column=0,sticky=W)
txtTotalCost=Entry(fCost2,font=('TH Sarabun New',16,'bold'),bd=8,justify='left',
                   textvariable=TotalCost)
txtTotalCost.grid(row=2,column=1,sticky=W)
#================================== Button =========================
btnTotal= Button(fButton,padx=16, fg="black",font=('TH Sarabun New',16,'bold'),width=5,
                text="Total",command=CostofItem).grid(row=0, column=0)
btnReceipt=Button(fButton,padx=16, fg="black",font=('TH Sarabun New',16,'bold'),width=5,
                text="Receipt",command=Receipt).grid(row=0, column=1)
btnReset=Button(fButton,padx=16, fg="black",font=('TH Sarabun New',16,'bold'),width=5,
                text="Reset",command=Reset).grid(row=0, column=2)
btnExit=Button(fButton,padx=16, fg="black",font=('TH Sarabun New',16,'bold'),width=5,
                text="Exit",command=qExit).grid(row=0, column=3)

root.mainloop()
