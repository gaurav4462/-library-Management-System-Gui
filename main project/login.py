from tkinter import *
from PIL import ImageTk,Image

def Admin_Login():
        root.destroy()
        import admin_login

def Student_Login():
        root.destroy()
        import student_login


root = Tk()
root.title("login Page")
root.geometry('400x350')
root['bg'] = '#D3EAFF'

f1 = Frame(root,bg="#C9E0F9")
f1.place(relheight=0.2,relwidth=1)
f2 = Frame(root,bg="#C9E0F9")
f2.place(rely=0.2,relheight=0.8,relwidth=0.5)

l1 = Label(f1,text="Library System",bg="#C9E0F9",fg = "black",font="bold")
l1.place(relx=0.05,rely=0.05,relheight=1,relwidth=0.9)
c1 = Frame(root,height=25, width=25)
c1.place(relx=0.5,rely=0.2,relheight=0.8,relwidth=0.5)

img = ImageTk.PhotoImage(Image.open("library.jpg"))

label = Label(c1, image = img)
label.pack()

b1 = Button(f2,text="Admin Login",bg='#C9E0F9',command=Admin_Login)
b1.place(relx=0.05,rely=0.3,relheight=0.15,relwidth=0.85)

b3 = Button(f2,text="Student Login",bg='#C9E0F9',command=Student_Login)
b3.place(relx=0.05,rely=0.6,relheight=0.15,relwidth=0.85)


root.mainloop()