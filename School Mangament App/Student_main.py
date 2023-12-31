
import tkinter as tk
from tkinter import messagebox, filedialog
import os
import shutil
import csv
import customtkinter as ctk
import subprocess

font="Arial"

ctk.set_appearance_mode('System')

student_window = ctk.CTk()
student_window.title("Student Main Page")
student_window.geometry("600x600")
student_window.grab_set()
student_window.configure(bg="light blue")

# Function for Student's Announcement Page
def student_announcement_page():
    announcement_window = ctk.CTkToplevel(student_window)
    announcement_window.title("Student's Announcements")
    announcement_window.geometry("800x600")
    announcement_window.configure(bg="light blue")
    announcement_window.grab_set()

    ctk.CTkLabel(announcement_window, text="Announcements", font=("Arial", 18)).pack(pady=10)

    global_announcements_button = ctk.CTkButton(announcement_window, text="Global Announcements",
                                        command=lambda:subprocess.run(['python', 'View Global Announcement.py']),
                                          font=("Arial", 16))
    global_announcements_button.pack(pady=20)

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
        assignments_window = ctk.CTkToplevel(student_window)
        assignments_window.title("Assignments")
        assignments_window.geometry("800x600")
       

        # Create labels and download buttons for each assignment
        for i, assignment in enumerate(assignments):
            assignment_label = ctk.CTkLabel(assignments_window, text=f"{i + 1}. {assignment['name']}", font=(font, 16))
            assignment_label.pack(pady=10)
            download_button = ctk.CTkButton(assignments_window, text="Download",
                                        command=lambda path=assignment['file_path']: download_assignment(path))
            download_button.pack()
    else:
        messagebox.showinfo("No Assignments", "There are no assignments available.")

# Create buttons for the student profile
announcements_button = ctk.CTkButton(student_window, text="Announcements", command=student_announcement_page,
                                  font=(font, 16))

# Create a new button for Assignments
assignments_button = ctk.CTkButton(student_window,
text="Assignments", command=view_assignments,
                                 font=(font, 16))

timetable_button = ctk.CTkButton(student_window, text="My Class Timetable", command=lambda:subprocess.run(['python', 'timetable.py'], check=True),
                               font=(font, 16))

# Place the buttons in the window
announcements_button.pack(pady=20)
assignments_button.pack(pady=20)
timetable_button.pack(pady=20)

# Start the student profile main event loop
student_window.mainloop()
