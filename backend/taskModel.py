from datetime import datetime
from pydantic import BaseModel, validator

class Task(BaseModel):
    title: str
    start_time: datetime
    stop_time: datetime = None
    
    @property
    def duration(self):
        if self.stop_time:
            return self.stop_time - self.start_time
        return None
    
    @validator('stop_time')
    def validate_times(cls, v, values, **kwargs):
        if 'start_time' in values and v is not None and v < values['start_time']:
            raise ValueError("stop_time must be after start_time")
        return v