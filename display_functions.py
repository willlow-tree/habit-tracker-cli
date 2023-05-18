from datetime import *
import os
import prettytable as pt
from core_functions import check_habit_completion, check_habit_streak
import questionary


def display_all_currently_tracked_habits(habits):
    """Display all of the currently tracked habits, sorted by their period.
    Takes in the list of habit classes."""

    table = pt.PrettyTable([])
    column_day = []
    column_week = []
    for habit in habits:
        if habit.period == "day":
            column_day.append(habit.name)
        if habit.period == "week":
            column_week.append(habit.name)

    # Pad the missing entries for each column (the columns should have the same number of rows)
    if len(column_day) > len(column_week):
        for i in range(len(column_day) - len(column_week)):
            column_week.append("")
    elif len(column_week) > len(column_day):
        for i in range(len(column_week) - len(column_day)):
            column_day.append("")

    table.add_column("Daily", column_day)
    table.add_column("Weekly", column_week)

    print(table)
    input()


def display_habit_menu(h_name, habits, history):
    """Display specific habit info - name, period, current streak, longest streak, date of creation and descripton (if there is one).
    Takes in the habit name (string), list of habit classes, and history dict."""

    field_names = [
        "Name",
        "Period",
        "Current streak",
        "Longest streak",
        "Date of creation",
    ]
    table = pt.PrettyTable(field_names)

    for habit in habits:
        if habit.name == h_name:
            # Getting habit's current and longest streak
            (curr_streak, longest_streak) = check_habit_streak(
                habit, history, time=datetime.now()
            )
            # Create a row for the table
            row = [
                habit.name,
                "{} per {}".format(habit.times_per_period, habit.period),
                curr_streak,
                longest_streak,
                datetime.strftime(habit.creation_date, "%a %d %b"),
            ]
            table.add_row(row)
            print(table)
            # Add description if it exists
            if habit.description is not None:
                print("Description:")
                print(habit.description)
            input()


def display_statistcs(habits, history):
    """Displays percentage of periods completed for each habit.
    ex: if daily habit exists for 10 days, and is marked complete for 8 of them, completion percentage = 80%.
    Takes in a list of habit classes and a history dict.
    """

    table = pt.PrettyTable([])

    # Get a list of dates to check
    delta_day = timedelta(days=1)
    start_date = datetime.max
    # Starting from the date of creation of earliest habit to the current day
    for habit in habits:
        if habit.creation_date <= start_date:
            start_date = habit.creation_date
    end_date = datetime.now()
    iter_date = start_date

    dates = []
    # Not including the current day and the current week (gives user time to complete the habit for today or this week)
    while iter_date < end_date:
        dates.append(iter_date)
        iter_date += delta_day

    if dates == []:
        print("Not enough data to display yet")
        return

    habit_data_completed = {}  # A dict of how many times a habit was marked complete
    habit_num_of_periods = {}  # A dict contaning the number of periods the habit should be marked complete
    habit_completion_percentage = {} # A dict containing the percentage of marked periods/should be marked periods
    column_habits = [] # List of habit names

    for habit in habits:
        column_habits.append(habit.name)
        habit_num_of_periods[habit.name] = 0
        habit_data_completed[habit.name] = 0
        habit_completion_percentage[habit.name] = 0

    # Adding list of habit names to the table
    table.add_column("Habits", column_habits)

    for date in dates:
        for habit in habits:
            if habit.period == "day":
                if date >= habit.creation_date:
                    goal_reached = check_habit_completion(habit, history, datetime.combine(date, datetime.min.time()))[1]
                    habit_num_of_periods[habit.name] += 1
                    if goal_reached:
                        habit_data_completed[habit.name] += 1
            if habit.period == 'week':
                if date.isocalendar()[2] == 7:
                    if date >= habit.creation_date:
                        goal_reached = check_habit_completion(habit, history, datetime.combine(date, datetime.min.time()))[1]
                        habit_num_of_periods[habit.name] += 1
                        if goal_reached:
                            habit_data_completed[habit.name] += 1

    column_habit_comp_percentage = []

    for habit in habits:
        habit_completion_percentage[habit.name] = int(
            round((habit_data_completed[habit.name] / habit_num_of_periods[habit.name]), 2,) * 100)
        
        if habit.period == 'day':
            period = 'days'
        else:
            period = 'weeks'

        column_habit_comp_percentage.append(
            str(habit_completion_percentage[habit.name])
            + " %"
            + "  of {} {}".format(habit_num_of_periods[habit.name], period)
        )

    table.add_column("Percentage completed", column_habit_comp_percentage)

    # Column containing the longest streak for each habit
    column_longest_streak = []
    for h_name in column_habits:
        for habit in habits:
            if h_name == habit.name:
                longest_streak = check_habit_streak(habit, history)[1]
                column_longest_streak.append(longest_streak)

    table.add_column("Longest streak", column_longest_streak)

    print(table)
    input()


