def menu( ):
    option = input("Choose an option by entering the number: 1: Add Task 2: View Task 3: View List 4: Exit ")
    return option
def add_tasks( ):
    while True:
        new_task = input("Enter the task to add or type end to return to menu:").strip().lower()
        if new_task == "end":
            break
        else:
            todo_list.append(new_task)
            
def view_task( ):
    for task in todo_list:
        print("- {}").format(task)
        
def view_list( ):
        print("- {}").format(todo_list)
        
todolist = ["buy clothes", "pay bills", "ring parents"]

while True:
    option =menu()
    
    if option == "1":
        add_tasks()
    
    elif option == "2":
        print("Here is your current task")
        view_task
    elif option == "3":
        print("Here is your to-do list")
        view_list    
    elif option == "4":
        break
    else:
        print("Invalid option. Please try again")
        

        
            
        
    