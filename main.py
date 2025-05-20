import csv

class Task:
    def __init__(self, description, status = "Not completed"):
        self.description = description
        self.status = status

    def __str__(self):
        status_task = '✅' if self.status == "Completed" else '❌'
        return f"Description: {self.description} - Status: {self.status} {status_task}"
    
# --- Start Add Task Function ---
tasks = []
def add_task():
    description  = input("Enter a description of your task: ")
    #check tasks is not empty
    if not description:
        print("Please list your tasks for the day 🌟")
        return
    # Create object from class Task
    task = Task(description)
    tasks.append(task )
    print("\nTask added successfully ✅\n")
    #print(task )
    save_tasks_to_file()
#add_task()
# --- End Add Task Function ---

# --- Start View Task Function ---
def view_tasks():
    if not tasks:
        print("\n No tasks available, enter option 1 to add task")
    else:
        print("\nList of Tasks:\n")
        #enumerate() adds a counter as the key of the enumerate object.
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
#view_tasks()
# --- End View Task Function ---


def mark_tasks_as_Completed():
    # Call view_tasks() to display all tasks
    view_tasks()
    description_id = int(input("Enter the id of description tasks to mark as completed: "))
    # -1 => because I start from 1 
    tasks[description_id - 1].status = "Completed"
    print(f"\nTask {description_id} has been marked as completed ✅")
    save_tasks_to_file()
    #view_tasks()

# add_task()  
# mark_tasks_as_Completed()  
# --- End Mark Tasks as Completed ---

# --- Start Delete Tasks ---
def delete_task():
    view_tasks()
    description_id_to_del = int(input("Enter the id of description tasks you want deleted: "))
    # del keyword is used to delete objects
    del tasks[description_id_to_del -1]
    print(f"\nTask {description_id_to_del} has been deleted.")
    save_tasks_to_file()
# --- End Delete Tasks ---


# --- Start Save Tasks to CSV File ---
def save_tasks_to_file():
    with open("tasks.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["description", "status"])  # Write header row
        for task in tasks:
            writer.writerow([task.description, task.status])
    print("Tasks have been saved to tasks.csv.")
# --- End Save Tasks to CSV File ---


# --- Start writing to tasks .csv file ---
def load_tasks_from_file():
    try:
        with open("tasks.csv", mode="r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                description, status = row
                tasks.append(Task(description, status))
    except FileNotFoundError:
        print("No previous tasks found, starting fresh.")
# --- End writing to tasks .csv file ---

def main():
    while True:
        print("\n💫 Welcome, write your tasks for the day 💫 ")
        print("\n Select one of the following options\n")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            add_task()  
        elif choice == '2':
            view_tasks()  
        elif choice == '3':
            mark_tasks_as_Completed()  
        elif choice == '4':
            delete_task()  
        elif choice == '5':
            print("Exiting the app 👋🏻")
            break  # الخروج من البرنامج
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()