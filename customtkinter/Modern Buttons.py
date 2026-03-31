import customtkinter

# Modern Buttons
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
alpha = customtkinter.CTk()
alpha.title("Alpha")
alpha.iconbitmap("icon_2.ico")
alpha.geometry("500x500")


def hello():
    my_label.configure(text=my_button.cget("text"))


my_button = customtkinter.CTkButton(alpha,
                                    text="Hello World", command=hello
                                    , height=100, width=200
                                    , font=("Times New Roman", 20),
                                    text_color="Black"
                                    , fg_color="white",
                                    hover_color="gray",
                                    corner_radius=40,
                                    bg_color="white",
                                    border_width=10, border_color="green",
                                    state="normal"
                                    )
my_button.pack(padx=100, pady=100)
my_label = customtkinter.CTkLabel(alpha, text="")
my_label.pack(padx=20, pady=20)
alpha.mainloop()
# Explain the properties of a button object (CTkButton)
# [1] command=hello: Bind the button to a function (Callback); when clicked,
#     commands are executed inside hello.
# [2] height=100, width=200: Specify the fixed dimensions of the button in pixels.
# [3] font=("Times New Roman", 20): Specify the font type and size.
# [4] text_color="Black": The color of the text appearing on the button.
# [5] fg_color="white": (Foreground Color) The color of the primary button (the body).
# [6] hover_color="gray": The color of the button that appears to the user only when the mouse hovers over it.
# [7] corner_radius=40: Degree of curvature of the corners; the higher the number, the more circular the button
#     becomes (a feature not found in the old tkinter).
# [8] bg_color="white": The color of the outer button background (appearing behind curved corners),
#     usually used to match the color of the parent window.
# [9] border_width=10: The thickness of the frame surrounding the button.
# [10] border_color="green": The color of the frame surrounding the button.
# [11] state="normal": The button's state; "normal" means clickable, and "disabled" makes it non-interactive (grey).
# [12] my_label.configure(text=...): This method is the correct way to modify the properties of any element (such as text)
#      "while the program is running" without having to recreate it.
# [13] my_button.cget("text"): The cget function is short for (Get Configuration); its function is to extract the value
#      of a specific property from the element (here we extracted the text on the button).
