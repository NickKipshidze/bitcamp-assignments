import tkinter, customtkinter, time
from random import choice

def genascii(start: int, end: int) -> str: 
    return [chr(char) for char in range(start, end+1)]

WIDTH: int = 512
HEIGHT: int = 256

settings = {
    "password_length": 8, 
    "letters_upper": True, 
    "letters_lower": True, 
    "numbers": True, 
    "symbols": True
}

LETLOWER: list = genascii(97, 122)
LETUPPER: list = genascii(65, 90)
LETTERS: list = LETUPPER + LETLOWER
NUMBERS: list = genascii(48, 57)
SYMBOLS: list = genascii(33, 47)+genascii(58, 64)+genascii(91, 96)+genascii(123, 126)

def generate_password(
        length: int = 4, 
        letters_upper: bool = True, 
        letters_lower: bool = True, 
        numbers: bool = True, 
        symbols: bool = True
    ) -> str:

    random_range = []

    if letters_upper:
        random_range += LETUPPER
    if letters_lower:
        random_range += LETLOWER
    if numbers:
        random_range += NUMBERS
    if symbols:
        random_range += SYMBOLS

    return "".join([choice(random_range) for _ in range(length)])

def display_password(
        label: tkinter.Label, 
        button: tkinter.Button, 
        settings: dict
    ) -> None:

    button["state"] = tkinter.DISABLED
    label.clipboard_clear()

    for char in label.cget("text"):
        label.configure(
            text=label.cget("text")[:-2]
        )

        time.sleep(0.05)
        label.update()

    for char in generate_password(
        settings["password_length"], 
        settings["letters_upper"], 
        settings["letters_lower"], 
        settings["numbers"], 
        settings["symbols"]
    ):
        label.configure(
            text=label.cget("text")+char
        )

        time.sleep(0.05)
        label.update()

    button["state"] = tkinter.ACTIVE

def set_setting(
        value: any, 
        key: str, 
        settings_menu: tkinter.Menu = None
    ) -> None:
    global settings
    settings[key] = value

    if type(value) == bool:
        if key == "letters_lower": index = 1
        if key == "letters_upper": index = 2
        if key == "numbers": index = 3
        if key == "symbols": index = 4
        settings_menu.entryconfigure(index, label=["add ", "remove "][int(value)] + " ".join(settings_menu.entrycget(index, option="label").split(" ")[1:]))

def main() -> None:
    root = tkinter.Tk()
    root.title("Nick's Password Generator")
    root.geometry(f"{WIDTH}x{HEIGHT}")
    root.config(background = "#FFFFFF")

    menubar = tkinter.Menu(root)

    settings_menu = tkinter.Menu(menubar, tearoff=0)

    length_menu = tkinter.Menu(settings_menu, tearoff=0)
    length_menu.add_command(label="6", command=lambda: set_setting(6, "password_length"))
    length_menu.add_command(label="8", command=lambda: set_setting(8, "password_length"))
    length_menu.add_command(label="10", command=lambda: set_setting(10, "password_length"))
    length_menu.add_command(label="12", command=lambda: set_setting(12, "password_length"))
    length_menu.add_command(label="14", command=lambda: set_setting(14, "password_length"))

    settings_menu.add_cascade(label="Length", menu=length_menu)

    settings_menu.add_command(label="remove lower letters", command=lambda: set_setting(not settings["letters_lower"], "letters_lower", settings_menu))
    settings_menu.add_command(label="remove upper letters", command=lambda: set_setting(not settings["letters_upper"], "letters_upper", settings_menu))
    settings_menu.add_command(label="remove numbers", command=lambda: set_setting(not settings["numbers"], "numbers", settings_menu))
    settings_menu.add_command(label="remove symbols", command=lambda: set_setting(not settings["symbols"], "symbols", settings_menu))

    password_menu = tkinter.Menu(menubar, tearoff=0)
    password_menu.add_command(label="Copy to clipboard", command=lambda: root.clipboard_append(lbl_password._text))

    menubar.add_cascade(label="Settings", menu=settings_menu)
    menubar.add_cascade(label="Password", menu=password_menu)

    lbl_title = tkinter.Label(
        root, 
        text="🔒 Nick's Password Generator 🔒", 
        bg="#FFFFFF", 
        font=("Monospace", 16)
    )
    lbl_password = customtkinter.CTkLabel(
        root, 
        text=". . .",
        bg_color="#FFFFFF", 
        fg_color="#000000", 
        corner_radius=8,
        font=("Monospace", 26), 
        padx=50, pady=10
    )
    btn_generate = customtkinter.CTkButton(
        root, 
        text="Generate Password",
        corner_radius=16,
        font=("Monospace", 26), 
        command=lambda: display_password(lbl_password, btn_generate, settings)
    )

    lbl_title.pack(expand=True)
    lbl_password.pack(expand=True)
    btn_generate.pack(expand=True)

    root.config(menu=menubar)
    root.mainloop()

if __name__ == "__main__":
    main()