
import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog
import webbrowser
import os
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import customtkinter as ctk
import subprocess

# Create the main window
window = ctk.CTk()
window.title("Teacher Dashboard")
window.geometry("600x600")
#window.configure(bg_color="skyblue1")

# Initialize user role
user_role = None  # Keeps track of the current user's role (teacher or student)

# Predefined login credentials
predefined_credentials = {
    "John": {"class": "11", "section": "A", "password": "123", "role": "teacher"},
}

# Create a directory to store uploaded assignments
upload_dir = os.path.expanduser("~")

# Initialize global_announcements
global_announcements = []

# Function to handle assignment upload by the teacher
def upload_assignment():
    file_path = filedialog.askopenfilename(title="Upload Assignment", filetypes=[("PDF Files", "*.pdf"), ("PNG Files", "*.png")])

    if file_path:
        # Check if the file is a PDF or PNG
        if file_path.endswith((".pdf", ".png")):
            # Save the assignment file to the "Assignments" folder
            assignment_filename = os.path.basename(file_path)
            save_path = os.path.join("Assignments", assignment_filename)
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            os.replace(file_path, save_path)
            # Allow the teacher to provide separate instructions
            instruction = simpledialog.askstring("Assignment Instructions", "Enter assignment instructions (optional):")
            # Display the instructions in a messagebox
            if instruction:
                messagebox.showinfo("Assignment Instructions", instruction)
            else:
                messagebox.showinfo("Assignment Instructions", "No additional instructions provided.")
        else:
            messagebox.showerror("Invalid File", "Only PDF and PNG files are allowed.")

# Function to show teacher options
def show_teacher_options():
    def on_announcements():
        open_announcements_page()

    def on_my_timetable():
        my_timetable_page()

    def on_create_test():
        create_test()

    def on_check_grade():
        check_grade()

    def on_assignments():
        teacher_assignments_page()

    button_width = 16
    button_height = 3

    # Create buttons for various options
    announcements_button = ctk.CTkButton(window, text="Announcements", command=on_announcements,
                                    fg_color="black", font=("Arial", 16))
    #announcements_button.grid(row=1, column=1)
    announcements_button.pack(pady=10)

    my_timetable_button = ctk.CTkButton(window, text="My Timetable", command=on_my_timetable,
                                   fg_color="black", font=("Arial", 16))
    #my_timetable_button.grid(row=4, column=1)
    my_timetable_button.pack(pady=10)

    create_test_button = ctk.CTkButton(window, text="Create Test", command=on_create_test,
                                   fg_color="black", font=("Arial", 16))
    #create_test_button.grid(row=7, column=1)
    create_test_button.pack(pady=10)

    check_grade_button = ctk.CTkButton(window, text='''Check
Student
Grade''', command=on_check_grade, fg_color="black",
                                    font=("Arial", 16))
    #check_grade_button.grid(row=11, column=1)
    check_grade_button.pack(pady=10)

    assignments_button = ctk.CTkButton(window, text="Assignments", command=upload_assignment,
                                   fg_color="black", font=("Arial", 16))
    #assignments_button.grid(row=14, column=1)
    assignments_button.pack(pady=10)

    # Add an option for adding global announcements
    '''add_announcement_button = ctk.CTkButton(window, text="Add_Global Announcement", command=lambda: open_announcement_editor(True),
                                  fg_color="black", font=("Arial", 16))
    #add_announcement_button.grid(row=17, column=1)
    add_announcement_button.pack(pady=10)'''

# Show teacher options without the need for a button
show_teacher_options()

# Function For Teacher's Create Test
def create_test():
    webbrowser.open("https://quizizz.com/?lng=en")

# Function for Teacher's Assignments Page
def teacher_assignments_page():
    # Create the teacher's assignments page window
    assignments_window = ctk.CTkToplevel(master=window)
    assignments_window.title("Teacher's Assignments")
    assignments_window.geometry("800x600")
    assignments_window.configure(bg_color="light green")
    assignments_window.grab_set()
    ctk.Label(assignments_window, text="Teacher's Assignments", font=("Arial", 18), bg_color="light green").pack(pady=10)

