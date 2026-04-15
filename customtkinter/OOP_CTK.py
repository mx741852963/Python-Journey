# OOP CTK
import customtkinter as ctk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme(r"Themes\lavender.json")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Alpha")
        self.iconbitmap("icon_2.ico")
        self.geometry("700x700")

        self.my_text = ctk.CTkTextbox(self, width=600, height=300)
        self.my_text.pack()
        self.my_button = ctk.CTkButton(self, text="Clear Box", command=self.clear)
        self.my_button.pack()

    def clear(self):
        self.my_text.delete(0.0, "end")


# Define App
app = App()
app.mainloop()
