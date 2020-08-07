import sys
import win32gui
from PyQt5.QtWidgets import QApplication, QWidget

parent = 0


def callback(a, none):
    global parent
    b = win32gui.FindWindowEx(a, 0, "SHELLDLL_DefView", None)
    if b > 0:
        c = win32gui.FindWindowEx(b, 0, "SysListView32", "FolderView")
        parent = c


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(0, 0)
    w.setWindowTitle('First PyQt5')
    w.show()

    win32gui.EnumWindows(callback, None)
    child = win32gui.FindWindow(None, "First PyQt5")
    win32gui.SetParent(child, parent)

    sys.exit(app.exec_())
