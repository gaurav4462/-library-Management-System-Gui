
from base64 import b64decode
from tkinter import *
from tkinter import ttk
from matplotlib.ft2font import BOLD
import mysql.connector
import pandas as pd


window = Tk()
window.geometry('1070x550')
window['bg'] = '#D3EAFF'
window.title("Admin Page")

def check_list():

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


    

    Scbar=Scrollbar(c2,orient=VERTICAL)


    trv=ttk.Treeview(c2,selectmode='browse',height=24,yscrollcommand=Scbar.set)
    trv.place(x=0,y=0)
    Scbar.pack(side=RIGHT,fill=Y)
    Scbar.config(command=trv.yview)
    trv["columns"]=("1","2","3","4","5",)
    trv['show']='headings'
    trv.column("1",width=155,anchor=CENTER)
    trv.column("2",width=110,anchor='c')
    trv.column("3",width=200,anchor='c')
    trv.column("4",width=65,anchor='c')
    trv.column("5",width=98,anchor='c')
    trv.heading("1",text="Name")
    trv.heading("2",text="User Name")
    trv.heading("3",text="E-Mail")
    trv.heading("4",text="Gender")
    trv.heading("5",text="Contact")

    query="""SELECT * FROM INFO""" 
    conn1=conn.cursor()
    conn1.execute(query)
    records = conn1.fetchall()
    for i in records:
        trv.insert("",'end',values=(i[0],i[1],i[2],i[3],i[4]))

    search1=StringVar()
    searchbox=ttk.Combobox(c1,textvariable=search1,width=10,font=("times new roman",13,"bold"),state="readonly")
    searchbox["values"]=("User_Name","E-Mail")
    searchbox.place(x=0,y=0,height=30)
    searchentry1=StringVar()
    searchentry=Entry(c1,textvariable=searchentry1,font=("Arial",15),bg="#C9E0F9")
    searchentry.place(x=120,y=0,height=30,width=380)
    def search():
        for i in trv.get_children():
            trv.delete(i)
        if search1.get()=="User_Name":
            record=None
            query=f"""SELECT * FROM INFO WHERE User_Name='{searchentry1.get()}';""" 
            conn1=conn.cursor()
            conn1.execute(query)
            record=conn1.fetchall()
            for i in record:
                trv.insert("",'end',iid=i[0],values=(i[0],i[1],i[2],i[3],i[4]))
        elif search1.get()=="E-Mail":
            record=None
            query=f"SELECT * FROM INFO WHERE EMAIL='{searchentry1.get()}';"
            conn1=conn.cursor()
            conn1.execute(query)
            record=conn1.fetchall()
            for i in record:
                trv.insert("",'end',iid=i[0],values=(i[0],i[1],i[2],i[3],i[4]))


    searchbutton=Button(c1,text="SEARCH",font=("arial",10),bg="#C9E0F9",command=search)
    searchbutton.place(x=450,y=0,height=30)


def view_books():

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

    query="""SELECT BOOK_CODE,BOOK_TITLE,CATEGORY,AUTHOR,BOOK_EDITION FROM BOOK_DETAILS""" 
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
            query=f"""SELECT BOOK_CODE,BOOK_TITLE,CATEGORY,AUTHOR,BOOK_EDITION FROM BOOK_DETAILS WHERE BOOK_CODE='{searchentry1.get()}';""" 
            conn1=conn.cursor()
            conn1.execute(query)
            record=conn1.fetchall()
            for i in record:
                trv.insert("",'end',iid=i[0],values=(i[0],i[1],i[2],i[3],i[4]))
        elif search1.get()=="Book_Title":
            record=None
            query=f"""SELECT BOOK_CODE,BOOK_TITLE,CATEGORY,AUTHOR,BOOK_EDITION FROM BOOK_DETAILS WHERE BOOK_TITLE='{searchentry1.get()}';""" 
            conn1=conn.cursor()
            conn1.execute(query)
            record=conn1.fetchall()
            for i in record:
                trv.insert("",'end',iid=i[0],values=(i[0],i[1],i[2],i[3],i[4]))
        elif search1.get()=="Category":
            record=None
            query=f"""SELECT BOOK_CODE,BOOK_TITLE,CATEGORY,AUTHOR,BOOK_EDITION FROM BOOK_DETAILS WHERE CATEGORY='{searchentry1.get()}';""" 
            conn1=conn.cursor()
            conn1.execute(query)
            record=conn1.fetchall()
            for i in record:
                trv.insert("",'end',iid=i[0],values=(i[0],i[1],i[2],i[3],i[4]))
    searchbutton=Button(c1,text="SEARCH",font=("arial",10),bg="#C9E0F9",command=search)
    searchbutton.place(x=450,y=0,height=30)
    b25 = Button(c1,text="Available Book",font=("arial",10),bg="#C9E0F9",command=vab)
    b25.place(x=530,y=0,height=30)
    

