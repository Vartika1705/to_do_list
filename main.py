class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def complete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task marked as completed.")
        else:
            print("Task not found in the to-do list.")

todo_list = ToDoList()