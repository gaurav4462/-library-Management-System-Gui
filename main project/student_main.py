from tkinter import *
from tkinter import ttk
from matplotlib.ft2font import BOLD
import mysql.connector
import student_login as sl




window = Tk()
window.geometry('1000x600')
window['bg'] = '#D3EAFF'
window.title("Student Page")


def check_info():

    c1 = Canvas(f2,bg='#C9E0F9')
    c1.place(relheight=1,relwidth=1)

    l1 = Label(c1,text="Student Info",font="40,bold",bg="#C9E0F9")
    l1.place(relheight=0.1,relwidth=1)
    def connectivity(hostname,username,password,db_name):
        conn=mysql.connector.connect(
        host=hostname,
        user=username,
        passwd=password,
        db=db_name)
        return conn
    conn=connectivity("localhost","root","gaurav","lms")

    query=f"""SELECT * FROM INFO Where User_Name = '{sl.name_student.get()}'""" 
    conn1=conn.cursor()
    conn1.execute(query)
    records = conn1.fetchall()

    

    l1 = Label(c1,text=f"User Name = {records[0][1]}",bg="#C9E0F9", anchor='w')
    l1.place(rely=0.1,relheight=0.05,relwidth=0.5)
    l2 = Label(c1,text=f"Name = {records[0][0]} ",bg="#C9E0F9",anchor='w')
    l2.place(rely=0.16,relheight=0.05,relwidth=0.5)
    l3 = Label(c1,text=f"E-Mail = {records[0][2]}",bg="#C9E0F9", anchor='w')
    l3.place(rely=0.22,relheight=0.05,relwidth=0.5)
    l4 = Label(c1,text=f"Contect = {records[0][4]}",bg="#C9E0F9", anchor='w')
    l4.place(rely=0.28,relheight=0.05,relwidth=0.5)
    l5 = Label(c1,text=f"Gender = {records[0][3]} ",bg="#C9E0F9", anchor='w')
    l5.place(rely=0.34,relheight=0.05,relwidth=0.5)
    l5 = Label(c1,text='----------------------------------------------------------------------------------------------------------------',bg="#C9E0F9")
    l5.place(rely=0.40,relheight=0.05,relwidth=1)

    def update():
        c2 = Canvas(f2,bg='#C9E0F9')
        c2.place(rely=0.4,relheight=0.6,relwidth=1)

        def update_():

            def connectivity(hostname,username,password,db_name):
                conn=mysql.connector.connect(
                host=hostname,
                user=username,
                passwd=password,
                db=db_name)
                return conn
            conn=connectivity("localhost","root","gaurav","lms")

            cursor = conn.cursor()

            cursor.execute(f'''
                            UPDATE info SET 
                            EMAIL = '{x2.get()}',  
                            CONTACT = '{x4.get()}'
                            Where User_Name = '{sl.name_student.get()}'
                            ''')

            conn.commit()
            x8 = Label(c2,text = 'update successfully ',bg="#C9E0F9",fg = 'green')
            x8.place(relheight=1,relwidth=1)

            check_info()

        x1 = Label(c2,text="Enter New Email :",bg="#C9E0F9")
        x1.place(relx=0.05,rely=0.1,relheight=0.1,relwidth=0.45)
        x2 = Entry(c2,bg="#C9E0F9")
        x2.place(relx=0.5,rely=0.1,relheight=0.1,relwidth=0.45)
        x3 = Label(c2,text="Enter New Contect :",bg="#C9E0F9")
        x3.place(relx=0.05,rely=0.3,relheight=0.1,relwidth=0.45)
        x4 = Entry(c2,bg="#C9E0F9")
        x4.place(relx=0.5,rely=0.3,relheight=0.1,relwidth=0.45)
        x5 = Button(c2,text='Update',command=update_)
        x5.place(relx=0.35,rely=0.5,relheight=0.1,relwidth=0.3)


        
    def updatep():
        c3 = Canvas(f2,bg='#C9E0F9')
        c3.place(rely=0.4,relheight=0.6,relwidth=1)

        def updatep_():

            def connectivity(hostname,username,password,db_name):
                conn=mysql.connector.connect(
                host=hostname,
                user=username,
                passwd=password,
                db=db_name)
                return conn
            conn=connectivity("localhost","root","gaurav","lms")

            cursor = conn.cursor()
            query = f'''Select password_ from info where User_Name = '{sl.name_student.get()}';'''
            cursor.execute(query)
            record_ = cursor.fetchall()

            if str(y2.get()) == record_[0][0]:
                if str(y4.get()) == str(y6.get()):

                    cursor = conn.cursor()

                    cursor.execute(f'''
                                    UPDATE info SET  
                                    Password_ = '{y4.get()}'
                                    Where User_Name = '{sl.name_student.get()}'
                                    ''')

                    conn.commit()
                    y8 = Label(c3,text = 'update successfully',bg="#C9E0F9",fg = 'green')
                    y8.place(relheight=1,relwidth=1)

                else:
                    y8 = Label(c3,text="Password Not Match",bg="#C9E0F9", fg = 'red',font=BOLD)
                    y8.place(relx=0.2,rely=0.7,relheight=0.1,relwidth=0.45)
                    
            else:
                y8 = Label(c3,text="Wrong Password ",bg="#C9E0F9", fg = 'red',font=BOLD)
                y8.place(relx=0.2,rely=0.7,relheight=0.1,relwidth=0.45)


        y1 = Label(c3,text="Enter Your Current Password :",bg="#C9E0F9")
        y1.place(relx=0.05,rely=0.1,relheight=0.1,relwidth=0.45)
        y2 = Entry(c3,bg="#C9E0F9",show='*',)
        y2.place(relx=0.5,rely=0.1,relheight=0.1,relwidth=0.45)
        y3 = Label(c3,text="Enter New Password :              ",bg="#C9E0F9")
        y3.place(relx=0.05,rely=0.25,relheight=0.1,relwidth=0.45)
        y4 = Entry(c3,bg="#C9E0F9",show='*',)
        y4.place(relx=0.5,rely=0.25,relheight=0.1,relwidth=0.45)
        y5 = Label(c3,text="Re-Enter New Password :             ",bg="#C9E0F9")
        y5.place(relx=0.05,rely=0.4,relheight=0.1,relwidth=0.45)
        y6 = Entry(c3,bg="#C9E0F9",show='*',)
        y6.place(relx=0.5,rely=0.4,relheight=0.1,relwidth=0.45)
        y7 = Button(c3,text='Update',command=updatep_)
        y7.place(relx=0.35,rely=0.55,relheight=0.1,relwidth=0.3)



    v1 = Button(f2,text='Edit Profile',command=update)
    v1.place(relx=0.6,rely=0.12,relheight=0.05,relwidth=0.3)
    v2 = Button(f2,text='Update Password',command=updatep)
    v2.place(relx=0.6,rely=0.19,relheight=0.05,relwidth=0.3)
    


