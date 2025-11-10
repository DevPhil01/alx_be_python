# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use a match case statement to respond based on priority
match priority:
    case "high":
        reminder = f"Your task '{task}' is a HIGH priority task. Focus on completing it first."
    case "medium":
        reminder = f"Your task '{task}' has a MEDIUM priority. Schedule some time to get it done today."
    case "low":
        reminder = f"Your task '{task}' is a LOW priority. You can handle it after other important tasks."
    case _:
        reminder = f"Priority level for your task '{task}' is not recognized."

# Modify reminder if the task is time-bound
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Print the customized reminder
print("\n--- DAILY REMINDER ---")
print(reminder)
