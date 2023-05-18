import sqlite3
from datetime import *

db = sqlite3.connect("database.db")
c = db.cursor()

# c.execute("""CREATE TABLE History (
#             timelog text PRIMARY KEY,
#             habit_name text
# );""")

# c.execute("""CREATE TABLE Habits (
#             habit_name text PRIMARY KEY,
#             habit_description text,
#             habit_period text,
#             times_per_period integer,
#             habit_creation_date text
# )""")

# c.execute("DROP TABLE Habits;")
# c.execute("DROP TABLE History;")

t_format = "%Y-%m-%d %H:%M:%S.%f"

# c.execute("""INSERT INTO History VALUES
#         ('2023-03-10 15:00:00.000000', 'study'),
#         ('2023-03-11 15:00:00.000000', 'workout'),
#         ('2023-03-16 15:00:00.000000', 'study'),
#         ('2023-03-18 15:00:00.000000', 'workout'),
#         ('2023-03-21 16:00:00.000000', 'workout'),
#         ('2023-03-23 14:00:00.000000', 'meditate'),
#         ('2023-03-23 15:00:00.000000', 'study'),
#         ('2023-03-24 16:00:00.000000', 'study'),
#         ('2023-03-24 17:58:24.000000', 'meditate'),
#         ('2023-03-25 15:00:00.000000', 'workout')""")

# c.execute("""INSERT INTO Habits VALUES
#             ('meditate', 'focus, clear your mind and relax', 'day', 2, '2023-03-23 14:00:00');""")

# c.execute("""INSERT INTO Habits(habit_name, habit_period, times_per_period, habit_creation_date)
#             VALUES
#             ('study', 'day', 2, '2023-03-10 15:00:00'),
#             ('workout', 'week', 1, '2023-03-11 15:00:00');""")

# db.commit()

# c.execute("UPDATE Habits SET habit_creation_date = '2023-03-10 15:00:00.000000' WHERE habit_name = 'study'")


# c.execute("INSERT INTO History VALUES ('2023-04-03 16:00:00.000000', 'meditate');")
# db.commit()

# c.execute("DELETE FROM History;")
# db.commit()

# c.execute(
#     """INSERT INTO History VALUES
#         ('2023-04-06 15:00:00.000000', 'study'),
#         ('2023-04-06 16:00:00.000000', 'study'),
#         ('2023-04-06 17:00:00.000000', 'meditate'),
#         ('2023-04-07 15:00:00.000000', 'study'),
#         ('2023-04-07 16:00:00.000000', 'study'),
#         ('2023-04-07 14:00:00.000000', 'meditate'),
#         ('2023-04-07 13:00:00.000000', 'meditate'),
#         ('2023-04-08 16:00:00.000000', 'study'),
#         ('2023-04-08 17:58:24.000000', 'study');"""
# )

# db.commit()


# c.execute("""INSERT INTO History VALUES
#         ('2023-03-29 15:00:00.000000', 'workout'),
#         ('2023-04-01 16:00:00.000000', 'workout'),
#         ('2023-04-04 17:00:00.000000', 'workout');""")
# db.commit()

# c.execute("""INSERT INTO History VALUES
# ('2023-03-31 15:00:00.000000', 'workout');""")
# db.commit()

# c.execute("DELETE FROM Habits;")
# db.commit()

# c.execute("DELETE FROM History;")
# db.commit()

# c.execute("DELETE FROM History WHERE timelog = '2023-04-01 16:00:00.000000'")
# db.commit()

# ---------------------------------------


# c.execute(
#     """INSERT INTO History VALUES
#         ('2023-03-20 15:00:00.000000', 'study'),

#         ('2023-03-21 16:00:00.000000', 'study'),
#         ('2023-03-21 17:00:00.000000', 'workout'),

#         ('2023-03-22 17:00:00.000000', 'study'),

#         ('2023-03-23 15:00:00.000000', 'study'),
#         ('2023-03-23 10:00:00.000000', 'meditate'),
#         ('2023-03-23 20:00:00.000000', 'meditate'),

