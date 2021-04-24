from tkinter import *
window = Tk()
window.title('GitHub Desktop')
window.geometry('600x500')


lbl1 = Label(window, text='Sign in', font = ('Helvetica', 35),fg = 'Gray')
lbl1.grid(column = 0,row = 0)


txt = Entry(window, width = 50)
txt.grid(column = 0,row = 5)

lbl2 = Label(window, text='Login', font = ('Helvetica', 10),fg = 'Black')
lbl2.grid(column = 2,row = 5)


txt1 = Entry(window, width = 50)
txt1.grid(column = 0,row = 10)

lbl3 = Label(window, text='Password', font = ('Helvetica', 10),fg = 'Black')
lbl3.grid(column = 2,row = 10)

lbl0 = Label(window, text='')
lbl0.grid(column = 0,row = 100)


def clicked():
	if txt.get() == 'eremmev' and txt1.get() == 'ger302h01s212':
		lbl0.configure(text="Hello!", font = ('Helvetica', 20),fg = 'Gray')
		lbl0.grid(column = 0, row = 40)  
	else:
		lbl0.configure(text='Login or password is not correct', font = ('Helvetica', 15),fg = 'Red')
		lbl0.grid(column = 0, row = 80)


btn1 = Button(window, text = 'Дальше',fg = 'White', bg = 'Gray', command=clicked)
btn1.grid(column = 0, row = 18)

window.mainloop()