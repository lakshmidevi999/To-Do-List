class ToDoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task[0]} - {'Completed' if task[1] else 'Pending'}")
        else:
            print("Your to-do list is empty.")

    def add_task(self, task_name):
        self.tasks.append([task_name, False])
        print(f"Task '{task_name}' added to your to-do list.")

    def mark_task_completed(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1][1] = True
            print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number.")

    def remove_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task[0]}' removed from your to-do list.")
        else:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()
    while True:
        print("\nOptions:")
        print("1. Display to-do list")
        print("2. Add a task")
        print("3. Mark a task as completed")
        print("4. Remove a task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            task_name = input("Enter task name: ")
            todo_list.add_task(task_name)
        elif choice == '3':
            todo_list.display_tasks()
            task_number = int(input("Enter task number to mark as completed: "))
            todo_list.mark_task_completed(task_number)
        elif choice == '4':
            todo_list.display_tasks()
            task_number = int(input("Enter task number to remove: "))
            todo_list.remove_task(task_number)
        elif choice == '5':
            print("Thank you for using the to-do list application!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
