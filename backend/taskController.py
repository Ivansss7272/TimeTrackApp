import datetime
import os
from dotenv import load_dotenv
from typing import List, Optional

load_dotenv()

class Task:
    def __init__(self, id: int, title: str, start_time: datetime.datetime, stop_time: datetime.datetime):
        self.id = id
        self.title = title
        self.start_time = start_time
        self.stop_time = stop_time
        self.duration = self.calculate_duration()

    def calculate_duration(self) -> datetime.timedelta:
        return self.stop_time - self.start_time

class TaskController:
    def __init__(self):
        self.tasks = []
        self.id_counter = 1

    def create_task(self, title: str, start_time: datetime.datetime, stop_time: datetime.datetime) -> Optional[Task]:
        if start_time >= stop_time:
            print("Error: Start time must be before stop time")
            return None
        task = Task(self.id_counter, title, start_time, stop_time)
        self.tasks.append(task)
        self.id_counter += 1
        return task

    def list_tasks(self, date: Optional[datetime.date] = None) -> List[Task]:
        if date:
            return [task for task in self.tasks if task.start_time.date() == date or task.stop_time.date() == date]
        return self.tasks

    def update_task(self, id: int, title: Optional[str] = None, start_time: Optional[datetime.datetime] = None, stop_time: Optional[datetime.datetime] = None) -> bool:
        for task in self.tasks:
            if task.id == id:
                if title:
                    task.title = title
                if start_time and stop_time:
                    if start_time >= stop_time:
                        print("Error: Start time must be before stop time")
                        return False
                    task.start_time = start_time
                    task.stop_time = stop_time
                    task.duration = task.calculate_duration()
                elif start_time:
                    if start_time >= task.stop_time:
                        print("Error: Start time must be before stop time")
                        return False
                    task.start_time = start_time
                    task.duration = task.calculate_duration()
                elif stop_time:
                    if task.start_time >= stop_time:
                        print("Error: Start time must be before stop time")
                        return False
                    task.stop_time = stop_time
                    task.duration = task.calculate_duration()
                return True
        return False

    def delete_task(self, id: int) -> bool:
        for i, task in enumerate(self.tasks):
            if task.id == id:
                del self.tasks[i]
                return True
        return False

def sample_usage():
    controller = TaskController()
    task1 = controller.create_task("Task 1", datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(hours=1))
    if task1:
        print(f"Task created: ID={task1.id}, Title={task1.title}, Duration={task1.duration}")
    else:
        print("Failed to create task.")

sample_usage()