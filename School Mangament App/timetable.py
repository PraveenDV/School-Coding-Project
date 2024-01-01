import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, simpledialog
import sqlite3
import customtkinter as ctk

timetable_window = tk.Tk()
timetable_window.title("My Timetable")
timetable_window.geometry("800x600")
timetable_window.configure(bg="white")
timetable_window.grab_set()


class TimetableApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Timetable App")
            self.timetable_data = {}
            self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
            self.periods = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            self.subject_colors = {
                    "Maths": "#FF6AFF",
                    "Physics": "#00FFFF",
                    "Chemistry": "#00FF00",
                    "Biology": "#FFD700",  
                    "CS": "#FF1493"
                    #"English":"steelblue"
            }
            self.button_frame = tk.Frame(root)
            self.button_frame.pack(pady=10)
            self.add_button = tk.Button(self.button_frame, text="Add Entry", command=self.add_entry)
            self.add_button.pack(side=tk.LEFT, padx=10)
            self.edit_button = tk.Button(self.button_frame, text="Edit Entry", command=self.edit_entry)
            self.edit_button.pack(side=tk.LEFT, padx=10)
            self.display_button = tk.Button(self.button_frame, text="Display Timetable", command=self.display_timetable)
            self.display_button.pack(side=tk.LEFT, padx=10)
            self.timetable_frame = tk.Frame(root)
            self.timetable_frame.pack()
            for i, day in enumerate(self.days):
                tk.Label(self.timetable_frame, text=day.capitalize(), padx=10, pady=5, relief=tk.RIDGE, width=12).grid(row=0, column=i+1)
            for j, period in enumerate(self.periods):
                tk.Label(self.timetable_frame, text=period, padx=10, pady=5, relief=tk.RIDGE, width=6).grid(row=j+1, column=0)
            for i, day in enumerate(self.days):
                for j, period in enumerate(self.periods):
                    label = tk.Label(self.timetable_frame, textvariable=self.get_subject_var(day, period), padx=10, pady=5, relief=tk.RIDGE, width=12)
                    label.grid(row=j+1, column=i+1)
                    label.config(bg="spring green", fg="skyblue")

        def get_subject_var(self, day, period):
            return tk.StringVar(value=self.timetable_data.get(day, {}).get(period, "-----"))

        def add_entry(self):
            day = simpledialog.askstring("Add Entry", "Enter the day (1-6):")
            period = simpledialog.askstring("Add Entry", "Enter the period (1-9):")
            if day and period:
                subject = self.choose_subject()
                if subject is not None:
                    day = int(day) - 1
                    period = int(period) - 1
                    if 0 <= day < len(self.days) and 0 <= period < len(self.periods):
                        if self.days[day] not in self.timetable_data:
                            self.timetable_data[self.days[day]] = {}
                        self.timetable_data[self.days[day]][self.periods[period]] = subject
                        messagebox.showinfo("Success", "Entry added successfully!")
                        self.update_timetable()
                    else:
                        messagebox.showerror("Error", "Invalid day or period.")
            else:
                messagebox.showerror("Error", "All fields are required.")

        def choose_subject(self):
            subject_choice = tk.StringVar(value=list(self.subject_colors.keys())[0])
            subject_menu = tk.OptionMenu(self.root, subject_choice, *self.subject_colors.keys())
            subject_menu.pack()
            ok_button = tk.Button(self.root, text="OK", command=lambda: subject_menu.destroy())
            ok_button.pack()
            self.root.wait_window(subject_menu)
            subject = subject_choice.get()
            return subject

        def update_timetable(self):
            for i, day in enumerate(self.days):
                for j, period in enumerate(self.periods):
                    label = tk.Label(self.timetable_frame, textvariable=self.get_subject_var(day, period), padx=10, pady=5, relief=tk.RIDGE, width=12)
                    label.grid(row=j+1, column=i+1)
                    subject = self.timetable_data.get(day, {}).get(period, "-----")
                    label.config(bg=self.subject_colors.get(subject, "lightgray"), fg="white")

        def edit_entry(self):
            day = simpledialog.askstring("Edit Entry", "Enter the day (1-6):")
            period = simpledialog.askstring("Edit Entry", "Enter the period (1-9):")
            if day and period:
                day = int(day) - 1
                period = int(period) - 1
                if 0 <= day < len(self.days) and 0 <= period < len(self.periods):
                    if self.days[day] in self.timetable_data and self.periods[period] in self.timetable_data[self.days[day]]:
                        new_subject = self.choose_subject()
                        if new_subject is not None:
                            self.timetable_data[self.days[day]][self.periods[period]] = new_subject
                            messagebox.showinfo("Success", "Entry edited successfully!")
                            self.update_timetable()
                    else:
                        messagebox.showerror("Error", "Entry not found.")
                else:
                    messagebox.showerror("Error", "Invalid day or period.")
            else:
                messagebox.showerror("Error", "Day and period are required.")

        def display_timetable(self):
            if not self.timetable_data:
                messagebox.showinfo("Timetable", "No entries to display.")
            else:
                timetable_text = ""
                for day in self.days:
                    timetable_text += f"{day.capitalize()}:\n"
                    for period in self.periods:
                        subject = self.timetable_data.get(day, {}).get(period, "-----")
                        timetable_text += f"  {period} - {subject}\n"
                messagebox.showinfo("Timetable", timetable_text)

      
if __name__ == "__main__":
    app = TimetableApp(timetable_window) 
    timetable_window.mainloop()
