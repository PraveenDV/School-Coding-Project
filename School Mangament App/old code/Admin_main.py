import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog
import pandas as pd
import subprocess
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import customtkinter as ctk



bg_color="azure"
text_color="black"
button_color="cornflower blue"

# Create an empty list to store announcements
global global_announcements
global_announcements= []
global admin_announcements
admin_announcements= []


def open_announcement_editor(is_global):
    #def save_to_csv():
        

    def save_announcement(announcement_text):
        if is_global:
            global_announcements.append(announcement_text)
            print(global_announcements)
        else:
            admin_announcements.append(announcement_text)
            print(admin_announcements)

        with open('global_announcements.csv', 'a', newline='') as file1:
            writer = csv.writer(file1)
            writer.writerow([announcement for announcement in global_announcements])

        with open('admin_announcements.csv', 'a', newline='') as file2:
            writer = csv.writer(file2)
            writer.writerow([announcement for announcement in admin_announcements])

        announcement_editor_window.destroy()

    def send_announcement_email(announcement_text):
        recipient_email = ''

        subject = 'Announcement'
        send_email(subject, announcement_text, recipient_email)

        save_announcement(announcement_text)

    

    def send_email(subject, body, to_email):
        email = 'meetpythontest@gmail.com'
        password = ''

        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login(email, password)

        message = MIMEMultipart()
        message['From'] = email
        message['To'] = to_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        smtp.sendmail(email, to_email, message.as_string())
        smtp.quit()

    announcement_editor_window = ctk.CTkToplevel()
    announcement_editor_window.title("Announcement Editor")
    announcement_editor_window.geometry("600x400")
    announcement_editor_window.configure(bg="light green")

    announcement_entry = ctk.CTkTextbox(announcement_editor_window, height=10, width=40)
    announcement_entry.pack(pady=20)

    send_on_app_button = tk.Button(announcement_editor_window, 
                                   text="Send Announcement On App", 
                                    fg="black", width=20, 
                                   height=2, 
                                   command=lambda: save_announcement(announcement_entry.get("1.0", "end-1c")))
    send_on_app_button.pack(pady=10)


    send_through_email_button = ctk.CTkButton(announcement_editor_window, 
                                          text="Send Announcement Through Email", 
                                          
                                          fg_color='black',
                                          width=20, 
                                          height=2, 
                                          command=lambda: send_announcement_email(announcement_entry.get("1.0", "end-1c")))
    send_through_email_button.pack(pady=10)



#Viewing the announcements 
def view_announcements(is_global):
    announcements = global_announcements if is_global else admin_announcements

    if not announcements:
        messagebox.showinfo("Announcements", "No announcements available.")

    elif announcements:
        new_window=ctk.CTkToplevel(admin_window)

        if announcements==global_announcements:
            text=pd.read_csv("global_announcements.csv")
            l=ctk.CTkLabel(new_window, text=text)
            l.place(relx=0.0)

        elif announcements==admin_announcements:
            text=pd.read_csv("admin_announcements.csv")
            l=ctk.CTkLabel(new_window, text=text)
            l.place(relx=0.0)



# Create the Admin main page window
admin_window = ctk.CTk()
admin_window.title("Admin Main Page")
admin_window.geometry("800x600")
admin_window.configure(bg=bg_color)
admin_window.grab_set()




# Define a function to open the admin timetable
def open_admin_timetable():
    try:
        subprocess.run(['python', 'admin_timetable.py'], check=True)
    except FileNotFoundError:
        messagebox.showerror("Error", "Admin timetable code file not found.")
    


# Create a button to open the admin timetable
admin_timetable_button = ctk.CTkButton(admin_window, text="Open Admin Timetable", command=open_admin_timetable,
                                    fg_color=text_color,
                                    font=("Arial", 18))
admin_timetable_button.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

# Create a button to open the announcements page
announcements_button = ctk.CTkButton(admin_window, text="Announcements", fg_color=text_color, font=("Arial", 18))
announcements_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

def open_announcement_options():
    announcement_options_window = ctk.CTkToplevel(master=admin_window)
    announcement_options_window.title("Announcement Options")
    announcement_options_window.geometry("400x400")

    view_global_announcement_button = ctk.CTkButton(announcement_options_window, text="View Global Announcements", command=lambda: view_announcements(True),
                                    fg_color="black", font=("Arial", 16), width=20, height=2)
    view_global_announcement_button.pack(pady=10)

    view_admin_announcement_button = ctk.CTkButton(announcement_options_window, text="View Admin Announcements", command=lambda: view_announcements(False),
                                    fg_color="black", font=("Arial", 16), width=20, height=2)
    view_admin_announcement_button.pack(pady=10)

    add_admin_announcement_button = ctk.CTkButton(announcement_options_window, text="Add Admin Announcement", command=lambda: open_announcement_editor(False),
                                    fg_color="black", font=("Arial", 16), width=20, height=2)
    add_admin_announcement_button.pack(pady=10)

    add_global_announcement_button = ctk.CTkButton(announcement_options_window, text="Add Global Announcement", command=lambda: open_announcement_editor(True),
                                    fg_color="black", font=("Arial", 16), width=20, height=2)
    add_global_announcement_button.pack(pady=10)

announcements_button.configure(command=open_announcement_options)

# Define actions for button2, button3, and so on
def button2_action():
    pass

def button3_action():
    pass

def button4_action():
    pass

def button5_action():
    pass

def button6_action():
    pass

# Create buttons 2 to 6
button2 = ctk.CTkButton(admin_window, text="Button 2", command=button2_action,
                    fg_color=text_color, font=("Arial", 18))
button2.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

button3 = ctk.CTkButton(admin_window, text="Button 3", command=button3_action,
                    fg_color=text_color, font=("Arial", 18))
button3.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

button4 = ctk.CTkButton(admin_window, text="Button 4", command=button4_action,
                     fg_color=text_color, font=("Arial", 18))
button4.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

button5 = ctk.CTkButton(admin_window, text="Button 5", command=button5_action,
                     fg_color=text_color, font=("Arial", 18))
button5.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

button6 = ctk.CTkButton(admin_window, text="Button 6", command=button6_action,
                     fg_color=text_color, font=("Arial", 18))
button6.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

print(admin_announcements, global_announcements)

# Start the main event loop for the Admin main page
admin_window.mainloop()
