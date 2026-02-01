from task_manager.extensions import db
from sqlalchemy.sql import func
class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(), nullable = False)
    description = db.Column(db.Text, nullable = True)
    status = db.Column(db.Boolean, default = False)
    
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    due_date = db.Column(db.Date, nullable = True)


    def __repr__(self):
        return f"<Task {self.id}- {self.title}"