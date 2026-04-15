# Input Popup Boxes
import customtkinter as ctk

ctk.set_appearance_mode("black")
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
root.title("Alpha")
root.iconbitmap("icon_2.ico")
root.geometry("800x800")


def input_popup():
    dialog = ctk.CTkInputDialog(
        text="What is your name?",
        # text_color="red", dont work idk
        title="Hello There",
        fg_color="pink",
        button_fg_color="red",
        button_text_color="black",
        button_hover_color="white",
        entry_fg_color="white",
        entry_text_color="black",
        entry_border_color="red",
    )
    thing = dialog.get_input()
    if thing:
        my_label.configure(text=f"Hello {thing}")
    else:
        my_label.configure(text="Please enter a name")


my_button = ctk.CTkButton(
    root,
    text="Click me",
    command=input_popup,
    corner_radius=20,
)
my_button.pack(pady=40)
my_label = ctk.CTkLabel(root, text="")
my_label.pack(pady=10)


root.mainloop()