def Find_Book():


    def connectivity(hostname,username,password,db_name):
        conn=mysql.connector.connect(
        host=hostname,
        user=username,
        passwd=password,
        db=db_name)
        return conn
    conn=connectivity("localhost","root","gaurav","lms")
    c1 = Canvas(f2,bg='#C9E0F9')
    c1.place(relheight=0.07,relwidth=1)
    c2 = Canvas(f2,bg='#C9E0F9')
    c2.place(rely=0.06,relheight=0.94,relwidth=1)


    Scbar=Scrollbar(c2)
    Scbar.pack(side=RIGHT,fill=Y)

    trv=ttk.Treeview(c2,selectmode='browse',height=24,yscrollcommand=Scbar.set)
    trv.place(x=0,y=0)
  
    Scbar.config(command=trv.yview)
    trv["columns"]=("1","2","3","4","5",)
    trv['show']='headings'
    trv.column("1",width=80,anchor=CENTER)
    trv.column("2",width=248,anchor='c')
    trv.column("3",width=80,anchor='c')
    trv.column("4",width=130,anchor='c')
    trv.column("5",width=90,anchor='c')
    trv.heading("1",text="BOOK_CODE")
    trv.heading("2",text="BOOK_TITLE")
    trv.heading("3",text="CATEGORY")
    trv.heading("4",text="AUTHOR")
    trv.heading("5",text="BOOK_EDITION")

    query="""SELECT BOOK_CODE,BOOK_TITLE,CATEGORY,AUTHOR,BOOK_EDITION FROM av_book""" 
    conn1=conn.cursor()
    conn1.execute(query)
    records_ = conn1.fetchall()
    for i in records_:
        trv.insert("",'end',values=(i[0],i[1],i[2],i[3],i[4]))

    search1=StringVar()
    searchbox=ttk.Combobox(c1,textvariable=search1,width=10,font=("times new roman",13,"bold"),state="readonly")
    searchbox["values"]=("Book_Code","Book_Title","Category")
    searchbox.place(x=0,y=0,height=30)
    searchentry1=StringVar()
    searchentry=Entry(c1,textvariable=searchentry1,font=("Arial",15),bg="#C9E0F9")
    searchentry.place(x=120,y=0,height=30,width=380)
    def search():
        for i in trv.get_children():
            trv.delete(i)
        if search1.get()=="Book_Code":
            record=None
            query=f"""SELECT BOOK_CODE,BOOK_TITLE,CATEGORY,AUTHOR,BOOK_EDITION FROM av_book WHERE BOOK_CODE='{searchentry1.get()}';""" 
            conn1=conn.cursor()
            conn1.execute(query)
            record=conn1.fetchall()
            for i in record:
                trv.insert("",'end',iid=i[0],values=(i[0],i[1],i[2],i[3],i[4]))
        elif search1.get()=="Book_Title":
            record=None
            query=f"""SELECT BOOK_CODE,BOOK_TITLE,CATEGORY,AUTHOR,BOOK_EDITION FROM av_book WHERE BOOK_TITLE='{searchentry1.get()}';""" 
            conn1=conn.cursor()
            conn1.execute(query)
            record=conn1.fetchall()
            for i in record:
                trv.insert("",'end',iid=i[0],values=(i[0],i[1],i[2],i[3],i[4]))
        elif search1.get()=="Category":
            record=None
            query=f"""SELECT BOOK_CODE,BOOK_TITLE,CATEGORY,AUTHOR,BOOK_EDITION FROM av_book WHERE CATEGORY='{searchentry1.get()}';""" 
            conn1=conn.cursor()
            conn1.execute(query)
            record=conn1.fetchall()
            for i in record:
                trv.insert("",'end',iid=i[0],values=(i[0],i[1],i[2],i[3],i[4]))
    searchbutton=Button(c1,text="SEARCH",font=("arial",10),bg="#C9E0F9",command=search)
    searchbutton.place(x=450,y=0,height=30)