def Add_book():

    def add_book():

        def connectivity(hostname,username,password,db_name):
            conn=mysql.connector.connect(
            host=hostname,
            user=username,
            passwd=password,
            db=db_name)
            return conn
        conn=connectivity("localhost","root","gaurav","lms")



        if z2.get() and z4.get() and z6.get() and z8.get() and z10.get() and z12.get() and z14.get() and z16.get() and z18.get() and z20.get() and z22.get():

            query = '''SELECT BOOK_CODE FROM BOOK_DETAILS'''
            conn1=conn.cursor()
            conn1.execute(query)
            records = conn1.fetchall()
            count = 0
            for i in range(len(records)):

                if str(z2.get()) == records[i][0]:
                    count +=1

            if count == 1:
                out_put3 =Label(c1,text='Book Already Exist',fg = "red",font="bold",bg='#C9E0F9')
                out_put3.place(rely = 0.9,relwidth=1, relheight=0.1)
            else:
                query="""INSERT INTO BOOK_DETAILS VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""" 
                data=(z2.get(),z4.get(),z6.get(),z8.get(),z10.get(),z12.get(),z14.get(),z16.get(),z18.get(),z20.get(),z22.get())
                conn1=conn.cursor()
                conn1.execute(query,data)
                conn.commit()

                query1="""INSERT INTO av_book VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""" 
                conn1=conn.cursor()
                conn1.execute(query1,data)
                conn.commit()



                z2.delete(0,END)
                z4.delete(0,END)
                z6.delete(0,END)
                z8.delete(0,END)
                z10.delete(0,END)
                z12.delete(0,END)
                z14.delete(0,END)
                z16.delete(0,END)
                z18.delete(0,END)
                z20.delete(0,END)
                z22.delete(0,END)
                out_put3 =Label(c1,text='Added',fg = "green",font="bold",bg='#C9E0F9')
                out_put3.place(rely = 0.9,relwidth=1, relheight=0.1)

        else:
            out_put3 =Label(c1,text='Input Required',fg = "red",font="bold",bg='#C9E0F9')
            out_put3.place(rely = 0.9,relwidth=1, relheight=0.1)


    s1=StringVar()
    s2=StringVar()
    s3=StringVar()
    s4=StringVar()
    s5=StringVar()
    s6=StringVar()
    s7=StringVar()
    s8=StringVar()
    s9=StringVar()
    s10=StringVar()

    c1 = Canvas(f2,bg='#C9E0F9')
    c1.place(relheight=1,relwidth=1)



    z1 = Label(c1,text="Book Code         :",font="bold",bg="#C9E0F9")
    z1.place(relx=0.05,rely=0.05,relheight=0.04,relwidth=0.45)
    z2 = Entry(c1,textvariable=s1,font="bold",bg="#C9E0F9")
    z2.place(relx=0.5,rely=0.05,relheight=0.04,relwidth=0.45)
    z3 = Label(c1,text="BOOK_TITLE      :",font="bold",bg="#C9E0F9")
    z3.place(relx=0.05,rely=0.12,relheight=0.04,relwidth=0.45)
    z4 = Entry(c1,textvariable=s2,font="bold",bg="#C9E0F9")
    z4.place(relx=0.5,rely=0.12,relheight=0.04,relwidth=0.45)
    z5 = Label(c1,text="CATEGORY        :",font="bold",bg="#C9E0F9")
    z5.place(relx=0.05,rely=0.19,relheight=0.04,relwidth=0.45)
    z6 = Entry(c1,textvariable=s3,font="bold",bg="#C9E0F9")
    z6.place(relx=0.5,rely=0.19,relheight=0.04,relwidth=0.45)
    z7 = Label(c1,text="AUTHOR            :",font="bold",bg="#C9E0F9")
    z7.place(relx=0.05,rely=0.26,relheight=0.04,relwidth=0.45)
    z8 = Entry(c1,textvariable=s4,font="bold",bg="#C9E0F9")
    z8.place(relx=0.5,rely=0.26,relheight=0.04,relwidth=0.45)
    z9 = Label(c1,text="PUBLICATION    :",font="bold",bg="#C9E0F9")
    z9.place(relx=0.05,rely=0.33,relheight=0.04,relwidth=0.45)
    z10 = Entry(c1,textvariable=s5,font="bold",bg="#C9E0F9")
    z10.place(relx=0.5,rely=0.33,relheight=0.04,relwidth=0.45)
    z11 = Label(c1, text="PUBLISH_DATE  :",font="bold",bg="#C9E0F9")
    z11.place(relx=0.05,rely=0.40,relheight=0.04,relwidth=0.45)
    z12 = Entry(c1,font="bold",bg="#C9E0F9")
    z12.place(relx=0.5,rely=0.40,relheight=0.04,relwidth=0.45)
    z13 = Label(c1,text="BOOK_EDITION  :",font="bold",bg="#C9E0F9")
    z13.place(relx=0.05,rely=0.47,relheight=0.04,relwidth=0.45)
    z14 = Entry(c1,font="bold",bg="#C9E0F9")
    z14.place(relx=0.5,rely=0.47,relheight=0.04,relwidth=0.45)
    z15 = Label(c1,text="PRICE                :",font="bold",bg="#C9E0F9")
    z15.place(relx=0.05,rely=0.54,relheight=0.04,relwidth=0.45)
    z16 = Entry(c1,textvariable=s6,font="bold",bg="#C9E0F9")
    z16.place(relx=0.5,rely=0.54,relheight=0.04,relwidth=0.45)
    z17 = Label(c1,text="RACK_NUM        :",font="bold",bg="#C9E0F9")
    z17.place(relx=0.05,rely=0.61,relheight=0.04,relwidth=0.45)
    z18 = Entry(c1,textvariable=s7,font="bold",bg="#C9E0F9")
    z18.place(relx=0.5,rely=0.61,relheight=0.04,relwidth=0.45)
    z19 = Label(c1,text="DATE_ARRIVAL  :",font="bold",bg="#C9E0F9")
    z19.place(relx=0.05,rely=0.68,relheight=0.04,relwidth=0.45)
    z20 = Entry(c1,font="bold",bg="#C9E0F9")
    z20.place(relx=0.5,rely=0.68,relheight=0.04,relwidth=0.45)
    z21 = Label(c1,text="SUPPLIER_ID     :",font="bold",bg="#C9E0F9")
    z21.place(relx=0.05,rely=0.75,relheight=0.04,relwidth=0.45)
    z22 = Entry(c1,textvariable=s8,font="bold",bg="#C9E0F9")
    z22.place(relx=0.5,rely=0.75,relheight=0.04,relwidth=0.45)
    b1 = Button(f2,text="Add Book",command=add_book)
    b1.place(relx=0.25,rely=0.85,relheight=0.05,relwidth=0.5)


