
import tkinter as tk
from tkinter import messagebox, filedialog
import os
import shutil
import csv



# Sample assignment data    
assignments = [
    {"name": "Assignment 1", "file_path": "assignment1.pdf"},
    {"name": "Assignment 2", "file_path": "assignment2.png"},
]

# Function to show a "Feature coming soon" message
def feature_coming_soon():
    messagebox.showinfo("Feature Coming Soon", "This feature is coming soon.")

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
        assignments_window = tk.Toplevel(student_window)
        assignments_window.title("Assignments")
        assignments_window.geometry("800x600")
        assignments_window.configure(bg="light blue")

        # Create labels and download buttons for each assignment
        for i, assignment in enumerate(assignments):
            assignment_label = tk.Label(assignments_window, text=f"{i + 1}. {assignment['name']}", font=(font1, 16))
            assignment_label.pack(pady=10)
            download_button = tk.Button(assignments_window, text="Download",
                                        command=lambda path=assignment['file_path']: download_assignment(path))
            download_button.pack()
    else:
        messagebox.showinfo("No Assignments", "There are no assignments available.")

# Create buttons for the student profile
announcements_button = tk.Button(student_window, text="Announcements", command=feature_coming_soon,
                                bg="red2", fg="white", font=(font, 16))

# Create a new button for Assignments
assignments_button = tk.Button(student_window, tex bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

=============== RESTART: D:\School Mangament App\Student_main.py ==============t="Assignments", command=view_assignments,
                               bg="dodger blue", fg="white", font=(font, 16))

timetable_button = tk.Button(student_window, text="My Class Timetable", command=feature_coming_soon,
                             bg="green4", fg="white", font=(font1, 16))

grade_button = tk.Button(student_window, text="Check My Grade", command=feature_coming_soon,
                         bg="dark orchid", fg="white", font=(font1, 16))

# Place the buttons in the window
announcements_button.pack(pady=20)
assignments_button.pack(pady=20)
timetable_button.pack(pady=20)
grade_button.pack(pady=20)

# Create a profile button in the top right corner
profile_button = tk.Button(student_window, text="Profile", command=feature_coming_soon,
                           bg="hot pink", fg="white", font=(font1, 12))
profile_button.place(relx=0.9, rely=0.05, anchor="ne")

# Start the student profile main event loop
student_window.mainloop()
