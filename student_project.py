"""
Lists
Student Project
Project Title:
"""

names = []
tasks = []
status = []

print("Welcome to the Group Task Planner, a program to manage group projects")
new_task = input("\nThere are currently no tasks, please input a new task: ")
task_status = "INCOMPLETE"
tasks.append(new_task)
status.append(task_status)
person = input("Which member will be assigned this task?: ")
names.append(person)

## -- A while loop for the program to always ask for user input -- ##
while True:
    print("\nHere are your teams current tasks:")
    ## -- A for range loop is used in order to iterate through the Tasks list and print all of the elements -- ##
    for i in range(len(tasks)):
        print(names[i] + ": " + tasks[i] + "(" + status[i] + ")")
    
    action = input("\nEnter \"add\" to add a task, \"upd\" to update a task, or \"exit\" to quit: ")
## -- Breaks the while loop and ends the program -- ##
    if action.lower() == "exit":
        break

## -- If the user chooses to add a new task, the program asks for a description of the task and a person to assign it to --##
    if action.lower() == "add":
        new_task = input("Enter your new task: ")
        task_status = "INCOMPLETE"
        tasks.append(new_task)
        status.append(task_status)
        person = input("Which member will be assigned this task?: ")
        names.append(person)

## -- If the user chooses to update a task, the program will ask to enter a number based on the position of the task before displaying the choices -- ##
    if action.lower() == "upd":
    ## -- The task_selection variable represents the index of the task in the Tasks list -- ##
        task_selection = int(input("Please choose a task (1 for the first task, etc): "))
        task_selection -= 1
        task_action = input("Enter \"mod\" to modify task description or person, \"del\" to delete the task, or \"com\" to complete the task: ")
    
    ## -- This action allows the user to update the description of a task or reassign the task to a new person -- ##
        if task_action.lower() == "mod":
            mod_choice = input("Enter \"des\" to change task description, or \"per\" to assign to a different person: ")
        ## -- In order to replace the strings, the insert method is used to insert an element using the task_selection variable as the index. -- ##
        ## -- The delete method is used afterward in order to delete the old string that was moved over by incrementing task_selection by one -- ##
            if mod_choice.lower() == "des":
                task_name = input("Enter a new task description: ")
                tasks.insert(task_selection, task_name)
                del tasks[task_selection + 1]
        ## -- Else clause used for names instead of task descriptions -- ##
            else:
                rename = input("Enter the name of the member to reassign: ")
                names.insert(task_selection, rename)
                del names[task_selection + 1]   
    ## -- This action deletes a task using delete method and the task_selection variable as the index -- ##
        if task_action.lower() == "del":
            del names[task_selection]
            del tasks[task_selection]
            del status[task_selection]
    ## This action changes the status of a task to complete, using the same process as the mod choice, and using the Status list instead -- ##
        if task_action.lower() == "com":
            status.insert(task_selection, "COMPLETE")
            del status[task_selection + 1]