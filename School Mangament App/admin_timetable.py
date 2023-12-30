'''import customtkinter as ctk

#Class for timetable 
class Timetable:
    def __init__(self, days, periods, subject):
        self.days = days
        self.periods = periods
        self.subject=subject
        #self.schedule = [[None for _ in range(periods)] for _ in range(days)]

    def add_class(self, day, period, subject):
        if day < 1 or day > self.days or period < 1 or period > self.periods or self.subject=="":
            print("Invalid day or period or enter subject.")

        else:
            self.schedule[day-1][period-1] = class_name
            print(f"Class '{class_name}' added to {self.get_day_name(day)}, Period {period}.")
            day=ctk.CTkInputDialog(text="Enter day")
            period=ctk.CTkInputDialog(text="Enter number of periods")
            subject=ctk.CTkInputDialog(text="Enter subject")

    def get_day_name(self, day):
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        return days_of_week[day-1]

    def display_timetable(self):
        print("Timetable:")
        for day in range(self.days):
            print(f"\n{self.get_day_name(day + 1)}:")
            for period in range(self.periods):
                class_name = self.schedule[day][period]
                print(f"  Period {period + 1}: {class_name if class_name else 'Free'}")

# Example usage:
days_of_week = 6  # Monday to Saturday
class_periods = 8  

timetable = Timetable(days_of_week, class_periods)

# Adding classes to the timetable
timetable.add_class(1, 1, "Math")
timetable.add_class(1, 3, "English")
timetable.add_class(2, 2, "Science")
timetable.add_class(3, 4, "History")

# Displaying the timetable
timetable.display_timetable()


#Code for displaying the timetable page
timetable_window = ctk.CTk()
timetable_window.title("Timetable")
timetable_window.geometry("800x600")
#timetable_window.configure()
timetable_window.grab_set()
ctk.set_appearance_mode("System") 

create_tt_btn=ctk.CTkButton(timetable_window, width='30px', height='30px', corner_radius=3)
create_tt_btn.pack()

timetable_window.mainloop()


import customtkinter as ctk

# Class for timetable
class Timetable:
    def __init__(self, days, periods):
        self.days = days
        self.periods = periods
        self.schedule = [[None for _ in range(periods)] for _ in range(days)]

    def add_class(self, day, period, subject):
        if day < 1 or day > self.days or period < 1 or period > self.periods or subject == "":
            print("Invalid day, period, or subject.")
        else:
            self.schedule[day - 1][period - 1] = subject
            print(f"Class '{subject}' added to {self.get_day_name(day)}, Period {period}.")

    def get_day_name(self, day):
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        return days_of_week[day - 1]

    def display_timetable(self):
        print("Timetable:")
        for day in range(self.days):
            print(f"\n{self.get_day_name(day + 1)}:")
            for period in range(self.periods):
                subject = self.schedule[day][period]
                print(f"  Period {period + 1}: {subject if subject else 'Free'}")

# Example usage:
days_of_week = 6  # Monday to Saturday
class_periods = 8

timetable = Timetable(days_of_week, class_periods)

# Adding classes to the timetable
timetable.add_class(1, 1, "Math")
timetable.add_class(1, 3, "English")
timetable.add_class(2, 2, "Science")
timetable.add_class(3, 4, "History")

# Displaying the timetable
timetable.display_timetable()

# Code for displaying the timetable page
timetable_window = ctk.CTk()
timetable_window.title("Timetable")
timetable_window.geometry("800x600")
timetable_window.grab_set()
ctk.set_appearance_mode("System")

create_tt_btn = ctk.CTkButton(timetable_window, text="Create Timetable", command=timetable.display_timetable)
create_tt_btn.pack()

timetable_window.mainloop()'''


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

days = 6
periods = 9
recess_break_aft = 5 # recess after 5th Period
fini = None
butt_grid = []


period_names = list(map(lambda x: 'Period ' + str(x), range(1, 9+1)))
day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
teacher_name=""


