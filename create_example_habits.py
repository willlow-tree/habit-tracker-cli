from datetime import *
import sqlite3

db = sqlite3.connect("database.db")
c = db.cursor()

def insert_completion_mark(date, name):
    c.execute("INSERT INTO History VALUES (?,?)", (date, name))
    db.commit()
def create_mock_habit(name, desc, period, times_per_period, date_of_creation):
    if desc is not None:
        c.execute("INSERT INTO Habits VALUES (?, ?, ?, ?, ?)", (name, desc, period, times_per_period, date_of_creation))
        db.commit()
    else:
        c.execute("INSERT INTO Habits(habit_name, habit_period, times_per_period, habit_creation_date) VALUES (?, ?, ?, ?)", (name, period, times_per_period, date_of_creation))
        db.commit()

date = datetime.now().date() 
date = date - timedelta(days=28)

def insert_test_values(habits):
    global date
    for h in habits:
        if h == 'study':
            insert_completion_mark(datetime.combine(date, time(15, 0, 0, 1)), 'study')
        if h == 'workout':
            insert_completion_mark(datetime.combine(date, time(16, 0, 0, 1)), 'workout')
        if h == 'meditate1':
            insert_completion_mark(datetime.combine(date, time(10, 0, 0, 1)), 'meditate')
        if h == 'meditate2':
            insert_completion_mark(datetime.combine(date, time(19, 0, 0, 1)), 'meditate')
        if h == 'water plants':
            insert_completion_mark(datetime.combine(date, time(18, 0, 0, 1)), 'water plants')
        if h == 'sleep':
            insert_completion_mark(datetime.combine(date, time(20, 0, 0, 1)), 'sleep schedule')
    date += timedelta(days=1)

def create_mock_habits():
    create_mock_habit('study', None, 'day', 1, datetime.combine(date, time(9, 0,0,1)))
    create_mock_habit('workout', None, 'week', 2, datetime.combine(date, time(9, 30,0,1)))
    insert_test_values(['study', 'workout'] )
    insert_test_values(['study'])
    insert_test_values(['study', 'workout'] )
    insert_test_values(['study'])   
    insert_test_values(['study'])
    insert_test_values(['study'])
    create_mock_habit('meditate', None, 'day', 2, datetime.combine(date, time(8, 20,0,1)))
    insert_test_values(['study', 'meditate1', 'meditate2'] )
    insert_test_values(['study'])
    insert_test_values(['study', 'workout'] )
    insert_test_values(['study'] )
    insert_test_values(['study'] )
    insert_test_values(['study', 'meditate1', 'meditate2'] )
    insert_test_values(['study', 'meditate1', 'meditate2', 'workout'] )
    insert_test_values(['study', 'meditate1', 'meditate2'] )
    insert_test_values(['study', 'meditate1', 'meditate2'] )
    insert_test_values(['study', 'meditate1', 'water plants'] )
    insert_test_values(['study'])
    insert_test_values(['study', 'meditate1', 'meditate2', 'workout', 'water plants'] )
    insert_test_values(['study', 'meditate1', 'meditate2'] )
    insert_test_values(['study', 'meditate1', 'meditate2', 'workout', 'water plants'] )
    insert_test_values(['study', 'meditate1', 'meditate2'] )
    insert_test_values(['study', 'meditate1', 'meditate2'] )
    insert_test_values(['study', 'meditate1', 'meditate2', 'water plants'] )
    create_mock_habit('sleep schedule', 'go to sleep no later than 23:00', 'day', 1, datetime.combine(date, time(19, 40,0,1)))
    insert_test_values(['study', 'meditate1', 'meditate2', 'workout', 'sleep'] )
    insert_test_values(['sleep'] )
    insert_test_values(['study', 'meditate1', 'meditate2', 'sleep', 'water plants'] )
    insert_test_values(['water plants'] )
    insert_test_values(['study', 'meditate1', 'meditate2'] )

create_mock_habits()