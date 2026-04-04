# Scrollable Frames
import customtkinter as ctk

ctk.set_appearance_mode("black")
ctk.set_default_color_theme("dark-blue")
alpha = ctk.CTk()
alpha.title("Alpha")
alpha.iconbitmap("icon_2.ico")
alpha.geometry("800x800")
# create a scrollable frames
my_frame = ctk.CTkScrollableFrame(
    alpha,
    orientation="vertical",
    width=250,
    height=300,
    label_text="Alpha",
    label_fg_color="white",
    label_anchor="center",
    label_text_color="black",
    corner_radius=50,
    # bg_color="white",
    scrollbar_button_hover_color="black",
    scrollbar_fg_color="pink",
    scrollbar_button_color="red",
    border_width=5,
    border_color="green",
    fg_color="gray",
)
# my_frame.pack(fill="both", expand=True)
my_frame.pack(pady=40)
# for loop for buttons
for _ in range(20):
    ctk.CTkButton(my_frame, text="This is a Button ", fg_color="green").pack(pady=5)
alpha.mainloop()
# 1. CTkScrollableFrame (Sliding Frame) Properties
# label_text="Alpha": Add a fixed text title that appears at the top of the frame.
# label_fg_color and label_text_color: Control the background color of the title and its text color.
# label_anchor="center": Specifies the title alignment (center, right, or left).
# orientation="vertical": Specifies the scroll direction; in your case it is
# vertical (Vertical), and can be horizontal (Horizontal).
# 2. Customize Scrollbar (Scrollbar Customization)
# scrollbar_fg_color="pink": Colorizes the path along which the scrollbar moves.
# scrollbar_button_color="red": Colorize the slider button itself that the user drags.
# scrollbar_button_hover_color="black": Change the color of the slider button when the mouse hovers over it
# 3. Programming Logic (The For Loop) Using for_in range(20):
# This is a very clever approach to programming references;
# instead of writing 20-button code manually,
# I created it and filled it into the frame automatically.
# 4. Technical note for reference (Layout Note)
# I put the line my_frame.pack(fill="both", expand=True) in a comment.
# If you activate it, the frame will expand to fill all the available space in the window,
# regardless of its size, which is very useful in Machine Learning applications when viewing long spreadsheets.
