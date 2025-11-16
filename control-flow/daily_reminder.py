# daily_reminder.py

print("Personal Daily Reminder")

# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Validate priority
while priority not in ("high", "medium", "low"):
    print("Invalid priority. Please enter high, medium, or low.")
    priority = input("Priority (high/medium/low): ").lower()

# Validate time_bound
while time_bound not in ("yes", "no"):
    print("Please answer with yes or no.")
    time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process task based on priority
match priority:
    case "high":
        base_message = f"'{task}' is a high priority task"
    case "medium":
        base_message = f"'{task}' is a medium priority task"
    case "low":
        base_message = f"'{task}' is a low priority task"
    case _:
        base_message = f"'{task}' is a task of unspecified priority"

# Provide customized reminder
if time_bound == "yes":
    print(f"Reminder: {base_message} that requires immediate attention today!")
else:
    print(f"Note: {base_message}. Consider completing it when you have free time.")
