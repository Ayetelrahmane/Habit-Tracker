# Habit Tracker

## Project Overview

Habit Tracker is a Python-based command-line application designed to help users create, manage and analyse their personal habits.

The application uses a command-line interface (CLI) and a MySQL database to store habits and their completion records.

Users can:

* Create a habit
* Complete a habit
* Delete a habit
* View all habits
* View Daily habits
* View Weekly habits
* View the longest streak for a specific habit
* View the habit with the longest streak

The project demonstrates object-oriented programming, functional programming, SQL database operations, and automated testing with pytest.

## Technologies Used

* Python 3.13.5 — Used to develop the Habit Tracker application and implement the application logic.
* MySQL — Used to store habits and habit completion records in a relational database.
* MySQL Connector/Python — Used to connect the Python application to the MySQL database and execute SQL queries.
* pytest — Used to create and run automated tests for the application's functionality.

## Development Tools

* JupyterLab — Used as the development environment for writing and testing the Python project.
* Anaconda — Used to manage the Python environment and installed packages.
* GitHub — Used to host and manage the project repository.

## Project Structure

The project is organised into separate folders and modules, with each component responsible for a specific part of the application. This structure promotes modularity and separation of concerns.

### Folder Descriptions

**1. `backend/`**

Contains the main Python application modules and core functionality.

| File            | Responsibility                                                                         |
| --------------- | -------------------------------------------------------------------------------------- |
| `__init__.py`   | Marks the backend directory as a Python package.                                       |
| `CLI.py`        | Provides the command-line interface through which users interact with the application. |
| `Models.py`     | Defines the `Habit` class and its attributes.                                          |
| `Database.py`   | Manages connections to the production and test databases.                              |
| `Repository.py` | Handles database operations, including creating, completing, and deleting habits.      |
| `Analytics.py`  | Retrieves habit data and performs filtering and streak calculations.                   |

**2. `tests/`**

Contains automated tests written using pytest.

| File                 | Responsibility                                                                                           |
| -------------------- | -------------------------------------------------------------------------------------------------------- |
| `conftest.py`        | Provides the database connection fixture and prepares a consistent test database state before each test. |
| `test_repository.py` | Tests habit management operations and database functionality.                                            |
| `test_analytics.py`  | Tests habit retrieval, filtering, and streak calculations.                                               |

**3. `database/`**

Contains SQL scripts used to create and populate the application and test databases.

| File                              | Responsibility                                                 |
| --------------------------------- | -------------------------------------------------------------- |
| `HabitTracker_schema.sql`         | Creates the production database structure.                     |
| `HabitTracker_PredefinedData.sql` | Inserts predefined habits and their completion records.        |
| `HabitTracker_test_schema.sql`    | Creates the database structure required for automated testing. |
| `HabitTracker_test_data.sql`      | Provides sample data used by the automated tests.              |

### Root Files

* `README.md`: Provides project documentation and instructions.
* `requirements.txt`: Lists the Python dependencies required by the application.
* `LICENSE`: Specifies the terms under which the project can be used and distributed.
* `.gitignore`: Specifies files and folders that Git should exclude from version control.

## Database Schema

The application uses a MySQL database named `habit_tracker`.

The database contains two main tables:

### `habit_info`

This table stores the information about each habit.

| Column              | Description                                 |
| ------------------- | ------------------------------------------- |
| `habit_id`          | Unique identifier for each habit            |
| `habit_name`        | Name of the habit                           |
| `habit_description` | Description of the habit                    |
| `periodicity`       | Frequency of the habit: `Daily` or `Weekly` |
| `created_at`        | Date and time when the habit was created    |

### `habit_completion`

This table stores the completion records for each habit.

| Column            | Description                                |
| ----------------- | ------------------------------------------ |
| `completion_id`   | Unique identifier for each completion      |
| `habit_id`        | ID of the completed habit                  |
| `completion_date` | Date and time when the habit was completed |

The `habit_id` column in `habit_completion` is a foreign key referencing `habit_info`.

