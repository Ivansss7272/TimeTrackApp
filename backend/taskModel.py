from datetime import datetime, timedelta
from pydantic import BaseModel, validator, ValidationError

class TaskEntry(BaseModel):
    title: str
    start_datetime: datetime
    end_datetime: datetime = None
    
    @property
    def elapsed_time(self):
        if self.end_datetime:
            return self.end_datetime - self.start_datetime
        return None
    
    @validator('end_datetime')
    def end_after_start(cls, value, values, **kwargs):
        if 'start_datetime' in values and value is not None and value < values['start_datetime']:
            raise ValueError("end_datetime must be later than start_datetime")
        return value

if __name__ == "__main__":
    try:
        current_time = datetime.now()
        task_entry = TaskEntry(
            title="New Task", 
            start_datetime=current_time, 
            end_datetime=current_time - timedelta(hours=1)
        )
    except ValidationError as e:
        print(f"Task entry creation failed: {e}")