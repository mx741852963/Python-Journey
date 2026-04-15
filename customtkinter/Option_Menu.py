# Option Menu
import customtkinter as ctk

ctk.set_appearance_mode("black")
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
root.title("Alpha")
root.iconbitmap("icon_2.ico")
root.geometry("700x700")


def color_picker(choice):
    my_label.configure(text=choice, text_color=choice)


def color_picker_two():
    my_label.configure(text=my_option.get(), text_color=my_option.get())


def color_picker_pink():
    my_option.set("pink")
    my_label.configure(text=my_option.get(), text_color=my_option.get())


color = ["Red", "Green", "Blue"]
my_option = ctk.CTkOptionMenu(
    root,
    values=color,
    dynamic_resizing=True,
    # command=color_picker
)
my_option.pack(pady=40)
my_label = ctk.CTkLabel(root, text="")
my_label.pack()
pick_button = ctk.CTkButton(root, text="Pick", command=color_picker_two)
pick_button.pack()
pick_pink = ctk.CTkButton(root, text="Pink", command=color_picker_pink)
pick_pink.pack()
root.mainloop()
