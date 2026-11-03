from backend.Database import create_connection
from backend.Repository import create_habit, complete_habit, delete_habit
from backend.Analytics import get_all_habits, get_habits_by_periodicity, get_longest_streak_for_habit, get_longest_streak_all_habits


def display_menu():
    """Display the main menu of the Habit Tracker application."""
    print(" ")
    print("=======================================")
    print("      Welcome to Habit Tracker       ")
    print("---------------------------------------")
    print("      Build consistency every day  ")
    print("=======================================")
    print("1. Create a habit")
    print("2. Complete a habit")
    print("3. Delete a habit")
    print("4. View all habits") 
    print("5. View Daily habits") 
    print("6. View Weekly habits") 
    print("7. View longest streak for a habit") 
    print("8. View longest streak for all habits")
    print("9. Exit")
    print(" ")


def main():
    """Run the Habit Tracker application."""
    connection = create_connection()
    
    try:
        while True:
            display_menu()

            choice = input("Choose an option: ").strip()

            if choice == "1":
                habit_name = input("Enter habit name: ").strip()
                habit_description = input("Enter habit description: ").strip()
                periodicity = input("Enter periodicity (Daily/Weekly): ").strip().capitalize()

                result = create_habit(
                    connection,
                    habit_name,
                    habit_description,
                    periodicity
                )

                print(result)
    
            elif choice == "2":
                habit_name = input("Enter habit name: ").strip()
                
        
                result = complete_habit(
                    connection,
                    habit_name
                )

                print(result)

            elif choice == "3":
                habit_name = input("Enter habit name: ").strip()

                result = delete_habit(
                    connection,
                    habit_name
                )

                print(result)

            elif choice == "4":
                habits = get_all_habits(
                    connection
                )

                if not habits:
                    print("No habits found.")

                else:
                    print("All Habits:")
                    for habit in habits:
                        print(habit.habit_name)
                    
                

            elif choice == "5":
                periodicity = "Daily"
                habits = get_habits_by_periodicity(
                    connection,
                    periodicity
                )
                if not habits:
                    print("No Daily habits found.")
                
                else:
                    print("All Daily habits:")
                    for habit in habits:   
                        print(habit.habit_name)

            elif choice == "6":
                periodicity = "Weekly"
                habits = get_habits_by_periodicity(
                    connection,
                    periodicity
                )
                if not habits: 
                    print("No Weekly habits found.")
                else:
                    print("All Weekly habits:")
                    for habit in habits:   
                        print(habit.habit_name)

            elif choice == "7":
                habit_name = input("Enter habit name: ").strip()
                
                result = get_longest_streak_for_habit(
                    connection,
                    habit_name
                )
                
                if result is None:
                    print(f"Habit '{habit_name}' does not exist.")
                else:
                    print(f"{habit_name} has a longest streak of {result}.")


            elif choice == "8":
                result = get_longest_streak_all_habits(
                    connection
                )
                if result is None: 
                    print("No habits found.") 
                else: 
                    habit_name, streak = result 
                    print(f"{habit_name} has the longest streak with {streak}.")

            elif choice == "9":
                print("Goodbye!")
                break

            else:
                print("Invalid option. Please choose a number from 1 to 9.")

    finally:
        connection.close()

if __name__ == "__main__":
    main()