def Return_Book():
    
    c2 = Canvas(f2,bg='#C9E0F9')
    c2.place(relheight=1,relwidth=1)
    def connectivity(hostname,username,password,db_name):
        conn=mysql.connector.connect(
        host=hostname,
        user=username,
        passwd=password,
        db=db_name)
        return conn
    conn=connectivity("localhost","root","gaurav","lms")

    def return_book():

        query = f"""SELECT * FROM  book_issue WHERE BOOK_CODE =  '{p2.get()}' ;"""
        conn1=conn.cursor()
        conn1.execute(query)
        record=conn1.fetchall()
        if len(record) > 0:
            query=f"""DELETE FROM  book_issue WHERE BOOK_CODE =  '{p2.get()}' """
            conn1=conn.cursor()
            conn1.execute(query) 
            conn.commit()

            query1=f"""select * from BOOK_DETAILS where BOOK_CODE =  '{p2.get()}'; """
            conn2=conn.cursor()
            conn2.execute(query1)
            records = conn2.fetchall()
            query2 = f'''INSERT INTO av_book 
                        value("{records[0][0]}","{records[0][1]}","{records[0][2]}","{records[0][3]}","{records[0][4]}","{records[0][5]}",
                             "{records[0][6]}","{records[0][7]}","{records[0][8]}","{records[0][9]}","{records[0][10]}"); '''

            conn3=conn.cursor()
            conn3.execute(query2)
            conn.commit()
            p2.delete(0,END)
            c3 = Canvas(f2,bg='#C9E0F9')
            c3.place(rely=0.3,relheight=0.5,relwidth=1)
            
            q7 = Label(c3,text="Return Successful ",font="bold",bg="#C9E0F9",fg= 'green')
            q7.place(relheight=1,relwidth=0.9)
        else :
            q7 = Label(c3,text="Book Not available ",font="bold",bg="#C9E0F9",fg= 'green')
            q7.place(relheight=1,relwidth=0.9)



    def view():
        query=f"""SELECT * FROM book_issue WHERE BOOK_CODE = '{p2.get()}' """ 
        conn1=conn.cursor()
        conn1.execute(query)
        records_ = conn1.fetchall()
        if len(records_) == 0:
            c3 = Canvas(f2,bg='#C9E0F9')
            c3.place(rely=0.3,relheight=0.5,relwidth=1)
            q6 = Label(c3,text="Book Not Available ",font="bold",bg="#C9E0F9",fg= 'red')
            q6.place(relheight=1,relwidth=0.9)
        else:
            c3 = Canvas(f2,bg='#C9E0F9')
            c3.place(rely=0.3,relheight=0.5,relwidth=1)
            c3 = Canvas(f2,bg='#C9E0F9')
            c3.place(rely=0.3,relheight=0.5,relwidth=1)
            q1 = Label(c3,text=f"BOOK_CODE    :   {records_[0][0]}",font="bold",bg="#C9E0F9", anchor='w')
            q1.place(rely=0.1,relheight=0.1,relwidth=0.7)
            q2 = Label(c3,text=f"User_Name     :   {records_[0][1]}",font="bold",bg="#C9E0F9", anchor='w')
            q2.place(rely=0.23,relheight=0.1,relwidth=0.7)
            q3 = Label(c3,text=f"Data_Issue   :   {records_[0][2]}",font="bold",bg="#C9E0F9", anchor='w')
            q3.place(rely=0.36,relheight=0.1,relwidth=1)
            q4 = Label(c3,text=f"Date_Return   :   {records_[0][3]}",font="bold",bg="#C9E0F9", anchor='w')
            q4.place(rely=0.49,relheight=0.1,relwidth=0.7)
            b7 = Button(c3,text="Return Book",command=return_book)
            b7.place(relx=0.25,rely=0.7,relheight=0.1,relwidth=0.5)


    p1 = Label(c2,text="Book Code         :",font="bold",bg="#C9E0F9")
    p1.place(relx=0.05,rely=0.05,relheight=0.04,relwidth=0.45)
    p2 = Entry(c2,font=BOLD,bg="#C9E0F9")
    p2.place(relx=0.5,rely=0.05,relheight=0.04,relwidth=0.45)
    b6 = Button(c2,text="Check",command=view)
    b6.place(relx=0.25,rely=0.13,relheight=0.05,relwidth=0.5)


