from database import sessionLocal
from models import Tasks

tasks = [
    Tasks(id=1, title='task1', done=False),
    Tasks(id=2, title='task2', done=False),
    Tasks(id=3, title='task3', done=True),     
]

db = sessionLocal()

db.add_all(tasks)
db.commit()