When a habit is deleted, its associated completion records are also deleted through the database's `ON DELETE CASCADE` constraint.

### Database Relationship

Each habit can have multiple completion records:

**`habit_info` 1 → many `habit_completion`**

This relationship allows the application to keep a history of habit completions and use this data to calculate completion streaks.

## Installation and Requirements

### Requirements

Before running the Habit Tracker, make sure the following are installed:

* Python 3.13.5 (used for development and testing)
* MySQL Server

Optional tools:

* MySQL Workbench
* JupyterLab (if running or reviewing the project in JupyterLab)

The Python packages required by the project are:

* mysql-connector-python
* pytest

The Python packages can be installed using:

```bash
pip install -r requirements.txt
```

### Installation

1. Download or clone the project files from the GitHub repository.
2. Open the project folder in JupyterLab, a terminal, or another Python environment.
3. From the project root directory, install the required Python packages:

```bash
pip install -r requirements.txt
```

### Database Setup

The project includes separate SQL scripts for setting up the application database and the test database.

#### Application Database

The application database uses the following SQL files, located in the `database/` folder:

* `HabitTracker_schema.sql` — Creates the `habit_tracker` database and the `habit_info` and `habit_completion` tables.
* `HabitTracker_PredefinedData.sql` — Inserts the predefined habits and their completion records.

To set up the application database:

> **⚠️ Important:** Run `HabitTracker_PredefinedData.sql` only once on a newly initialized or empty database. The script clears existing habit and completion data before inserting the predefined records.

1. Start MySQL Server.
2. Open MySQL Workbench and connect to your MySQL server.
3. Open `database/HabitTracker_schema.sql`.
4. Execute the script to create the `habit_tracker` database and its tables.
5. Open `database/HabitTracker_PredefinedData.sql`.
6. Execute the script to insert the predefined habit data.
7. Verify that the data has been inserted successfully.

The predefined data includes five habits covering both daily and weekly periodicities.

#### Test Database

Separate SQL files located in the `database/` folder are provided for the automated testing environment:

* `HabitTracker_test_schema.sql` — Creates the database structure required for testing.
* `HabitTracker_test_data.sql` — Inserts the predefined test data used to verify database and analytics functionality.

To prepare the test database:

1. Execute `database/HabitTracker_test_schema.sql` once to create the test database and its required tables.
2. Open a terminal in the project directory.
3. Run the automated tests using:

```bash
python -m pytest -v
```

The test database is now ready for automated testing.

The `tests/conftest.py` fixture automatically resets the test database and loads `HabitTracker_test_data.sql` before each test.

The test data provides predefined completion records that allow the repository and analytics functions, including longest-streak calculations, to be tested using consistent data.

### Database Configuration

The application reads the MySQL connection settings from environment variables in `backend/Database.py`.

The following environment variables are supported:

| Environment Variable | Purpose           | Default             |
| -------------------- | ----------------- | ------------------- |
| `DB_HOST`            | MySQL server host | `localhost`         |
| `DB_USER`            | MySQL username    | `root`              |
| `DB_PASSWORD`        | MySQL password    | `""` (empty string) |

The application database is named `habit_tracker`, while the test database is named `habit_tracker_test`.

If the default MySQL settings are suitable, no environment variables need to be configured.

If custom MySQL credentials are required, set the environment variables before running the application or tests.

#### Windows

In Command Prompt:

```bash
set DB_HOST=localhost
set DB_USER=root
set DB_PASSWORD=your_password
```

In PowerShell:

```powershell
$env:DB_HOST="localhost"
$env:DB_USER="root"
$env:DB_PASSWORD="your_password"
```

#### macOS / Linux

```bash
export DB_HOST="localhost"
export DB_USER="root"
export DB_PASSWORD="your_password"
```

The MySQL server must be running before starting the application or running database-dependent tests.

The project does not use a `.env` file, so environment variables should be configured directly in the operating system or terminal environment.

## How to Run the Application

The Habit Tracker is operated through a command-line interface (CLI). After completing the installation and database setup, the application can be started from the project directory.

### Start the Application

