from models.ollama_client import OllamaClient
from schemas.caption_request import CaptionRequest, Prompt


class CaptionService:
    def __init__(self, model:str):
        self.client = OllamaClient(model)

    @staticmethod
    def get_system_prompt() -> str:
        return (
            "You are an AI product content generator for e‑commerce images. "
            "Given a product image (and optional user hint), produce:\n"
            "1. A concise, compelling, keyword‑rich product title (<= 60 characters) suitable for online marketplaces.\n"
            "2. A persuasive, factual product description (120-200 words) covering: visible materials, form factor, key features, "
            "benefits, use cases, target audience, differentiators. Do not invent specs you cannot see; if uncertain, use generic but honest descriptors.\n"
            "3. 8-12 high‑value SEO keywords (single or short multi‑word phrases) in an array (no duplicates, lowercase, no filler words).\n"
            "Rules:\n"
            "- American English.\n"
            "- No exaggerated claims (avoid words like 'best', 'ultimate').\n"
            "- Sentence case for title; no trailing period in title.\n"
            "- Do not mention the analysis process.\n"
            "- If image lacks detail, acknowledge limits briefly.\n"
            "Output strict JSON with keys: title (string), description (string), keywords (array of strings)."
        )

    @staticmethod
    def get_user_prompt(image_path: str) -> str:
        user_instructions = (
            f"Analyze the product shown in the image at path: {image_path}.\n"
            "Return ONLY the JSON object (no markdown, no extra text).\n"
        )
        user_instructions += "Generate the JSON now."
        return user_instructions

    def generate_caption(self, image_path: str) -> str:
        system_prompt = Prompt(
            role="system",
            content=self.get_system_prompt()
        )
        user_prompt = Prompt(
            role="user",
            content=self.get_user_prompt(image_path)
        )
        request = CaptionRequest(image_path=image_path, prompt=[system_prompt, user_prompt])
        return self.client.generate_caption(request)