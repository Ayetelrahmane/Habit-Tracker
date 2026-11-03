class Habit:
    """Represent a habit tracked by the Habit Tracker application. 
    Stores the habit's ID, name, description, periodicity
    and creation date."""
    
    def __init__(self, habit_id, habit_name, habit_description, periodicity, created_at):
        self.habit_id = habit_id
        self.habit_name = habit_name
        self.habit_description = habit_description
        self.periodicity = periodicity
        self.created_at = created_at
