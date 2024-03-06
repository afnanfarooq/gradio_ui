import gradio as gr

def print_text(text):
    print(text)
    return ""

iface = gr.Interface(fn=print_text, inputs="text", outputs=None, title="Text Printer")
iface.launch()
