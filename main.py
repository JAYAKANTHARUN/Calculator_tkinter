from tkinter import *#import tkinter

root=Tk()

root.title("CALCULATOR")
image=PhotoImage(file="calc.png")
root.iconphoto(False, image)

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

root.mainloop()