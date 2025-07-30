import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Reload Queue Printer")
app.geometry("300x200")


header_app = ctk.CTkLabel(app, text="Reinicicar fila de impressão")
header_app.pack(pady=20, padx=10)

def button_function():
    print("Deletar arquivos em fila")

appButton = ctk.CTkButton(app, text="Deletar arquivos em fila", command=button_function)
appButton.pack(pady=20, padx=10)

app.mainloop()

