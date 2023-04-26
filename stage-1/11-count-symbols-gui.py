import tkinter

root = tkinter.Tk()
root.title("")
root.geometry("512x512")
root.configure(background="#b5ffa8")
root.resizable(False, False)

def update_label():
    text = input_box.get()

    length_label.config(text = f"{text} has {len(text)} characters.")
    length_label.place(x = 256-length_label.winfo_width()//2)

    if len(text) < 1:
        length_label.config(text = "აუცილებელია რაიმე შეიყვანო")

input_label = tkinter.Label(root, text="What is the input string? ", bg="#b5ffa8", font=("Monospace", 16))
input_box = tkinter.Entry(root, font=("Monospace", 16))

length_label = tkinter.Label(root, text="(:", font=("Monospace", 16), bg="#b5ffa8")

input_label.place(x=100, y=10)
input_box.place(x=125, y=100)

length_label.place(x=256-length_label.winfo_width()//2, y=300)

while True:
    root.update()
    update_label()