def status():
    c4 = Canvas(f2,bg='#C9E0F9')
    c4.place(relheight=1,relwidth=1)
    def connectivity(hostname,username,password,db_name):
        conn=mysql.connector.connect(
        host=hostname,
        user=username,
        passwd=password,
        db=db_name)
        return conn
    conn=connectivity("localhost","root","gaurav","lms")
    Scbar=Scrollbar(c4)
    Scbar.pack(side=RIGHT,fill=Y)
    trv=ttk.Treeview(c4,selectmode='browse',height=24,yscrollcommand=Scbar.set)
    trv.place(relheight=1,relwidth=0.98)

    Scbar.config(command=trv.yview)
    trv["columns"]=("1","2","3","4",'5')
    trv['show']='headings'
    trv.column("1",width=200,anchor=CENTER)
    trv.column("2",width=80,anchor='c')
    trv.column("3",width=100,anchor='c')
    trv.column("4",width=80,anchor='c')
    trv.column("5",width=80,anchor='c')
    trv.heading("1",text="BOOK_TITLE")
    trv.heading("2",text="BOOK_CODE")
    trv.heading("3",text="USER_NAME")
    trv.heading("4",text="ISSUE_DATE")
    trv.heading("5",text="RETURN_DATE")

    query=f"""SELECT BOOK_CODE,User_Name,DATE_ISSUE,DATE_RETURN FROM book_issue WHERE User_Name = '{sl.name_student.get()}' """ 
    conn1=conn.cursor()
    conn1.execute(query)
    records_ = conn1.fetchall()
    for i in range(len(records_)):
        query1=f"""SELECT BOOK_TITLE FROM book_details WHERE BOOK_CODE = '{records_[i][0]}' """ 
        conn2=conn.cursor()
        conn2.execute(query1)
        records1 = conn2.fetchall()
        trv.insert("",'end',values=(records1[0][0],records_[i][0],records_[i][1],records_[i][2],records_[i][3]))
    



def log_out():
    window.destroy()
    import login

f1 = Frame(window,bg="#C9E0F9")
f1.place(relx=0.02,rely=0.03,relheight=0.94,relwidth=0.33)
f2 = Frame(window,bg="#C9E0F9")
f2.place(relx=0.37,rely=0.03,relheight=0.94,relwidth=0.61)



b1 = Button(f1,text="Check Info", font="Arial 10",bg="#C9E0F9",command=check_info)
b1.place(relx=0.25,rely=0.05,relheight=0.1,relwidth=0.5)
b2 = Button(f1,text="Check Book Status", font="Arial 10",bg="#C9E0F9",command=status)
b2.place(relx=0.25,rely=0.25,relheight=0.1,relwidth=0.5)
b3 = Button(f1,text="Find Book", font="Arial 10",bg="#C9E0F9",command=Find_Book)
b3.place(relx=0.25,rely=0.45,relheight=0.1,relwidth=0.5)
b4 = Button(f1,text="Return Book", font="Arial 10",bg="#C9E0F9",command=Return_Book)
b4.place(relx=0.25,rely=0.65,relheight=0.1,relwidth=0.5)
b5 = Button(f1,text="Log Out", font="Arial 10",bg="#C9E0F9",command=log_out)
b5.place(relx=0.25,rely=0.85,relheight=0.1,relwidth=0.5)


window.mainloop()