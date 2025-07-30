from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["os","customtkinter"],
    "include_files": ["app.py", "main.py", "pythonIcon.png"],
}

executables = [
    Executable("main.py", base="Win32GUI", icon="pythonIcon.png")
]

setup(
    name="Reload Queue Printer",
    version="1.0",
    description="Programa para reiniciar fila de impressão.",
    options={"build_exe": build_exe_options},
    executables=executables
)