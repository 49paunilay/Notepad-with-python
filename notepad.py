from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
import webbrowser
root=Tk()
root.title("Notepad")
root.iconbitmap("")
root.geometry("600x400")

def callback(url):
    webbrowser.open_new(url)
link1 = Label(root, text="Get Code", fg="blue", cursor="hand2")
link1.pack(side=BOTTOM,fill=X)
link1.bind("<Button-1>", lambda e: callback("https://github.com/49paunilay/Music-player-With-python"))
def quitApp():
    root.destroy()
def openfile():
    global filename
    filename=askopenfilename(defaultextension='.txt',filetypes=[('All Files','*.*'),('Text Documents','*.txt')])
    if filename=="":
        filename=None
    else:
        root.title(os.path.basename(filename))
        textholder.delete(1.0,END)
        f=open(filename,'r')
        textholder.insert(1.0,f.read())
        f.close()

    print('openfile button clicked')
def savefile():
    global filename
    if filename==None:
        filename=asksaveasfilename(initialfile='Untitled',defaultextension='.txt',filetypes=[('All Files','*.*'),('Text Documents','*.txt')])
        print('Save file is clicked')
        if filename=="":
            filename=None
        else:
            f=open(filename,'w')
            f.write(textholder.get(1.0,END))
            f.close()
            root.title(os.path.basename(filename))
            print('Saved')
    else:
        f=open(filename,'w')
        f.write(textholder.get(1.0,END))
        f.close()


def cut():
    textholder.event_generate(("<<Cut>>"))
def Copy():
    textholder.event_generate(("<<Copy>>"))
def paste():
    textholder.event_generate(("<<Paste>>"))
def about():
    messagebox.showinfo('About','A Normal text editor')
def newfile():
    global filename
    root.title('Untitiled Note')
    filename=None
    textholder.delete(1.0,END)

#Menubar
mymenubar=Menu(root)
firstmenu=Menu(mymenubar,tearoff=0,bg="yellow")
firstmenu.add_command(label='New',command=newfile)
firstmenu.add_command(label='Open',command=openfile)
firstmenu.add_command(label='Save',command=savefile)
firstmenu.add_command(label='Quit',command=quitApp)
mymenubar.add_cascade(label='File',menu=firstmenu)
editmenu=Menu(mymenubar,tearoff=0)
editmenu.add_command(label='Copy',command=Copy)
editmenu.add_command(label='CUT',command=cut)
editmenu.add_command(label='Paste',command=paste)
mymenubar.add_cascade(label='Edit',menu=editmenu)
helpmenu=Menu(mymenubar,tearoff=0)
helpmenu.add_command(label='Know your text editor',command=about)
mymenubar.add_cascade(label='About',menu=helpmenu)
root.config(menu=mymenubar)
#Textholder
textholder=Text(root,font='lucida 13')
filename=None
textholder.pack(expand=True,fill=BOTH)
#Scroolbar
scrool=Scrollbar(textholder)
scrool.pack(side=RIGHT,fill=Y)
scrool.config(command=textholder.yview)
textholder.config(yscrollcommand=scrool.set)
root.mainloop()