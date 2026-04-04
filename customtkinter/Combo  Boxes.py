# Combo Check Boxes
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
alpha = customtkinter.CTk()
alpha.title("Alpha")
alpha.iconbitmap("icon_2.ico")
alpha.geometry("800x800")


def color_picker(choice):

    output_label.configure(text=choice, text_color=choice)


def color_picker_2():
    output_label.configure(text=my_combo.get(), text_color=my_combo.get())


def color_picker_yellow():
    my_combo.set("Yellow")
    output_label.configure(text=my_combo.get(), text_color=my_combo.get())


my_label = customtkinter.CTkLabel(alpha, text="Pick A Color", font=("Arial", 20))
my_label.pack(pady=40)
colors = ["red", "green", "blue"]
my_combo = customtkinter.CTkComboBox(
    alpha,
    values=colors,
    height=30,
    width=200,
    font=("Arial", 20),
    dropdown_font=("Arial", 20),
    corner_radius=30,
    text_color="purple",
    border_width=2,
    border_color="black",
    button_color="white",
    button_hover_color="red",
    dropdown_hover_color="gray",
    dropdown_fg_color="green",
    dropdown_text_color="orange",
    justify="center",
    # command=color_picker,
)
my_combo.pack(pady=0)
output_label = customtkinter.CTkLabel(alpha, text="", font=("Arial", 20))
output_label.pack(pady=20)
my_button = customtkinter.CTkButton(
    alpha, text="Pick A Color", font=("Arial", 20), command=color_picker_2
)
my_button.pack(pady=20)
yellow_button = customtkinter.CTkButton(
    alpha, text="Yellow", font=("Arial", 20), command=color_picker_yellow
)
yellow_button.pack(pady=20)
alpha.mainloop()
# 1. CTkComboBox Features (New)
# values=colors: Scroll a list (List) containing the options that will appear to the user.
# dropdown_font: Specifies the font of the text within the list when opened,
# which is separate from the chosen text font.
# button_color: Colorize the small arrow to the right of the list.
# button_hover_color: The color of the arrow when the mouse hovers over it.
# dropdown_fg_color: The background color of the dropdown menu itself.
# dropdown_text_color: Color the text within the menu options
# dropdown_hover_color: The color that appears behind the option when you hover over it within the list.
# justify="center": Align the selected text within the field (center, right, or left).
# 2. Software interaction with the list
# my_combo.get(): Fetch the option currently selected by the user from the list.
# my_combo.set("Yellow"): Forcing the list to choose a specific value
# programmatically (even if it is not present in the original list sometimes).
# command=color_picker: (If enabled) The menu calls the function immediately
# once the user selects a new color, and automatically passes the selected value
# as a parameter (Argument) to the function.
