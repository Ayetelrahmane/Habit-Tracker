from datetime import timedelta
from functools import reduce

from backend.Models import Habit


def get_all_habits(connection):
    """Return all currently tracked habits."""
    cursor = connection.cursor()

    query = "SELECT habit_id, habit_name, habit_description, periodicity, created_at FROM habit_info ORDER BY habit_id"
    cursor.execute(query)

    habits = cursor.fetchall()
    cursor.close()

    return list(
        map(
            lambda habit: Habit(
                habit[0],
                habit[1],
                habit[2],
                habit[3],
                habit[4]
            ),
            habits
        )
    ) 


def get_habits_by_periodicity(connection, periodicity):
    """Return all habits that have the specified periodicity."""

    habits = get_all_habits(connection)
     
    return list(
        filter(
            lambda habit: habit.periodicity == periodicity,
            habits
        )
    )


def are_consecutive(previous, current, periodicity):
    """Check whether two completion dates are consecutive."""

    if periodicity == "Daily":
        return current - previous == timedelta(days=1)

    elif periodicity == "Weekly":
        previous_week = previous - timedelta(days=previous.weekday())
        current_week = current - timedelta(days=current.weekday())

        return current_week - previous_week == timedelta(days=7)

    return False


def calculate_longest_streak(dates, periodicity):
    """Calculate the longest consecutive completion streak."""

    if not dates:
        return 0
        
    if periodicity == "Daily":
        dates = sorted(set(dates))

    elif periodicity == "Weekly":
        dates = sorted(
            set(
                map(
                    lambda date: date - timedelta(days=date.weekday()),
                    dates
                )
            )
        )
    
    else:
        return 0
    
    def update_streak(streaks, pair):
        """Update the current and longest streak."""

        current_streak, longest_streak = streaks
        previous, current = pair

        if are_consecutive(previous, current, periodicity):
            current_streak += 1
        else:
            current_streak = 1

        longest_streak = max(longest_streak, current_streak)

        return current_streak, longest_streak

    result = reduce(
        update_streak,
        zip(dates, dates[1:]),
        (1, 1)
    )

    return result[1]


def get_longest_streak_for_habit(connection, habit_name):
    """Return the longest completion streak for a specific habit."""
    cursor = connection.cursor()

    query = """
    SELECT hi.periodicity, hc.completion_date
    FROM habit_info hi
    LEFT JOIN habit_completion hc
        ON hi.habit_id = hc.habit_id
    WHERE hi.habit_name = %s
    ORDER BY hc.completion_date
    """ 

    cursor.execute(query, (habit_name,))

    results = cursor.fetchall()
    cursor.close()

    if not results:
        return None

    periodicity = results[0][0]

    dates = list(
        map(
            lambda result: result[1].date(),
            filter(
                lambda result: result[1] is not None,
                results
            )
        )
    )

    return calculate_longest_streak(dates, periodicity)


def get_longest_streak_all_habits(connection):
    """Return the habit with the longest completion streak."""
    cursor = connection.cursor()

    query = "SELECT habit_name FROM habit_info ORDER BY habit_id"

    cursor.execute(query)

    habits = cursor.fetchall()

    cursor.close()

    if not habits:
        return None

    habit_streaks = list(
        map(
            lambda habit: (
                habit[0],
                get_longest_streak_for_habit(connection, habit[0])
            ),
            habits
        )
    )

    valid_streaks = list(
        filter(
            lambda habit: habit[1] is not None,
            habit_streaks
        )
    )
    if not valid_streaks:
        return None
       
    return max(
        valid_streaks,
        key=lambda habit: habit[1]
    )