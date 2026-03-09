from pydantic import BaseModel


class start(BaseModel):
    start: int
class moves(BaseModel):
    act: int
