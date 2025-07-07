todo_list = []
while True:
    print("\n📝 Simple To-Do List")
    print("1. To Add Task")
    print("2. To View Tasks")
    print("3. To Remove Task")
    print("4. To Exit")
    user_choice = input("Enter your choice (1-4): ")
    if user_choice == '1':
        user_task = input("Enter the task to add: ")
        todo_list.append(user_task)
        print(f"✅ '{user_task}' has been added to your to-do list.")
    elif user_choice == '2':
        if not todo_list:
            print("📭 Your to-do list is empty.")
        else:
            print("📋 Your To-Do List:")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")
    elif user_choice == '3':
        if not todo_list:
            print("📭 Your to-do list is empty.")
        else:
            print("📋 Your To-Do List:")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")
            try:
                task_number = int(input("Enter the task number to remove: "))
                removed = todo_list.pop(task_number - 1)
                print(f"❌ The Task '{removed}' has been removed.")
            except (IndexError, ValueError):
                print("❌ Invalid input. Please try again.")
    elif user_choice == '4':
        print("👋 Exiting the To-Do List.Byeeee!!!!!")
        break
    else:
        print("❌ Invalid choice. Please enter only from 1–4.")
