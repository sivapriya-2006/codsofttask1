class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added successfully!')

    def view_tasks(self):
        if not self.tasks:
            print('No tasks found. Your to-do list is empty.')
        else:
            print('Your To-Do List:')
            for index, task in enumerate(self.tasks, start=1):
                print(f'{index}. {task}')

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            completed_task = self.tasks.pop(task_index - 1)
            print(f'Task "{completed_task}" marked as completed!')
        else:
            print('Invalid task index. Please enter a valid task index.')

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            deleted_task = self.tasks.pop(task_index - 1)
            print(f'Task "{deleted_task}" deleted successfully!')
        else:
            print('Invalid task index. Please enter a valid task index.')


def main():
    todo_list = TodoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_index = int(input("Enter the task index to mark as completed: "))
            todo_list.mark_completed(task_index)
        elif choice == '4':
            task_index = int(input("Enter the task index to delete: "))
            todo_list.delete_task(task_index)
        elif choice == '5':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
