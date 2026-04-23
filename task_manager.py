from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, title):
        new_task = Task(title)
        self.tasks.append(new_task)
        print(f"✓ Aufgabe '{title}' wurde hinzugefügt!")
    
    def list_tasks(self):
        if not self.tasks:
            print("Keine Aufgaben vorhanden.")
            return
        
        for i, task in enumerate(self.tasks):
            status = "✅" if task.is_completed else "❌"
            print(f"{i+1}. [{status}] {task.title}")
    
    def complete_task(self, index):
        task_index = index - 1
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].is_completed = True
            print(f"✓ Aufgabe '{self.tasks[task_index].title}' wurde erledigt!")
        else:
            print("❌ Ungültige Aufgabennummer!")
    
    def delete_task(self, index):
        task_index = index - 1
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"✓ Aufgabe '{removed_task.title}' wurde gelöscht!")
        else:
            print("❌ Ungültige Aufgabennummer!")