from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

class abstractkeyboard(QWidget):
    def __init__(self):
        super().__init__()
        self.m_name = ''

    # virtual function
    def update(self):
        pass

    def getName(self):
        return self.m_name

    def setName(self, name):
        self.m_name = name
        print(self.m_name)

    def onKeyPressed(self, key, value):
        recevier = QApplication.focusWidget()
        if recevier is None:
            return
        keyPress = QKeyEvent(QEvent.KeyPress, key, Qt.NoModifier, value)
        keyRelease = QKeyEvent(QEvent.KeyRelease, key, Qt.NoModifier, value)

        QApplication.sendEvent(recevier, keyPress)
        QApplication.sendEvent(recevier, keyRelease)
