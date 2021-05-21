import tkinter as tk
from tkinter import *
import webbrowser

pw = ''
sicherheit = 0

def info():
    webbrowser.open('http://github.com/nsde/pwc')

def info2():
    webbrowser.open('https://hilfe.aol.de/articles/tipps-fur-starke-passworter')


fenster = tk.Tk()
fenster.geometry('430x400')
fenster.configure(bg='#0054C2')
fenster.title('Passwort Checker 3.0 Ultra')
fenster.iconphoto(False, tk.PhotoImage(file='C:/Styx/PasswortChecker/assets/pictures/icon.png'))

fenster.minsize(220,200)
fenster.maxsize(880,800)

text = tk.Label(fenster,text='',fg='red',bg='#0054C2',font=('arial', 15))
text.pack()


def ush():
    pw = eingabe.get()
    sonderzeichen = 0
    mittelsicher = 0
    zahl = 0
    sonderzeichen = 0
    sonderzeichen += pw.count('^')
    sonderzeichen += pw.count('°')
    sonderzeichen += pw.count('!')
    sonderzeichen += pw.count('"')
    sonderzeichen += pw.count('§')
    sonderzeichen += pw.count('$')
    sonderzeichen += pw.count('%')
    sonderzeichen += pw.count('&')
    sonderzeichen += pw.count('/')
    sonderzeichen += pw.count('{')
    sonderzeichen += pw.count('(')
    sonderzeichen += pw.count('[')
    sonderzeichen += pw.count(')')
    sonderzeichen += pw.count(']')
    sonderzeichen += pw.count('=')
    sonderzeichen += pw.count('}')
    sonderzeichen += pw.count('?')
    sonderzeichen += pw.count('\u005C')
    sonderzeichen += pw.count('ß')
    sonderzeichen += pw.count('`')
    sonderzeichen += pw.count('´')
    sonderzeichen += pw.count('*')
    sonderzeichen += pw.count('+')
    sonderzeichen += pw.count('~')
    sonderzeichen += pw.count('\u0027')
    sonderzeichen += pw.count('#')
    sonderzeichen += pw.count('<')
    sonderzeichen += pw.count('>')
    sonderzeichen += pw.count('|')
    sonderzeichen += pw.count(';')
    sonderzeichen += pw.count(',')
    sonderzeichen += pw.count(':')
    sonderzeichen += pw.count('.')
    sonderzeichen += pw.count('_')
    sonderzeichen += pw.count('-')

    mittelsicher = 0
    mittelsicher += pw.count('x')
    mittelsicher += pw.count('q')
    mittelsicher += pw.count('X')
    mittelsicher += pw.count('Q')
    mittelsicher += pw.count('z')
    mittelsicher += pw.count('Z')
    mittelsicher += pw.count('v')
    mittelsicher += pw.count('V')
    mittelsicher += pw.count('c')
    mittelsicher += pw.count('C')
    mittelsicher += pw.count('y')
    mittelsicher += pw.count('Y')
    mittelsicher += pw.count('ü')
    mittelsicher += pw.count('Ü')
    mittelsicher += pw.count('Ö')
    mittelsicher += pw.count('ö')
    mittelsicher += pw.count('ä')
    mittelsicher += pw.count('Ä')

    zahl = 0
    zahl += pw.count('1')
    zahl += pw.count('2')
    zahl += pw.count('3')
    zahl += pw.count('4')
    zahl += pw.count('5')
    zahl += pw.count('6')
    zahl += pw.count('7')
    zahl += pw.count('8')
    zahl += pw.count('9')
    zahl += pw.count('0')
    sicherheit = len(pw) + (sonderzeichen * 2) + (mittelsicher * 1.5) + (zahl * 0.5)
    text = tk.Label(fenster, text='Ihre Sicherheits-Punktzahl: ' + str(sicherheit), fg='white', bg='#0054C2',font=('arial', 15))
    text.pack()

#BG: 'C:/Styx/PasswortChecker/assets/pictures/bg.png'

titel = tk.Label(fenster,text='Passwort Checker 3.0 Ultra \n',fg='white',bg='#0054C2', font=('Calibri Light', 25),anchor='sw')
titel.pack()

eingabe=tk.Entry(fenster,textvariable=pw,fg='white',bg='#003C8A',font=('arial', 17))
eingabe.pack()

ok = tk.Button(fenster,text='Ok', command=ush,fg='white',bg='#0054C2',font=('arial', 15, 'bold'))
ok.pack()

info = tk.Button(fenster,text='Hilfe und Info', command=info,fg='white',bg='#0054C2',font=('arial', 15))
info.pack()

info2 = tk.Button(fenster,text='Tipps für Sicherheit im Internet',command=info2,fg='white',bg='#0054C2',font=('arial', 10))
info2.pack()

exit = tk.Button(fenster,text='Beenden',command=fenster.destroy,fg='white',bg='#0054C2',font=('arial',10))
exit.pack()

disclaimer = tk.Label(fenster,text='Geben Sie niemals ihr echtes Passwort an! \n Erstellt von NeoStyxDE. Informationen auf github.com/nsde.',fg='white',bg='#0054C2',font=('arial', 7, 'italic'))
disclaimer.pack()

fenster.mainloop()
print('Programm wird ausgeführt...')
