import tkinter as tk
from tkinter import *
from tkinter import messagebox, simpledialog
#import pandas as pd
from datetime import date
from csv import *
bg_clr="#f2ea09"

admin_window=tk.Tk()
admin_window.title("Admin Page")
admin_window.geometry("800x400")
admin_window.configure(background=bg_clr)


def make_announcements_screen():

        announcement_screen=tk.Toplevel()
        announcement_screen.title("Announce")
        announcement_screen.geometry("400x400")
        announcement_screen.grab_set()
        h1=Label(announcement_screen, text="Make Announcement")
        announcement=Text(announcement_screen, height=50, width=50)

        def get_date():
                today=date.today()

        #Retrieving the announcement and saving it into a csv file
        def save_announcement():
                ancmt_list=[]
                ancmt1=announcement.get('1.0', 'end-1c')
                ancmt_list.append(ancmt1)
                with open("data_files/admin_announcements.csv", 'w') as file:
                        Writer=writer(file)
                        Writer.writerow(["Announcements"])
                        Writer.writerow(ancmt_list)
                        print("announcement made")
        ancmt_btn=Button(announcement_screen, text="Make Announcement", bg="white",command=lambda:(save_announcement(),
                        announcement_screen.quit()))
        h1.pack()
        ancmt_btn.pack(side="bottom")
        announcement.pack() 



ancmt_screen_btn=Button(admin_window, text="Make Announcements", bg="white", command=lambda:make_announcements_screen())
ancmt_screen_btn.pack(pady=20)

timetable_btn=Button(admin_window, text="Timetable", bg="white")
timetable_btn.pack(pady=20)

teacher_entry_btn = tk.Button(admin_window, text="Add Teachers",
                 bg="white")
#teacher_entry_btn.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
teacher_entry_btn.pack(pady=20)

student_entry_btn = tk.Button(admin_window, text="Add Students",
                     bg="white")
#student_entry_btn.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
student_entry_btn.pack(pady=20)

profile_btn = tk.Button(admin_window, text="Profile", bg="white")
profile_btn.place(relx=0.9, rely=0.05, anchor="ne")
profile_btn.pack(pady=20)


admin_window.mainloop()
