-- File Name: HabitTracker_test_schema.sql
-- Purpose: This script initializes the test database schema for the Habit Tracker application.
--          It creates the tables and relationships required to run the automated tests.

-- Instructions:
-- 1. Ensure that MySQL is installed and running.
-- 2. Open MySQL Workbench or another MySQL client and connect to the server.
-- 3. Open this script in MySQL Workbench.
-- 4. Execute the script to create the habit_tracker_test database and its tables.
-- 5. Verify that the database and tables were created successfully.
-- 6. The HabitTracker_test_data.sql file can then be used to insert sample data for the test suite.
-- 7. Run the pytest test suite from the project folder.

-- The script covers the following areas:
-- 1. Creating the test database for the Habit Tracker application.
-- 2. Creating tables for habit information and habit completions.
-- 3. Defining a one-to-many relationship between habits and completions.
-- 4. Enforcing referential integrity using a foreign key constraint.

-- Key tables created:
-- - habit_info: Stores details of the habits used during testing.
-- - habit_completion: Stores completion records for the test habits.

CREATE DATABASE IF NOT EXISTS habit_tracker_test; 
USE habit_tracker_test;

-- Table to store habit information 
CREATE TABLE IF NOT EXISTS habit_info (
    habit_id INT NOT NULL AUTO_INCREMENT,  -- Unique ID for each habit
    habit_name VARCHAR(100) NOT NULL UNIQUE,       -- Name of the habit
    habit_description TEXT DEFAULT NULL,   -- Description of the habit
    periodicity ENUM('Daily', 'Weekly') NOT NULL,  -- Habit frequency 
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,       -- Habit's creation date and time
    PRIMARY KEY (habit_id)  -- Primary key for the habit_info table
);


-- Table to store habit completion information 
CREATE TABLE IF NOT EXISTS habit_completion (
    completion_id INT NOT NULL AUTO_INCREMENT, -- Unique id for each habit completion
    habit_id INT NOT NULL, -- Foreign key referencing the habit id
    completion_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, -- Habit's completion date and time
    PRIMARY KEY (completion_id), -- Primary key for the habit_completion table
	FOREIGN KEY (habit_id)
        REFERENCES habit_info (habit_id)
        ON DELETE CASCADE  -- Deletes related completion records when a habit is deleted
);


-- End of file