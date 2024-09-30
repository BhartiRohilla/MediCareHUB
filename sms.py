from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas

def exit():
    result=messagebox.askyesno('confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass

def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=patienttable.get_children()
    newlist=[]
    for index in indexing:
        content=patienttable.item(index)
        datalist=content['values']
        newlist.append(datalist)

    table=pandas.DataFrame(newlist,columns=['Patient_Id','Name','mobile','age','gender','attending dr. name','admitted date','admitted time'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Success','Data is saved successfuly')

def update_patient():
    def update_data():
        query = 'update patient set name=%s,mobile=%s,age=%s,gender=%s,Attending_Dr_Name=%s where Patient_Id=%s'
        mycursor.execute(query,(nameentry.get(), mobile_numberentry.get(), ageentry.get(), genderentry.get(),drnameentry.get(),Patient_Identry.get()))
        con.commit()
        messagebox.showinfo('Success', 'patient data is modified successfully',parent=update_window)
        update_window.destroy()
        show_patient()


    update_window = Toplevel()
    update_window.title('Update patient')
    update_window.resizable(False, False)
    update_window.grab_set()
    Patient_Idlabel = Label(update_window, text='Patient Id', font=('times new roman', 20, 'bold'))
    Patient_Idlabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    Patient_Identry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    Patient_Identry.grid(row=0, column=1, padx=15, pady=10)

    namelabel = Label(update_window, text='Name', font=('times new roman', 20, 'bold'))
    namelabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameentry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    nameentry.grid(row=1, column=1, padx=15, pady=10)

    mobile_numberlabel = Label(update_window, text='Mobile', font=('times new roman', 20, 'bold'))
    mobile_numberlabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    mobile_numberentry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    mobile_numberentry.grid(row=2, column=1, padx=15, pady=10)

    agelabel = Label(update_window, text='Age', font=('times new roman', 20, 'bold'))
    agelabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    ageentry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    ageentry.grid(row=3, column=1, padx=15, pady=10)

    genderlabel = Label(update_window, text='Gender', font=('times new roman', 20, 'bold'))
    genderlabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    genderentry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    genderentry.grid(row=4, column=1, padx=15, pady=10)

    drnamelabel = Label(update_window, text='Attending Dr. Name', font=('times new roman', 20, 'bold'))
    drnamelabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    drnameentry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    drnameentry.grid(row=5, column=1, padx=15, pady=10)

    update_patient_button = ttk.Button(update_window, text='UPDATE',command=update_data)
    update_patient_button.grid(row=6, columnspan=2, pady=15)

    indexing=patienttable.focus()
    content=patienttable.item(indexing)
    listdata=content['values']
    Patient_Identry.insert(0,listdata[0])
    nameentry.insert(0,listdata[1])
    mobile_numberentry.insert(0, listdata[2])
    ageentry.insert(0, listdata[3])
    genderentry.insert(0, listdata[4])
    drnameentry.insert(0, listdata[5])

def show_patient():
    query = 'select * from patient'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    patienttable.delete(*patienttable.get_children())
    for data in fetched_data:
        patienttable.insert('', END, values=data)

def delete_patient():
    indexing=patienttable.focus()
    print(indexing)
    content=patienttable.item(indexing)
    content_serial=content['values'][0]
    query='delete from patient where Patient_Id=%s'
    mycursor.execute(query,content_serial)
    con.commit()
    messagebox.showinfo('Deleted',f'Patient selected with Patient ID {content_serial} is deleted succesfully')
    query='select * from patient'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    patienttable.delete(*patienttable.get_children())
    for data in fetched_data:
        patienttable.insert('',END,values=data)

def search_patient():
    def search_data():
        query="""select * from patient where Patient_Id=%s or name=%s or mobile=%s or age=%s or gender=%s or Attending_Dr_Name=%s"""
        mycursor.execute(query,(Patient_Identry.get(),nameentry.get(),mobile_numberentry.get(),ageentry.get(),genderentry.get(),drnameentry.get()))
        patienttable.delete(*patienttable.get_children())
        fetched_data=mycursor.fetchall()
        for data in fetched_data:


            patienttable.insert('',END,values=data)


    search_window = Toplevel()
    search_window.title('Search patient')
    search_window.resizable(False, False)
    search_window.grab_set()
    Patient_Idlabel = Label(search_window, text='Patient Id', font=('times new roman', 20, 'bold'))
    Patient_Idlabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    Patient_Identry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    Patient_Identry.grid(row=0, column=1, padx=15, pady=10)

    namelabel = Label(search_window, text='Name', font=('times new roman', 20, 'bold'))
    namelabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameentry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    nameentry.grid(row=1, column=1, padx=15, pady=10)

    mobile_numberlabel = Label(search_window, text='Mobile', font=('times new roman', 20, 'bold'))
    mobile_numberlabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    mobile_numberentry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    mobile_numberentry.grid(row=2, column=1, padx=15, pady=10)

    agelabel = Label(search_window, text='Age', font=('times new roman', 20, 'bold'))
    agelabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    ageentry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    ageentry.grid(row=3, column=1, padx=15, pady=10)

    genderlabel = Label(search_window, text='Gender', font=('times new roman', 20, 'bold'))
    genderlabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    genderentry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    genderentry.grid(row=4, column=1, padx=15, pady=10)

    drnamelabel = Label(search_window, text='Attending Dr. Name', font=('times new roman', 20, 'bold'))
    drnamelabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    drnameentry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    drnameentry.grid(row=5, column=1, padx=15, pady=10)

    search_patient_button = ttk.Button(search_window, text='SEARCH PATIENT', command=search_data)
    search_patient_button.grid(row=6, columnspan=2, pady=15)

def add_patient():
    def add_data():
        global mycursor, con
        if Patient_Identry.get=='' or nameentry.get()=='' or mobile_numberentry.get()=='' or ageentry.get()=='' or genderentry.get()=='' or drnameentry.get()=='':
            messagebox.showerror('Error','All fields are required',parent=add_window)
        else:
            currentdate = time.strftime('%d/%m/%y')
            currenttime = time.strftime('%H:%M:%S')
            try:
                query = 'insert into patient values(%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query, (
                Patient_Identry.get(), nameentry.get(), mobile_numberentry.get(), ageentry.get(), genderentry.get(),
                drnameentry.get(),
                currentdate, currenttime))
                con.commit()
                result = messagebox.askyesno('Confirm', 'Data is added successfully.Do you want to clean the form?',
                                             parent=add_window)
                if result:
                    Patient_Identry.delete(0, END)
                    nameentry.delete(0, END)
                    mobile_numberentry.delete(0, END)
                    ageentry.delete(0, END)
                    genderentry.delete(0, END)
                    drnameentry.delete(0, END)
                else:
                    pass
            except:
                 messagebox.showerror('Error','Patient Id cannot be repeated.',parent=add_window)
                 return

            query='select *from patient'
            mycursor.execute(query)
            fetched_data = mycursor.fetchall()
            patienttable.delete(*patienttable.get_children())
            for data in fetched_data:
                datalist=list(data)
                patienttable.insert('',END,values=datalist)

    add_window=Toplevel()
    add_window.title('Add patient')
    add_window.resizable(False,False)
    add_window.grab_set()
    Patient_Idlabel=Label(add_window,text='Patient Id',font=('times new roman',20,'bold'))
    Patient_Idlabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    Patient_Identry=Entry(add_window,font=('roman',15,'bold'),width=24)
    Patient_Identry.grid(row=0,column=1,padx=15,pady=10)

    namelabel = Label(add_window, text='Name', font=('times new roman', 20, 'bold'))
    namelabel.grid(row=1, column=0, padx=30,pady=15,sticky=W)
    nameentry = Entry(add_window, font=('roman', 15, 'bold'),width=24)
    nameentry.grid(row=1, column=1,padx=15,pady=10)

    mobile_numberlabel = Label(add_window, text='Mobile', font=('times new roman', 20, 'bold'))
    mobile_numberlabel.grid(row=2, column=0, padx=30,pady=15,sticky=W)
    mobile_numberentry = Entry(add_window, font=('roman', 15, 'bold'),width=24)
    mobile_numberentry.grid(row=2, column=1,padx=15,pady=10)

    agelabel = Label(add_window, text='Age', font=('times new roman', 20, 'bold'))
    agelabel.grid(row=3, column=0, padx=30,pady=15,sticky=W)
    ageentry = Entry(add_window, font=('roman', 15, 'bold'),width=24)
    ageentry.grid(row=3, column=1,padx=15,pady=10)

    genderlabel = Label(add_window, text='Gender', font=('times new roman', 20, 'bold'))
    genderlabel.grid(row=4, column=0, padx=30, pady=15,sticky=W)
    genderentry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    genderentry.grid(row=4, column=1, padx=15, pady=10)

    drnamelabel = Label(add_window, text='Attending Dr. Name', font=('times new roman', 20, 'bold'))
    drnamelabel.grid(row=5, column=0, padx=30, pady=15,sticky=W)
    drnameentry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    drnameentry.grid(row=5, column=1, padx=15, pady=10)

    add_patient_button=ttk.Button(add_window,text='ADD PATIENT',command=add_data)
    add_patient_button.grid(row=6,columnspan=2,pady=15)


def connect_databse():
    def connect():
        global mycursor,con
        try:
            con=pymysql.connect(host=hostentry.get(),user=userentry.get(),password=Passwordentry.get())
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Invalid Details',parent=connectwindow)
            return
        try:
            query = 'create database hospitalmanagementsystem'
            mycursor.execute(query)
            query = 'use hospitalmanagementsystem'
            mycursor.execute(query)
            query = 'create table patient(Patient_Id int not null primary key,name varchar(30),mobile varchar(10),age int,' \
                    'gender varchar(30),Attending_Dr_Name varchar(20),admitted_date varchar(50),admitted_time varchar(50)) '
            mycursor.execute(query)
        except:
            query='use hospitalmanagementsystem'
            mycursor.execute(query)
        messagebox.showinfo('Success', 'Database connection is successful', parent=connectwindow)
        connectwindow.destroy()
        addpatientbutton.config(state=NORMAL)
        searchpatientbutton.config(state=NORMAL)
        updatepatientbutton.config(state=NORMAL)
        showpatientbutton.config(state=NORMAL)
        exportpatientbutton.config(state=NORMAL)
        deletepatientbutton.config(state=NORMAL)
        exitbutton.config(state=NORMAL)

    connectwindow=Toplevel()
    connectwindow.grab_set()
    connectwindow.geometry('470x250+730+230')
    connectwindow.title('Database Connection')
    connectwindow.resizable(0,0)

    hostnamelabel=Label(connectwindow,text='Host name',font=('arial',20,'bold'))
    hostnamelabel.grid(row=0,column=0,padx=20)

    hostentry=Entry(connectwindow,font=('roman',15,'bold'),bd=2)
    hostentry.grid(row=0,column=1,padx=40,pady=20)

    usernamelabel = Label(connectwindow, text='User name', font=('arial', 20, 'bold'))
    usernamelabel.grid(row=1, column=0, padx=20)

    userentry = Entry(connectwindow, font=('roman', 15, 'bold'), bd=2)
    userentry.grid(row=1, column=1, padx=40, pady=20)

    Passwordlabel = Label(connectwindow, text='Password', font=('arial', 20, 'bold'))
    Passwordlabel.grid(row=2, column=0, padx=20)

    Passwordentry = Entry(connectwindow, font=('roman', 15, 'bold'), bd=2)
    Passwordentry.grid(row=2, column=1, padx=40, pady=20)

    connectbutton=ttk.Button(connectwindow,text='Connect',command=connect)
    connectbutton.grid(row=3,columnspan=2)

count=0
text=''
def slider():
    global text,count
    if count==len(s):
        count=0
        text=''
    text=text+s[count]
    sliderlabel.config(text=text)
    count+=1
    sliderlabel.after(100,slider)

def clock():
    global date,currenttime
    date=time.strftime('%d/%m/%y')
    currenttime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'Date:{date}\nTime:{currenttime}')
    datetimeLabel.after(1000,clock)

