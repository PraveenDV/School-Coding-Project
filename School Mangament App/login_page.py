import tkinter as tk
from tkinter import *
from tkinter import messagebox
import webbrowser
import subprocess
from PIL import ImageTk, Image
import ast
import customtkinter as ctk

def login():
    admin_db=open('admin_db.txt', 'r')
    student_db=open('student_db.txt')
    teacher_db=open('teacher_db.txt')

    d1=admin_db.read()
    d2=student_db.read()
    d3=teacher_db.read()

    username=entry1.get()
    password=entry2.get()

    if username and password in d1:
        subprocess.run(['python', 'Admin.py'], check=True)
    elif username and password in d2:
        subprocess.run(['python', 'Student_main.py'], check=True)
    elif username and password in d3:
        subprocess.run(['python', 'Teacher_main.py'], check=True)
    else:
        messagebox.showerror(message='Invalid credentials')

# create custom tkinter window
login_window = ctk.CTk()  
login_window.geometry("600x440")
login_window.title('Login')

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

forget_password_button = ctk.CTkButton(master=frame, text="Forgot password?")#command=forget_password_page)
forget_password_button.place(x=155, y=195)

# Create custom button
button1 = ctk.CTkButton(master=frame, width=220, text="Login", command=login, corner_radius=6)
button1.place(x=50, y=240)
login_window.mainloop()

# Function for Main Page (after login)
def main_page(user_data):
   # Check the user's role to determine available actions
    if user_data["role"] == "teacher":
        subprocess.run(['python', 'Teacher_main.py'], check=True)
    if user_data["role"] == "student":
        subprocess.run(['python', 'Student_main.py'],check=True)
    if user_data["role"] == "admin":
        subprocess.run(['python', 'Admin.py'], check=True)    
    #tk.Label(main_window, text="Main Page", font=("Arial", 18), bg="lime green").pack(pady=10)

if __name__=="__main__":
    login_window.mainloop()