def Delete_book():
    def connectivity(hostname,username,password,db_name):
        conn=mysql.connector.connect(
        host=hostname,
        user=username,
        passwd=password,
        db=db_name)
        return conn
    conn=connectivity("localhost","root","gaurav","lms")

    def delete_book():

        query = f"""SELECT * FROM  av_book WHERE BOOK_CODE =  '{p2.get()}' ;"""
        conn1=conn.cursor()
        conn1.execute(query)
        record=conn1.fetchall()
        if len(record) > 0:
            query=f"""DELETE FROM  BOOK_DETAILS WHERE BOOK_CODE =  '{p2.get()}' """
            conn1=conn.cursor()
            conn1.execute(query) 
            conn.commit()

            query1=f"""DELETE FROM  av_book WHERE BOOK_CODE =  '{p2.get()}' """
            conn2=conn.cursor()
            conn2.execute(query1)
            conn.commit()
            p2.delete(0,END)
            q7 = Label(c2,text="DELETED ",font="bold",bg="#C9E0F9",fg= 'green')
            q7.place(rely=0.25,relheight=0.7,relwidth=0.9)
        else :
            q7 = Label(c2,text="Book Con Not Be Deleted ",font="bold",bg="#C9E0F9",fg= 'green')
            q7.place(rely=0.25,relheight=0.7,relwidth=0.9)


        
        

    def view():
        

        query=f"""SELECT BOOK_CODE,BOOK_TITLE,AUTHOR,BOOK_EDITION,PRICE FROM BOOK_DETAILS WHERE BOOK_CODE = '{p2.get()}' """ 
        conn1=conn.cursor()
        conn1.execute(query)
        records_ = conn1.fetchall()
        if len(records_) == 0:
            q6 = Label(c2,text="Book Not Available ",font="bold",bg="#C9E0F9",fg= 'red')
            q6.place(rely=0.25,relheight=0.7,relwidth=0.9)
        else:
            q1 = Label(c2,text=f"BOOK_CODE    :   {records_[0][0]}",font="bold",bg="#C9E0F9", anchor='w')
            q1.place(rely=0.25,relheight=0.05,relwidth=0.7)
            q2 = Label(c2,text=f"BOOK_TITLE     :   {records_[0][1]}",font="bold",bg="#C9E0F9", anchor='w')
            q2.place(rely=0.33,relheight=0.05,relwidth=0.7)
            q3 = Label(c2,text=f"AUTHOR            :   {records_[0][2]}",font="bold",bg="#C9E0F9", anchor='w')
            q3.place(rely=0.41,relheight=0.05,relwidth=1)
            q4 = Label(c2,text=f"BOOK_EDITION :   {records_[0][3]}",font="bold",bg="#C9E0F9", anchor='w')
            q4.place(rely=0.49,relheight=0.05,relwidth=0.7)
            q5 = Label(c2,text=f"PRICE                :   {records_[0][4]}",font="bold",bg="#C9E0F9", anchor='w')
            q5.place(rely=0.57,relheight=0.05,relwidth=0.7)
            b7 = Button(c2,text="Delete Book",command=delete_book)
            b7.place(relx=0.25,rely=0.85,relheight=0.05,relwidth=0.5)

    c2 = Canvas(f2,bg='#C9E0F9')
    c2.place(relheight=1,relwidth=1)
           



    p1 = Label(c2,text="Book Code         :",font="bold",bg="#C9E0F9")
    p1.place(relx=0.05,rely=0.05,relheight=0.04,relwidth=0.45)
    p2 = Entry(c2,font="bold",bg="#C9E0F9")
    p2.place(relx=0.5,rely=0.05,relheight=0.04,relwidth=0.45)
    b6 = Button(c2,text="View Book",command=view)
    b6.place(relx=0.25,rely=0.13,relheight=0.05,relwidth=0.5)


