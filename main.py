from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
import tkinter.font as font


root=Tk()
root.title("Reservations system")
root.configure(background='#3d4b52',padx=9,pady=9)
#Style section>>
style=ttk.Style()
#('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
style.theme_use('vista')
style.configure('TLabel',background='#3d4b52',foreground='#DEB887',font=('Helvitica',12,'bold'))
style.configure('TRadiobutton',background='#3d4b52',foreground='#DEB887',font=('Helvitica',12,'bold'))

#here is a Full name section>>
#ttk.Label(root,text = "Full Name :",).grid(row=0,column=0,padx=10,pady=10)
EntryFullName=ttk.Entry(root,width=30,font=('Helvitica',16))


EntryFullName.grid(row=0,column=0,columnspan=2)

#ttk.Label(root,text='Gender :').grid(row=1,column=0)
SpanGender=StringVar()
ttk.Radiobutton(root,text='Male',variable=SpanGender,value='Male').grid(row=1,column=0)
ttk.Radiobutton(root,text='Female',variable=SpanGender,value='Female').grid(row=1,column=1)

#here is a Comment>>
#ttk.Label(root,text='Comment :',justify = CENTER).grid(row=2,column=0)
text=tkinter.Text(root  ,width=30,height=15,font=('Helvitica',16)).grid(row=2,column=0,columnspan=2)
#Finally buttons>>
Submitbutton=ttk.Button(root,text='Submit')
Submitbutton = font.Font()
Submitbutton = tkinter.Button(root,text="Submit",justify = CENTER, bg='#008080',fg='#DEB887',bd=0,font=('Helvitica',16))

Submitbutton.grid(row=3,column=1,sticky='snew',ipadx=20,ipady=12)
Listbutton=tkinter.Button(root,text='List Resrevation',bg='#008080',fg='#DEB887',bd=0,font=('Helvitica',16))
Listbutton.grid(row=3,column=0,sticky='snew',ipadx=20,ipady=12)



root.mainloop()