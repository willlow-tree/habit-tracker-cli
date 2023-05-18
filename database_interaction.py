import datetime
from classes import Habit


def load_habits(habits, cursor):
    """Loads/Updates habits list from the database."""
    habits.clear()
    cursor.execute("SELECT * FROM Habits;")
    t_format = "%Y-%m-%d %H:%M:%S.%f"
    for habit in cursor:
        habits.append(
            Habit(
                habit[0],
                habit[1],
                habit[2],
                habit[3],
                datetime.datetime.strptime(habit[4], t_format),
            )
        )


def load_history(history, cursor):
    """Loads/Updates history from the database"""
    history.clear()
    t_format = "%Y-%m-%d %H:%M:%S.%f"
    cursor.execute("SELECT * FROM History;")
    for log in cursor:
        date = datetime.datetime.strptime(log[0], t_format)
        history[date] = log[1]


def mark_habit_complete(h_name, habits, cursor, db, time=None):
    """Inserts into a database a pair of values for habit name and time of completion.
    Optionally you can provide a time, by default it is the current time"""
    if time == None:
        time = datetime.datetime.now()

    for habit in habits:
        if habit.name == h_name:
            cursor.execute("INSERT INTO History VALUES (?, ?);", (time, habit.name))
            db.commit()
            string =  "\n- Marked complete {}".format(h_name)
            print(string)
            input()
            return
    print("Habit not found")


def unmark_habit_complete(h_name, habits, cursor, db, time=None):
    """Deletes habit completion entry from the database for the given date (current day by default)"""
    if time == None:
        time = datetime.datetime.now()

    for habit in habits:
        if habit.name == h_name:
            timelog_like = "{}%".format(datetime.datetime.strftime(time, "%Y-%m-%d"))
            cursor.execute(
                "SELECT * FROM History WHERE habit_name == ? and timelog LIKE ? ORDER BY timelog DESC LIMIT(1);",
                (h_name, timelog_like),
            )
            select = cursor.fetchall()
            if select == []:
                print("Habit was not marked complete today")
                input()
            else:
                cursor.execute(
                    "DELETE FROM History WHERE habit_name == ? and timelog LIKE ? ORDER BY timelog DESC LIMIT(1);",
                    (h_name, timelog_like),
                )
                db.commit()
                string = "\n- Unmarked {}".format(h_name)
                print(string)
                input()
                return
    print("Habit not found")


def create_new_habit(habits, cursor, db, time=datetime.datetime.now()):
    """Creates new habit in the database using user prompts. The user chooses habit name,
    perod, how many times per period it should be completed, and can optionally provide description."""
    # INPUT
    print("q - go back")
    print("Enter habit name:")
    inp = input().strip()
    if inp == "q":
        return
    for habit in habits:
        if inp == habit.name:
            print("Habit with the same name already exists")
            return
    h_name = inp

    print("Enter habit description: \n Leave blank for no description")
    h_description = input().strip()
    if h_description == "":
        h_description = None
    if len(h_description) > 100:
        print("The maximum length of habit description is 100 characters.")
        return

    print("Enter habit period: \n 'day','week'")
    h_period = input().strip()
    if h_period != "day" and h_period != "week":
        print("Wrong period format")
        return

    print("How many times per period should the habit be compelted?")
    try:
        times_per_period = int(input().strip())
        if times_per_period <= 0 or times_per_period > 5:
            print("Value should be between 1 and 5")
            return
    except ValueError:
        print("Wrong format")
        return

    cursor.execute(
        "INSERT INTO Habits (habit_name, habit_description, habit_period, times_per_period, habit_creation_date) VALUES (?, ?, ?, ?, ?);",
        (h_name, h_description, h_period, times_per_period, time),
    )
    db.commit()
    print("Habit successfully added.")


def delete_habit(h_name, habits, cursor, db):
    """Deletes habit from the database, along with all the recorded completion entries for this habit."""
    for habit in habits:
        if h_name == habit.name:
            cursor.execute("DELETE FROM Habits WHERE habit_name = ?;", (h_name,))
            cursor.execute("DELETE FROM History WHERE habit_name = ?;", (h_name,))
            db.commit()
            print("Habit successfully deleted")
            return
    print("Habit not found")