#         ('2023-03-24 16:00:00.000000', 'study'),
#         ('2023-03-24 10:00:00.000000', 'meditate'),
#         ('2023-03-24 20:00:00.000000', 'meditate'),
#         ('2023-03-24 17:00:00.000000', 'workout'),

#         ('2023-03-25 15:00:00.000000', 'study'),
#         ('2023-03-25 10:00:00.000000', 'meditate'),
#         ('2023-03-25 20:00:00.000000', 'meditate'),

#         ('2023-03-26 15:00:00.000000', 'study'),
#         ('2023-03-26 10:00:00.000000', 'meditate'),
#         ('2023-03-26 20:00:00.000000', 'meditate'),

        
#         ('2023-03-27 15:00:00.000000', 'study'),
#         ('2023-03-27 10:00:00.000000', 'meditate'),
#         ('2023-03-27 18:00:00.000000', 'water plants'),

#         ('2023-03-28 15:00:00.000000', 'study'),

#         ('2023-03-29 15:00:00.000000', 'study'),
#         ('2023-03-29 10:00:00.000000', 'meditate'),
#         ('2023-03-29 20:00:00.000000', 'meditate'),
#         ('2023-03-29 17:00:00.000000', 'workout'),
#         ('2023-03-29 18:00:00.000000', 'water plants'),

#         ('2023-03-30 15:00:00.000000', 'study'),
#         ('2023-03-30 10:00:00.000000', 'meditate'),
#         ('2023-03-30 20:00:00.000000', 'meditate'),

#         ('2023-03-31 15:00:00.000000', 'study'),
#         ('2023-03-31 10:00:00.000000', 'meditate'),
#         ('2023-03-31 20:00:00.000000', 'meditate'),
#         ('2023-03-31 17:00:00.000000', 'workout'),
#         ('2023-03-31 18:00:00.000000', 'water plants'),

#         ('2023-04-01 15:00:00.000000', 'study'),
#         ('2023-04-01 10:00:00.000000', 'meditate'),
#         ('2023-04-01 20:00:00.000000', 'meditate'),

#         ('2023-04-02 15:00:00.000000', 'study'),
#         ('2023-04-02 10:00:00.000000', 'meditate'),
#         ('2023-04-02 20:00:00.000000', 'meditate'),

#         ('2023-04-03 15:00:00.000000', 'study'),
#         ('2023-04-03 10:00:00.000000', 'meditate'),
#         ('2023-04-03 20:00:00.000000', 'meditate'),
#         ('2023-04-03 18:00:00.000000', 'water plants'),

#         ('2023-04-04 15:00:00.000000', 'study'),
#         ('2023-04-04 10:00:00.000000', 'meditate'),
#         ('2023-04-04 20:00:00.000000', 'meditate'),
#         ('2023-04-04 17:00:00.000000', 'workout'),
#         ('2023-04-04 22:00:00.000000', 'sleep schedule'),

#         ('2023-04-05 22:00:00.000000', 'sleep schedule'),

#         ('2023-04-06 15:00:00.000000', 'study'),
#         ('2023-04-06 10:00:00.000000', 'meditate'),
#         ('2023-04-06 20:00:00.000000', 'meditate'),
#         ('2023-04-06 18:00:00.000000', 'water plants'),
#         ('2023-04-06 22:00:00.000000', 'sleep schedule'),

        

#         ('2023-04-08 18:00:00.000000', 'water plants'),

#         ('2023-04-09 15:00:00.000000', 'study'),
#         ('2023-04-09 10:00:00.000000', 'meditate'),
#         ('2023-04-09 20:00:00.000000', 'meditate');"""
# )

# c.execute("DELETE FROM History WHERE habit_name ='sleep schdeule';")

# c.execute("INSERT INTO History VALUES ('2023-04-11 22:00:00.000000', 'sleep schedule');")

# db.commit()


# c.execute("SELECT * FROM History;")



# print("---------------------------------")

c.execute("SELECT * FROM History WHERE habit_name == 'study' and timelog LIKE '2023-04-08%' ORDER BY  timelog DESC LIMIT(1);")
selection = c.fetchall()
print(selection)
if selection != []:
    print("me")
