from pydantic import BaseModel

class Sales(BaseModel):
    name: str
    year: int
    month: str
    sales: int
