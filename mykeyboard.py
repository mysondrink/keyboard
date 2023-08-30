import re

from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from abstractkeyboard import abstractkeyboard
from keybutton import keybutton

NORMAL_BUTTON_WIDTH = 55
NORMAL_BUTTON_HEIGHT = 45

BACKSPACE_ICON = "./Image/backspace.png"
ENTER_ICON     = "./Image/enter.png"
SPACE_ICON     = "./Image/space.png"
CAPLOCK_ICON   = "./Image/caplock.png"
CLOSE_ICON = "./Image/close.png"

BUTTON_SPACING_RATIO = 0.030
BUTTON_WIDTH_RATIO   = 0.09
BUTTON_HEIGHT_RATIO  = 0.2

list_4 = [Qt.Key_Q]
list_1 = ['q','w','e','r','t','y','u','i','o','p']
list_2 = ['cap','a','s','d','f','g','h','j','k','l']
list_3 = ['con','z','x','c','v','b','n','m','back','close']

class ChineseWidget(QListWidget):
    pressedChanged = Signal(int, str)
    def __init__(self):
        super().__init__()
        self.setFocusPolicy(Qt.NoFocus)
        self.setViewMode(QListView.ListMode)
        self.setFlow(QListView.LeftToRight)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollMode(QListWidget.ScrollPerPixel)
        QScroller.grabGesture(self, QScroller.LeftMouseButtonGesture)
        self.setStyleSheet("                                                                           \
                  QListWidget { outline: none; border:1px solid #00000000; color: black; }    \
                  QListWidget::Item { width: 50px; height: 50px; }                            \
                  QListWidget::Item:hover { background: #4395ff; color: white; }              \
                  QListWidget::item:selected { background: #4395ff; color: black; }           \
                  QListWidget::item:selected:!active { background: #00000000; color: black; } \
                  ")
        self.loadChineseLib()
        self.loadChinesePhraseLib()

    def setText(self, text):
        if text == '':
            self.clear()
            return
        for i in range(self.count()):
            self.takeItem(i)
        self.clear()

        self.addOneItem(text)
        # if self.list_pinyin == None or self.list_hanzi == None:
        #     return
        # for i in range(len(self.list_pinyin)):
        # 拼音匹配
        word = 'bafang'
        matching_indices = [index for index, char in enumerate(self.list_pinyin) if char == text]
        print(matching_indices)
        for i in range(len(matching_indices)):
            if self.count() <= 30:
                str_chr = self.list_hanzi[matching_indices[i]]
                self.addOneItem(str_chr)
            else:
                break

    def onItemClicked(self, item):
        text = item.text()
        key = -1
        self.pressedChanged.emit(key, text)
        self.setText("")

    def addOneItem(self, text):
        item = QListWidgetItem(text)
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(50)
        item.setFont(font)

        item.setTextAlignment(Qt.AlignCenter)

        isChinese = False if not u'\u4e00'<=text[0]<=u'\u9fff' else True

        width = font.pointSize()
        if isChinese:
            width += len(text) * font.pointSize() * 1.5
        else:
            width += len(text) * font.pointSize() * 2/3

        item.setSizeHint(QSize(width, 50))

        self.addItem(item)

    def loadChineseLib(self):
        self.list_pinyin = []
        self.list_hanzi = []

        f = open(r'./Resources/ChineseLib/pinyin.txt', 'r', encoding="utf-8")
        lines = f.readlines()
        for text in lines:
        # for text in lines[210:221]:
            # for j in range(len(i)):
            #     if not u'\u4e00'<=i[j]<=u'\u9fff':
            #         print(i[j])
            text = text.strip()
            pattern = re.compile(r'[^\u4e00-\u9fa5]')
            match = re.search(pattern, text)
            if match:
                m = match.start()
            else:
                m = -1
            first = text[m:len(text)]
            second = text[:m]
            self.list_pinyin.append(first)
            self.list_hanzi.append(second)

        # 拼音匹配
        # word = 'bafang'
        # matching_indices = [index for index, char in enumerate(list_pinyin) if char == word]
        # print(matching_indices)

    def loadChinesePhraseLib(self):
        f = open(r'./Resources/ChinesePhraseLib/pinyin_phrase.txt', 'r', encoding="utf-8")
        lines = f.readlines()
        for text in lines:
            # for text in lines[210:221]:
            if text[0] == '#':
                continue
            text = text.strip()
            pattern = re.compile(r':')
            match = re.search(pattern, text)
            if match:
                m = match.start()
            else:
                m = -1
            first = text[m:len(text)]
            strinfo = re.compile(r' ')
            non_chinese_indices = [k.start() for k in re.finditer(strinfo, first)]
            str_abb = ''
            for i in range(len(non_chinese_indices)):
                str_abb += first[non_chinese_indices[i] + 1]
            strinfo = re.compile(r'[:\s]')
            first = strinfo.sub('', first)
            second = text[:m]
            # list_pinyin_2.append(first)
            # list_cizu.append(second)
            self.list_pinyin.append(first)
            self.list_hanzi.append(second)

            self.list_pinyin.append(str_abb)
            self.list_hanzi.append(second)

    def loadGoogleChineseLib(self):
        pass