# c.execute("SELECT * FROM History;")


# # c.execute("SELECT * FROM History WHERE timelog LIKE '2023-04-10%'")
# c.execute("SELECT * FROM History LIMIT 1;")
# selection = c.fetchall()
# print(selection)
# print(logs)
# some_date = datetime.datetime.strptime(logs[0][0], t_format)
# print(some_date)
# print(type(some_date))

# def insert_completion_mark(date, name):
#     c.execute("INSERT INTO History VALUES (?,?)", (date, name))
#     db.commit()
# def create_mock_habit(name, desc, period, times_per_period, date_of_creation):
#     if desc is not None:
#         c.execute("INSERT INTO Habits VALUES (?, ?, ?, ?, ?)", (name, desc, period, times_per_period, date_of_creation))
#         db.commit()
#     else:
#         c.execute("INSERT INTO Habits(habit_name, habit_period, times_per_period, habit_creation_date) VALUES (?, ?, ?, ?)", (name, period, times_per_period, date_of_creation))
#         db.commit()

# date = datetime.now().date() 
# date = date - timedelta(days=20)

# def insert_test_values(habits, date):
#     for h in habits:
#         if h == 'study':
#             insert_completion_mark(datetime.combine(date, time(15, 0, 0, 1)), 'study')
#         if h == 'workout':
#             insert_completion_mark(datetime.combine(date, time(16, 0, 0, 1)), 'workout')
#         if h == 'meditate1':
#             insert_completion_mark(datetime.combine(date, time(10, 0, 0, 1)), 'meditate')
#         if h == 'meditate2':
#             insert_completion_mark(datetime.combine(date, time(19, 0, 0, 1)), 'meditate')
#         if h == 'water plants':
#             insert_completion_mark(datetime.combine(date, time(18, 0, 0, 1)), 'water plants')
#         if h == 'sleep':
#             insert_completion_mark(datetime.combine(date, time(18, 0, 0, 1)), 'sleep schedule')
#     date += timedelta(days=1)

# def create_mock_habits():
#     create_mock_habit('study', None, 'day', 1, datetime.combine(date, time(9, 0,0,1)))
#     create_mock_habit('workout', None, 'week', 2, datetime.combine(date, time(9, 30,0,1)))
#     insert_test_values(['study'], date)
#     insert_test_values(['study', 'workout'], date)
#     insert_test_values(['study'], date)
#     insert_test_values(['study'], date)
#     create_mock_habit('meditate', None, 'day', 2, datetime.combine(date, time(8, 20,0,1)))
#     insert_test_values(['study', 'meditate1', 'meditate2'], date)
#     insert_test_values(['study', 'meditate1', 'meditate2', 'workout'], date)
#     insert_test_values(['study', 'meditate1', 'meditate2'], date)
#     insert_test_values(['study', 'meditate1', 'meditate2'], date)
#     insert_test_values(['study', 'meditate1', 'water plants'], date)
#     insert_test_values(['study'])
#     insert_test_values(['study', 'meditate1', 'meditate2', 'workout', 'water plants'], date)
#     insert_test_values(['study', 'meditate1', 'meditate2'], date)
#     insert_test_values(['study', 'meditate1', 'meditate2', 'workout', 'water plants'], date)
#     insert_test_values(['study', 'meditate1', 'meditate2'], date)
#     insert_test_values(['study', 'meditate1', 'meditate2'], date)
#     insert_test_values(['study', 'meditate1', 'meditate2', 'water plants'], date)
#     create_mock_habit('sleep schedule', 'go to sleep no later than 23:00', 'day', 1, datetime.combine(date, time(19, 40,0,1)))
#     insert_test_values(['study', 'meditate1', 'meditate2', 'workout', 'sleep'], date)
#     insert_test_values(['sleep'], date)
#     insert_test_values(['study', 'meditate1', 'meditate2', 'sleep', 'water plants'], date)
#     insert_test_values(['water plants'], date)
#     insert_test_values(['study', 'meditate1', 'meditate2'], date)

# create_mock_habits()