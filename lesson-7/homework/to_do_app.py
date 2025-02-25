class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
    
    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        return Task(data["task_id"], data["title"], data["description"], data.get("due_date"), data["status"])

class FileHandler:
    def save_tasks(self, tasks):
        pass

    def load_tasks(self):
        return []

class ToDoApp:
    def __init__(self, file_handler):
        self.file_handler = file_handler
        self.tasks = self.file_handler.load_tasks()
    
    def add_task(self):
        task_id = input("Enter Task ID: ")
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        due_date = input("Enter Due Date (YYYY-MM-DD) (optional): ") or None
        status = input("Enter Status (Pending/In Progress/Completed): ")
        self.tasks.append(Task(task_id, title, description, due_date, status))
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(task.to_dict())

    def update_task(self):
        task_id = input("Enter Task ID to update: ")
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = input("Enter new title: ") or task.title
                task.description = input("Enter new description: ") or task.description
                task.due_date = input("Enter new due date (YYYY-MM-DD): ") or task.due_date
                task.status = input("Enter new status (Pending/In Progress/Completed): ") or task.status
                print("Task updated successfully!")
                return
        print("Task not found.")
    
    def delete_task(self):
        task_id = input("Enter Task ID to delete: ")
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        print("Task deleted successfully!")

    def filter_tasks(self):
        status = input("Enter status to filter by (Pending/In Progress/Completed): ")
        filtered_tasks = [task for task in self.tasks if task.status == status]
        if not filtered_tasks:
            print("No tasks found with that status.")
        else:
            for task in filtered_tasks:
                print(task.to_dict())

    def save_tasks(self):
        self.file_handler.save_tasks(self.tasks)
        print("Tasks saved successfully!")

    def menu(self):
        while True:
            print("\nWelcome to the To-Do Application!")
            print("1. Add a new task")
            print("2. View all tasks")
            print("3. Update a task")
            print("4. Delete a task")
            print("5. Filter tasks by status")
            print("6. Save tasks")
            print("7. Exit")
            choice = input("Enter your choice: ")
            
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.filter_tasks()
            elif choice == "6":
                self.save_tasks()
            elif choice == "7":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Example usage
file_handler = FileHandler()
todo_app = ToDoApp(file_handler)
todo_app.menu()
