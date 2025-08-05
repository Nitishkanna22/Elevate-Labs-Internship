tasks = []

def addTask():
    task = input("Enter your task: ")
    tasks.append(task)
    print(f"Task '{task}' is added to the list")

def deleteTask():
    if not tasks:
        print("No tasks available to delete")
        return
    
    print("Current tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    
    task = input("Enter the task to be deleted: ")
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' is deleted from the list")
    else:
        print("The task you have entered is not found")

def showTask():
    if not tasks:
        print("No tasks in your list")
    else:
        print("Your current tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def Exit():
    print("Exiting the application...")
    print("Thank you for using the Task Manager!")

is_running = True

while is_running:
    print()
    print("**********************")
    print("Enter 1 to insert a task")
    print("Enter 2 to delete a task")
    print("Enter 3 to show tasks")
    print("Enter 4 to exit")
    print("**********************")

    try:
        option = int(input("Enter your option (1-4): "))

        if option == 1:
            addTask()

        elif option == 2:
            deleteTask()

        elif option == 3:
            showTask()

        elif option == 4:
            Exit()
            is_running = False

        else:
            print("Invalid option! Please enter a number between 1-4")

    except ValueError:
        print("Invalid input! Please enter a valid number")