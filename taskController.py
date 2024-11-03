import datetime
from typing import List, Optional

class Task:
    def __init__(self, title, start_time, stop_time):
        self.id = id(self)
        self.title = title
        self.start_time = start_time
        self.stop_time = stop_time
        self.validate_times()
        self.duration = self.calculate_duration()

    def calculate_duration(self):
        return self.stop_time - self.start_time

    def validate_times(self):
        if self.start_time >= self.stop_time:
            raise ValueError("Start time must be before stop time.")

class TaskController:
    def __init__(self):
        self.tasks = []

    def create_task(self, title: str, start_time: datetime.datetime, stop_time: datetime.datetime) -> Task:
        try:
            new_task = Task(title, start_time, stop_time)
            self.tasks.append(new_task)
            return new_task
        except ValueError as e:
            print(f"Error creating task: {e}")
            return None

    def get_tasks(self, date: Optional[datetime.date] = None) -> List[Task]:
        if date:
            return [task for task in self.tasks if task.start_time.date() == date or task.stop_time.date() == date]
        return self.tasks

    def update_task(self, task_id: int, title: Optional[str] = None,
                    start_time: Optional[datetime.datetime] = None,
                    stop_time: Optional[datetime.datetime] = None) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                if title:
                    task.title = title
                if start_time:
                    task.start_time = start_time
                if stop_time:
                    task.stop_time = stop_time
                try:
                    task.validate_times()
                    task.duration = task.calculate_duration()
                    return task
                except ValueError as e:
                    print(f"Error updating task {task_id}: {e}")
                    return None
        print(f"Task with id {task_id} not found.")
        return None

    def delete_task(self, task_id: int) -> bool:
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                return True
        print(f"Task with id {task_id} not found.")
        return False

if __name__ == "__main__":
    controller = TaskController()
    try:
        task1 = controller.create_task("Task 1", datetime.datetime(2023, 1, 1, 9), datetime.datetime(2023, 1, 1, 17))
        task2 = controller.create_task("Task 2", datetime.datetime(2023, 1, 2, 10), datetime.datetime(2023, 1, 2, 15))
        tasks_for_today = controller.get_tasks(datetime.date.today())
        all_tasks = controller.get_tasks()
        controller.update_task(task1.id, start_time=datetime.datetime(2023, 1, 1, 8))
        controller.delete_task(task2.id)
    except Exception as e:
        print(f"An error occurred: {e}")