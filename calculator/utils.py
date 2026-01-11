import sys

def windowsIconVerifier():
    if sys.platform.startswith('win'):
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID( 
        u'PySide 6 Calculator'
        )

def isValidNumber(string: str) -> bool:
    valid = False
    try:
        float(string)
        valid = True
    except ValueError:
        valid = False
    return valid