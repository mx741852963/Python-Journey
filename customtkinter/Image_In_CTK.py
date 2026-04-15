# Image In CTK
import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("black")
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
root.title("Alpha")
root.iconbitmap("icon_2.ico")
root.geometry("700x700")
my_image = ctk.CTkImage(
    light_image=Image.open(
        r"C:\Users\ahmad\Desktop\Python-project\customtkinter\new-year.jpg"
    ),
    dark_image=Image.open(
        r"C:\Users\ahmad\Desktop\Python-project\customtkinter\new-year.jpg"
    ),
    size=(700, 700),
)
my_label = ctk.CTkLabel(root, text="", image=my_image)
my_label.pack(pady=20)

root.mainloop()
