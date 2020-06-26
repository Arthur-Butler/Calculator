from tkinter import*
CalGUI=Tk()
CalGUI.geometry("400x250") 
sum=''
def Addition(sum):
    sum=sum+'+'
def Subtraction(sum):
    sum=sum+'-'
def Multiplication(sum):
    sum=sum+'*'
def Division(sum):
    sum=sum+'/'
def One(sum):
    sum=sum+'1'
def Two(sum):
    sum=sum+'2'
def Three(sum):
    sum=sum+'3'
def Four(sum):
    sum=sum+'4'
def Five(sum):
    sum=sum+'5'
def Six(sum):
    sum=sum+'6'
def Seven(sum):
    sum=sum+'7'
def Eight(sum):
    sum=sum+'8'
def Nine(sum):
    sum=sum+'9'
def Zero(sum):
    sum=sum+'0'
Plus_Btn=Button(text="+",command=Addition(sum),width=5,height=2).place(x=10,y=40)
Minus_Btn=Button(text="-",command=Subtraction(sum),width=5,height=2).place(x=80,y=40)
Times_Btn=Button(text="x",command=Multiplication(sum),width=5,height=2).place(x=160,y=40)
Divede_Btn=Button(text="/",command=Division(sum),width=5,height=2).place(x=240,y=40)
One_Btn=Button(text="1",command=One(sum),width=5,height=2).place(x=10,y=80)
Two_Btn=Button(text="2",command=Two(sum),width=5,height=2).place(x=80,y=80)
Three_Btn=Button(text="3",command=Three(sum),width=5,height=2).place(x=160,y=80)
Four_Btn=Button(text="4",command=Four(sum),width=5,height=2).place(x=240,y=80)
Five_Btn=Button(text="5",command=Five(sum),width=5,height=2).place(x=10,y=120)
Six_Btn=Button(text="6",command=Six(sum),width=5,height=2).place(x=80,y=120)
Seven_Btn=Button(text="7",command=Seven(sum),width=5,height=2).place(x=160,y=120)
Eight_Btn=Button(text="8",command=Eight(sum),width=5,height=2).place(x=240,y=120)
Nine_Btn=Button(text="9",command=Nine(sum),width=5,height=2).place(x=80,y=160)
Zero_Btn=Button(text="0",command=Zero(sum),width=5,height=2).place(x=160,y=160)
def Equals(sum):
    for i in len(sum):
        if sum[i]=="+":
            num=sum[i]
Equal_Btn=Button(text="=",command=Equals,width=4,height=5).place(x=350,y=40)
Cal_lbl=Label(text=(sum),width=40,height=2,bg="blue").place(x=5,y=10)
CalGUI.mainloop()
