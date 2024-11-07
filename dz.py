from datetime import datetime

class Task:
    def __init__(self, title, description, deadline):
        self.title = title  
        self.description = description  
        self.deadline = deadline  
        self.is_completed = False  

    def mark_as_completed(self):
        self.is_completed = True  

    def __str__(self):
        return f"Завдання: {self.title}\nОпис: {self.description}\nДедлайн: {self.deadline}\nСтатус: {'Виконано' if self.is_completed else 'Не виконано'}"

class TaskManager:
    def __init__(self):
        self.tasks = []  

    def add_task(self, task):
        self.tasks.append(task)  

    def remove_task(self, task_title):
        self.tasks = [task for task in self.tasks if task.title != task_title]

    def mark_task_as_completed(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                task.mark_as_completed()
                return f"Завдання '{task_title}' виконане."
        return f"Завдання з назвою '{task_title}' не знайдено."

    def list_tasks(self):
        if not self.tasks:
            return "Немає завдань."
        return "\n\n".join(str(task) for task in self.tasks)

task_manager = TaskManager()

task1 = Task("Завершити проект", "Необхідно завершити проект до кінця тижня", "2024-11-10")
task2 = Task("Прочитати книгу", "Прочитати книгу до кінця місяця", "2024-11-30")
task3 = Task("Вивчити Python", "Вивчити основи Python", "2024-12-15")

task_manager.add_task(task1)
task_manager.add_task(task2)
task_manager.add_task(task3)

print("Список завдань:")
print(task_manager.list_tasks())

print("\n" + task_manager.mark_task_as_completed("Завершити проект"))

print("\nОновлений список завдань:")
print(task_manager.list_tasks())

task_manager.remove_task("Прочитати книгу")

print("\nОстаточний список завдань:")
print(task_manager.list_tasks())
