import tkinter as tk
from tkinter import *
import webbrowser
import os

fenster = tk.Tk()
fenster.geometry('430x200')
fenster.configure(bg='#0054C2')
fenster.title('Background Task Killer')
fenster.iconphoto(False, tk.PhotoImage(file='C:/Styx/BTK/assets/pictures/icon.png'))

fenster.minsize(220,200)
fenster.maxsize(880,800)

titel = tk.Label(fenster,text='BTK 1.0',fg='white',bg='#0054C2', font=('Calibri Light', 25),anchor='sw')
titel.pack()

def all():
    fenster.title('PLEASE WAIT...')
    os.system("taskkill /f /im AnyDesk.exe")
    os.system("taskkill /f /im SearchUI.exe")
    os.system("taskkill /f /im Calculator.exe")
    os.system("taskkill /f /im Microsoft.Photos.exe")
    os.system("taskkill /f /im OfficeClickToRun.exe")
    os.system("taskkill /f /im SkypeBackgroundHost.exe")
    os.system("taskkill /f /im SkypeApp.exe")
    os.system("taskkill /f /im WinStore.App.exe")
    os.system("taskkill /f /im Music.UI.exe")
    os.system("taskkill /f /im MicrosoftEdge.exe")
    os.system("taskkill /f /im MicrosoftEdgeCP.exe")
    os.system("taskkill /f /im MicrosoftEdgeSH.exe")
    os.system("taskkill /f /im HxOutlook.exe")
    os.system("taskkill /f /im chrome.exe")
    os.system("taskkill /f /im Video.UI.exe")
    os.system("taskkill /f /im backgroundTaskHost.exe") # Office
    fenster.title('Background Task Killer')


ok = tk.Button(fenster,text='Kill all', command=all,fg='white',bg='#0054C2',font=('arial', 35, 'bold'))
ok.pack()

disclaimer = tk.Label(fenster,text='We assume no liability for OS problems. \n Only use carefully and if you have OS experience.',fg='#1A2E32',bg='#0054C2',font=('arial', 8, 'italic'))
disclaimer.pack()

fenster.mainloop()
