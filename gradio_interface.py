from gradio import Interface, Textbox

def greet(name):
    return "Hello, " + name + "!"

iface = Interface(
    fn=greet, 
    inputs=Textbox(label="Name"), 
    outputs="text"
)

iface.launch(share=False)