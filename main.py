from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

user_data = {}

def register_user():
    if new_username_entry.get() == '' or new_password_entry.get() == '':
        messagebox.showerror('Error', 'Fields cannot be empty')
    else:
        user_data[new_username_entry.get()] = new_password_entry.get()
        messagebox.showinfo('Success', 'User registered successfully!')
        register_window.destroy()

def open_register_window():
    global register_window, new_username_entry, new_password_entry
    register_window = Toplevel(window)
    register_window.title('Register')
    register_window.geometry('400x300')
    
    Label(register_window, text='Register', font=('times new roman', 20, 'bold')).pack(pady=20)
    
    Label(register_window, text='Username', font=('times new roman', 14)).pack(pady=5)
    new_username_entry = Entry(register_window, font=('times new roman', 14))
    new_username_entry.pack(pady=5)
    
    Label(register_window, text='Password', font=('times new roman', 14)).pack(pady=5)
    new_password_entry = Entry(register_window, font=('times new roman', 14), show='*')
    new_password_entry.pack(pady=5)
    
    Button(register_window, text='Register', font=('times new roman', 14), command=register_user).pack(pady=20)

def login():
    if username_entry.get() == '' or password_entry.get() == '':
        messagebox.showerror('Error', 'Fields cannot be empty')
    elif username_entry.get() in user_data and user_data[username_entry.get()] == password_entry.get():
        messagebox.showinfo('Success', 'Welcome')
        window.destroy()
        import sms  
    else:
        messagebox.showerror('Error', 'Please enter correct credentials')

window = Tk()

window.geometry('1280x700+0+0')
window.title('Login')

window.resizable(False, False)

background_image = ImageTk.PhotoImage(file="MediCareHUB/assets/bg1img.png")
bg_label = Label(window, image=background_image)
bg_label.place(x=0, y=0)

login_frame = Frame(window, bg='white smoke', pady=10)
login_frame.place(x=400, y=150)

logo_image = PhotoImage(file='MediCareHUB/assets/img_1.png')
logo_label = Label(login_frame, image=logo_image)
logo_label.grid(row=0, column=0, columnspan=2)

username_image = PhotoImage(file='MediCareHUB/assets/img_2.png')
username_label = Label(login_frame, image=username_image, text='Username', compound=LEFT, font=('times new roman', 20, 'bold'), bg='white')
username_label.grid(row=1, column=0, pady=10, padx=20)
username_entry = Entry(login_frame, font=('times new roman', 20, 'bold'), bd=5, fg='royalblue')
username_entry.grid(row=1, column=1, pady=10, padx=20)

password_image = PhotoImage(file='MediCareHUB/assets/img.png')
password_label = Label(login_frame, image=password_image, text='Password', compound=LEFT, font=('times new roman', 20, 'bold'), bg='white')
password_label.grid(row=2, column=0, pady=10, padx=20)
password_entry = Entry(login_frame, font=('times new roman', 20, 'bold'), bd=5, fg='royalblue', show='*')
password_entry.grid(row=2, column=1, pady=10, padx=20)

login_button = Button(login_frame, text='Login', font=('times new roman', 14, 'bold'), width=15, fg='white', bg='cornflowerblue', activebackground='white', cursor='hand2', command=login)
login_button.grid(row=3, column=1, pady=10)

register_button = Button(login_frame, text='Register', font=('times new roman', 14, 'bold'), width=15, fg='white', bg='green', activebackground='white', cursor='hand2', command=open_register_window)
register_button.grid(row=3, column=0, pady=10)

window.mainloop()
