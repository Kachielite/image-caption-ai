from pydantic.v1 import BaseModel

class Prompt(BaseModel):
    role: str
    content: str


class CaptionRequest(BaseModel):
    image_path: str
    prompt: list[Prompt]