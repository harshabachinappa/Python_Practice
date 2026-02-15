class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task): #add task function
        self.tasks.append({"task": task, "completed": False})
        print("Task added successfully!")

    def remove_task(self, task): #remove task function
        for i in self.tasks:
            if i["task"] == task:
                self.tasks.remove(i)
                print("Task removed successfully!")
                return
        print("Task not found in the list.")

    def mark_completed(self, task): #task mark completed function
        for i in self.tasks:
            if i["task"] == task:
                i["completed"] = True
                print("Task marked as completed!")
                return
        print("Task not found in the list.")

    def display_tasks(self): #display all tasks function
        if self.tasks:
            print("Tasks:")
            for i, j in enumerate(self.tasks, start=1):
                status = "Completed" if j["completed"] else "Not Completed"
                print(f"{i}. {j['task']} - {status}")
        else:
            print("No tasks in the list.")

def main(): 
    todo_list = TodoList()
    
    while True:
        print("\nTODO LIST MENU:")
        print("1. Add a new task")
        print("2. Remove a task")
        print("3. Mark task as completed")
        print("4. Display tasks")
        print("5. Close")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            task = input("Enter a task to add: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter a task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            task = input("Enter task to mark as completed: ")
            todo_list.mark_completed(task)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            print("Closing")
            break
        else:
            print("Invalid choice. Please enter a valid choice.")
main() #calling main
