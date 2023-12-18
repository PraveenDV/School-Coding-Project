class Timetable:
    def __init__(self, days, periods):
        self.days = days
        self.periods = periods
        self.schedule = [[None for _ in range(periods)] for _ in range(days)]

    def add_class(self, day, period, class_name):
        if day < 1 or day > self.days or period < 1 or period > self.periods:
            print("Invalid day or period.")

        else:
            self.schedule[day-1][period-1] = class_name
            print(f"Class '{class_name}' added to {self.get_day_name(day)}, Period {period}.")

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
'''timetable.add_class(1, 1, "Math")
timetable.add_class(1, 3, "English")
timetable.add_class(2, 2, "Science")
timetable.add_class(3, 4, "History")'''

# Displaying the timetable
timetable.display_timetable()
