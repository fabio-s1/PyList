import json
import os
from datetime import datetime

# Constants
TASKS_FILE = os.path.join(os.path.dirname(__file__), "tasks.json")
MAX_TITLE_LENGTH = 50
MAX_DESCRIPTION_LENGTH = 200


def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet.")
        return

    print("\nYour tasks:")
    for i, task in enumerate(tasks, 1):
        status = "☑" if task["done"] else "☒"
        print(f"{i}. [{status}] {task['title']}")
        if task["description"]:
            print(f"   → {task['description']}")


def add_task(tasks):
    title = input("\nEnter task title: ").strip()
    if len(title) > MAX_TITLE_LENGTH:
        print(f"Title must be less than {MAX_TITLE_LENGTH} characters.")
        return
        
    description = input("Enter task description (optional): ").strip()
    if len(description) > MAX_DESCRIPTION_LENGTH:
        print(f"Description must be less than {MAX_DESCRIPTION_LENGTH} characters.")
        return

    if title:
        tasks.append({
            "title": title,
            "description": description,
            "done": False,
            "created_at": datetime.now().isoformat(),
            "completed_at": None
        })
        save_tasks(tasks)
        print("Task added!")
    else:
        print("Task must have a title.")


def mark_done(tasks):
    show_tasks(tasks)
    try:
        number = int(input("\nEnter the task number to mark as done: "))
        if 1 <= number <= len(tasks):
            tasks[number - 1]["done"] = True
            save_tasks(tasks)
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    show_tasks(tasks)
    try:
        number = int(input("\nEnter the task number to delete: "))
        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            save_tasks(tasks)
            print(f"Task '{removed['title']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = load_tasks()
    while True:
        print("\n--- PyList Menu ---")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
