import tkinter as tk
from tkinter import *
from tkinter import messagebox, simpledialog
import pandas as pd
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

ancmt_screen_btn=Button(admin_window, text="Make Announcements", bg="white", command=lambda:make_announcements_screen(), pady=10)
ancmt_screen_btn.pack()

admin_window.mainloop()
