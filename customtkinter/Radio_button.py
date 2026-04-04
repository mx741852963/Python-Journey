# Radio button
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
alpha = ctk.CTk()
alpha.title("Alpha")
alpha.iconbitmap("icon_2.ico")
alpha.geometry("800x800")


def get_red():
    if radio_var.get() == "other":
        my_label_two.configure(text="pick a choice")
    elif radio_var.get() == "Yes":
        my_label_two.configure(text="Of course")
    else:
        my_label_two.configure(text="Rally??")


my_label = ctk.CTkLabel(alpha, text="Do you like your Pizza?", font=("Arial", 20))
my_label.pack(pady=20)
radio_var = ctk.StringVar(value="other")
my_radio = ctk.CTkRadioButton(
    alpha,
    text="Yes I Do",
    font=("Arial", 20),
    value="Yes",
    variable=radio_var,
    radiobutton_width=25,
    radiobutton_height=25,
    corner_radius=1,
    border_width_checked=10,
    border_width_unchecked=5,
    border_color="red",
    hover_color="green",
    fg_color="pink",
    text_color="blue",
    state="normal",
    text_color_disabled="purple",
    # width=50,
    # height=50,
    # command=get_red,
)
my_radio.pack(pady=20)
my_radio_two = ctk.CTkRadioButton(
    alpha,
    text="No",
    font=("Arial", 20),
    value="No",
    variable=radio_var,
    # command=get_red,
)
my_radio_two.pack(pady=20)
my_button = ctk.CTkButton(alpha, text="Select", font=("Arial", 20), command=get_red)
my_button.pack(pady=20)
my_label_two = ctk.CTkLabel(alpha, text="", font=("Arial", 20))
my_label_two.pack(pady=20)
alpha.mainloop()
# 1. Teamwork concept (Radio Groups) variable=radio_var: This is the magic link;
# When multiple buttons give the same variable (radio_var),
# the program understands that it is "one group", and once one button is selected the other is
# automatically deselected.value="Yes" and value="No":
# The unique value that the variable will have when that particular button is selected
# 2. CTkRadioButton Aesthetic and Technical Characteristics
# border_width_checked: The thickness of the outer frame of the circle when the button is selected.
# border_width_unchecked: The thickness of the outer frame when the button is not selected.
# corner_radius: In radio buttons, this controls the shape of the inner "dot";
# a value of 1 makes it look like a small square inside a circle.
# state="disabled": Disable the button so that the user cannot click it.
# text_color_disabled: The color of the custom text that appears when the button is
# disabled (here chosen by "purple").
# 3. Software Logic (Logic)
# get_red() function: Uses the if/elif/else conditional system to check the value stored inside radio_var.
# Initial value: Setting StringVar(value="other") makes the program start without choosing
# "Yes" or "No", allowing you to set a default state (such as "pick a choice" text).
