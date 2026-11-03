import os
import mysql.connector


def create_connection():
    """Create a connection to the production habit_tracker database."""
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database="habit_tracker"
    )


def create_test_connection():
    """Create a connection to the habit_tracker_test database."""
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database="habit_tracker_test"
    )

