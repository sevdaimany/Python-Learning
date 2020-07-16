from tkinter import *

import calendar

root = Tk()

root.configure(bg='gray')
root.geometry('700x600')
root.resizable(width = False , height = False)

root.title('sevdas calendar :)))))))))')

mycal =calendar.calendar(2020)

cal_year =Label(root,text = mycal ,font ='consolas 10 bold',fg = 'pink',bg ='gray')
cal_year.pack()

root.mainloop()