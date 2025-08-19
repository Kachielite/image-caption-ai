import ollama


from schemas.caption_request import CaptionRequest


class OllamaClient:
    def __init__(self, model:str):
        self.model = model

    def generate_caption(self, request: CaptionRequest):
        print(f"Generating caption using model: {self.model}")
        print(f"Request prompt: {request.prompt}")
        try:
            response = ollama.chat(
                model=self.model,
                messages=request.prompt,
            )
        except Exception as e:
            print(f"Ollama API call failed: {e}")
            raise
        print(f"Response from Ollama: {response}")
        if not response:
            raise ValueError("No response from Ollama API")
        if 'message' not in response or 'content' not in response['message']:
            raise ValueError(f"Malformed response from Ollama: {response}")
        content = response['message']['content']
        if not content or not content.strip():
            raise ValueError(f"Ollama returned empty content. Full response: {response}")
        return content