1. Open Anaconda Prompt or a terminal.
2. Navigate to the folder containing the project files.
3. Run the following command:

```bash
python -m backend.CLI
```

### Using the CLI

The main menu allows the user to interact with the application by selecting the available options.

The application provides functionality to:

* Create a habit
* Complete a habit
* Delete a habit
* View all habits
* View daily habits
* View weekly habits
* View the longest streak for a specific habit
* View the habit with the longest streak
* Exit the application

The user can select an option from the menu and provide the required information when prompted.

### Database Connection

Before running the application, make sure that:

1. The MySQL server is running.
2. The habit_tracker database has been created.
3. The database tables and predefined data have been loaded according to the Database Setup section.
4. The environment variables, or their default values, match your local MySQL configuration.

Once these requirements are satisfied, the application is ready to run.

## Usage Examples

The Habit Tracker is operated through the command-line interface.

### Create a Habit

```text
Habit name: Study
Habit description: Study Python for 30 minutes
Periodicity: Daily
```

### Complete a Habit

```text
Habit name: Study
```

### Delete a Habit

```text
Habit name: Study
```

### View Habits

```text
4. View all habits
5. View Daily habits
6. View Weekly habits
```

### Analyse Habit Streaks

```text
Habit name: Study
Longest streak: 5
```

## Streak Calculation

A streak represents consecutive periods in which a habit was completed at least once.

* **Daily habits:** Each calendar day counts as one period. Multiple completions on the same day count only once.
* **Weekly habits:** Each Monday-to-Sunday calendar week counts as one period. Multiple completions within the same week count only once.
* A **missing required period breaks the streak**.
* Weekly periods are normalised to Monday-to-Sunday weeks.

## Testing

The project uses `pytest` for automated testing.

The test suite verifies that the main functionality of the Habit Tracker works correctly and that invalid inputs are handled appropriately. It covers:

* Habit creation and input validation
* Habit completion and deletion
* Duplicate habit prevention
* Habit retrieval and filtering by periodicity
* Daily and weekly longest-streak calculations

### Running Tests

From the project root directory, run the following command to execute the automated tests:

```bash
python -m pytest
```

For detailed test results, including individual test outcomes, run:

```bash
python -m pytest -v
```

The test suite contains 33 automated tests covering repository operations and analytics functionality.

## Functional Programming

The project incorporates functional programming concepts in the analytics functionality.

It uses:

* **`filter()`** — used to select habits that match a specific periodicity, such as Daily or Weekly.
* **`map()`** — used to transform collections of data when required.
* **`reduce()`** — used to process completion data when calculating streak-related results.
* **Lambda functions** — used where a short function is appropriate for filtering or transforming data.

The `backend/Repository.py` module handles habit-changing database operations such as creation, completion and deletion. The `backend/Analytics.py` module retrieves the data required for analysis, converts database records into `Habit` objects, and applies functional programming techniques to filter habits and calculate streaks.

This separation keeps database operations and analytical processing organised while demonstrating the use of functional programming within the analytics layer.

## Error Handling and Validation

The application validates user input and handles common database errors to prevent invalid data from being stored.

Examples of validation and error handling include:

* Only `Daily` and `Weekly` are accepted.
* Duplicate habit names are rejected.
* Database integrity errors are handled by the repository functions.
* Invalid operations return clear error messages to the user.
* Database cursors are closed after database operations.

Keeping validation and database-related error handling in the repository layer helps keep the CLI focused on user interaction while maintaining a clear separation of responsibilities.

## Future Improvements

The current application provides the core functionality required for a habit tracking system. Further improvements could be added in future versions, such as:

* Adding a graphical user interface (GUI)
* Adding user accounts and authentication
* Providing more detailed habit statistics and visualisations
* Adding reminders and notifications for incomplete habits
* Allowing users to edit existing habits
* Adding more advanced reporting and progress tracking
* Supporting additional habit periodicities

These improvements could extend the functionality of the application while keeping the existing database and modular architecture.


## Author

**Ayet Elrahmane**

Habit Tracker — Python, MySQL, and pytest project.
