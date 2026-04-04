# The Switch Widget
import customtkinter as ctk

ctk.set_appearance_mode("black")
ctk.set_default_color_theme("dark-blue")
alpha = ctk.CTk()
alpha.title("Alpha")
alpha.iconbitmap("icon_2.ico")
alpha.geometry("800x800")


def switching():
    # my_switch.configure(text=switch_var.get())
    my_label.configure(text=switch_var.get())


def clicker():
    # my_switch.deselect()
    # my_switch.select()
    my_switch.toggle()


switch_var = ctk.StringVar(value="on")
my_switch = ctk.CTkSwitch(
    alpha,
    text="switch",
    command=switching,
    variable=switch_var,
    onvalue="on",
    offvalue="off",
    # width=100,
    switch_width=40,
    switch_height=20,
    corner_radius=10,
    border_color="red",
    border_width=2,
    fg_color="white",
    progress_color="green",
    button_color="blue",
    button_hover_color="green",
    text_color="black",
    state="normal",
)
my_switch.pack(padx=10, pady=10)
my_label = ctk.CTkLabel(alpha, text="")
my_label.pack(padx=20, pady=20)
my_button = ctk.CTkButton(alpha, text="Click Me", command=clicker)
my_button.pack(padx=20, pady=20)
alpha.mainloop()
# 1. CTkSwitch Structural Properties
# switch_width and switch_height: Control the dimensions of
# the sliding part of the switch (rectangle) separately from the total area of the element.
# progress_color="green": The color of the filled part that appears when the key (the activated side) is activated.
# button_color="blue": The color of the small circle (handle) that moves inside the switch.
# button_hover_color="green": Changes the color of the sliding circle when you hover your mouse over it.
# fg_color="white": The color of the inactive part of the key path.
# 2. Software connectivity and control
# variable=switch_var: Bind the state of a key to a text variable to monitor its value.
# onvalue="on" and offvalue="off": Specifies the texts that the variable
# will carry when the key is turned on or off.
# command=switching: Execute a specific function immediately after manually changing the key state.
# my_switch.toggle(): A function that programmatically reverses the state of
# a key (if On becomes Off and vice versa).
# my_switch.select() and my_switch.deselect(): Functions to control whether
# a key is activated or deactivated programmatically without user intervention
