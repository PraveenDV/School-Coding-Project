import tkinter as tk
from tkinter import *
from tkinter import messagebox
import webbrowser
import subprocess
from PIL import ImageTk, Image
import ast


sign_up_window = tk.Tk()
sign_up_window.title("Sign Up")
sign_up_window.geometry("800x800")
sign_up_window.grab_set()


def open_login_page():
    subprocess.run(['python', 'login_page.py'],check=True)

roles=['Admin', 'Teacher', 'Student']


def sign_up():
    user=username.get()
    password=password_entry.get()
    confirm_pass=cpassword_entry.get()
    role=role_var.get()
       
    if user and password==confirm_pass:
       
       if role=='Admin':
         try:
            file=open('admin_db.txt', 'r+')
            d=file.read()
            r=ast.literal_eval(d)
            dict1={user:password}
            r.update(dict1)
            file.truncate(0)
            file.close()

            file=open('admin_db.txt', 'w')
            w=file.write(str(r))

            messagebox.showinfo('Signup', "Succesfully signed up!")
            subprocess.run(['python', 'Admin.py'],check=True)
            sign_up_window.destroy()
         except:
            file=open('admin_db.txt', 'w')
            data=str({'Username':'password'})
            file.write(data)
            file.close()

       if role=='Teacher':
         try:
            file=open('teacher_db.txt', 'r+')
            d=file.read()
            r=ast.literal_eval(d)
            dict1={user:password}
            r.update(dict1)
            file.truncate(0)
            file.close()

            file=open('teacher_db.txt', 'w')
            w=file.write(str(r))

            messagebox.showinfo('Signup', "Succesfully signed up!")
            subprocess.run(['python', 'Teacher_main.py'],check=True)
            sign_up_window.destroy()
         except:
            file=open('teacher_db.txt', 'w')
            data=str({'Username':'password'})
            file.write(data)
            file.close()

       if role=='Student':
         try:
            file=open('student_db.txt', 'r+')
            d=file.read()
            r=ast.literal_eval(d)
            dict1={user:password}
            r.update(dict1)
            file.truncate(0)
            file.close()

            file=open('student_db.txt', 'w')
            w=file.write(str(r))

            messagebox.showinfo('Signup', "Succesfully signed up!")
            subprocess.run(['python', 'Student_main.py'],check=True)
            sign_up_window.destroy()
         except:
            file=open('student_db.txt', 'w')
            data=str({'Username':'password'})
            file.write(data)
            file.close()
       

    else: 
            messagebox.showerror(message='Please enter username and password')


image=ImageTk.PhotoImage(Image.open('assets\schoolLogo.png'))
Label(sign_up_window, image=image, bg="white").place(x=50, y=50)

frame=Frame(sign_up_window, width=150, height=150).place(x=450, y=50)
heading=Label(frame, width=25, text="Sign Up", fg='teal', font=('Arial', 25, 'bold'))
heading.place(x=350, y=50)

Label(frame, text='Username:', font=('Arial', 11)).place(x=500, y=150)
username=Entry(frame, fg='black', border=2, font=("Arial", 11))
username.place(x=500, y=180)

Label(frame, text='Password:', font=('Arial', 11)).place(x=500, y=220)
password_entry=Entry(frame, fg='black', border=2, font=("Arial", 11),show='*')
password_entry.place(x=500, y=250)

Label(frame, text='Confirm password:', font=('Arial', 11)).place(x=500, y=320)
cpassword_entry=Entry(frame, fg='black', border=2, font=("Arial", 11),show='*')
cpassword_entry.place(x=500, y=350)

Label(frame, text='Sign up as?', font=('Arial', 11)).place(x=500, y=420)
role_var=tk.StringVar(sign_up_window)
role_var.set(roles[0])
dropdown=tk.OptionMenu(sign_up_window, role_var, *roles)
dropdown.place(x=500, y=450)

sign_up_button=Button(frame, pady=5, text="Sign Up", font=("Arial", 11, "bold"), width=20, command=sign_up)
sign_up_button.place(x=500, y=500)

Label(frame, text="Already have an account?", fg="black", font=("Arial", 11)).place(x=500, y=600)
signin=Button(frame, width=6, text='Sign in', cursor='hand2', fg='#57a1f8', border=0, command=open_login_page)
signin.place(x=670, y=600)

if __name__=='__main__':
    sign_up_window.mainloop()

