import sys
from PySide2.QtWidgets import *

from mykeyboard import MyKeyBoard
from numberkeyboard import NumberKeyBoard

qss = "QLineEdit {                    \
            border-style: none;        \
            padding: 3px;              \
            border-radius: 5px;        \
            border: 1px solid #dce5ec; \
            font-size: 30px;           \
        }                              \
        "

def main():
    app = QApplication()

    mywin = QWidget()
    mywin.setWindowTitle("keyboard")
    mywin.resize(850, 370)
    textInput = QLineEdit()
    textInput.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
    textInput.setStyleSheet(qss)
    mykeyboard = MyKeyBoard()
    v = QVBoxLayout()
    v.addWidget(textInput, 1)
    v.addWidget(mykeyboard, 5)
    mywin.setLayout(v)
    mywin.show()
    """
    """
    mywin2 = QWidget()
    mywin2.setWindowTitle("number")
    mywin2.resize(450,370)
    numberkeyboard = NumberKeyBoard()
    textInput2 = QLineEdit()
    textInput2.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
    textInput2.setStyleSheet(qss)

    v2 = QVBoxLayout()
    v2.addWidget(textInput2, 1)
    v2.addWidget(numberkeyboard, 5)
    mywin2.setLayout(v2)
    mywin2.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
