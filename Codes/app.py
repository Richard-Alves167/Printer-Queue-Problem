from main import ReloadPrintQueuePrinter
import customtkinter as ctk
import os
import ctypes
import sys
import time

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
if not is_admin() and "--as-admin" not in sys.argv:
    params = f'"{__file__}" --as-admin'
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, params, None, 1
    )
    sys.exit()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Reload Queue Printer")
app.geometry("300x200")

header_app = ctk.CTkLabel(app, text="Reinicicar fila de impressão")
header_app.pack(pady=20, padx=10)

def button_function():
    ReloadPrintQueuePrinter()
    path = os.path.expandvars(r'%systemroot%\System32\spool\PRINTERS')
    try :
        if not os.listdir(path):
            ctk.CTkLabel(app, text="Arquivos excluídos com sucesso!\n Tente imprimir seus arquivos novamente...").pack(pady=20, padx=10)
        else :
            ctk.CTkLabel(app, text="Ainda existem arquivos em que não foram possíveis de excluir.").pack(pady=20, padx=10)
    except:
        ctk.CTkLabel(app, text="Falta de permissão de administrador.").pack(pady=20, padx=10)


appButton = ctk.CTkButton(app, text="Deletar arquivos em fila", command=button_function)
appButton.pack(pady=20, padx=10)

app.mainloop()

