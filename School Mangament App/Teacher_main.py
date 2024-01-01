
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
import shutil

ctk.set_appearance_mode('System')

# Create the main window
window = ctk.CTk()
window.title("Teacher Dashboard")
window.geometry("600x600")
window.configure(bg="light blue")
#window.configure(bg_color="skyblue1")

# Create a directory to store uploaded assignments
upload_dir = os.path.expanduser("~")

# Initialize global_announcements
global_announcements = []

def upload_assignment():
    file_path = filedialog.askopenfilename(title="Upload Assignment", filetypes=[("PDF Files", "*.pdf"), ("PNG Files", "*.png"), ("JPG Files", "*.jpg")])

    if file_path:
        # Check if the file is a PDF or PNG
        if file_path.endswith((".pdf", ".png", ".jpg")):
            # Save the assignment file to the "Assignments" folder
            assignment_filename = os.path.basename(file_path)
            save_path = os.path.join("D:\School Mangament App\Assignments", assignment_filename)
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            try:
                shutil.copy(file_path, save_path)
            except shutil.Error as e:
                messagebox.showerror("Error", f"Failed to move file: {e}")
        else:
            messagebox.showerror("Invalid File", "Only PDF, PNG and JPG files are allowed.")

# Function For Teacher's Create Test
def create_test():
    webbrowser.open("https://quizizz.com/?lng=en")

# Function to open a file dialog for downloading an assignment
def download_assignment(file_path):
    save_path = filedialog.asksaveasfilename(defaultextension=".pdf", initialfile=file_path)
    if save_path:
        # Copy the assignment file to the selected save path
        shutil.copyfile(file_path, save_path)
        messagebox.showinfo("Download Assignment", f"Downloading {os.path.basename(file_path)} to {save_path}")

# Function to list assignments in the "Assignments" folder
def list_assignments():
    assignments_folder = "Assignments"  # Folder where assignments are stored
    assignments = []

    if os.path.exists(assignments_folder):
        # Get a list of files in the assignments folder
        assignment_files = os.listdir(assignments_folder)

        for file_name in assignment_files:
            # Create a dictionary for each assignment with its name and file path
            assignment = {
                "name": file_name,  # You can modify this to display a more user-friendly name
                "file_path": os.path.join(assignments_folder, file_name)
            }
            assignments.append(assignment)

    return assignments

# Function to view assignments
def view_assignments():
    assignments = list_assignments()

    if assignments:
        # Create a new window for assignments
        assignments_window = ctk.CTkToplevel(window)
        assignments_window.title("Assignments")
        assignments_window.geometry("800x600")
       

        # Create labels and download buttons for each assignment
        for i, assignment in enumerate(assignments):
            assignment_label = ctk.CTkLabel(assignments_window, text=f"{i + 1}. {assignment['name']}", font=("Arial", 16))
            assignment_label.pack(pady=10)
            download_button = ctk.CTkButton(assignments_window, text="Download",
                                        command=lambda path=assignment['file_path']: download_assignment(path))
            download_button.pack()
    else:
        messagebox.showinfo("No Assignments", "There are no assignments available.")


# Function for My Timetable Page
def my_timetable_page():
    subprocess.run(['python','timetable.py'], check=True)

def view_admin_announcement():
    subprocess.run(['python', 'view_admin_announcement.py'], check=True)

def view_global_announcement():
    subprocess.run(['python', 'View Global Announcement.py'], check=True)

def open_announcement_options():
    announcement_options_window = ctk.CTkToplevel(master=window)
    announcement_options_window.title("Announcement Options")
    announcement_options_window.geometry("400x400")

    view_global_announcement_button = ctk.CTkButton(
        announcement_options_window,
        text="View Global Announcements",
        command=lambda: view_global_announcement(),
        font=("Arial", 16)
    )
    view_global_announcement_button.pack(pady=10)

    view_admin_announcement_button = ctk.CTkButton(
        announcement_options_window,
        text="View Admin Announcements",
        command=lambda: view_admin_announcement(),
        font=("Arial", 16)
    )
    view_admin_announcement_button.pack(pady=10)

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

# Create buttons for various options
announcements_button = ctk.CTkButton(window, text="Announcements", command=open_announcement_options,
                                     font=("Arial", 16))
announcements_button.pack(pady=30)

my_timetable_button = ctk.CTkButton(window, text="My Timetable", command=my_timetable_page,
                                    font=("Arial", 16))
my_timetable_button.pack(pady=30)

create_test_button = ctk.CTkButton(window, text="Create Test", command=create_test,
                                    font=("Arial", 16))
create_test_button.pack(pady=30)

assignments_button = ctk.CTkButton(window, text="Upload Assignments", command=upload_assignment,
                                    font=("Arial", 16))
assignments_button.pack(pady=30)

view_assignments_button = ctk.CTkButton(window, text="View Assignments", command=view_assignments,
                                    font=("Arial", 16))
view_assignments_button.pack(pady=30)


# Start the main event loop
window.mainloop()
