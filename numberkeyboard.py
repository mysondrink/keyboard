from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from abstractkeyboard import abstractkeyboard
from keybutton import keybutton

BACKSPACE_ICON = "./Image/backspace.png"
CLOSE_ICON = "./Image/close.png"

list_1 = ['1', '2', '3']
list_2 = ['4', '5', '6']
list_3 = ['7', '8', '9']
list_4 = ['close', '0', 'back']
list_key = [Qt.Key_0, Qt.Key_1, Qt.Key_2, Qt.Key_3, Qt.Key_4, Qt.Key_5, Qt.Key_6, Qt.Key_7, Qt.Key_8, Qt.Key_9]

class NumberKeyBoard(abstractkeyboard):
    def __init__(self):
        super().__init__()
        self.num_list = ''
        self.createButton()

    def createButton(self):
        self.layout = QVBoxLayout()
        self.h1 = QHBoxLayout()
        self.h2 = QHBoxLayout()
        self.h3 = QHBoxLayout()
        self.h4 = QHBoxLayout()
        self.h1.setSizeConstraint(QLayout.SetNoConstraint)
        self.h2.setSizeConstraint(QLayout.SetNoConstraint)
        self.h3.setSizeConstraint(QLayout.SetNoConstraint)
        self.h4.setSizeConstraint(QLayout.SetNoConstraint)

        for i in range(3):
            button = keybutton(list_1[i])
            button.setText(list_1[i])
            button.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
            button.pressed.connect(self.getButtonInfo)
            self.h1.addWidget(button)
        for i in range(3):
            button = keybutton(list_2[i])
            button.setText(list_2[i])
            button.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
            button.pressed.connect(self.getButtonInfo)
            self.h2.addWidget(button)
        for i in range(3):
            button = keybutton(list_3[i])
            button.setText(list_3[i])
            button.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
            button.pressed.connect(self.getButtonInfo)
            self.h3.addWidget(button)
        for i in range(3):
            button = keybutton(list_4[i])
            button.setText(list_4[i])
            button.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
            button.pressed.connect(self.getButtonInfo)
            self.h4.addWidget(button)
        self.layout.addLayout(self.h1, 15)
        self.layout.addLayout(self.h2, 15)
        self.layout.addLayout(self.h3, 15)
        self.layout.addLayout(self.h4, 15)
        self.setLayout(self.layout)

        button = self.findChildren(QPushButton)
        for i in button:
            if i.value == 'back':
                i.setText('')
                i.setIcon(QIcon(BACKSPACE_ICON))
                i.setIconSize(QSize(40, 40))
            elif i.value == 'close':
                i.setText('')
                i.setIcon(QIcon(CLOSE_ICON))
                i.setIconSize(QSize(40, 40))

    def getButtonInfo(self, info):
        if info == 'back':
            super().onKeyPressed(Qt.Key_Backspace, "")
        elif info == 'close':
            return
        else:
            num = int(info)
            super().onKeyPressed(list_key[num], info)


