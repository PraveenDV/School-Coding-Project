import tkinter as tk
from tkinter import simpledialog, messagebox
import webbrowser
import subprocess
import customtkinter as ctk
# Create the main window
window = ctk.CTk()
window.title("Smart Brigade")
window.geometry("800x600")

ctk.CTkLabel(window, width=25, text="Namaskara!", font=('Century Gothic', 25, 'bold')).pack()
ctk.CTkLabel(window, width=25, text="Welcome to Smart Brigade", font=('Century Gothic', 25, 'bold')).pack()

# Function to display sign up page
def display_sign_up():
    subprocess.run(['python', 'sign_up_page.py'])

#Signup button
button_signup = ctk.CTkButton(window, text="Sign Up", command= display_sign_up,
                           font=("Arial", 24))
button_signup.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

# Create the Login button
button_login = ctk.CTkButton(window, text="Login", command=lambda: login_page(),
                          font=("Arial", 24))
button_login.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

# Function for the login page
def login_page():
    subprocess.run(['python', 'login_page.py'])    

# Function for Quiz Page
def create_test():
    webbrowser.open("https://quizizz.com/?lng=en")

# Start the main event loop
window.mainloop()