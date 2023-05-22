import unittest, sqlite3
import core_functions
import database_interaction
from datetime import *

db = sqlite3.connect("database.db")
cursor = db.cursor()

history = {}
habits = []

database_interaction.load_habits(habits, cursor)
database_interaction.load_history(history, cursor)

study_h = None
workout_h = None
meditate_h = None

for habit in habits:
    if habit.name == 'study':
        study_h = habit
    elif habit.name == 'workout':
        workout_h = habit
    elif habit.name == 'meditate':
        meditate_h = habit

starting_date = datetime.now() - timedelta(28)
maxtime = time.max

class test_app(unittest.TestCase):
    def test_check_habit_completon(self):
        # tesing daily habits
        self.assertEqual(core_functions.check_habit_completion(meditate_h, history, datetime.combine(starting_date + timedelta(23), maxtime)), (2, True))
        self.assertEqual(core_functions.check_habit_completion(meditate_h, history, datetime.combine(starting_date + timedelta(15), maxtime)), (1, False))
        self.assertEqual(core_functions.check_habit_completion(meditate_h, history, datetime.combine(starting_date + timedelta(16), maxtime)), (0, False))
        # testing weekly habits
        self.assertEqual(core_functions.check_habit_completion(workout_h, history, datetime.combine(starting_date + timedelta(19), maxtime), 'day')[0], 1)
        self.assertEqual(core_functions.check_habit_completion(workout_h, history, datetime.combine(starting_date + timedelta(23), maxtime)), (1, False))
        self.assertEqual(core_functions.check_habit_completion(workout_h, history, datetime.combine(starting_date + timedelta(19), maxtime)), (2, True))
    def test_habit_streak(self):
        self.assertEqual(core_functions.check_habit_streak(study_h, history, datetime.combine(starting_date + timedelta(23), maxtime)), (24, 24))
        self.assertEqual(core_functions.check_habit_streak(study_h, history, datetime.combine(starting_date + timedelta(24), maxtime)), (0, 24))
        self.assertEqual(core_functions.check_habit_streak(workout_h, history, datetime.combine(starting_date + timedelta(23), maxtime)), (3, 3))
        self.assertEqual(core_functions.check_habit_streak(workout_h, history, datetime.combine(starting_date + timedelta(27), maxtime)), (0, 3))


unittest.main()