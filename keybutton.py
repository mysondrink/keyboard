from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

DEFAULT_STYLE_SHEET = "QPushButton { background: #4395ff; border-radius: 5px;" \
                      "margin: 5px;font-size: 26px; color:white;}" \
                      "QPushButton:pressed { background: #01ddfd}"

class keybutton(QPushButton):
    pressed = Signal(str)
    def __init__(self, value):
        super().__init__()
        self.setFocusPolicy(Qt.NoFocus)
        self.setStyleSheet(DEFAULT_STYLE_SHEET)
        self.enum = {"Auto":0, "LowerCase":1, "UpperCase":2, "SpecialChar":3}

        self.key = 0
        self.value = value
        self.display = ''

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # 在这里编写你自定义的点击事件处理逻辑
            self.pressed.emit(self.value)
        super().mousePressEvent(event)

    def setValue(self, value):
        self.value = value

    def onReponse(self):
        pass

    def swtichCapsLock(self):
        pass

    def switchSpecialChar(self):
        pass

    def switching(self):
        pass

    def findEnum(self):
        pass

    def setDisplayContent(self):
        pass