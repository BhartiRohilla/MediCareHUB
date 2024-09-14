from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

def login():
    if usernameentry.get()==''or passwordentry.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    elif usernameentry.get()=='Bharti' and passwordentry.get()=='1234':
        messagebox.showinfo('Success','Welcome')
        window.destroy()
        import sms

    else:
        messagebox.showerror('Error','please enter correct credentials')

window=Tk()

window.geometry('1280x700+0+0')
window.title('Login')

window.resizable(False,False)

backgroundImage=ImageTk.PhotoImage(file='bg1img.png')

bgLabel=Label(window,image=backgroundImage)
bgLabel.place(x=0,y=0)

loginframe=Frame(window,bg='white smoke',pady=10)
loginframe.place(x=400,y=150)

logoimage=PhotoImage(file='img_1.png')

logolabel=Label(loginframe,image=logoimage)
logolabel.grid(row=0,column=0,columnspan=2)
usernameimage=PhotoImage(file='img_2.png')
usernamelabel=Label(loginframe,image=usernameimage,text='Username',compound=LEFT
                    ,font=('times new roman',20,'bold'),bg='white')
usernamelabel.grid(row=1,column=0,pady=10,padx=20)
usernameentry=Entry(loginframe,font=('times new roman',20,'bold'),bd=5,fg='royalblue')
usernameentry.grid(row=1,column=1,pady=10,padx=20)

passwordimage=PhotoImage(file='img.png')
passwordlabel=Label(loginframe,image=passwordimage,text='Password',compound=LEFT
                    ,font=('times new roman',20,'bold'),bg='white')
passwordlabel.grid(row=2,column=0,pady=10,padx=20)

passwordentry=Entry(loginframe,font=('times new roman',20,'bold'),bd=5,fg='royalblue')
passwordentry.grid(row=2,column=1,pady=10,padx=20)

loginbutton=Button(loginframe,text='Login',font=('times new roman',14,'bold'),width=15
                   ,fg='white',bg='cornflowerblue'
                   ,activebackground='white',cursor='hand2',command=login)
loginbutton.grid(row=3,column=1,pady=10)
window.mainloop()
