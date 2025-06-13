# Simple To-Do List App in Python (Command Line Interface)
# Intern Name:NITIN NATH GOSWAMI
# Intern id:217256425
# Internship Task for @indolike
# Different Emojies picked From @emojiepedia.org

tasks = []

def show_menu():
    print("\n--- TO-DO LIST MENU 📋---")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark task as done")
    print("4. Delete a task")
    print("5. Exit")

def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "done": False})
    print(f"✅ Task added: {task}")

def view_tasks():
    if not tasks:
        print("📭 No tasks yet.")
        return
    print("\n📝 Your Tasks:")
    for i, t in enumerate(tasks, 1):
        status = "✅ Done" if t["done"] else "❌ Not done"
        print(f"{i}. {t['task']} [{status}]")

def mark_done():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as done: "))
        tasks[task_num - 1]["done"] = True
        print("✔️ Task marked as done.")
    except (IndexError, ValueError):
        print("⚠️ Invalid task number!")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        deleted = tasks.pop(task_num - 1)
        print(f"🗑️ Deleted: {deleted['task']}")
    except (IndexError, ValueError):
        print("⚠️ Invalid task number!")

# 🎯 Main Program Loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("👋 Goodbye! Keep crushing/doing the tasks.")
        break
    else:
        print("❌ Invalid choice. Please select from the menu.")
