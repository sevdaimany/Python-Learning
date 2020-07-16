from tkinter import *

#============================================================== settings ===========================================================
root = Tk()
root.geometry('400x200')
root.resizable(width = False , height = False)
root.title('calculator')
color = 'mediumpurple'
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

#========================================================== buttons ============================================================================
btn_plus = Button(top_third , text = '+' , width = 10 , bg = 'paleturquoise')
btn_plus.pack(side= LEFT , padx = 5 ,pady = 5)

btn_minus = Button(top_third , text = '-' , width = 10 , bg = 'paleturquoise')
btn_minus.pack(side= LEFT , padx = 5 ,pady = 5)

btn_mul = Button(top_third , text = '*' , width = 10 , bg = 'paleturquoise')
btn_mul.pack(side= LEFT , padx = 5 ,pady = 5)

btn_div = Button(top_third , text = '/' , width = 10 , bg = 'paleturquoise')
btn_div.pack(side= LEFT , padx = 5 ,pady = 5)

#========================================================== Entries and Labels ========================================================================
label_first_num = Label(top_first, text = 'Input Number1:' , bg  ='lightgray')
label_first_num.pack(side=LEFT, pady=10, padx=10)

first_num = Entry(top_first)
first_num.pack(side = LEFT)

label_second_num = Label(top_second, text = 'Input Number2:' , bg  ='lightgray')
label_second_num.pack(side=LEFT, pady=10, padx=10)

second_num = Entry(top_second)
second_num.pack(side=LEFT)


result = Label(top_forth, text = 'Result: ' , bg  ='lightgray',  width = 10)
result.pack(side=LEFT, pady=10, padx=10)

res_num =Label(top_forth, bg  ='white'  , width = 10)
res_num.pack(side=LEFT)



root.mainloop()