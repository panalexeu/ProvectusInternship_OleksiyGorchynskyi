from pydantic import BaseModel


class Prompt(BaseModel):
    content: list
