import customtkinter as ctk

from gui import CSVJoinerApp

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")  # Modo escuro
    ctk.set_default_color_theme("blue")  # Tema azul
    app = CSVJoinerApp()
    app.mainloop()
