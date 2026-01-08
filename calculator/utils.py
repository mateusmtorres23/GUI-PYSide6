from pathlib import Path
import sys

ROOT_DIR = Path(__file__).parent
FILES_DIR = ROOT_DIR / "files"
ICON_PATH = FILES_DIR / "icon.png"

def windowsIconVerifier():
    if sys.platform.startswith('win'):
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID( 
        u'PySide 6 Calculator'
        )