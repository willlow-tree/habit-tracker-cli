import os
import sqlite3
import display_functions
import database_interaction
import questionary

app_open = True
history = {}
habits = []

# Questionary style 
custom_style = display_functions.create_questionary_style()

os.system("clear")

# Connecting to database
db = sqlite3.connect("database.db")
cursor = db.cursor()

# Loading History & Habits
database_interaction.load_habits(habits, cursor)
database_interaction.load_history(history, cursor)

display_functions.display_weekly_calendar(habits, history)

while app_open:
    # Options for the menu
    choices = [
        "display weekly calendar",
        "mark habit complete",
        "unmark habit",
        "list all currently tracked habits",
        "create habit",
        "delete habit",
        "display specific habit menu",
        "display my statistcs",
        "quit",
    ]

    choice = questionary.select("Select action", choices, style=custom_style).ask()
    if choice == "display weekly calendar":
        display_functions.display_weekly_calendar(habits, history)
        os.system("clear")

    if choice == "mark habit complete":
        print("Enter habit name:")
        habit_choices = [habit.name for habit in habits]
        if habit_choices == []:
            print("No habits found")
            input()
        else:
            habit_choices.append("go back")
            chosen_habit = questionary.select(
                "Choose habit to mark complete:", habit_choices, style=custom_style
            ).ask()
            if chosen_habit != "go back":
                database_interaction.mark_habit_complete(
                    chosen_habit, habits, cursor, db
                )
        os.system("clear")

    if choice == "unmark habit":
        print("Enter habit name:")
        habit_choices = [habit.name for habit in habits]
        if habits == []:
            print("No habits found")
            input()
        else:
            habit_choices.append("go back")
            chosen_habit = questionary.select(
                "Choose habit to unmark:", habit_choices, style=custom_style
            ).ask()
            if chosen_habit != "go back":
                database_interaction.unmark_habit_complete(
                    chosen_habit, habits, cursor, db
                )
        os.system("clear")

    if choice == "list all currently tracked habits":
        if habits == []:
            print("No habits found")
            input()
        else:
            display_functions.display_all_currently_tracked_habits(habits)
            os.system("clear")

    if choice == "create habit":
        database_interaction.create_new_habit(habits, cursor, db)
        os.system("clear")

    if choice == "delete habit":
        habit_choices = [habit.name for habit in habits]
        if habit_choices == []:
            print("No habits found")
            input()
        else:
            chosen_habit = questionary.select(
                "Choose habit to mark complete:", habit_choices, style=custom_style
            ).ask()
            answer = questionary.confirm(
                "Are you sure want to delete {}?".format(chosen_habit), style=custom_style
            ).ask()
            if answer:
                database_interaction.delete_habit(chosen_habit, habits, cursor, db)
        os.system("clear")

    if choice == "display specific habit menu":
        habit_choices = [habit.name for habit in habits]
        if habit_choices == []:
            print("No habits found")
            input()
        else:
            chosen_habit = questionary.select(
                "Choose habit to display:", habit_choices, style= custom_style
            ).ask()
            display_functions.display_habit_menu(chosen_habit, habits, history)

        os.system("clear")

    if choice == "display my statistcs":
        if habits == []:
            print("No habits found")
            input()
            os.system("clear")
        else:
            display_functions.display_statistcs(habits, history)

            os.system("clear")

    if choice == "quit":
        os.system("clear")
        quit()

    # Update history & habtis
    database_interaction.load_habits(habits, cursor)
    database_interaction.load_history(history, cursor)
    os.system("clear")