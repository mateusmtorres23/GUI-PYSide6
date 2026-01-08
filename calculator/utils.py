import sys

def windowsIconVerifier():
    if sys.platform.startswith('win'):
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID( 
        u'PySide 6 Calculator'
        )