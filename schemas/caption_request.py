from typing import Optional

from pydantic.v1 import BaseModel

class Prompt(BaseModel):
    role: str
    content: str
    images: Optional[list[str]] = None  # Optional image path for the prompt, if needed


class CaptionRequest(BaseModel):
    prompt: list[Prompt]