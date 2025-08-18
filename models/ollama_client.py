import ollama


from schemas.caption_request import CaptionRequest


class OllamaClient:
    def __init__(self, request: CaptionRequest, model: str):
        self.request = request
        self.model = model

    def generate_caption(self):
        print(f"Generating caption using model: {self.model}")
        response = ollama.chat(
            model=self.model,
            messages=self.request.prompt,
            options={"image": self.request.image_path}
        )
        if not response:
            raise ValueError("No response from Ollama API")
        print(f"Response from Ollama: {response}")
        return response['message']['content']