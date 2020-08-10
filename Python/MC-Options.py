# >>Change hidden minecraft settings and options!<<

import tkinter as tk
import sys, os, time

#--TK WINDOW STUFF--

win = tk.Tk()
win.geometry('500x600')
win.configure(bg='#0054C2')
win.title('MCOptions 1.0')
win.iconphoto(False, tk.PhotoImage(file='C:/Styx/MCOptions/assets/pictures/icon.png'))

win.minsize(220,200)
win.maxsize(1920,1080)

def restart():
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 

def closeapp():
    win.destroy()

def apply():
        
    try: # debugging stuff with current_process (see except)

#       Reading Process

        current_process = 'openfile-reading'
        ofile = open('C:\\Users\\rorosz\\AppData\\Roaming\\.minecraft\\options.txt')
        current_process = 'read lines'
        opts = ['this','is','a','test!']
        opts.clear()
        opts = ofile.readlines()

#       Check if user input is correct

        if str(unifont_ent.get()) == 'true' or str(unifont_ent.get()) == 'false' or str(unifont_ent.get()) == '':
            unifont_ent["bg"] = '#003C8A'
            pass
        else:
            info_txt["text"] = 'Couldn\'t save: Invalid user input.'
            info_txt["bg"] = 'red'
            unifont_ent["bg"] = 'red'
            return
        
        if fps_ent.get() != '':
            try:
                fps_test = int(fps_ent.get())
                fps_test += 1
                if fps_test > 1 and fps_test < 1001:
                    fps_ent["bg"] = '#003C8A'
                    pass
                else:
                    info_txt["text"] = 'Couldn\'t save: Invalid user input.'
                    info_txt["bg"] = 'red'
                    return
            except:
                info_txt["text"] = 'Couldn\'t save: Invalid user input.'
                info_txt["bg"] = 'red'
                return
        else:
            pass


        if str(ait_ent.get()) == 'true' or str(ait_ent.get()) == 'false' or str(ait_ent.get()) == '':
            ait_ent["bg"] = '#003C8A'
            pass
        else:
            info_txt["text"] = 'Couldn\'t save: Invalid user input.'
            info_txt["bg"] = 'red'
            ait_ent["bg"] = 'red'
            return

        ofile.close
        current_process = 'var config'

#       Input Config:

        unifont_inp = str(unifont_ent.get())
        fps_inp = str(fps_ent.get())
        ait_inp = str(ait_ent.get())

        current_process = 'opts line config'

#       Options Config:

        opts[8] = 'forceUnicodeFont:' + unifont_inp + '\n'
        opts[22] = 'maxFPS:' + fps_inp + '\n'
        opts[35] = 'advancedItemTooltips:' + ait_inp + '\n'

#       Writing Process

        current_process = 'openfile-writing'
        ofile = open('C:/Users/rorosz/AppData/Roaming/.minecraft/options.txt','w+')
        current_process = 'write lines'
        ofile.writelines(opts)
        ofile.close()

#       Finish info

        info_txt["text"] = 'Sucessfully saved.'
        info_txt["bg"] = 'green'

    except:
        info_txt["text"] = 'FILE ERROR. Last process: "' + current_process + '".'
        info_txt["bg"] = 'red'
        return

#GUI

    #MENUBAR

mBar = tk.Menu(win)

        #APP

mApp = tk.Menu(mBar,tearoff=0)
mApp.add_command(label='Restart',command=restart)
mApp.add_command(label='Close',command=closeapp)
mBar.add_cascade(label='Application',menu=mApp)
win["menu"] = mBar

    #STATUS AND SAVE-BUTTON

info_txt = tk.Label(win,fg='white',bg='#0048A6',text='Welcome to MCOptions!',font=('arial',18,"bold"),height=1,width=100)
info_txt.pack()

space_txt = tk.Label(win,fg='#0054C2',bg='#0054C2',text='\n',font=('arial',8),height=1,width=100)
space_txt.pack()

save_btn = tk.Button(win,text='Save',bd=0,command=apply,fg='white',bg='#003C8A',font=('arial', 15),width=10,height=1)
save_btn.pack()

space_txt2 = tk.Label(win,fg='#0054C2',bg='#0054C2',text='\n',font=('arial',8),height=1,width=100)
space_txt2.pack()

    #FORCE UNICODE FONT

unifont_txt = tk.Label(win,fg='white',bg='#0054C2',text='Unicode Font',font=('arial',15,'bold'))
unifont_txt.pack()

unifont_inf = tk.Label(win,fg='white',bg='#0054C2',text='Normal: false.\nUse the unicode font for languages like arabic or chinese.\nInput: true/false',font=('arial',10,'italic'))
unifont_inf.pack()

unifont_ent = tk.Entry(win,fg='white',bg='#003C8A',font=('arial',15),bd=0,width=5)
unifont_ent.pack()

unifont_inp = unifont_ent.get()

space_unf = tk.Label(win,fg='#0054C2',bg='#0054C2',text='\n',font=('arial',8),height=1,width=100)
space_unf.pack()

    #MAX FPS

fps_txt = tk.Label(win,fg='white',bg='#0054C2',text='Max FPS',font=('arial',15,'bold'))
fps_txt.pack()

fps_inf = tk.Label(win,fg='white',bg='#0054C2',text='Normal: 60.\nFrames per second. For good PCs, we recommend entering 144 or even 255.\nInput: number',font=('arial',10,'italic'))
fps_inf.pack()

fps_ent = tk.Entry(win,fg='white',bg='#003C8A',font=('arial',15),bd=0,width=4)
fps_ent.pack()

fps_inp = fps_ent.get()

space_fps = tk.Label(win,fg='#0054C2',bg='#0054C2',text='\n',font=('arial',8),height=1,width=100)
space_fps.pack()

    #ADVANCED ITEM TOOLTIPS

ait_txt = tk.Label(win,fg='white',bg='#0054C2',text='Better Tooltips',font=('arial',15,'bold'))
ait_txt.pack()

ait_inf = tk.Label(win,fg='white',bg='#0054C2',text='Normal: false.\nWill show advanced item tooltips in inventory.\nInput: true/false',font=('arial',10,'italic'))
ait_inf.pack()

ait_ent = tk.Entry(win,fg='white',bg='#003C8A',font=('arial',15),bd=0,width=5)
ait_ent.pack()

ait_inp = ait_ent.get()

space_ait = tk.Label(win,fg='#0054C2',bg='#0054C2',text='\n',font=('arial',8),height=1,width=100)
space_ait.pack()

    #MAINLOOP

win.mainloop()
