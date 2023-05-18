import datetime

def check_habit_completion(habit, history, time=datetime.datetime.now(), period=None, upto=datetime.datetime.max):
    """This function can check if the habit was completed on given day/week. If no period is passed, it check habit completion accroding to habit's period,
    and additionaly return if the goal was reached. So you can check if weekly habit was completed on a given day, but it will not return the goal_reached var."""
    
    if period == None:
        period = habit.period
        return_goal = True
    else:
        return_goal = False

    times_completed = 0
    if period == 'day':
        for log in history.keys():
            if log.date() == time.date() and habit.name == history[log] and log <= upto:
                times_completed += 1
    if period == 'week':
            for log in history.keys():
                if log.isocalendar()[1] == time.isocalendar()[1] and habit.name == history[log] and log <= upto:
                    times_completed += 1

    goal_reached = None
    if return_goal:
        if times_completed >= habit.times_per_period:
            goal_reached = True
        else:
            goal_reached = False
        
    return (times_completed, goal_reached)


def check_habit_streak(habit, history, time=datetime.datetime.now()):
    """Checks the streak of a habit according to it's period (day/week) and how many times per period it should be completed.
    Returns the streak up to a time argument (by default it is the current time), and the longest streak for the given habit."""

    time = time.date()
 
    delta_day = datetime.timedelta(days=1)
    delta_week = datetime.timedelta(days=7)

    try:
        start_date = min(history.keys()).date()
    except ValueError:
        start_date = time
    iter_date = start_date

    ###maybe start on sunday?
    iter_week = start_date + ((7-start_date.isocalendar()[2]) * delta_day) 
    end_date = time

    dates = []
    weeks = []

    while iter_date <= end_date:
        dates.append(iter_date)
        iter_date += delta_day
    
    #log.isocalendar()[1] == time.isocalendar()[1]
    while iter_week <= end_date:
        weeks.append(iter_week)
        iter_week += delta_week

    streak = 0
    longest_streak = 0


    for date in dates:
        date_todatetime = datetime.datetime.combine(date, datetime.datetime.max.time())
        end_date_todatetime = datetime.datetime.combine(end_date, datetime.datetime.max.time())
        if habit.period == 'day':
            goal_reached = check_habit_completion(habit, history, time=date_todatetime, upto=end_date_todatetime)[1]
            if goal_reached:
                streak += 1
                if streak > longest_streak:
                    longest_streak = streak
            else:
                streak = 0

    completed_week = 0
    flagged = False
    for date in dates:
        date_todatetime = datetime.datetime.combine(date, datetime.datetime.max.time())
        end_date_todatetime = datetime.datetime.combine(end_date, datetime.datetime.max.time())
        if habit.period == 'week':
            times_completed_week, goal_reached = check_habit_completion(habit, history, time=date_todatetime, upto=end_date_todatetime)
            if times_completed_week >= habit.times_per_period and flagged == False:
                streak += 1
                flagged = True
                if streak > longest_streak:
                    longest_streak = streak
            
            if date.isocalendar()[2] == 7:
                completed_week = 0
                flagged = False
                if goal_reached == False:
                    streak = 0

    return (streak, longest_streak)