class MyKeyBoard(abstractkeyboard):
    def __init__(self):
        super().__init__()
        self.m_isChinese = False
        self.InitUI()
        self.resetButton()

    def InitUI(self):
        self.m_chineseWidget = ChineseWidget()
        self.m_chineseWidget.itemClicked.connect(self.m_chineseWidget.onItemClicked)
        self.m_chineseWidget.itemClicked.connect(self.clearBufferText)
        self.m_chineseWidget.pressedChanged.connect(super().onKeyPressed)
        self.layout = QVBoxLayout()
        self.h1 = QHBoxLayout()
        self.h2 = QHBoxLayout()
        self.h3 = QHBoxLayout()
        self.h1.setSizeConstraint(QLayout.SetNoConstraint)
        self.h2.setSizeConstraint(QLayout.SetNoConstraint)
        self.h3.setSizeConstraint(QLayout.SetNoConstraint)

        self.pinyin = ''

        for i in range(len(list_1)):
            button = keybutton(list_1[i])
            button.setText(list_1[i])
            button.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
            button.pressed.connect(self.getButtonInfo)
            self.h1.addWidget(button)
        for i in range(len(list_2)):
            button = keybutton(list_2[i])
            button.setText(list_2[i])
            button.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
            button.pressed.connect(self.getButtonInfo)
            self.h2.addWidget(button)
        for i in range(len(list_3)):
            button = keybutton(list_3[i])
            button.setText(list_3[i])
            button.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
            button.pressed.connect(self.getButtonInfo)
            self.h3.addWidget(button)

        self.layout.setSizeConstraint(QLayout.SetNoConstraint)
        self.layout.setSpacing(0)
        self.layout.setMargin(0)
        self.layout.addWidget(self.m_chineseWidget, 12)
        self.layout.addLayout(self.h1, 15)
        self.layout.addLayout(self.h2, 15)
        self.layout.addLayout(self.h3, 15)
        self.setLayout(self.layout)

    def resetButton(self):
        button = self.findChildren(QPushButton)
        for i in button:
            if i.value == 'cap':
                i.setText('')
                i.setIcon(QIcon(CAPLOCK_ICON))
                i.setIconSize(QSize(40, 40))
            elif i.value == 'con':
                i.setText('中')
            elif i.value == 'back':
                i.setText('')
                i.setIcon(QIcon(BACKSPACE_ICON))
                i.setIconSize(QSize(40, 40))
            elif i.value == 'close':
                i.setText('')
                i.setIcon(QIcon(CLOSE_ICON))
                i.setIconSize(QSize(40, 40))

    def getButtonInfo(self, info):
        if info == 'back':
            if self.pinyin == '':
                super().onKeyPressed(Qt.Key_Backspace, "")
            else:
                self.pinyin = self.pinyin[:-1]
                self.m_chineseWidget.setText(self.pinyin)
        elif info == 'cap':
            print(self.pinyin)
            return
        elif info == 'con':
            print(self.pinyin)
            return
        elif info == 'close':
            print(self.pinyin)
            return
        else:
            self.pinyin += info
            self.m_chineseWidget.setText(self.pinyin)
        print(self.pinyin)

    def clearBufferText(self):
        self.pinyin = ''
        self.m_chineseWidget.clear()

    # def onKeyPressed(self,value):
    #     print(value)
