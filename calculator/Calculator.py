from tkinter import *

#============================================================== settings ===========================================================
root = Tk()
root.geometry('400x200')
root.resizable(width = False , height = False)
root.title('calculator')
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

#========================================================== buttons ============================================================================
btn_plus = Button(top_third , text = '+' , width = 10 , bg = 'light blue')
btn_plus.pack(side= LEFT , padx = 5 ,pady = 5)

btn_minus = Button(top_third , text = '-' , width = 10 , bg = 'light blue')
btn_minus.pack(side= LEFT , padx = 5 ,pady = 5)

btn_mul = Button(top_third , text = '*' , width = 10 , bg = 'light blue')
btn_mul.pack(side= LEFT , padx = 5 ,pady = 5)

btn_div = Button(top_third , text = '/' , width = 10 , bg = 'light blue')
btn_div.pack(side= LEFT , padx = 5 ,pady = 5)
root.mainloop()