'''def select_fac():
    global fini
    fini = str(combo1.get())
    print(fini)
    update_table(fini)'''

def process_button(d, p):
    details = tk.Tk()
    tk.Label(details, text="Enter teacher name: ", 
                        font=('Consolas', 12, 'bold')).pack(side=tk.LEFT)
    teach_name=tk.Text(details).pack(tk.LEFT)
    text_val=teach_name.get()
    teacher_name=text_val
    tk.Button(
        details,
        text="OK",
        font=('Consolas'),
        width=10,
        command=details.destroy
    ).pack(pady=10)

    details.mainloop()

    '''print(d, p, fini)
    
    cursor = conn.execute(f"SELECT SECTION, SUBCODE FROM SCHEDULE\
                WHERE DAYID={d} AND PERIODID={p} AND FINI='{fini}'")
    cursor = list(cursor)
    print("section", cursor)
    if len(cursor) != 0:
        sec_li = [x[0] for x in cursor]
        t = ', '.join(sec_li)
        subcode = cursor[0][1]
        cur1 = conn.execute(f"SELECT SUBNAME, SUBTYPE FROM SUBJECTS\
            WHERE SUBCODE='{subcode}'")
        cur1 = list(cur1)
        subname = str(cur1[0][0])
        subtype = str(cur1[0][1])

        if subtype == 'T':
            subtype = 'Theory'
        elif subtype == 'P':
            subtype = 'Practical'

    #     print(subcode, fini, subname, subtype, fname, femail)
    else:
        sec_li = subcode = subname = subtype = t = 'None'

    tk.Label(details, text='Class Details', font=('Consolas', 15, 'bold')).pack(pady=15)
    tk.Label(details, text='Day: '+day_names[d], font=('Consolas'), anchor="w").pack(expand=1, fill=tk.X, padx=20)
    tk.Label(details, text='Period: '+str(p+1), font=('Consolas'), anchor="w").pack(expand=1, fill=tk.X, padx=20)
    tk.Label(details, text='Subject Code: '+subcode, font=('Consolas'), anchor="w").pack(expand=1, fill=tk.X, padx=20)
    tk.Label(details, text='Subect Name: '+subname, font=('Consolas'), anchor="w").pack(expand=1, fill=tk.X, padx=20)
    tk.Label(details, text='Subject Type: '+subtype, font=('Consolas'), anchor="w").pack(expand=1, fill=tk.X, padx=20)
    tk.Label(details, text='Faculty Initials: '+fini, font=('Consolas'), anchor="w").pack(expand=1, fill=tk.X, padx=20)
    tk.Label(details, text='Sections: '+t, font=('Consolas'), anchor="w").pack(expand=1, fill=tk.X, padx=20)'''

for i in range(days):
        for j in range(periods):
            get teacher_name
             update_table(j,teacher_name)


def update_table(fini):
    
            '''cursor = conn.execute(f"SELECT SECTION, SUBCODE FROM SCHEDULE\
                WHERE DAYID={i} AND PERIODID={j} AND FINI='{fini}'")
            cursor = list(cursor)
            print(cursor)'''
            
            butt_grid[i][j]['bg'] = 'white'
            butt_grid[i][j]['text'] = teacher_name
            '''if len(cursor) != 0:
                subcode = cursor[0][1]
                cur1 = conn.execute(F"SELECT SUBTYPE FROM SUBJECTS WHERE SUBCODE='{subcode}'")
                cur1 = list(cur1)
                subtype = cur1[0][0]
                butt_grid[i][j]['fg'] = 'white'
                if subtype == 'T':
                    butt_grid[i][j]['bg'] = 'green'
                elif subtype == 'P':
                    butt_grid[i][j]['bg'] = 'blue'

                sec_li = [x[0] for x in cursor]
                t = ', '.join(sec_li)
                butt_grid[i][j]['text'] = "Sections: " + t
                print(i, j, cursor[0][0])
            else:'''
            #butt_grid[i][j]['fg'] = 'black'
            #butt_grid[i][j]['text'] = "No Class"
            #butt_grid[i][j].update()




                            
    



