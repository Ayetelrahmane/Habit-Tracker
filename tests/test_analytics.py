from datetime import date

from backend.Analytics import (
    calculate_longest_streak,
    get_all_habits,
    get_habits_by_periodicity,
    get_longest_streak_for_habit,
    get_longest_streak_all_habits,
)
from backend.Repository import create_habit


def test_get_all_habits(connection):
    """Test that all currently tracked habits are returned."""
    result = get_all_habits(connection)
    habit_names = [habit.habit_name for habit in result]
    assert habit_names == ["Read", "Exercise", "Journal", "Plan the Week", "Digital Detox"]


def test_get_daily_habits(connection):
    """Test that all Daily habits are returned."""
    result = get_habits_by_periodicity(connection, "Daily")
    habit_names = [habit.habit_name for habit in result]
    assert habit_names == ["Read", "Exercise", "Journal"]


def test_get_weekly_habits(connection):
    """Test that all Weekly habits are returned."""
    result = get_habits_by_periodicity(connection, "Weekly")
    habit_names = [habit.habit_name for habit in result]
    assert habit_names == ["Plan the Week", "Digital Detox"]


def test_calculate_daily_streak():
    """Test calculation of a consecutive Daily streak."""
    dates = [
        date(2026, 8, 1),
        date(2026, 8, 2),
        date(2026, 8, 3),
        date(2026, 8, 4),
    ]
    result = calculate_longest_streak(dates, "Daily")
    assert result == 4
    

def test_calculate_weekly_streak():
    """Test calculation of a consecutive Weekly streak."""
    dates = [
        date(2026, 8, 23),
        date(2026, 8, 30),
        date(2026, 9, 6),
        date(2026, 9, 13),
    ]
    result = calculate_longest_streak(dates, "Weekly")
    assert result == 4


def test_calculate_duplicate_daily_streak():
    """Test that duplicate Daily completion dates count only once."""
    dates = [
        date(2026, 8, 7),
        date(2026, 8, 7),
        date(2026, 8, 8),
    ]
    result = calculate_longest_streak(dates, "Daily")
    assert result == 2


def test_calculate_duplicate_weekly_streak():
    """Test that multiple completions in the same week count only once."""
    dates = [
        date(2026, 8, 24),
        date(2026, 8, 27),
        date(2026, 8, 31),
    ]
    result = calculate_longest_streak(dates, "Weekly")
    assert result == 2

    
def test_broken_daily_streak():
    """Test that a gap breaks a Daily streak."""
    dates = [
        date(2026, 8, 15),
        date(2026, 8, 16),
        date(2026, 8, 17),
        date(2026, 8, 18),
        date(2026, 8, 20),
    ]
    result = calculate_longest_streak(dates, "Daily")
    assert result == 4


def test_broken_weekly_streak():
    """Test that a gap breaks a Weekly streak."""
    dates = [
        date(2026, 8, 2),
        date(2026, 8, 9),
        date(2026, 8, 16),
        date(2026, 8, 30),
    ]
    result = calculate_longest_streak(dates, "Weekly")
    assert result == 3


def test_different_weekdays_for_weekly_streak():
    """Test that different weekdays can form a Weekly streak."""
    dates = [
        date(2026, 8, 23),
        date(2026, 8, 29),
        date(2026, 9, 6),
    ]
    result = calculate_longest_streak(dates, "Weekly")
    assert result == 3


def test_empty_completion_dates():
    """Test that an empty list gives a streak of zero."""
    dates = []
    result = calculate_longest_streak(dates, "Daily")
    assert result == 0


def test_single_completion_dates():
    """Test that a single completion gives a streak of one."""
    dates = [date(2026, 9, 1)]
    result = calculate_longest_streak(dates, "Daily")
    assert result == 1


def test_longest_streak_read(connection):
    """Test the longest streak for the Read habit."""
    result = get_longest_streak_for_habit(connection, "Read")
    assert result == 10


def test_longest_streak_exercise(connection):
    """Test the longest streak for the Exercise habit."""
    result = get_longest_streak_for_habit(connection, "Exercise")
    assert result == 8

    
def test_longest_streak_journal(connection):
    """Test the longest streak for the Journal habit."""
    result = get_longest_streak_for_habit(connection, "Journal")
    assert result == 30


def test_longest_streak_plan_the_week(connection):
    """Test the longest streak for the Plan the Week habit."""
    result = get_longest_streak_for_habit(connection, "Plan the Week")
    assert result == 2


def test_longest_streak_digital_detox(connection):
    """Test the longest streak for the Digital Detox habit."""
    result = get_longest_streak_for_habit(connection, "Digital Detox")
    assert result == 4


def test_longest_streak_for_uncompleted_habit(connection):
    """Test that an existing habit with no completions has a streak of zero."""
    create_habit(connection, "New Habit", "Test habit", "Daily")
    result = get_longest_streak_for_habit(connection, "New Habit")
    assert result == 0


def test_longest_streak_non_existing_habit(connection):
    """Test that a non-existing habit returns None."""
    result = get_longest_streak_for_habit(
        connection,
        "Does Not Exist"
    )

    assert result is None

    
def test_longest_streak_all_habits_with_uncompleted_habit(connection):
    """Test that an uncompleted habit does not affect the overall longest streak."""
    create_habit(connection, "New Habit", "Test habit", "Daily")
    result = get_longest_streak_all_habits(connection)
    assert result is not None
    assert result[0] == "Journal"
    assert result[1] == 30


def test_longest_streak_all_habits(connection):
    """Test that the habit with the longest streak is returned."""
    result = get_longest_streak_all_habits(connection)
    assert result == ("Journal", 30)