#GUI part
root=ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('radiance')

root.geometry('1174x680+0+0')
root.resizable(0,0)
root.title('Hospital management system')
datetimeLabel=Label(root,font=('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()
s='HOSPITAL MANAGEMENT SYSTEM'#s[count]=S when count is 0
sliderlabel=Label(root,text=s,font=('arial',18,'italic bold'),width=30)
sliderlabel.place(x=200,y=0)
slider()

connectbutton=ttk.Button(root,text='connect To database',command=connect_databse)
connectbutton.place(x=990,y=0)

leftframe=Frame(root)
leftframe.place(x=50,y=80,width=300,height=600)

logo_image=PhotoImage(file='MediCareHUB/assets/img_3.png')
logo_label=Label(leftframe,image=logo_image)
logo_label.grid(row=0,column=0)

addpatientbutton=ttk.Button(leftframe,text='Add Patient',width=25,state=DISABLED,command=add_patient)
addpatientbutton.grid(row=1,column=0,pady=12)

searchpatientbutton=ttk.Button(leftframe,text='Search Patient',width=25,state=DISABLED,command=search_patient)
searchpatientbutton.grid(row=2,column=0,pady=10)

deletepatientbutton=ttk.Button(leftframe,text='Delete Patient',width=25,state=DISABLED,command=delete_patient)
deletepatientbutton.grid(row=3,column=0,pady=10)

updatepatientbutton=ttk.Button(leftframe,text='Update Patient',width=25,state=DISABLED,command=update_patient)
updatepatientbutton.grid(row=4,column=0,pady=10)

showpatientbutton=ttk.Button(leftframe,text='Show Patient',width=25,state=DISABLED,command=show_patient)
showpatientbutton.grid(row=5,column=0,pady=10)

exportpatientbutton=ttk.Button(leftframe,text='Export Data',width=25,state=DISABLED,command=export_data)
exportpatientbutton.grid(row=6,column=0,pady=10)

exitbutton=ttk.Button(leftframe,text='Exit',width=25,state=DISABLED,command=exit)
exitbutton.grid(row=7,column=0,pady=10)

rightframe=Frame(root)
rightframe.place(x=350,y=80,width=820,height=600)

scrollbarx=Scrollbar(rightframe,orient=HORIZONTAL)
scrollbary=Scrollbar(rightframe,orient=VERTICAL)

patienttable=ttk.Treeview(rightframe,columns=('Patient_Id','Name','Mobile Number','age','gender','Attending Dr. name',
                                 'Admitted date','Admitted time'),
                          xscrollcommand=scrollbarx.set,yscrollcommand=scrollbary.set)
scrollbarx.config(command=patienttable.xview)
scrollbary.config(command=patienttable.yview)
scrollbarx.pack(side=BOTTOM,fill=X)
scrollbary.pack(side=RIGHT,fill=Y)
patienttable.pack(fill=BOTH,expand=1)

patienttable.heading('Patient_Id',text='Patient_Id')
patienttable.heading('Name',text='Name')
patienttable.heading('Mobile Number',text='Mobile Number')
patienttable.heading('age',text='age')
patienttable.heading('gender',text='Gender')
patienttable.heading('Attending Dr. name',text='Attending Dr. name')
patienttable.heading('Admitted date',text='Admitted date')
patienttable.heading('Admitted time',text='Admitted time')

patienttable.column('Patient_Id',width=200,anchor=CENTER)
patienttable.column('Name',width=200,anchor=CENTER)
patienttable.column('Mobile Number',width=200,anchor=CENTER)
patienttable.column('age',width=70,anchor=CENTER)
patienttable.column('gender',width=150,anchor=CENTER)
patienttable.column('Attending Dr. name',width=300,anchor=CENTER)
patienttable.column('Admitted date',width=150,anchor=CENTER)
patienttable.column('Admitted time',width=150,anchor=CENTER)

style=ttk.Style()

style.configure('Treeview',rowheight=35,font=('times new roman',12,'bold'))
style.configure('Treeview.Heading',font=('times new roman',14,'bold'))

patienttable.config(show='headings')

root.mainloop()
