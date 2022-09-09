from tkinter import *
from datatable import f
import mysql.connector
from numpy import var

def reg_page():
    try:
        class main:

            def __init__(self,root):
                self.root=Toplevel(window)
                self.root.title("Registration Page")
                self.root['bg'] = '#D3EAFF'
                self.root.geometry("1200x700")

                
                def connectivity(hostname,username,password,db_name):
                    conn=mysql.connector.connect(
                    host=hostname,
                    user=username,
                    passwd=password,
                    db=db_name)
                    return conn
                conn=connectivity("localhost","root","gaurav","lms")



                def submit_from():
                    if z2.get() and z4.get() and z6.get() and z8.get() and z11.get() and z13.get() and z15.get():

                        if z11.get() !=  z13.get():
                            out_put4 =Label(lframe2,text="Passwrd Not Same",fg = "red",font="bold",bg="#C9E0F9")
                            out_put4.place( relwidth=1, relheight=1)
                        else:
                            count = 0
                            query = '''SELECT User_Name FROM INFO '''
                            conn1=conn.cursor()
                            conn1.execute(query)
                            records = conn1.fetchall()
                            for i in range(len(records)):
                                if str(z15.get()) in records[i][0]:
                                    out_put5 =Label(lframe2,text='Username Not Exist',fg = "red",font="bold",bg="#C9E0F9")
                                    out_put5.place(relwidth=1, relheight=1) 
                                    count +=1
                            if count == 0:
                                out_put3 =Label(lframe2,text='Successful',fg = "green",font="bold",bg="#C9E0F9")
                                out_put3.place(relwidth=1, relheight=1) 

                                query="""INSERT INTO INFO VALUES (%s,%s,%s,%s,%s,%s);""" 
                                data=(f"{self.Fname.get()} {self.Lname.get()}",self.Uname.get(),self.Email.get(),self.Gender.get(),self.Contact.get(),self.Pass.get())
                                conn1=conn.cursor()
                                conn1.execute(query,data)
                                conn.commit()
                                z2.delete(0,END)
                                z4.delete(0,END)
                                z15.delete(0,END)
                                z6.delete(0,END)
                                z8.delete(0,END)
                                z11.delete(0,END)
                                z13.delete(0,END)
                                return conn1






                    else:
                        out_put3 =Label(lframe2,text='Input Required',fg = "red",font="bold",bg="#C9E0F9")
                        out_put3.place(relwidth=1, relheight=1)

                    


                self.Fname=StringVar()
                self.Lname=StringVar()
                self.Uname=StringVar()
                self.Email=StringVar()
                self.Gender=StringVar()
                self.Contact=StringVar()
                self.Pass=StringVar()
                self.Rpass=StringVar()


                f3 = Frame(self.root,bg="#C9E0F9")
                f3.place(relheight=1,relwidth=1)
                l3 = Label(f3,text="Student Registration",bg="black",fg = "white")
                l3.place(relheight=0.05,relwidth=1)
                z1 = Label(f3,text="Firstname                  ",font="bold",bg="#C9E0F9")
                z1.place(relx=0.02,rely=0.1,relheight=0.05,relwidth=0.45)
                z2 = Entry(f3,textvariable=self.Fname,font="bold",bg="#C9E0F9")
                z2.place(relx=0.47,rely=0.1,relheight=0.05,relwidth=0.45)
                z3 = Label(f3,text="Lastname                   ",font="bold",bg="#C9E0F9")
                z3.place(relx=0.02,rely=0.19,relheight=0.05,relwidth=0.45)
                z4 = Entry(f3,textvariable=self.Lname,font="bold",bg="#C9E0F9")
                z4.place(relx=0.47,rely=0.19,relheight=0.05,relwidth=0.45)
                z14 = Label(f3,text="Username                   ",font="bold",bg="#C9E0F9")
                z14.place(relx=0.02,rely=0.28,relheight=0.05,relwidth=0.45)
                z15 = Entry(f3,textvariable=self.Uname,font="bold",bg="#C9E0F9")
                z15.place(relx=0.47,rely=0.28,relheight=0.05,relwidth=0.45)
                z5 = Label(f3,text="Email                         ",font="bold",bg="#C9E0F9")
                z5.place(relx=0.02,rely=0.37,relheight=0.05,relwidth=0.45)
                z6 = Entry(f3,textvariable=self.Email,font="bold",bg="#C9E0F9")
                z6.place(relx=0.47,rely=0.37,relheight=0.05,relwidth=0.45)
                z7 = Label(f3,text="Contact Number        ",font="bold",bg="#C9E0F9")
                z7.place(relx=0.02,rely=0.46,relheight=0.05,relwidth=0.45)
                z8 = Entry(f3,textvariable=self.Contact,font="bold",bg="#C9E0F9")
                z8.place(relx=0.47,rely=0.46,relheight=0.05,relwidth=0.45)
                z9 = Label(f3,text="Select Gender           ",font="bold",bg="#C9E0F9")
                z9.place(relx=0.02,rely=0.55,relheight=0.05,relwidth=0.45)
                gender_frame = LabelFrame(f3,bg="#C9E0F9")
                gender_frame.place(relx=0.47,rely=0.55,relheight=0.05,relwidth=0.45)
                male_rb = Radiobutton(gender_frame, text='Male',variable=self.Gender,value='male',bg="#C9E0F9")
                male_rb.place(relwidth=0.45,relheight=1)
                female_rb = Radiobutton(gender_frame, text='Female',variable=self.Gender,value='female',bg="#C9E0F9")
                female_rb.place(relx = 0.5,relwidth=0.5,relheight=1)
                z10 = Label(f3, text="Enter Password       ",font="bold",bg="#C9E0F9")
                z10.place(relx=0.02,rely=0.64,relheight=0.05,relwidth=0.45)
                z11 = Entry(f3,textvariable=self.Pass,font="bold",show='*',bg="#C9E0F9")
                z11.place(relx=0.47,rely=0.64,relheight=0.05,relwidth=0.45)
                z12 = Label(f3,text="Re-Enter Password",font="bold",bg="#C9E0F9")
                z12.place(relx=0.02,rely=0.73,relheight=0.05,relwidth=0.45)
                z13 = Entry(f3,textvariable=self.Rpass,font="bold",show='*',bg="#C9E0F9")
                z13.place(relx=0.47,rely=0.73,relheight=0.05,relwidth=0.45)
                b3 = Button(f3,text="Submit",font="bold",bg="#C9E0F9",command=submit_from)
                b3.place(relx=0.70,rely=0.82,relheight=0.05,relwidth=0.22)
                lframe2 = LabelFrame(f3,text="Status",bg="#C9E0F9")
                lframe2.place(rely=0.9,relheight=0.09,relwidth=1)


                    

        ab=main(window)
        window.mainloop()
    except:
        pass


