from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["os","customtkinter"],
    "include_files": ["app.py", "main.py", "appIcon.ico"],
}

executables = [
    Executable("app.py", base="Win32GUI", target_name="App Debug Printer", icon="appIcon.ico")
]

setup(
    name="Reload Queue Printer",
    version="1.0",
    description="Programa para reiniciar fila de impressão.",
    options={"build_exe": build_exe_options},
    executables=executables
)