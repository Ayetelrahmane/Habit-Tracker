from backend.Repository import create_habit, complete_habit, delete_habit


def test_create_daily_habit(connection):
    """Test that a habit with Daily periodicity can be created successfully."""
    result = create_habit(
        connection,
        "Study",
        "Spend focused time studying or learning",
        "Daily"
    )  
    assert result == "Habit 'Study' is created successfully"
    
    cursor = connection.cursor()
    cursor.execute(
        "SELECT habit_name, periodicity FROM habit_info WHERE habit_name = %s",
        ("Study",)
    )

    habit = cursor.fetchone()
    cursor.close()
    assert habit == ("Study", "Daily")


def test_create_weekly_habit(connection):
    """Test that a habit with Weekly periodicity can be created successfully."""
    result = create_habit(
        connection,
        "Meal Prep",
        "Prepare healthy meals for the week",
        "Weekly"
    )   
    assert result == "Habit 'Meal Prep' is created successfully"

    cursor = connection.cursor()
    cursor.execute(
        "SELECT habit_name, periodicity FROM habit_info WHERE habit_name = %s",
        ("Meal Prep",)
    )
    habit = cursor.fetchone()
    cursor.close()
    assert habit == ("Meal Prep","Weekly")

    
def test_create_habit_invalid_periodicity(connection):
    """Test that habit creation rejects periodicities other than Daily or Weekly."""
    result = create_habit(
        connection,
        "Declutter",
        "Organize and remove things you no longer need",
        "Monthly"
    )   
    assert result == "Periodicity must be Daily or Weekly."

    cursor = connection.cursor()
    cursor.execute(
        "SELECT habit_id FROM habit_info WHERE habit_name = %s",
        ("Declutter",)
    )
    habit = cursor.fetchone()
    cursor.close()
    assert habit is None
    

def test_create_empty_habit_name(connection):
    """Test that habit creation rejects an empty habit name."""
    result = create_habit(
        connection,
        "",
        "Test habit",
        "Daily"
    )

    assert result == "Habit name cannot be empty."

    cursor = connection.cursor()
    cursor.execute(
        "SELECT habit_id FROM habit_info WHERE habit_name = %s",
        ("",)
    )

    habit = cursor.fetchone()
    cursor.close()

    assert habit is None

    
def test_create_duplicate_habit(connection):
    """Test that creating a habit with a duplicate name is rejected."""
    result = create_habit(
        connection,
        "Journal",
        "Write down thoughts, experiences, or goals",
        "Daily"
    )     
    assert result == "A habit named 'Journal' already exists."

    cursor = connection.cursor()
    cursor.execute(
        "SELECT habit_id FROM habit_info WHERE habit_name = %s",
        ("Journal",)
    )
    habits = cursor.fetchall()
    cursor.close()
    assert len(habits) == 1

    
def test_create_with_custom_date(connection):
    """Test that a habit can be created successfully with a custom creation date."""
    result = create_habit(
        connection,
        "Grocery Shopping",
        "Buy groceries for the upcoming week",
        "Weekly",
        "2026-07-17"
    )
    assert result == "Habit 'Grocery Shopping' is created successfully"

    cursor = connection.cursor()
    cursor.execute(
        "SELECT habit_id, habit_name, created_at FROM habit_info WHERE habit_name = %s",
        ("Grocery Shopping",)
    )
    habit = cursor.fetchone()
    cursor.close()
    assert habit is not None 
    assert habit[0] is not None 
    assert habit[1] == "Grocery Shopping"
    assert habit[2].date().isoformat() == "2026-07-17"


def test_complete_existing_habit(connection):
    """Test that an existing habit can be checked off successfully."""

    cursor = connection.cursor()
    cursor.execute("""
        SELECT COUNT(*)
        FROM habit_info AS h
        JOIN habit_completion AS hc
            ON h.habit_id = hc.habit_id
        WHERE h.habit_name = %s
        """,
        ("Journal",)
    )
    before = cursor.fetchone()[0]
    cursor.close()
    
    result = complete_habit(connection, "Journal")

    assert result == "Habit 'Journal' is checked off successfully"

    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM habit_completion hc
        JOIN habit_info hi ON hc.habit_id = hi.habit_id
        WHERE hi.habit_name = %s
        """,
        ("Journal",))

    after = cursor.fetchone()[0]
    cursor.execute(
        """SELECT hc.completion_date
        FROM habit_completion AS hc
        JOIN habit_info AS h
            ON h.habit_id = hc.habit_id
        WHERE h.habit_name = %s
        ORDER BY hc.completion_id DESC
        LIMIT 1""",
        ("Journal",)
    )

    completion = cursor.fetchone()
    cursor.close()

    assert after == before + 1
    assert completion is not None
    assert completion[0] is not None

    
def test_complete_non_existing_habit(connection):
    """Test that completing a non-existing habit returns an appropriate failure message."""
    result = complete_habit(
        connection,
        "Cook A New Recipe"
    )
    assert result == "Habit 'Cook A New Recipe' does not exist."

    
def test_complete_habit_custom_date(connection):
    """Test that an existing habit can be checked off with a custom completion date."""
    result = complete_habit(
        connection,
        "Digital Detox",
        "2026-09-18"
    )
    assert result == "Habit 'Digital Detox' is checked off successfully"

    cursor = connection.cursor()
    cursor.execute(
        """SELECT h.habit_id, h.habit_name, hc.completion_date
        FROM habit_info AS h
        JOIN habit_completion AS hc
            ON h.habit_id = hc.habit_id
        WHERE h.habit_name = %s
         AND DATE(hc.completion_date) = %s """,
        ("Digital Detox", "2026-09-18")
    )
    
    habit = cursor.fetchone()
    cursor.close()
    assert habit is not None
    assert habit[0] is not None
    assert habit[1] == "Digital Detox"
    assert habit[2].date().isoformat() == "2026-09-18"


def test_delete_existing_habit(connection):
    """Test that an existing habit can be deleted successfully."""
    result = delete_habit(
        connection,
        "Read"
    )
    assert result == "Habit 'Read' is deleted successfully"

    cursor = connection.cursor()
    cursor.execute(
        "SELECT habit_id FROM habit_info WHERE habit_name = %s",
        ("Read",)
    )
    habit = cursor.fetchone()
    cursor.close()
    assert habit is None
    

def test_delete_habit_cascades_completions(connection):
    """Test that deleting a habit also deletes its completion records."""
    
    cursor = connection.cursor()
    cursor.execute(
        "SELECT habit_id FROM habit_info WHERE habit_name = %s",
        ("Read",)
    )
    habit_id = cursor.fetchone()[0]
    cursor.execute(
        "SELECT COUNT(*) FROM habit_completion WHERE habit_id = %s",
        (habit_id,)
    )
    before = cursor.fetchone()[0]
    cursor.close()
    assert before > 0

    result = delete_habit(
        connection,
        "Read"
    )
    assert result == "Habit 'Read' is deleted successfully"
    
    cursor = connection.cursor()
    cursor.execute(
        "SELECT COUNT(*) FROM habit_completion WHERE habit_id = %s",
        (habit_id,)
    )
    after = cursor.fetchone()[0]
    cursor.close()
    assert after == 0

    
def test_delete_non_existing_habit(connection):
    """Test that deleting a non-existing habit returns an appropriate failure message."""
    result = delete_habit(
        connection,
        "Declutter"
    )
    assert result == "Habit 'Declutter' does not exist"
