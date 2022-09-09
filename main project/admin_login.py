from tkinter import *

window = Tk()
window.geometry('500x300')
window['bg'] = '#D3EAFF'
window.title("Admin Login")


def nextpage_admin():
    if name_admin.get() =="Gaurav76" and password_admin.get() == "Gaurav@123":
        window.destroy()
        import admin_main
    else :
        out_put =Label(f2,text="Invlid Username Or Password",bg="#C9E0F9",fg = "red",font="bold")
        out_put.place(rely=0.22, relwidth=1, relheight=0.1)

name_admin=StringVar()
password_admin=StringVar()

f2 = Frame(window,bg="#C9E0F9")
f2.place(relheight=1,relwidth=1)
l2 = Label(f2,text="Admin Login",bg="black",fg = "white",font="bold")
l2.place(relheight=0.2,relwidth=1)
y1 = Label(f2,text="Username",font="bold",bg="#C9E0F9")
y1.place(relx=0.05,rely=0.4,relheight=0.125,relwidth=0.45)
y2 = Entry(f2,textvariable=name_admin,font="bold",bg="#C9E0F9")
y2.place(relx=0.5,rely=0.4,relheight=0.125,relwidth=0.45)
y3 = Label(f2,text="Password",font="bold",bg="#C9E0F9")
y3.place(relx=0.05,rely=0.625,relheight=0.125,relwidth=0.45)
y4 = Entry(f2,textvariable=password_admin,font="bold",show='*',bg="#C9E0F9")
y4.place(relx=0.5,rely=0.625,relheight=0.125,relwidth=0.45)
b2 = Button(f2,text="Login",font="bold",command=nextpage_admin,bg="#C9E0F9")
b2.place(relx=0.5,rely=0.85,relheight=0.125,relwidth=0.45)

window.mainloop()