# Widget Animation
import customtkinter as ctk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme(r"Themes\lavender.json")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Alpha")
        self.iconbitmap("icon_2.ico")
        self.geometry("700x700")
        self.ax_y = 1000
        self.my_frame = ctk.CTkFrame(self)
        # self.my_frame.pack(fill="both", expand=True)
        self.my_frame.pack(pady=10)
        self.up_button = ctk.CTkButton(self.my_frame, text="Up", command=self.up)
        self.up_button.grid(
            row=0,
            column=0,
            padx=10,
            # sticky="e"
        )
        self.down_button = ctk.CTkButton(self.my_frame, text="Down", command=self.down)
        self.down_button.grid(row=0, column=1, padx=10)

        self.my_text = ctk.CTkTextbox(
            self, width=600, height=300, fg_color="white", text_color="black"
        )
        self.my_text.place(relx=0.5, y=self.ax_y, anchor="center")

    def up(self):
        if self.ax_y >= 300:
            self.ax_y -= 20
            self.my_text.place(relx=0.5, y=self.ax_y, anchor="center")
            self.up_button.configure(text=self.ax_y)
            self.after(5, self.up)

    def down(self):
        if self.ax_y <= 1000:
            self.ax_y += 20
            self.my_text.place(relx=0.5, y=self.ax_y, anchor="center")
            self.down_button.configure(text=self.ax_y)
            self.after(5, self.down)


# Define App
app = App()
app.resizable(True, True)
app.mainloop()
