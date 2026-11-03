-- File Name: HabitTracker_schema.sql
-- Purpose: This script initializes the schema for a habit tracker database, creating
--          tables and relationships to manage habit information and completion efficiently.

-- Instructions:
-- 1. Ensure you have a MySQL database server installed and running.
-- 2. Open a MySQL client or MySQL Workbench and connect to the server.
-- 3. Copy and paste this script into the MySQL client or use the "Open File" option in MySQL Workbench.
-- 4. Execute the script to create the database schema.
-- 5. Verify that all tables and relationships are created without errors.
-- 6. After running this script, use the companion files to insert sample data and select it.
-- 7. Ensure that all components work as expected before proceeding to further development.

-- The script covers the following areas:
-- 1. Creating tables for managing habit data and completion.
-- 2. Defining relationships (one-to-many) between entities.
-- 3. Ensuring referential integrity and data consistency through foreign key constraints.

-- Key tables created:
-- - habit_info: Stores details of different habits.
-- - habit_completion: Stores records of habit completions, including completion dates.


-- Create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS habit_tracker; 
USE habit_tracker;

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