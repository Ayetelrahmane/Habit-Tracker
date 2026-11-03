from pathlib import Path
import pytest
from backend.Database import create_test_connection


@pytest.fixture
def connection():
    """Provide a clean test database connection for each test."""
    connection = create_test_connection()
    cursor = connection.cursor()

    try:
        test_data_file = Path(__file__).resolve().parents[1]/ "database" / "HabitTracker_test_data.sql"

        with open(test_data_file, "r", encoding="utf-8") as file:
            sql_script = file.read()
            
            statements = sql_script.split(";") 
            
            for statement in statements: 
                statement = statement.strip()
                
                if statement: 
                    cursor.execute(statement)
            
            connection.commit() 
            yield connection 
            
    finally: 
        cursor.close()
        connection.close()
