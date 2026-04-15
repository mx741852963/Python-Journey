# TextBox
import customtkinter as ctk

ctk.set_appearance_mode("black")
ctk.set_default_color_theme("dark-blue")
alpha = ctk.CTk()
alpha.title("Alpha")
alpha.iconbitmap("icon_2.ico")
alpha.geometry("800x800")

thing = ""


def delete():
    my_text.delete(0.0, "end")


def copy():
    global thing
    thing = my_text.get(0.0, "end")


def paste():
    if thing:
        my_text.insert("end", thing)
    else:
        my_text.insert("end", "There is nothing to paste")


my_text = ctk.CTkTextbox(
    alpha,
    width=600,
    height=300,
    corner_radius=50,
    text_color="white",
    # bg_color="silver",
    border_color="blue",
    border_width=2,
    border_spacing=10,
    fg_color="black",
    font=("bold", 20),
    wrap="word",
    activate_scrollbars=True,
    scrollbar_button_color="pink",
    scrollbar_button_hover_color="red",
    # font=ctk.CTkFont(size=20),
)
my_text.pack(pady=20)
my_frame = ctk.CTkFrame(alpha)
my_frame.pack(pady=10)
delete_button = ctk.CTkButton(my_frame, text="Delete", command=delete)
copy_button = ctk.CTkButton(my_frame, text="Copy", command=copy)
paste_button = ctk.CTkButton(my_frame, text="Paste", command=paste)
delete_button.grid(row=0, column=0)
copy_button.grid(row=0, column=1, padx=10)
paste_button.grid(row=0, column=2)
alpha.mainloop()
