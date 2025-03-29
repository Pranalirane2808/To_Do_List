class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        return self.tasks

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        return self.tasks

    def get_tasks(self):
        return self.tasks
