from tkinter import *

def leftClickButton(event):
    x=(float(textboxweight.get())/(float(textboxheight.get())/100)**2)
    if x >= 30 :
        labelresult2.configure(text="อ้วนมาก",bg="red")
    elif 30>x>=25 :
        labelresult2.configure(text="อ้วน",bg="red")
    elif 25>x>=23 :
        labelresult2.configure(text="น้ำหนักเกิน",bg="orange")
    elif 23>x>=18.6 :
        labelresult2.configure(text="น้ำหนักปกติ",bg="green")
    elif 18.6>x :
        labelresult2.configure(text="ผอม",bg="yellow")
    labelresult.configure(text=f'{x:.1f}')
    
mainwindow = Tk()
labelheight= Label(mainwindow,text="ส่วนสูง (Cm): ")
labelheight.grid(row=0,column=0)
textboxheight=Entry(mainwindow,bg="pink")
textboxheight.grid(row=0,column=1)
labelweight= Label(mainwindow,text="น้ำหนัก (Kg): ")
labelweight.grid(row=1,column=0)
textboxweight=Entry(mainwindow,bg="pink")
textboxweight.grid(row=1,column=1)
calculatebottom=Button(mainwindow,text="คำนวน")
calculatebottom.bind('<Button-1>',leftClickButton)
calculatebottom.grid(row=2,column=0)
labelresult=Label(mainwindow,text="ผลลัพธ์")
labelresult.grid(row=2,column=1)
labelresult2=Label(mainwindow,text="ผลลัพธ์2")
labelresult2.grid(row=3,column=1)
mainwindow.mainloop()