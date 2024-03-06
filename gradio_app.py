import gradio as gr

def print_content(content):
    if isinstance(content, str):
        print("Text input:", content)
        return ""
    elif isinstance(content, gr.inputs.Image):
        print("Image input:", content)
        return content

interface = gr.Interface(fn=print_content, inputs=["text", "image"], outputs=["text", "image"], title="Text and Image Printer")
interface.launch()
