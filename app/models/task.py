from .. import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), nullable=False)
    task_title = db.Column(db.String(20), nullable=False)
    
    