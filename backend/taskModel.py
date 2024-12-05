from datetime import datetime
from pydantic import BaseModel, validator, ValidationError

class Task(BaseModel):
    title: str
    start_time: datetime
    stop_time: datetime = None
    
    @property
    def duration(self):
        try:
            if self.stop_time:
                return self.stop_time - self.start_time
        except TypeError as e:
            print(f"Error calculating duration: {e}")
        return None
    
    @validator('stop_time')
    def validate_times(cls, v, values, **kwargs):
        try:
            if 'start_time' in values and v is not None and v < values['start_time']:
                raise ValueError("stop_time must be after start_time")
        except ValueError as e:
            print(f"Validation Error: {e}")
            raise  
        return v

if __name__ == "__main__":
    try:
        task = Task(title="New Task", start_time=datetime.now(), stop_time=datetime.now() - datetime.timedelta(hours=1))
    except ValidationError as e:
        print(f"Task creation failed: {e}")