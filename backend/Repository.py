import mysql.connector


def create_habit(connection, habit_name, habit_description, periodicity, created_at=None):
    """Create a new habit in the database."""
    

    if periodicity not in ("Daily", "Weekly"):
        return "Periodicity must be Daily or Weekly."
        
    if not habit_name.strip():
        return "Habit name cannot be empty."

    cursor = connection.cursor()

    try:
        if created_at is None:
            query = "INSERT INTO habit_info (habit_name, habit_description, periodicity) VALUES (%s, %s, %s)"
            cursor.execute(query, (habit_name, habit_description, periodicity))

        else:
            query = "INSERT INTO habit_info (habit_name, habit_description, periodicity, created_at) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (habit_name, habit_description, periodicity, created_at))
    
        connection.commit()
    
        return f"Habit '{habit_name}' is created successfully"
    
    except mysql.connector.IntegrityError:
        connection.rollback()

        return f"A habit named '{habit_name}' already exists."

    finally:
        cursor.close()


def complete_habit(connection, habit_name, completion_date=None):
    """Record a completed task for a habit."""
    cursor = connection.cursor()

    try:
        query = "SELECT habit_id FROM habit_info WHERE habit_name = %s"
        cursor.execute(query, (habit_name,))
    
        habit = cursor.fetchone()
    
        if habit is None:
            return f"Habit '{habit_name}' does not exist."

        habit_id = habit[0]

        if completion_date is None:
            query = "INSERT INTO habit_completion (habit_id) VALUES (%s)"
            cursor.execute(query, (habit_id,))
        else:
            query = "INSERT INTO habit_completion (habit_id, completion_date) VALUES (%s, %s)"
            cursor.execute(query, (habit_id, completion_date))

    
        connection.commit()
    
        return f"Habit '{habit_name}' is checked off successfully"
        
    finally:
        cursor.close()


def delete_habit(connection, habit_name):
    """Delete a habit from the database."""
    cursor = connection.cursor()

    try:
        query = "DELETE FROM habit_info WHERE habit_name = %s"
        cursor.execute(query, (habit_name,))
    
        connection.commit()
        deleted = cursor.rowcount
    
        if deleted == 0:
            return f"Habit '{habit_name}' does not exist"
    
        return f"Habit '{habit_name}' is deleted successfully"

    finally:
        cursor.close()


    