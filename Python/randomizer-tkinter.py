# a simple randomizer with gui using tkinter
separator = ';'

from random import randint
import tkinter as tk

# build window
win = tk.Tk()
win.title('Randomizer')
win.geometry('600x200')
win.configure(bg='#00CC8B')

# create text
txt = tk.Label(win,text='Welcome!',font=('Ink Free',25,'bold'),bg='#00CC8B',fg='white')
txt.pack()
inf = tk.Label(win,text='Please type anything you want seperated by semicolon\nExample:"Apple;Banana;Cherries"',font=('Ink Free',15,'bold'),bg='#00CC8B',fg='white')
inf.pack()


# show random
def create():
  try:
      inptxt = str(inp.get())
      lst = inptxt.split(separator) 
      zufallnr = randint(0,(len(lst))-1)
      txt['text'] = (lst[zufallnr])
  except:
      txt['text'] = 'ERROR'


# create input field and button
inp = tk.Entry(win,font=('Ink Free',15,'bold'),bg='#00CC8B',fg='white')
inp.pack()
go = tk.Button(win,text='Go',font=('Ink Free',15,'bold'),bg='#00CC8B',fg='white',command=create)
go.pack()


win.mainloop()
