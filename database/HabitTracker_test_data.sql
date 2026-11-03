-- File Name: HabitTracker_test_data.sql
-- Purpose: This script inserts sample data into the test database for use by the automated test suite.

-- Instructions:
-- 1. Ensure that the HabitTracker_test_schema.sql script has been executed
--    to create the habit_tracker_test database and its tables.
-- 2. Open MySQL Workbench or another MySQL client and connect to the MySQL server.
-- 3. Ensure that the habit_tracker_test database is available.
-- 4. Use this script to insert the sample habits and completion records required
--    by the automated tests.
-- 5. The conftest.py fixture automatically executes this script before each test
--    to provide a clean and consistent starting dataset.

-- The script includes:
-- 1. Sample data for the following tables:
--    - habit_info: Stores the test habits and their details.
--    - habit_completion: Stores completion records used to test streak calculations
--      and habit completion functionality.

-- The test data is used to verify:
-- - Habit retrieval and filtering by periodicity.
-- - Habit completion functionality.
-- - Daily and Weekly streak calculations.
-- - Longest streak for individual habits.
-- - Longest streak across all habits.
-- - Database relationships and constraints.


USE habit_tracker_test;


SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE habit_completion;
TRUNCATE TABLE habit_info;
SET FOREIGN_KEY_CHECKS = 1;


-- Inserting habit data into the habit_info table
INSERT INTO habit_info (habit_name, habit_description, periodicity, created_at) 
VALUES 
('Read','Read for at least 20 minutes','Daily', '2026-08-03 14:30:00'),
('Exercise','Complete a workout or physical activity','Daily', '2026-08-05 08:45:00'),
('Journal','Write down thoughts, experiences, or goals','Daily','2026-08-01 09:15:00'),
('Plan the Week', 'Review goals and plan the upcoming week', 'Weekly','2026-08-15 13:40:00'),
('Digital Detox', 'Take some time away from social media and screens', 'Weekly','2026-08-18 07:55:00');


    

-- Inserting habit completion data into the habit_completion table

-- Daily habits
-- 1. Read
INSERT INTO habit_completion
(habit_id, completion_date)
VALUES
(1, '2026-08-03 15:00:00'),
(1, '2026-08-04 09:20:00'),
(1, '2026-08-05 18:10:00'),
(1, '2026-08-06 11:45:00'),
(1, '2026-08-07 20:30:00'),
(1, '2026-08-08 14:15:00'),
(1, '2026-08-09 10:05:00'),
(1, '2026-08-10 19:40:00'),
(1, '2026-08-11 16:25:00'),
(1, '2026-08-12 21:10:00'),
(1, '2026-08-14 17:50:00'),
(1, '2026-08-15 08:40:00'),
(1, '2026-08-16 14:35:00'),
(1, '2026-08-18 10:30:00'),
(1, '2026-08-19 18:45:00'),
(1, '2026-08-20 12:20:00'),
(1, '2026-08-21 20:05:00'),
(1, '2026-08-22 09:55:00'),
(1, '2026-08-25 19:25:00'),
(1, '2026-08-26 13:50:00'),
(1, '2026-08-28 08:25:00'),
(1, '2026-08-29 15:45:00'),
(1, '2026-08-30 20:20:00'),
(1, '2026-08-31 10:50:00'),
(1, '2026-09-01 18:35:00');


-- 2. Exercise
INSERT INTO habit_completion
(habit_id, completion_date)
VALUES
(2, '2026-08-08 18:00:00'),
(2, '2026-08-09 17:20:00'),
(2, '2026-08-10 19:10:00'),
(2, '2026-08-11 18:30:00'),
(2, '2026-08-12 17:45:00'),
(2, '2026-08-13 20:00:00'),
(2, '2026-08-14 18:15:00'),
(2, '2026-08-15 17:30:00'),
(2, '2026-08-17 19:20:00'),
(2, '2026-08-18 17:50:00'),
(2, '2026-08-19 18:35:00'),
(2, '2026-08-20 20:10:00'),
(2, '2026-08-21 17:40:00'),
(2, '2026-08-23 19:05:00'),
(2, '2026-08-24 17:25:00'),
(2, '2026-08-25 18:50:00'),
(2, '2026-08-26 20:00:00'),
(2, '2026-08-27 17:35:00'),
(2, '2026-08-28 18:20:00'),
(2, '2026-08-30 16:45:00'),
(2, '2026-08-31 18:10:00'),
(2, '2026-09-01 17:55:00'),
(2, '2026-09-02 19:30:00'),
(2, '2026-09-04 17:40:00'),
(2, '2026-09-05 18:25:00'),
(2, '2026-09-06 19:15:00');


-- 3. Journal
INSERT INTO habit_completion
(habit_id, completion_date)
VALUES
(3, '2026-08-01 22:00:00'),
(3, '2026-08-02 21:45:00'),
(3, '2026-08-03 22:10:00'),
(3, '2026-08-04 21:50:00'),
(3, '2026-08-05 22:05:00'),
(3, '2026-08-06 21:30:00'),
(3, '2026-08-07 22:15:00'),
(3, '2026-08-08 21:40:00'),
(3, '2026-08-09 22:00:00'),
(3, '2026-08-10 21:55:00'),
(3, '2026-08-11 22:20:00'),
(3, '2026-08-12 21:35:00'),
(3, '2026-08-13 22:05:00'),
(3, '2026-08-14 21:50:00'),
(3, '2026-08-15 22:10:00'),
(3, '2026-08-16 21:45:00'),
(3, '2026-08-17 22:00:00'),
(3, '2026-08-18 21:30:00'),
(3, '2026-08-19 22:15:00'),
(3, '2026-08-20 21:50:00'),
(3, '2026-08-21 22:05:00'),
(3, '2026-08-22 21:40:00'),
(3, '2026-08-23 22:20:00'),
(3, '2026-08-24 21:55:00'),
(3, '2026-08-25 22:10:00'),
(3, '2026-08-26 21:45:00'),
(3, '2026-08-27 22:00:00'),
(3, '2026-08-28 21:35:00'),
(3, '2026-08-29 22:15:00'),
(3, '2026-08-30 21:50:00');


-- Weekly habits
-- 4. Plan the Week
INSERT INTO habit_completion
(habit_id, completion_date)
VALUES
(4, '2026-08-16 10:00:00'),
(4, '2026-08-23 10:30:00'),
(4, '2026-09-06 09:45:00');


-- 5. Digital Detox
INSERT INTO habit_completion
(habit_id, completion_date)
VALUES
(5, '2026-08-23 18:00:00'),
(5, '2026-08-30 18:00:00'),
(5, '2026-09-06 18:00:00'),
(5, '2026-09-13 19:45:00'); 

    
-- End of file