import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
root = customtkinter.CTk()  # We created the basic object of the window (Window Object),
# which is an alternative to tk.Tk() in the standard library.
# root.configure(background="white")
root.title("Hello World")
root.iconbitmap('icon_2.ico')
root.geometry("600x350")


def button_function():
    print("button pressed")


# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=root, text="Hello")  # Create a modern
# "button" object, specifying its
# parent window (root) and the text that appears on it.
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
# Position the button using the relative coordinate system; 0.5
# means placing it exactly in the middle of the width
# and height, making the fulcrum the center of the button itself.

# button.pack(padx=80, pady=80)
root.mainloop()
# 1. pack (packing) system
# This system is based on the concept of "stacking"; that is, automatically placing items one by one.
# Mechanism: Takes the element and places it in the first available empty space (often from top to bottom).
# Features: Quick and easy to use for simple interfaces.
# Media (Parameters):
# side: to identify the entity (TOP, BOTTOM, LEFT, RIGHT).
# fill: To make the element expand to fill the space (X, Y, or BOTH).
# padx / pady: To add outer margins around the element.

# 2. Place system (precise positioning)
# This system is based on coordinates (Coordinates); that is, determining the
# location of an element in pixels or percentages.
# Mechanism: You are the sole controller of the location of
# the element; the system does not care where other elements are,
# you may place one element on top of another (Overlap).
# Features: Provides extreme precision in complex design.
# Media (Parameters):
# x / y: Specify the location in pixels (Absolute).
# relx / rely: Specifies the location as a percentage of the window size (Relative);
# for example, 0.5 means exactly halfway.
# anchor: Specify the pivot point (CENTER, NW, SE, etc.).