def vab():
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





def bs():
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
    trv["columns"]=("1","2","3","4")
    trv['show']='headings'
    trv.column("1",width=128,anchor=CENTER)
    trv.column("2",width=245,anchor='c')
    trv.column("3",width=128,anchor='c')
    trv.column("4",width=128,anchor='c')
    trv.heading("1",text="BOOK_CODE")
    trv.heading("2",text="User_Name")
    trv.heading("3",text="Date_Issue")
    trv.heading("4",text="Date_return")


    query="""SELECT * FROM book_issue""" 
    conn1=conn.cursor()
    conn1.execute(query)
    records_ = conn1.fetchall()
    for i in records_:
        trv.insert("",'end',values=(i[0],i[1],i[2],i[3]))


    search1=StringVar()
    searchbox=ttk.Combobox(c1,textvariable=search1,width=10,font=("times new roman",13,"bold"),state="readonly")
    searchbox["values"]=("Book_Code","User_Name")
    searchbox.place(x=0,y=0,height=30)
    searchentry1=StringVar()
    searchentry=Entry(c1,textvariable=searchentry1,font=("Arial",15),bg="#C9E0F9")
    searchentry.place(x=120,y=0,height=30,width=380)
    def search():
        for i in trv.get_children():
            trv.delete(i)
        if search1.get()=="Book_Code":
            record=None
            query=f"""SELECT * FROM book_issue WHERE BOOK_CODE='{searchentry1.get()}';""" 
            conn1=conn.cursor()
            conn1.execute(query)
            record=conn1.fetchall()
            for i in record:
                trv.insert("",'end',iid=i[0],values=(i[0],i[1],i[2],i[3]))
        elif search1.get()=="User_Name":
            record=None
            query=f"""SELECT * FROM book_issue WHERE User_Name='{searchentry1.get()}';""" 
            conn1=conn.cursor()
            conn1.execute(query)
            record=conn1.fetchall()
            for i in record:
                trv.insert("",'end',iid=i[0],values=(i[0],i[1],i[2],i[3]))
    searchbutton=Button(c1,text="SEARCH",font=("arial",10),bg="#C9E0F9",command=search)
    searchbutton.place(x=450,y=0,height=30)


