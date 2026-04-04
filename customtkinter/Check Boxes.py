# Check Boxes
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
alpha = customtkinter.CTk()
alpha.title("Alpha")
alpha.iconbitmap("icon_2.ico")
alpha.geometry("800x400")
my_label = customtkinter.CTkLabel(alpha, text="  ")


def game():
    if check_var.get() == "on":
        my_label.configure(text="You Clicked The Box")
        text_var.set("Awesome!")
    else:
        my_label.configure(text="You Did not Clicked The Box")


def clear_me():
    if check_var.get() == "on":
        my_check.deselect()
        my_label.configure(text="Clear")
        text_var.set("Would you like to see the other side?")


# check box state
check_var = customtkinter.StringVar(value="off")
# check box text
text_var = customtkinter.StringVar(value="Would you like to see the other side?")
my_check = customtkinter.CTkCheckBox(
    alpha,
    text="Would you like to see the other side?",
    variable=check_var,
    onvalue="on",
    offvalue="off",
    checkbox_width=20,
    checkbox_height=20,
    font=("helvetica", 18),
    corner_radius=50,
    fg_color="red",
    hover_color="white",
    text_color="blue",
    textvariable=text_var,
)
my_button = customtkinter.CTkButton(alpha, text="Submit", command=game)
clear_button = customtkinter.CTkButton(alpha, text="Clear", command=clear_me)
toggle_button = customtkinter.CTkButton(alpha, text="Toggle", command=my_check.toggle)
select_button = customtkinter.CTkButton(alpha, text="Select", command=my_check.select)
my_check.pack(pady=10)
select_button.pack(pady=10)
my_button.pack(pady=10)
toggle_button.pack(pady=10)
clear_button.pack(pady=10)
my_label.pack(pady=10)

alpha.mainloop()
# 1. Special Variables (Tkinter Variables)
# customtkinter.StringVar(value="off"): A library-specific text
# variable definition that monitors the state of an element instantaneously.
# check_var: Used to store the "state" of the box (is it specified or not).
# text_var: Used to dynamically change the "text" written next to the box
# while the program is running
# 2. CTkCheckBox (Checkbox) Properties
# variable=check_var: Bind the box to a state variable so the program
# knows if it is activated or not.
# onvalue="on" and offvalue="off": Specifies the values the check_var variable will
# take when activated or deactivated (you can change them to 1 and 0, for example).
# textvariable=text_var: Bind the visible text to the variable text_var;
# any change to this variable will immediately change the text on the screen
# checkbox_width and checkbox_height: Control the size of the small checkbox for selection.
# corner_radius=50: Make the square appear completely circular
# 3. Control functions (Methods)
# my_check.select(): A program command to activate the box (check it) automatically.
# my_check.deselect(): A command to programmatically deactivate the box.
# my_check.toggle(): An intelligent function that reverses the state; If it is activated,
# you cancel it, and if it is canceled, you do it.
# check_var.get(): Fetch the current value of the box (on or off) to process it in functions.
# text_var.set("..."): Update the text associated with the box immediately.
