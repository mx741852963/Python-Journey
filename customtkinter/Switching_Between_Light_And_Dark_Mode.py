# Switching Between Light And Dark Mode
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
alpha = ctk.CTk()
alpha.title("Alpha")
alpha.iconbitmap("icon_2.ico")
alpha.geometry("800x800")

mode = "dark"


def change_colors(choice):
    ctk.set_appearance_mode(choice)


def change():
    global mode
    if mode == "dark":
        ctk.set_appearance_mode("light")
        mode = "light"
        my_text.delete(0.0, "end")
        my_text.insert("end", mode)
    else:
        ctk.set_appearance_mode("dark")
        mode = "dark"
        my_text.delete(0.0, "end")
        my_text.insert("end", mode)


my_text = ctk.CTkTextbox(alpha, width=500, height=250)
my_text.pack(pady=20)
my_button = ctk.CTkButton(alpha, text="Change Theme", command=change)
my_button.pack(pady=20)
colors = ["blue", "dark-blue", "green"]
my_option = ctk.CTkOptionMenu(alpha, values=colors, command=change_colors)
my_option.pack(pady=20)
alpha.mainloop()
