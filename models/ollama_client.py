import ollama


from schemas.caption_request import CaptionRequest


class OllamaClient:
    def __init__(self, model:str):
        self.model = model

    def generate_caption(self, request: CaptionRequest):
        print(f"Generating caption using model: {self.model}")
        response = ollama.chat(
            model=self.model,
            messages=request.prompt,
            options={"image": request.image_path}
        )
        if not response:
            raise ValueError("No response from Ollama API")
        print(f"Response from Ollama: {response}")
        return response['message']['content']