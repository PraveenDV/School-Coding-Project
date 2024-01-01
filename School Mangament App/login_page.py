import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
import webbrowser
import subprocess
from PIL import ImageTk, Image
import ast
import customtkinter as ctk

ctk.set_appearance_mode('System')


def check():
    if os.path.getsize('admin_db.txt')==0:
        file=open('admin_db.txt', 'w')
        data=str({'Username':'password'})
        file.write(data)
        file.close()
    if os.path.getsize('teacher_db.txt')==0:
        file=open('teacher_db.txt', 'w')
        data=str({'Username':'password'})
        file.write(data)
        file.close()
    if os.path.getsize('student_db.txt')==0:
        file=open('student_db.txt', 'w')
        data=str({'Username':'password'})
        file.write(data)
        file.close()    

check()

# Function for Main Page (after login)
def login():
    admin_db=open(r'admin_db.txt', 'r+')
    student_db=open(r'student_db.txt','r+')
    teacher_db=open(r'teacher_db.txt', 'r+')

    d1=admin_db.read()
    d2=student_db.read()
    d3=teacher_db.read()

    r1=ast.literal_eval(d1)
    r2=ast.literal_eval(d2)
    r3=ast.literal_eval(d3)

    admin_db.close()
    teacher_db.close()
    student_db.close()

    username=entry1.get()
    password=entry2.get()

    if username in r1.keys() and password==r1[username]:
        subprocess.run(['python', r'Admin.py'], check=True)
    elif username in r2.keys() and password==r2[username]:
        subprocess.run(['python', r'Student_main.py'], check=True)
    elif username in r3.keys() and password==r3[username]:
        subprocess.run(['python', r'Teacher_main.py'], check=True)
    elif not username and not password:
        messagebox.showerror(message='Please provide the required credentials')
    else:
        messagebox.showerror(message='Invalid credentials')

# create custom tkinter window
login_window = ctk.CTk()  
login_window.geometry("600x440")
login_window.title('Login')
login_window.configure(bg="light blue")
# create a black background
background = ctk.CTkFrame(master=login_window, width=600, height=440, corner_radius=0)
background.place(relx=0, rely=0)

# create custom frame
frame = ctk.CTkFrame(master=background, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

l2 = ctk.CTkLabel(master=frame, text="Log into your Account", font=('Century Gothic', 20))
l2.place(x=50, y=45)

entry1 = ctk.CTkEntry(master=frame, width=220, placeholder_text='Username')
entry1.place(x=50, y=110)

entry2 = ctk.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
entry2.place(x=50, y=165)

# Create custom button
button1 = ctk.CTkButton(master=frame, width=220, text="Login", command=login, corner_radius=6)
button1.place(x=50, y=240)


'''def main_page(user_data):
   # Check the user's role to determine available actions
    if user_data["role"] == "teacher":
        subprocess.run(['python', 'Teacher_main.py'], check=True)
    if user_data["role"] == "student":
        subprocess.run(['python', 'Student_main.py'],check=True)
    if user_data["role"] == "admin":
        subprocess.run(['python', 'Admin.py'], check=True)    
    #tk.Label(main_window, text="Main Page", font=("Arial", 18), bg="lime green").pack(pady=10)'''

if __name__=="__main__":
    login_window.mainloop()