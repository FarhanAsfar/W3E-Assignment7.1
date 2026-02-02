from task_manager.extensions import db
from sqlalchemy.sql import func
import enum

class TaskStatus(enum.Enum):
    TODO = "todo"
    IN_PROGRESS = "in progress"
    DONE = "done"
    
class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(), nullable = False)
    description = db.Column(db.Text, nullable = True)
    status = db.Column(db.Enum(TaskStatus), name="task_status", nullable=False, default = TaskStatus.TODO)
    
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    due_date = db.Column(db.Date, nullable = True)


    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status.value,
            "due_date": self.due_date,
            "created_at": self.created_at,
        }
    
    def __repr__(self):
        return f"<Task {self.id}- {self.title}"