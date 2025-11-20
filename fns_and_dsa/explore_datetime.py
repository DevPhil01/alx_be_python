# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in a readable format: YYYY-MM-DD HH:MM:SS
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")


def calculate_future_date():
    """
    Asks the user for a number of days and calculates the future date.
    Prints the result in YYYY-MM-DD format.
    """
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days_to_add)
        formatted_future = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future}")
    except ValueError:
        print("Please enter a valid integer number of days.")


# Main execution
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
