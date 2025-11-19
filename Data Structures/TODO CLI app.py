print("Welcome to Muiz's Todo App where you can make your very own todo list\n " \
"Here to help your productivity")
name = input("Hello, What's your name: ")
print(f"Welcome {name}, let's get to making your very own todo list")

def add_task():
    """This function requests a task as input from the user and adds it to a dictionary of tasks
    whose key is the nominal order by  which it is entered by the user 
    i.e 1 for the first 2 for the 2nd etcetera .
    The values of the dictionary are a list that contains the task itself and the completion 
    status(Completed or Uncompleted)"""
    i = 0
    while True:
        user_tasks_and_status = []
        task = input("Enter your task :")
        user_tasks_and_status.append(task)
        user_tasks_and_status.append( "Uncompleted")
        user_tasks[i] = user_tasks_and_status
        i += 1
        continuance = input("Would you like to add another task? y/n ")
        if continuance == "n":
            break
def view_tasks():
    """This function prints the user_tasks and completion status 
    to the screen in a standard format"""
    print(f"{name}'s Todo List")
    print(" __Task--------------------------------Status__")
    for task_index, task in user_tasks.items():
        print(f"{task_index}. {task[0]}     {task[1]}")
def update_task():
    """This function updates the status of a previously entered task to completed"""
    while True:
        task_no = int(input("Enter the index no. of the task you want to update:"))
        user_tasks[task_no][1] ="Completed"
        print("Task Updated Successfully")
        continuance = input("Do you have any more tasks to update:")
        if continuance == "n":
            break
def delete_task():
     """This function deletes a task completely"""
     task_no = input("Enter the index no. of the task you want to delete:")
     del user_tasks[int(task_no)]
     print("Task Deleted Successfully")

user_tasks = {}
while True:
    print("""=== TODO APP ===
1. Add a task
2. View tasks
3. Mark task as done
4. Delete a task
5. Exit""")
    action = input("""Which of these would you like to do today?
Enter the number that corresponds to it on the menu: """)
   
    if action == "1":
        add_task()
    elif action == "2":
        view_tasks()
    elif action == "3":
       update_task()
    elif action == "4" :
       delete_task()
    elif action == "5":
        break
    else:
       print("Invalid entry")