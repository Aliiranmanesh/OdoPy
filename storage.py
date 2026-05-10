import json
import os

class Storage:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
    
    def save(self, tasks):
        data = []
        for task in tasks:
            data.append({
                "title": task.title,
                "is_completed": task.is_completed
            })
        
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    
    def load(self):
        if not os.path.exists(self.filename):
            return []
        
        with open(self.filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        from task import Task
        tasks = []
        for item in data:
            task = Task(item["title"])
            task.is_completed = item["is_completed"]
            tasks.append(task)
        
        return tasks


