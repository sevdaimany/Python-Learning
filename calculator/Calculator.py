from tkinter import *
import tkinter.messagebox


#============================================================== settings ===========================================================
root = Tk()
root.geometry('400x200')
root.resizable(width = False , height = False)
root.title('calculator')
# color = 'mediumpurple'
color = 'pink'
root.configure(bg = color)
#============================================================= frames ================================================================
top_first = Frame(root, width = 400 ,height = 50 , bg = color)
top_first.pack(side = TOP)

top_second = Frame(root, width = 400 ,height = 50 , bg = color)
top_second.pack(side = TOP)

top_third = Frame(root, width = 400 ,height = 50 , bg = color)
top_third.pack(side = TOP)

top_forth = Frame(root, width = 400 ,height = 50 , bg = color)
top_forth.pack(side = TOP)

#=================================================== variabels ======================================================================================
num1 = StringVar()
num2 =StringVar()
answer =StringVar()


#========================================================== buttons ============================================================================
# color ='paleturquoise'
color ='aliceblue'
btn_plus = Button(top_third , text = '+' , width = 10 , bg = color, command = lambda: operation('+'))
btn_plus.pack(side= LEFT , padx = 5 ,pady = 5)

btn_minus = Button(top_third , text = '-' , width = 10 , bg = color, command = lambda: operation('-'))
btn_minus.pack(side= LEFT , padx = 5 ,pady = 5)

btn_mul = Button(top_third , text = '*' , width = 10 , bg = color ,  command = lambda: operation('*'))
btn_mul.pack(side= LEFT , padx = 5 ,pady = 5)

btn_div = Button(top_third , text = '/' , width = 10 , bg = color , command = lambda: operation('/'))
btn_div.pack(side= LEFT , padx = 5 ,pady = 5)

#========================================================== Entries and Labels ========================================================================
label_first_num = Label(top_first, text = 'Input Number1:' , bg  ='lightgray')
label_first_num.pack(side=LEFT, pady=10, padx=10)

first_num = Entry(top_first,textvariable=num1)
first_num.pack(side = LEFT)

label_second_num = Label(top_second, text = 'Input Number2:' , bg  ='lightgray')
label_second_num.pack(side=LEFT, pady=10, padx=10)

second_num = Entry(top_second,textvariable=num2)
second_num.pack(side=LEFT)


result = Label(top_forth, text = 'Result: ' , bg  ='lightgray',  width = 10)
result.pack(side=LEFT, pady=10, padx=10)

res_num =Label(top_forth, bg  ='white'  , width = 10 , textvariable = answer)
res_num.pack(side=LEFT)



# ================================================== functions =======================================================================================

def operation(inputOperation):
    try:
    
        if inputOperation == '+':
             answer.set(float(num1.get()) + float(num2.get()))

        elif inputOperation == '-':
            answer.set(float(num1.get()) - float(num2.get()))

        elif inputOperation == '*':
             answer.set(float(num1.get())  * float(num2.get()))
            
    except:
        msgError('error')

    if inputOperation == '/':
        if float(num2.get()) == 0:
            msgError('division zero error')
        else: 
            try:
                answer.set(float(num1.get()) / float(num2.get()))
            except :
                msgError('error')


def msgError(msg):
    if msg == 'error':
        tkinter.messagebox.showerror('Error','something went wrong')
    elif msg == 'division zero error' :
        tkinter.messagebox.showerror('Division Error', 'Can Not Divide By 0')

           

root.mainloop()