def fac_tt_frame(tt, f):
    title_lab = tk.Label(
        tt,
        text='T  I  M  E  T  A  B  L  E',
        font=('Consolas', 20, 'bold'),
        pady=5
    )
    title_lab.pack()

    legend_f = tk.Frame(tt)
    legend_f.pack(pady=15)
    tk.Label(
        legend_f,
        text='Legend: ',
        font=('Consolas', 10, 'italic')
    ).pack(side=tk.LEFT)

    tk.Label(
        legend_f,
        text='Theory Classes',
        bg='green',
        fg='white',
        relief='raised',
        font=('Consolas', 10, 'italic'),
        height=2
    ).pack(side=tk.LEFT, padx=10)

    tk.Label(
        legend_f,
        text='Practical Classes',
        bg='blue',
        fg='white',
        relief='raised',
        font=('Consolas', 10, 'italic'),
        height=2
    ).pack(side=tk.LEFT, padx=10)

    global butt_grid
    global fini
    fini = f

    table = tk.Frame(tt)
    table.pack()

    first_half = tk.Frame(table)
    first_half.pack(side='left')

    recess_frame = tk.Frame(table)
    recess_frame.pack(side='left')

    second_half = tk.Frame(table)
    second_half.pack(side='left')

    recess = tk.Label(
        recess_frame,
        text='R\n\nE\n\nC\n\nE\n\nS\n\nS',
        font=('Consolas', 18, 'italic'),
        width=3,
        relief='sunken'
    )
    recess.pack()

    for i in range(days):
        b = tk.Label(
            first_half,
            text=day_names[i],
            font=('Consolas', 12, 'bold'),
            width=9,
            height=2,
            bd=5,
            relief='raised'
        )
        b.grid(row=i+1, column=0)

    for i in range(periods):
        if i < recess_break_aft:
            b = tk.Label(first_half)
            b.grid(row=0, column=i+1)
        else:
            b = tk.Label(second_half)
            b.grid(row=0, column=i)

        b.config(
            text=period_names[i],
            font=('Consolas', 12, 'bold'),
            width=9,
            height=1,
            bd=5,
            relief='raised'
        )

    for i in range(days):
        b = []
        for j in range(periods):
            if j < recess_break_aft:
                bb = tk.Button(first_half)
                bb.grid(row=i+1, column=j+1)
            else:
                bb = tk.Button(second_half)
                bb.grid(row=i+1, column=j)

            bb.config(
                text='Hello World!',
                font=('Consolas', 10),
                width=13,
                height=3,
                bd=5,
                relief='raised',
                wraplength=80,
                justify='center',
                command=lambda x=i, y=j: process_button(x, y)
            )
            b.append(bb)

        butt_grid.append(b)
        # print(b)
        b = []

    print(butt_grid[0][1], butt_grid[1][1])
    update_table(fini)



conn = sqlite3.connect(r'timetable.db')
if __name__ == "__main__":
    
    # connecting database

    tt = tk.Tk()
    tt.title('Teacher Timetable')

    fac_tt_frame(tt, fini)

    fac_select_f = tk.Frame(tt, pady=15)
    fac_select_f.pack()

    tk.Label(
        fac_select_f,
        text='Select Faculty:  ',
        font=('Consolas', 12, 'bold')
    ).pack(side=tk.LEFT)

    cursor = conn.execute("SELECT DISTINCT INI FROM FACULTY")
    fac_li = [row[0] for row in cursor]
    print(fac_li)
    combo1 = ttk.Combobox(
        fac_select_f,
        values=fac_li,
    )
    combo1.pack(side=tk.LEFT)
    combo1.current(0)

    b = tk.Button(
        fac_select_f,
        text="OK",
        font=('Consolas', 12, 'bold'),
        padx=10,
       #command=select_fac
    )
    b.pack(side=tk.LEFT, padx=10)
    b.invoke()


    tt.mainloop()
