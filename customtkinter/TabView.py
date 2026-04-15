# TabView
import customtkinter as ctk

ctk.set_appearance_mode("black")
ctk.set_default_color_theme("dark-blue")
alpha = ctk.CTk()
alpha.title("Alpha")
alpha.iconbitmap("icon_2.ico")
alpha.geometry("800x800")
tap_view = ctk.CTkTabview(
    alpha,
    width=600,
    height=300,
    text_color="black",
    corner_radius=20,
    fg_color="silver",
    anchor="w",
    segmented_button_fg_color="white",
    segmented_button_selected_color="pink",
    segmented_button_selected_hover_color="purple",
    segmented_button_unselected_color="red",
    segmented_button_unselected_hover_color="red",
)
tap_view.pack(side="top")
# Create Taps
tap_one = tap_view.add("One")
tap_two = tap_view.add("Two")
my_button = ctk.CTkButton(tap_one, text="One")
my_button.pack(anchor="center")
my_button2 = ctk.CTkButton(tap_two, text="Two")
my_button2.pack(anchor="center")


alpha.mainloop()
