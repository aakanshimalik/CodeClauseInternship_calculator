import tkinter as t
calculation=''

def add(symbol):
    global calculation
    calculation +=str(symbol)
    text_result.delete(1.0 ,"end")
    text_result.insert(1.0,calculation)

def evaluation():
    global calculation
    print(calculation)
    try:
        
        result=str(eval(calculation))
        calculation=''
        text_result.delete(1.0,"end")
        text_result.insert(1.0,result)
    except:
        clear_field()
        text_result.insert(1.0,"Error")

def clear_field():
    global calculation
    calculation=''
    text_result.delete(1.0,"end")

root=t.Tk()
root.geometry("310x275")

text_result=t.Text(root, height=2 , width=16 ,font=("Arial",24))
text_result.grid(columnspan=5)
btn1=t.Button(root,text="1",command=lambda:add(1),width=5,font=('Arial',14))
btn1.grid(row=2,column=1)
btn_2=t.Button(root,text="2",command=lambda:add(2),width=5,font=('Arial',14))
btn_2.grid(row=2,column=2)
btn3=t.Button(root,text="3",command=lambda:add(3),width=5,font=('Arial',14))
btn3.grid(row=2,column=3)
btn4=t.Button(root,text="4",command=lambda:add(4),width=5,font=('Arial',14))
btn4.grid(row=3,column=1)
btn5=t.Button(root,text="5",command=lambda:add(5),width=5,font=('Arial',14))
btn5.grid(row=3,column=2)
btn6=t.Button(root,text="6",command=lambda:add(6),width=5,font=('Arial',14))
btn6.grid(row=3,column=3)
btn7=t.Button(root,text="7",command=lambda:add(7),width=5,font=('Arial',14))
btn7.grid(row=4,column=1)
btn8=t.Button(root,text="8",command=lambda:add(8),width=5,font=('Arial',14))
btn8.grid(row=4,column=2)
btn9=t.Button(root,text="9",command=lambda:add(9),width=5,font=('Arial',14))
btn9.grid(row=4,column=3)
btn0=t.Button(root,text="0",command=lambda:add(0),width=5,font=('Arial',14))
btn0.grid(row=5,column=2)
btn_modulo=t.Button(root,text="%",command=lambda:add("%"),width=5,font=('Arial',14))
btn_modulo.grid(row=6,column=1)
btn_dot=t.Button(root,text=".",command=lambda:add("."),width=5,font=('Arial',14))
btn_dot.grid(row=6,column=2)
btn_plus=t.Button(root,text="+",command=lambda:add("+"),width=5,font=('Arial',14))
btn_plus.grid(row=2,column=4)
btn_minus=t.Button(root,text="-",command=lambda:add("-"),width=5,font=('Arial',14))
btn_minus.grid(row=3,column=4)
btn_multiplication=t.Button(root,text="*",command=lambda:add("*"),width=5,font=('Arial',14))
btn_multiplication.grid(row=4,column=4)
btn_division=t.Button(root,text="/",command=lambda:add("/"),width=5,font=('Arial',14))
btn_division.grid(row=5,column=4)
btn_open=t.Button(root,text="(",command=lambda:add("("),width=5,font=('Arial',14))
btn_open.grid(row=5,column=1)
btn_close=t.Button(root,text=")",command=lambda:add(")"),width=5,font=('Arial',14))
btn_close.grid(row=5,column=3)
btn_clear=t.Button(root,text="C",command=clear_field,width=5,font=('Arial',14))
btn_clear.grid(row=6,column=3)
btn_equal=t.Button(root,text="=",command=evaluation,width=5,font=('Arial',14))
btn_equal.grid(row=6,column=4,columnspan=3)

root.mainloop()