def Issue_Book():

    c1 = Canvas(f2,bg='#C9E0F9')
    c1.place(relheight=1,relwidth=1)

    l1 = Label(c1,text="Issue Book",font="40,bold",bg="#C9E0F9")
    l1.place(relheight=0.1,relwidth=1)

    def connectivity(hostname,username,password,db_name):
        conn=mysql.connector.connect(
        host=hostname,
        user=username,
        passwd=password,
        db=db_name)
        return conn
    conn=connectivity("localhost","root","gaurav","lms")


    def issue_book():

        if y2.get() and y4.get() and y6.get() and y8.get():

            query=f"""SELECT * FROM INFO WHERE User_Name = '{y2.get()}'""" 
            conn1=conn.cursor()
            conn1.execute(query)
            records_ = conn1.fetchall()

            if len(records_) == 0:
                y7 = Label(c1,text=f"{y2.get()} Not Exist",bg="#C9E0F9",fg='red',font=BOLD)
                y7.place(relx=0.05,rely=0.75,relheight=0.05,relwidth=1)


                query=f"""SELECT * FROM av_book Where BOOK_CODE = '{y4.get()}'""" 
                conn1=conn.cursor()
                conn1.execute(query)
                records = conn1.fetchall()
            else:

                if len(records) > 0:

                    query="""INSERT INTO book_issue VALUES (%s,%s,%s,%s);""" 
                    data=(y2.get(),y4.get(),y6.get(),y8.get())
                    conn1=conn.cursor()
                    conn1.execute(query,data)
                    conn.commit()

                    query1=f"""DELETE FROM  av_book WHERE BOOK_CODE =  '{y4.get()}' """
                    conn2=conn.cursor()
                    conn2.execute(query1)
                    conn.commit()
                    y7 = Label(c1,text="Book Issued",bg="#C9E0F9",fg='green',font=BOLD)
                    y7.place(relx=0.05,rely=0.75,relheight=0.05,relwidth=1)
                    y2.delete(0,END)
                    y4.delete(0,END)
                    y8.delete(0,END)

                else:
                    y7 = Label(c1,text="Book Not Available",bg="#C9E0F9",fg='red',font=BOLD)
                    y7.place(relx=0.05,rely=0.75,relheight=0.05,relwidth=1)
        else:
            y7 = Label(c1,text="Input Required",bg="#C9E0F9",fg='red',font=BOLD)
            y7.place(relx=0.05,rely=0.75,relheight=0.05,relwidth=1)


    x = pd.to_datetime("today").strftime("20%y-%m-%d")
    y1 = Label(c1,text="Enter User Name :",bg="#C9E0F9", anchor='w')
    y1.place(relx=0.05,rely=0.2,relheight=0.05,relwidth=0.45)
    y2 = Entry(c1,bg="#C9E0F9")
    y2.place(relx=0.5,rely=0.2,relheight=0.05,relwidth=0.45)
    y3 = Label(c1,text="Enter Book Code",bg="#C9E0F9", anchor='w')
    y3.place(relx=0.05,rely=0.3,relheight=0.05,relwidth=0.45)
    y4 = Entry(c1,bg="#C9E0F9")
    y4.place(relx=0.5,rely=0.3,relheight=0.05,relwidth=0.45)
    y5 = Label(c1,text="Enter Date_Issue",bg="#C9E0F9",anchor='w')
    y5.place(relx=0.05,rely=0.4,relheight=0.05,relwidth=0.45)
    y6 = Entry(c1,bg="#C9E0F9")
    y6.place(relx=0.5,rely=0.4,relheight=0.05,relwidth=0.45)
    y6.insert(0,x)
    y7 = Label(c1,text="Enter Date_Return",bg="#C9E0F9",anchor='w')
    y7.place(relx=0.05,rely=0.5,relheight=0.05,relwidth=0.45)
    y8 = Entry(c1,bg="#C9E0F9")
    y8.place(relx=0.5,rely=0.5,relheight=0.05,relwidth=0.45)
    y7 = Button(c1,text='Issue Book',command=issue_book)
    y7.place(relx=0.35,rely=0.6,relheight=0.05,relwidth=0.3)





