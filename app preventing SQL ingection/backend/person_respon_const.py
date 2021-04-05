from fastapi import Path, Body
from pydantic import BaseModel, Field
from typing import List, Optional

class Person_res(BaseModel):
    name: str
    age: int