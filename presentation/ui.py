import gradio as gr
from services.caption_service import CaptionService

class CaptionUI:
    def __init__(self, model_name: str):
        self.caption_service = CaptionService(model_name)

    def caption_image(self, image):
        return self.caption_service.generate_caption(image)

    def launch(self):
        interface = gr.Interface(
            fn=self.caption_image,
            inputs=gr.Image(type="filepath"),
            outputs="text",
            title="Image Captioning with Ollama",
            description="Upload an image and get a detailed description."
        )
        interface.launch()