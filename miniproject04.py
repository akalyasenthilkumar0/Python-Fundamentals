#--------------------------------------------------------------------------------------------------------------------

# Miniproject04 : To-Do List App

#--------------------------------------------------------------------------------------------------------------------

tasks = []

print("Miniproject04 - To Do List")

while True:
    print("\n--- To-Do List App ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if tasks:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i+1,".",tasks[i])
        else:
            print("No Tasks found")

    elif choice == "3":
        if tasks:
            
            for i in range(len(tasks)):
                print(i+1,".",tasks[i][0],"-",tasks[i][1])
            num= int(input("Enter task number completed:"))

            if 1<=num<=len(tasks):
                tasks[num-1][1]="DONE"
                print("Tasks marked as done.")
            else:
                print("Invalid task number")
        else:
            
            print("No tasks to mark.")
        

    elif choice == "4":
        if not tasks:
            print("No tasks to delete.")
        else:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                tasks.pop(num-1)
                print("Task deleted.")
            else:
                print("Invalid task number.")

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")

print("---------------------------------------------------------------------------------------------")
