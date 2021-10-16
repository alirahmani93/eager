from tkinter import *
win = Tk()
win.title('my first Graphic User Interface')
lb1 = Label(win,text = 'hello GUI')
lb1.config(background='red',foreground='yellow')
bt1 =Button(win)
ax=PhotoImage()

c1 = Canvas(win,width=300 , height =150)
c1.create_line(10,20,230,120,fill='red')
c1.pack

lb1.pack
bt1.pack

