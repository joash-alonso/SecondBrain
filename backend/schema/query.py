from pydantic import BaseModel
from datetime import datetime

class Query(BaseModel):
    query: str
    created_date: datetime.datetime
