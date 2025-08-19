from presentation.ui import CaptionUI


if __name__ == "__main__":
    model_name = "llava"
    app_ui = CaptionUI(model_name)
    app_ui.launch()