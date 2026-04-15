# New Top Level Windows
import customtkinter as ctk

ctk.set_appearance_mode("black")
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
root.title("Alpha")
root.iconbitmap("icon_2.ico")
root.geometry("400x200")


def new():
    new_window = ctk.CTkToplevel(root, fg_color="white")
    new_window.title("This is new window")
    new_window.geometry("400x200")
    new_window.resizable(False, False)

    def close():
        new_window.destroy()
        new_window.update()

    new_button = ctk.CTkButton(
        new_window,
        text="Click me",
        command=close,
    )
    new_button.pack(pady=40)


my_button = ctk.CTkButton(root, text="Open New Top Level Window", command=new)
my_button.pack(pady=20)


root.mainloop()
