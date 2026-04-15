# Custom Fonts Widget
import customtkinter as ctk

ctk.set_appearance_mode("black")
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
root.title("Alpha")
root.iconbitmap("icon_2.ico")
root.geometry("400x200")


def change():
    global myFont
    myFont.configure(
        family="Arial",
        size=30,
        # weight="bold",
        slant="roman",
        underline=False,
        overstrike=False,
    )


myFont = ctk.CTkFont(
    family="Helvetica",
    size=20,
    weight="bold",
    slant="italic",
    underline=True,
    overstrike=True,
)
my_label = ctk.CTkLabel(root, text="This is Text", font=myFont)

my_label.pack(pady=10)
my_button = ctk.CTkButton(root, text="Change", command=change)
my_button.pack(pady=10)
root.mainloop()
