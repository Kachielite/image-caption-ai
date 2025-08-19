# ImageCaption

ImageCaption is a learning project aimed at exploring the use of open-source Large Language Models (LLMs) from Hugging Face and related ecosystems for image captioning. The project demonstrates how to build a modular, Python-based web app that generates captions for images using state-of-the-art models.

## Features
- Upload images and receive AI-generated captions
- Optional hint input to guide caption generation
- Modular architecture (UI, service, model, schema)
- Easily extendable to support different captioning models

## Project Structure
```
app.py                  # Main entry point for the application
requirements.txt        # Python dependencies
models/                 # Model clients and related code
presentation/           # UI layer (Gradio interface)
schemas/                # Data schemas (e.g., caption request)
services/               # Business logic (caption generation)
```

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd ImageCaption
```

### 2. Create a Virtual Environment (Recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Ollama Locally
This project uses [Ollama](https://ollama.com/) to run open-source LLMs locally. Follow these steps:

1. **Install Ollama:**
   - On macOS:
     ```bash
     brew install ollama
     ollama serve &
     ```
   - Or download from [Ollama Downloads](https://ollama.com/download)

2. **Pull the LLaVA Model:**
   - LLaVA is a vision-language model for image captioning. To pull it:
     ```bash
     ollama pull llava
     ```
   - This will download the model and make it available for local inference.

### 5. Run the Application
```bash
python app.py
```

This will start the Gradio web interface. Open the provided URL in your browser to use the app.

## Usage
- Upload an image using the web interface.
- (Optional) Enter a hint to guide the caption generation.
- Click the button to generate a caption.
- The AI-generated caption will be displayed below the image.

## Customization
- To use a different model, modify the `model_name` parameter in the UI or service layer.
- Extend the `models/` directory to add new model clients.

## File Overview
- `app.py`: Launches the Gradio interface and wires up the UI.
- `presentation/ui.py`: Contains the Gradio UI logic and input/output handling.
- `services/caption_service.py`: Handles caption generation logic and model interaction.
- `models/ollama_client.py`: Example model client (replace or extend as needed).
- `schemas/caption_request.py`: Data schema for caption requests.

## Requirements
- Python 3.8+
- Ollama (for local LLM inference)
- See `requirements.txt` for Python package dependencies

## License
Specify your license here (e.g., MIT, Apache 2.0, etc.)

## Acknowledgements
- [Gradio](https://gradio.app/) for the web UI
- [Ollama](https://ollama.com/) for local LLM serving
- [Hugging Face](https://huggingface.co/) for open-source models

---
Feel free to modify this README to better fit your project's specifics.
