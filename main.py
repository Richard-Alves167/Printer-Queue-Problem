import os

def ReloadPrintQueuePrinter():
    os.system('net stop spooler"')
    os.system('del /Q /F /S "%systemroot%\System32\spool\PRINTERS\*.*"')
    os.system('net start spooler"')