def display_weekly_calendar(habits, history, time=datetime.now()):
    """Prints a table of tracked daily and weekly habits, their completion status, and current streak. Takes in a list of habit classes and a history dict."""
    os.system("clear")
    
    table = pt.PrettyTable([])

    # DATES COLUMN
    time_date = time.date()
    delta_day = timedelta(days=1)
    monday = time_date - delta_day * (time_date.isocalendar()[2] - 1)
    iter_day = monday

    dates_of_the_week = []

    for i in range(7):
        dates_of_the_week.append(iter_day)
        iter_day += delta_day

    t_format = "%a %d %b"

    # Dates column
    table_col_dates = []
    for date in dates_of_the_week:
        entry_date = datetime.strftime(date, t_format)
        if date == datetime.now().date():
            entry_date = ">> " + entry_date
        table_col_dates.append(entry_date)

    table.add_column("Date:", table_col_dates, align="r")

    # Daily habits column
    table_col_daily_h = [] # list of names for daily habits
    table_col_daily_completion = [] # list of how many times each habit was completed and completion check mark
    table_col_daily_streak = [] # list of streaks for daily habtis

    for date in dates_of_the_week:
        entry_daily_h = "" # singular habit name
        entry_daily_completion = "" # how many times was this habit completed and check mark
        entry_daily_streak = "" # streak for the habit
        if date <= datetime.now().date(): # only show entries if it is the current day or previous days
            for habit in habits:
                if habit.period == "day":
                    if habit.creation_date <= datetime.combine( # only show habit after it's creation day
                        date, datetime.max.time()
                    ):
                        # Habit name
                        entry_daily_h += "{} \n".format(habit.name)
                        # Habit completion
                        times_completed_day, goal_reached = check_habit_completion(
                            habit,
                            history,
                            datetime.combine(
                                date, datetime.max.time()
                            ),
                        )
                        # Completion mark
                        if goal_reached:
                            mark = "v"
                        else:
                            mark = "x"
                        entry_daily_completion += "{}/{} {} \n".format(
                            times_completed_day, habit.times_per_period, mark
                        )
                        # Habit streak
                        streak = check_habit_streak(
                            habit,
                            history,
                            time=datetime.combine(
                                date, datetime.max.time()
                            ),
                        )[0] 
                        entry_daily_streak += "{} \n".format(streak)

        # Appending entries to the list
        table_col_daily_h.append(entry_daily_h)
        table_col_daily_completion.append(entry_daily_completion)
        table_col_daily_streak.append(entry_daily_streak)

    # Appending lists to the table
    table.add_column("Daily:", table_col_daily_h)
    table.add_column("-", table_col_daily_completion)
    table.add_column("Streak: ", table_col_daily_streak)

    # Week column
    table_col_weekly_h = [] 
    table_col_weekly_completion = [] 
    table_col_weekly_streak = [] 

    for date in dates_of_the_week:
        entry_weekly_h = ""
        entry_weekly_completion = ""
        entry_weekly_streak = ""
        if date <= datetime.now().date(): 
            for habit in habits:
                if habit.period == "week":
                    date_todatetime = datetime.combine(
                        date, datetime.max.time()
                    )
                    if habit.creation_date <= date_todatetime:
                        times_completed_day = check_habit_completion(
                            habit, history, date_todatetime, "day"
                        )[0]
                        times_completed_week, goal_reached = check_habit_completion(
                            habit, history, date_todatetime, upto=date_todatetime
                        )

                        streak = check_habit_streak(
                            habit, history, time=date_todatetime
                        )[0]

                        # Display weekly habit if:
                        # 1) it was marked complete this day
                        # 2) it is today and the habit was not completed enough times this week
                        # 3) it was not completed enough times this week and its sunday (for checking previous weeks)
                        if (
                            times_completed_day >= 1
                            or (
                                datetime.now().date() == date
                                and times_completed_week < habit.times_per_period
                            )
                            or (date.isocalendar()[2] == 7 and goal_reached == False)
                        ):
                            # Habit name
                            entry_weekly_h += "{} \n".format(habit.name)

                            # Completion mark
                            if goal_reached:
                                mark = "v"
                            else:
                                mark = "x"

                            # Habit completion
                            entry_weekly_completion += "{}/{} {} \n".format(
                                times_completed_week, habit.times_per_period, mark
                            )

                            #Habit streak
                            entry_weekly_streak += "{} \n".format(streak)

        # Appending entries to the list
        table_col_weekly_h.append(entry_weekly_h)
        table_col_weekly_completion.append(entry_weekly_completion)
        table_col_weekly_streak.append(entry_weekly_streak)

    # Appending lists to the table
    table.add_column("Weekly:", table_col_weekly_h)
    table.add_column("--", table_col_weekly_completion)
    table.add_column("Streak:", table_col_weekly_streak)

    print(table)

    # Allows to scroll through previous weeks

    choices = ["previous week", "next week", "go back to options"]
    choice = questionary.select("", choices).ask()
    if choice == choices[0]:
        display_weekly_calendar(habits, history, time - timedelta(days=7))
    if choice == choices[1]:
        display_weekly_calendar(habits, history, time + timedelta(days=7))
    if choice == choices[2]:
        return


def create_questionary_style():
    """Creates custom style for user prompts using questionary module"""
    custom_style = questionary.Style([
        ('qmark', 'fg:#2a32cb bold'),       # token in front of the question
        ('question', 'bold'),               # question text
        ('answer', 'fg:#2a32cb bold'),      # submitted answer text behind the question
        ('pointer', 'fg:#2a32cb bold'),     # pointer used in select and checkbox prompts
        ('highlighted', 'fg:#2a32cb bold'), # pointed-at choice in select and checkbox prompts
        ('selected', 'fg:#2a32cb'),         # style for a selected item of a checkbox
        ('separator', 'fg:#2a32cb'),        # separator in lists
        ('instruction', ''),                # user instructions for select, rawselect, checkbox
        ('text', ''),                       # plain text
        ('disabled', 'fg:#2a32cb italic')   # disabled choices for select and checkbox prompts
    ])
    return custom_style