import json
import csv

# Load tasks from JSON file
def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("File not found. Creating a new tasks.json file.")
        return []

# Save tasks to JSON file
def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)
    print(f"Tasks saved to {filename}")

# Display tasks
def display_tasks(tasks):
    print("\nTask List:")
    print(f"{'ID':<5}{'Task Name':<20}{'Completed':<10}{'Priority':<10}")
    print("-" * 50)
    for task in tasks:
        print(f"{task['id']:<5}{task['task']:<20}{task['completed']:<10}{task['priority']:<10}")
    print("-" * 50)

# Modify a task (mark as completed or change priority)
def modify_task(tasks, task_id, completed=None, priority=None):
    for task in tasks:
        if task["id"] == task_id:
            if completed is not None:
                task["completed"] = completed
            if priority is not None:
                task["priority"] = priority
            print(f"Task {task_id} updated successfully.")
            return
    print(f"Task ID {task_id} not found.")

# Calculate task statistics
def calculate_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["completed"])
    pending_tasks = total_tasks - completed_tasks
    average_priority = round(sum(task["priority"] for task in tasks) / total_tasks, 2) if total_tasks else 0

    print("\nTask Completion Statistics:")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {average_priority}")

# Convert JSON data to CSV
def convert_to_csv(tasks, filename="tasks.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])  # Header row
        for task in tasks:
            writer.writerow([task["id"], task["task"], task["completed"], task["priority"]])
    print(f"Tasks converted to CSV file: {filename}")

# Main Execution
if __name__ == "__main__":
    tasks = load_tasks()
    display_tasks(tasks)
    calculate_stats(tasks)

    # Example modifications
    modify_task(tasks, 1, completed=True)  # Mark "Do laundry" as completed
    modify_task(tasks, 3, priority=2)  # Change priority of "Finish homework"

    save_tasks(tasks)  # Save modified tasks
    convert_to_csv(tasks)  # Convert tasks to CSV