window = Tk()
window.geometry('500x300')
window['bg'] = '#D3EAFF'
window.title("Student Login")




def nextPage_student():



    if x2.get() and x4.get():
        def connectivity(hostname,username,password,db_name):
            conn=mysql.connector.connect(
            host=hostname,
            user=username,
            passwd=password,
            db=db_name)
            return conn
        conn=connectivity("localhost","root","gaurav","lms")

        query = f'''SELECT Password_ FROM INFO Where User_Name = '{x2.get()}'; '''
        conn1=conn.cursor()
        conn1.execute(query)
        record = conn1.fetchall()



        if str(x4.get()) in record[0][0] :
            global var
            var = name_student.get()
            window.destroy()
            import student_main
    
        else :
            out_put2 =Label(f1,text="Invlid Username Or Password",fg = "red",font="bold")
            out_put2.place(rely=0.12, relwidth=1, relheight=0.1)
    else:
            out_put3 =Label(f1,text='Input Required',fg = "red",font="bold",bg="#C9E0F9")
            out_put3.place(rely=0.12, relwidth=1, relheight=0.1)

    

name_student=StringVar()
password_student=StringVar()

f1 = Frame(window,bg="#C9E0F9")
f1.place(relheight=1,relwidth=1)
l1 = Label(f1,text="Student Login",bg="black",fg = "white",font="bold")
l1.place(relheight=0.2,relwidth=1)
x1 = Label(f1,text="Username",font="bold",bg="#C9E0F9")
x1.place(relx=0.05,rely=0.4,relheight=0.125,relwidth=0.45)
x2 = Entry(f1,textvariable=name_student,font="bold",bg="#C9E0F9")
x2.place(relx=0.5,rely=0.4,relheight=0.125,relwidth=0.45)
x3 = Label(f1,text="Password             ",font="bold",bg="#C9E0F9")
x3.place(relx=0.05,rely=0.625,relheight=0.125,relwidth=0.45)
x4 = Entry(f1,textvariable=password_student,font="bold",show='*',bg="#C9E0F9")
x4.place(relx=0.5,rely=0.625,relheight=0.125,relwidth=0.45)
b1 = Button(f1,text="Login",font="bold",command=nextPage_student,bg="#C9E0F9")
b1.place(relx=0.05,rely=0.85,relheight=0.125,relwidth=0.45)
b2 = Button(f1,text="Ragister",font="bold",command=reg_page,bg="#C9E0F9")
b2.place(relx=0.5,rely=0.85,relheight=0.125,relwidth=0.45)

window.mainloop()