# Simple To-Do List Application

tasks = []

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append({"task": task, "completed": False})
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nTo-Do List:")
            for i in range(len(tasks)):
                status = "Completed" if tasks[i]["completed"] else "Pending"
                print(f"{i + 1}. {tasks[i]['task']} - {status}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            task_num = int(input("Enter task number to mark as completed: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]["completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            task_num = int(input("Enter task number to update: "))
            if 1 <= task_num <= len(tasks):
                new_task = input("Enter new task: ")
                tasks[task_num - 1]["task"] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number.")

    elif choice == "5":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                deleted = tasks.pop(task_num - 1)
                print("Deleted task:", deleted["task"])
            else:
                print("Invalid task number.")

    elif choice == "6":
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")