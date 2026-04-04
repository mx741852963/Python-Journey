# Segmented Buttons
import customtkinter as ctk

ctk.set_appearance_mode("black")
ctk.set_default_color_theme("dark-blue")
alpha = ctk.CTk()
alpha.title("Alpha")
alpha.iconbitmap("icon_2.ico")
alpha.geometry("800x800")


def clicker(value):
    # my_label.configure(text=f" Hello {my_seg_button.get()}")
    my_label.configure(text=f" Hello {value}")


my_values = ["one", "two", "three", "four", "five", "six", "seven", "eight"]
my_seg_button = ctk.CTkSegmentedButton(
    alpha,
    values=my_values,
    command=clicker,
    width=200,
    height=50,
    corner_radius=50,
    fg_color="white",
    # bg_color="black",
    font=("Arial", 12),
    selected_color="pink",
    selected_hover_color="purple",
    unselected_color="orange",
    unselected_hover_color="green",
    text_color="black",
    text_color_disabled="red",
    # dynamic_resizing=False,
)
my_seg_button.pack(pady=10)
# my_seg_button.set(my_values[0])
my_label = ctk.CTkLabel(alpha, text="", font=("Arial", 20))
my_label.pack(pady=10)
alpha.mainloop()
# 1. CTkSegmentedButton Properties
# values: A list of texts that will appear as buttons stuck together within an element.
# selected_color: The color of the button when selected.
# selected_hover_color: The color of the button chosen when the mouse hovers over it.
# unselected_color: Color of unselected buttons.
# unselected_hover_color: The color of the unselected button when the mouse hovers over it.
# dynamic_resizing: A property (if enabled) that allows an element to automatically resize
# to match the length of the text inside it.
# 2. Event Handling (Events)
# command=clicker: When any part is pressed, the function is automatically called and the
# value of the selected button is passed to it as a parameter (value).
# my_seg_button.get(): A function used to fetch text within the currently selected pane.
# my_seg_button.set(): A function used to programmatically select a part when the program starts.
