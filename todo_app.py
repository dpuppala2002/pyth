import argparse

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task_index):
        if task_index >= 0 and task_index < len(self.tasks):
            del self.tasks[task_index]
        else:
            print("Task index out of range.")

    def complete_task(self, task_index):
        if task_index >= 0 and task_index < len(self.tasks):
            self.tasks[task_index] += " [Completed]"
        else:
            print("Task index out of range.")

    def show_tasks(self):
        if self.tasks:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("No tasks in the list.")

def main():
    parser = argparse.ArgumentParser(description="ToDo List Application")
    parser.add_argument("--add", nargs='+', help="Add new task(s)")
    parser.add_argument("--delete", type=int, help="Delete task by index")
    parser.add_argument("--complete", type=int, help="Mark task as completed by index")
    args = parser.parse_args()

    todo_list = ToDoList()

    if args.add:
        for task in args.add:
            todo_list.add_task(task)
        todo_list.show_tasks()  # Show tasks after adding
    elif args.delete is not None:
        todo_list.delete_task(args.delete - 1)  # Adjust index for zero-based indexing
    elif args.complete is not None:
        todo_list.complete_task(args.complete - 1)  # Adjust index for zero-based indexing
    else:
        todo_list.show_tasks()

if __name__ == "__main__":
    main()
