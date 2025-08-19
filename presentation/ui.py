import gradio as gr
import json
from services.caption_service import CaptionService

class CaptionUI:
    def __init__(self, model_name: str):
        self.caption_service = CaptionService(model_name)

    def caption_image(self, image, hint: str = "") -> dict:
        try:
            # Get the JSON string from the caption service
            json_response = self.caption_service.generate_caption(image, hint)

            # Clean up the response - remove markdown code blocks if present
            cleaned_response = self.clean_json_response(json_response)

            # Try to parse the JSON string
            try:
                parsed_json = json.loads(cleaned_response)
                return parsed_json
            except json.JSONDecodeError as e:
                # If JSON parsing fails, return the raw response with an error message
                return {
                    "error": "Invalid JSON response",
                    "raw_response": json_response,
                    "cleaned_response": cleaned_response,
                    "json_error": str(e)
                }
        except Exception as e:
            # Handle any other errors from the caption service
            return {
                "error": "Caption generation failed",
                "error_message": str(e)
            }

    def clean_json_response(self, response: str) -> str:
        """Clean up the JSON response by removing markdown code blocks and extra whitespace"""
        # Strip whitespace
        cleaned = response.strip()

        # Remove markdown code blocks if present
        if cleaned.startswith('```json'):
            # Find the end of the opening code block
            start_idx = cleaned.find('{')
            if start_idx != -1:
                # Find the last closing brace before the closing ```
                if cleaned.endswith('```'):
                    cleaned = cleaned[start_idx:-3].strip()
                else:
                    cleaned = cleaned[start_idx:].strip()
        elif cleaned.startswith('```'):
            # Handle generic code blocks
            lines = cleaned.split('\n')
            if len(lines) > 2:
                # Remove first and last line (code block markers)
                cleaned = '\n'.join(lines[1:-1]).strip()

        return cleaned

    def launch(self):
        interface = gr.Interface(
            fn=self.caption_image,
            inputs=[
                gr.Image(type="filepath"),
                gr.Textbox(label="Hint (optional)", placeholder="Enter a hint about the image")
            ],
            outputs=gr.JSON(label="Product Information"),
            title="AI Product Content Generator",
            description="Upload a product image to generate an optimized title, description, and SEO keywords in JSON format."
        )
        interface.launch()