# Function to check student grade
def check_grade():
    messagebox.showinfo("Work in Progress", "Feature coming soon.")

# Function for My Timetable Page
def my_timetable_page():
    subprocess.run(['python','timetable.py'], check=True)

# Function to open the announcements page
def open_announcements_page():
    announcements_window = ctk.CTkToplevel(master=window)
    announcements_window.title("Announcements Page")
    announcements_window.geometry("600x400")
    announcements_window.configure(bg_color="skyblue1")

    def view_global_announcements():
        global global_announcements
        global_announcements = load_global_announcements()
        if global_announcements:
            announcements_text = "\n".join(global_announcements)
            messagebox.showinfo("Global Announcements", announcements_text)
        else:
            messagebox.showinfo("Global Announcements", "No global announcements available.")

    def add_global_announcement():
        open_announcement_editor(True)

    def view_admin_announcements():
        admin_announcements = load_admin_announcements()
        if admin_announcements:
            announcements_text = "\n".join(admin_announcements)
            messagebox.showinfo("Admin Announcements", announcements_text)
        else:
            messagebox.showinfo("Admin Announcements", "No admin announcements available.")

    view_global_button = ctk.CTkButton(announcements_window, text='''View Global
Announcements''', command=view_global_announcements,
                                  fg_color="black")
    add_global_button = ctk.CTkButton(announcements_window, text='''Add Global
 Announcement''', command=add_global_announcement,
                                  fg_color="black")
    view_admin_button = ctk.CTkButton(announcements_window, text='''View Admin
Announcements''', command=view_admin_announcements,
                                 fg_color="black")

    view_global_button.pack(pady=10)
    add_global_button.pack(pady=10)
    view_admin_button.pack(pady=10)

# Reusing the announcement editor from the previous code
def open_announcement_editor(is_global):
    def save_announcement(announcement_text, filename):
        if is_global:
            global_announcements.append(announcement_text)
            save_to_csv(filename, global_announcements)
        else:
            messagebox.showinfo("Access Denied", "Teachers cannot add admin announcements.")

    def send_announcement_email(announcement_text):
        recipient_email = "meetchangela1308@gmail.com"
        subject = 'Announcement'
        send_email(subject, announcement_text, recipient_email)
        if is_global:
            save_announcement(announcement_text, "global_announcements.csv")

    def save_to_csv(filename, announcements):
        current_directory = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_directory, filename)
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows([[announcement] for announcement in announcements])

    announcement_editor = ctk.CTkToplevel(master=window)
    announcement_editor.title("Announcement Editor")
    announcement_editor.geometry("400x400")

    announcement_text = ctk.CTkTextbox(announcement_editor, wrap=ctk.WORD)
    announcement_text.pack(pady=10)

    send_button = ctk.CTkButton(announcement_editor, text="Send Announcement", command=lambda: send_announcement_email(announcement_text.get("1.0", "end-1c")))
    send_button.pack()

    if is_global:
        save_button = ctk.CTkButton(announcement_editor, text="Save Announcement", command=lambda: save_announcement(announcement_text.get("1.0", "end-1c"), "global_announcements.csv"))
        save_button.pack()

# Load global announcements from CSV file
def load_global_announcements():
    return load_announcements("global_announcements.csv")

# Load admin announcements from CSV file
def load_admin_announcements():
    return load_announcements("admin_announcements.csv")

# Function to load announcements from CSV
def load_announcements(filename):
    current_directory = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_directory, filename)
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            return [row[0] for row in reader]
    else:
        return []

# Define the send_email function at the global scope
def send_email(subject, body, to):
    from_email = 'meetpythontest@gmail.com'
    from_password = 'Python@123!test'
    send_email = 'meetchangela1308@gmail.com'
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, from_password)
    server.sendmail(from_email, to, msg.as_string())
    server.quit()

# Start the main event loop
window.mainloop()
