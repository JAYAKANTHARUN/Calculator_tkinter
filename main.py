from tkinter import *#import tkinter

root=Tk()

root.title("CALCULATOR")
image=PhotoImage(file="calc.png")
root.iconphoto(False, image)

def clicknumber(number):
    #entry1.delete(0,END)
    present=entry1.get()
    entry1.delete(0,END)
    entry1.insert(0,str(present)+str(number))
    
def clickadd():
    global firstnumber,math
    math="add"
    firstnumber=entry1.get()
    entry1.delete(0,END)

def clicksub():
    global firstnumber,math
    math="sub"
    firstnumber=entry1.get()
    entry1.delete(0,END)

def clickmult():
    global firstnumber,math
    math="mult"
    firstnumber=entry1.get()
    entry1.delete(0,END)

def clickdiv():
    global firstnumber,math
    math="div"
    firstnumber=entry1.get()
    entry1.delete(0,END) 
    
def clickeq():
    secondnumber=entry1.get()
    entry1.delete(0,END)
    if math=="add":
        entry1.insert(0,int(firstnumber)+int(secondnumber))
    if math=="sub":
        entry1.insert(0,int(firstnumber)-int(secondnumber))
    if math=="mult":
        entry1.insert(0,int(firstnumber)*int(secondnumber))
    if math=="div":
        entry1.insert(0,int(firstnumber)/int(secondnumber))            
    
def clickclear():
    entry1.delete(0,END)

entry1=Entry(root,width=40)
entry1.grid(columnspan=3,padx=10,pady=10,row=0,column=0)

button1=Button(root,text="1",padx=50,pady=30,command=lambda : clicknumber(1))
button2=Button(root,text="2",padx=50,pady=30,command=lambda : clicknumber(2))
button3=Button(root,text="3",padx=50,pady=30,command=lambda : clicknumber(3))
button4=Button(root,text="4",padx=50,pady=30,command=lambda : clicknumber(4))
button5=Button(root,text="5",padx=50,pady=30,command=lambda : clicknumber(5))
button6=Button(root,text="6",padx=50,pady=30,command=lambda : clicknumber(6))
button7=Button(root,text="7",padx=50,pady=30,command=lambda : clicknumber(7))
button8=Button(root,text="8",padx=50,pady=30,command=lambda : clicknumber(8))
button9=Button(root,text="9",padx=50,pady=30,command=lambda : clicknumber(9))
button0=Button(root,text="0",padx=50,pady=30,command=lambda : clicknumber(0))
buttonadd=Button(root,text="+",padx=50,pady=30,command=clickadd)
buttonsub=Button(root,text="-",padx=50,pady=30,command=clicksub)
buttonmult=Button(root,text="x",padx=50,pady=30,command=clickmult)
buttondiv=Button(root,text="/",padx=50,pady=30,command=clickdiv)
buttoneq=Button(root,text="=",padx=50,pady=30,command=clickeq)
buttonclear=Button(root,text="CLEAR",padx=35,pady=30,command=clickclear)

button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
button0.grid(row=4,column=1)
buttonadd.grid(row=5,column=0)
buttonsub.grid(row=5,column=1)
buttonmult.grid(row=6,column=0)
buttondiv.grid(row=6,column=1)
buttoneq.grid(row=6,column=2)
buttonclear.grid(row=5,column=2)

root.mainloop()