def log_out():
    window.destroy()
    import login





f1 = Frame(window,bg="#C9E0F9")
f1.place(relx=0.02,rely=0.03,relheight=0.94,relwidth=0.33)
f2 = Frame(window,bd=3,bg="#C9E0F9")
f2.place(relx=0.37,rely=0.03,relheight=0.94,relwidth=0.61)



b1 = Button(f1,text="Check Student List", font="Arial 10",bg="#C9E0F9",command=check_list)
b1.place(relx=0.25,rely=0.05,relheight=0.1,relwidth=0.5)
b2 = Button(f1,text="View Books ", font="Arial 10",bg="#C9E0F9",command=view_books)
b2.place(relx=0.25,rely=0.18,relheight=0.1,relwidth=0.5)
b3 = Button(f1,text="Issue Book", font="Arial 10",bg="#C9E0F9",command=Issue_Book)
b3.place(relx=0.25,rely=0.31,relheight=0.1,relwidth=0.5)
b4 = Button(f1,text="Book Status ", font="Arial 10",bg="#C9E0F9",command=bs)
b4.place(relx=0.25,rely=0.44,relheight=0.1,relwidth=0.5)
b5 = Button(f1,text="Add Book", font="Arial 10",bg="#C9E0F9",command=Add_book)
b5.place(relx=0.25,rely=0.57,relheight=0.1,relwidth=0.5)
b6 = Button(f1,text="Delete Book", font="Arial 10",bg="#C9E0F9",command=Delete_book)
b6.place(relx=0.25,rely=0.70,relheight=0.1,relwidth=0.5)
b7 = Button(f1,text="Log Out", font="Arial 10",bg="#C9E0F9",command=log_out)
b7.place(relx=0.25,rely=0.83,relheight=0.1,relwidth=0.5)

window.mainloop()