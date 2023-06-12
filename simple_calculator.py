from tkinter import*

root=Tk()
root.title("simple calculator")

input=Entry(root,width=35,bd=5)
input.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

# clicking on numbers and operators
def button_click(number):
    current=input.get()
    input.delete(0,END)
    input.insert(0,str(current)+str(number))


# button =
def button_equal():
    try:
        result = eval(input.get())
        input.delete(0, END)
        input.insert(0, str(result))
    except Exception as e:
        input.delete(0,END)
        input.insert(0, "Error")

#button clear

def clear():
    input.delete(0,END)
    

#defining  number buttons

button1=Button(root,text="1",padx=33,pady=15,command=lambda: button_click(1))
button2=Button(root,text="2",padx=33,pady=15,command=lambda: button_click(2))
button3=Button(root,text="3",padx=33,pady=15,command=lambda: button_click(3))
button4=Button(root,text="4",padx=33,pady=15,command=lambda: button_click(4))
button5=Button(root,text="5",padx=33,pady=15,command=lambda: button_click(5))
button6=Button(root,text="6",padx=33,pady=15,command=lambda: button_click(6))
button7=Button(root,text="7",padx=33,pady=15,command=lambda: button_click(7))
button8=Button(root,text="8",padx=33,pady=15,command=lambda: button_click(8))
button9=Button(root,text="9",padx=33,pady=15,command=lambda: button_click(9))
button0=Button(root,text="0",padx=33,pady=15,command=lambda: button_click(0))

#defining symbol buttons
button_add=Button(root,text="+",padx=33,pady=15,command=lambda:button_click("+"))
button_sub=Button(root,text="-",padx=33,pady=15,command=lambda:button_click("-"))
button_mul=Button(root,text="*",padx=33,pady=15,command=lambda:button_click("*"))
button_div=Button(root,text="/",padx=34,pady=15,command=lambda:button_click("/"))
button_eql=Button(root,text="=",width=33,bd=5,command=button_equal)
button_clear=Button(root,text="Clear",padx=23,pady=15,command=clear)

# arranging buttons into window
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)
button_add.grid(row=4,column=1)
button_sub.grid(row=4,column=2)

button_clear.grid(row=5,column=0)
button_div.grid(row=5,column=1)
button_mul.grid(row=5,column=2)

button_eql.grid(row=6,column=0,columnspan=3)

root.mainloop()