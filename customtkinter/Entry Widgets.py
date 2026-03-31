# Entry Widgets
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
alpha = customtkinter.CTk()
alpha.title("Alpha")
alpha.iconbitmap("icon_2.ico")
alpha.geometry("800x400")


def submit():
    my_label.configure(text=f"Hello {my_enter.get()}")
    my_enter.configure(state="disabled")


def clear():
    my_enter.configure(state="normal")
    my_enter.delete(0, "end")


my_label = customtkinter.CTkLabel(alpha, text="", font=("Times New Roman", 20))
my_label.pack(pady=40)
my_enter = customtkinter.CTkEntry(alpha, placeholder_text="Enter Your Name"
                                  , font=("Times New Roman", 18)
                                  , height=40, width=200
                                  , corner_radius=20
                                  , text_color="Black"
                                  , placeholder_text_color="gray"
                                  , fg_color=("blue", "lightblue")  # (Light_Mode_Color, Dark_Mode_Color)
                                  , show="*"
                                  )
my_enter.pack(pady=20)
my_button = customtkinter.CTkButton(alpha, text="Submit", font=("Times New Roman", 20),
                                    command=submit)
my_button.pack(pady=10)
my_clear_button = customtkinter.CTkButton(alpha, text="Clear", font=("Times New Roman", 20),
                                          command=clear,
                                          )
my_clear_button.pack(pady=10)
alpha.mainloop()
# 1. Explain the properties of CTkEntry (input field)
# placeholder_text: Temporary text that appears inside a field to instruct the user (such as "Enter Your Name"),
# and disappears once you start typing.
# placeholder_text_color: The color of the guidance text above.
# fg_color=("blue", "lightblue"):
# A powerful feature of CustomTkinter; where you can scroll a "Tuple"
# that has two colors: one for light mode (Light Mode) and one for night mode (Dark Mode).
# 2.Software functions (Logic)
# my_enter.get(): The most important function in this reference;
# its function is to drag the text typed by the user into
# the input field and convert it to a text string (String).
# my_enter.delete(0, "end"): Used to empty the field. Intermediate
# 0 means start scanning from the first character,
# and "end" (or customtkinter.END) means scan to the last character.
# my_enter.configure(state="disabled"): Freeze the field to prevent
# the user from modifying the text after submission (Submit).
# my_enter.configure(state="normal"): Reactivates the field
# to allow typing again (usually used when pressing Clear).
