from pydantic.v1 import BaseModel


class CaptionRequest(BaseModel):
    image_path: str
    prompt: str