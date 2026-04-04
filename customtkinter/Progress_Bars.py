# Progress Bars
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
alpha = ctk.CTk()
alpha.title("Alpha")
alpha.iconbitmap("icon_2.ico")
alpha.geometry("800x800")


def increase():
    my_progress_bar.step()
    my_label.configure(text=int(my_progress_bar.get() * 100))


def start():
    my_progress_bar.start()


def stop():
    my_progress_bar.stop()


my_progress_bar = ctk.CTkProgressBar(
    alpha,
    orientation="horizontal",
    mode="indeterminate",
    determinate_speed=5,
    indeterminate_speed=0.5,
    width=300,
    height=12,
    corner_radius=5,
    # bg_color="white",
    border_color="green",
    border_width=2,
    progress_color="purple",
)
my_progress_bar.pack(pady=40)
# my_progress_bar.pack(fill="x")
# set default progress starting point
my_progress_bar.set(0)
my_button = ctk.CTkButton(alpha, text="Click me", command=increase)
my_button.pack(pady=40)
start_button = ctk.CTkButton(alpha, text="Start", command=start)
start_button.pack(pady=40)
end_button = ctk.CTkButton(alpha, text="End", command=stop)
end_button.pack(pady=40)
my_label = ctk.CTkLabel(alpha, text="Click me", font=("Arial", 20))
my_label.pack(pady=10)
alpha.mainloop()
# 1. CTkProgressBar Properties (Progress Bars)
# orientation="horizontal": Specifies the direction of the bar (vertical or horizontal).
# mode: Specifies how the tape works:
# determineate: (specific) Used when you know when the process will finish (e.g. 0% to 100%).
# indeterminate: (unspecified) in which a cursor moves back and forth,
# and is used when you do not know how long the process will end.
# determine_speed: The speed at which the tape moves when using the step() function in the specified pattern.
# indeterminate_speed: The speed of automatic cursor movement in the indefinite pattern.
# progress_color="purple": The color of the filled part of the progress bar
# 2. Software functions for progress control
# my_progress_bar.set(0): Manually specify the start value (takes values between 0.0 and 1.0).
# my_progress_bar.get(): Fetch the current value of the bar (returns a decimal value such as 0.5, which means 50%).
# my_progress_bar.step(): Move the bar one step forward based on the speed specified in the properties.
# my_progress_bar.start(): Starts automatic bar movement (very useful in indeterminate style).
# my_progress_bar.stop(): Stop automatic bar movement.
