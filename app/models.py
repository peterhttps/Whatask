from datetime import datetime

class Task:
    def __init__(self, id, title, description, is_completed=False, created_at=None, completed_at=None):
        self.id = id
        self.title = title
        self.description = description
        self.is_completed = is_completed
        self.created_at = created_at if created_at else datetime.now()
        self.completed_at = completed_at
