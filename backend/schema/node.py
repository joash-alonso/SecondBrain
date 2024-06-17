from pydantic import BaseModel
from datetime import datetime
from typing import List

class Node(BaseModel):
    id: int
    title: str
    text: str
    updated_date: datetime.datetime
    keyword: List[str]
