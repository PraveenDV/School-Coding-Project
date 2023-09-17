import tkinter as tk
from tkinter import *
from tkinter import messagebox, simpledialog

neon_bg_color="#f2ea09"

def show_student_dashboard():

    def display_timetable():
        
        timetable_window = tk.Tk()
        timetable_window.title("My Timetable")
        timetable_window.geometry("800x600")
        timetable_window.configure(bg="white")
        #timetable_window.grab_set()
    
    main_window = tk.Tk()
    main_window.title("Student Dashboard")
    main_window.geometry("800x600")
    main_window.configure(bg=neon_bg_color)

    tk.Label(main_window, text="Welcome, Student!", font=("Arial", 18), bg=neon_bg_color).pack(pady=10)

    # Buttons for student-specific features
    my_timetable_button = tk.Button(main_window, text="My Timetable", command=lambda: display_timetable(),#messagebox.showinfo("My Timetable", "Your timetable will be available soon."),
                                    bg="purple", fg="white", font=("Arial", 16))
    my_timetable_button.pack(pady=20)

    class_timetable_button = tk.Button(main_window, text="Class Timetable", command=lambda: messagebox.showinfo("Class Timetable", "Class timetable will be available soon."),
                                       bg="green", fg="white", font=("Arial", 16))
    class_timetable_button.pack(pady=20)

    check_grades_button = tk.Button(main_window, text="Check Student Grades", command=lambda: messagebox.showinfo("Check Student Grades", "Check grades here."),
                                    bg="purple", fg="white", font=("Arial", 16))
    check_grades_button.pack(pady=20)

    announcements_button = tk.Button(main_window, text="Announcements", command=lambda: messagebox.showinfo("Announcements", "No announcements at the moment."),
                                     bg="green", fg="white", font=("Arial", 16))
    announcements_button.pack(pady=20)
    
    main_window.mainloop()

    

show_student_dashboard()
