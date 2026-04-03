# Check Boxes
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
alpha = customtkinter.CTk()
alpha.title("Alpha")
alpha.iconbitmap("icon_2.ico")
alpha.geometry("800x400")
my_label = customtkinter.CTkLabel(alpha, text="  ")


def game():
    if check_var.get() == "on":
        my_label.configure(text="You Clicked The Box")
        text_var.set("Awesome!")
    else:
        my_label.configure(text="You Did not Clicked The Box")


def clear_me():
    if check_var.get() == "on":
        my_check.deselect()
        my_label.configure(text="Clear")
        text_var.set("Would you like to see the other side?")


# check box state
check_var = customtkinter.StringVar(value="off")
# check box text
text_var = customtkinter.StringVar(value="Would you like to see the other side?")
my_check = customtkinter.CTkCheckBox(
    alpha,
    text="Would you like to see the other side?",
    variable=check_var,
    onvalue="on",
    offvalue="off",
    checkbox_width=20,
    checkbox_height=20,
    font=("helvetica", 18),
    corner_radius=50,
    fg_color="red",
    hover_color="white",
    text_color="blue",
    textvariable=text_var,
)
my_button = customtkinter.CTkButton(alpha, text="Submit", command=game)
clear_button = customtkinter.CTkButton(alpha, text="Clear", command=clear_me)
toggle_button = customtkinter.CTkButton(alpha, text="Toggle", command=my_check.toggle)
select_button = customtkinter.CTkButton(alpha, text="Select", command=my_check.select)
my_check.pack(pady=10)
select_button.pack(pady=10)
my_button.pack(pady=10)
toggle_button.pack(pady=10)
clear_button.pack(pady=10)
my_label.pack(pady=10)

alpha.mainloop()
