# Sliders
import customtkinter as ctk

ctk.set_appearance_mode("black")
ctk.set_default_color_theme("dark-blue")
alpha = ctk.CTk()
alpha.title("Alpha")
alpha.iconbitmap("icon_2.ico")
alpha.geometry("800x800")


def sliding(value):
    my_label.configure(text=int(value))


my_slider = ctk.CTkSlider(
    alpha,
    from_=0,
    to=100,
    command=sliding,
    orientation="horizontal",
    number_of_steps=10,
    width=200,
    height=20,
    border_width=5,
    border_color="red",
    fg_color="black",
    hover=True,
    button_hover_color="white",
    progress_color="green",
    button_color="purple",
    state="normal",
)
my_slider.pack(pady=20)
# Defined starting point
my_slider.set(0)
my_label = ctk.CTkLabel(alpha, text="", font=("Arial", 20))
my_label.pack(pady=20)
alpha.mainloop()
# 1. CTkSlider Properties
# from_=0 and to=100: Specify the start and end points of the range of values.
# number_of_steps=10: Split the range into specific steps; Here the cursor
# will move every 10 degrees instead of continuous smooth movement.
# orientation: Specify the slider orientation (horizontal or vertical).
# progress_color="green": The color of the traversed part of the slider.
# button_color="purple": The color of the circle (handle) that the user moves.
# button_hover_color="white": The color of the handle when the mouse hovers over it.
# hover=True: Activates interaction effects when the mouse hovers over the element.
# 2. Software interaction
# command=sliding: Call the function immediately when the slider is moved,
# passing the current value as a parameter (value).
# my_slider.set(0): Programmatically specify the start value of the slider when the interface is turned on.
# my_slider.get(): A function used to fetch the current value at which the slider stops at any given time.
