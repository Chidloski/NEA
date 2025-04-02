from PyQt5.QtWidgets import QLabel, QWidget, QRadioButton
from PyQt5.QtGui import QFontMetrics, QFont
from PyQt5 import QtCore
import math


class AutoResizingWidget(QWidget):
    def setFontParams(self, size, bold, padding, wordWrap):
        self.maxFont = size
        self.bold = bold
        self.padding = padding
        self.wordWrap = wordWrap

    def setText(self, text):
        super().setText(text)
        self.adjustFontSize()

    def setFont(self, font):
        if not self.resizing:  # Avoid recursive loop
            super().setFont(font)
            self.adjustFontSize()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.adjustFontSize()

    def adjustFontSize(self):

        if self.resizing or not self.text():
            return  # Prevent recursive calls
        
        self.resizing = True  # Set flag to avoid infinite loop
        font = super().font()
        fontSize = self.maxFont if font.pointSize() > 0 else 12  # Ensure valid font size
        font.setPointSize(fontSize)
        font.setBold(self.bold)
        fm = QFontMetrics(font)

        if not self.wordWrap:

            while fm.width(self.text()) > (self.width() - self.padding) and fontSize > 1:
                fontSize -= 1
                font.setPointSize(fontSize)
                fm = QFontMetrics(font)

            font.setPointSize(fontSize)

        while fontSize > 1:
            font.setPointSize(fontSize)
            fm = QFontMetrics(font)

            lines = fm.width(self.text()) / self.width()
            height = math.ceil((5 + fm.lineSpacing()) * lines)

            if self.objectName() == "descriptionLabel":
                print(f"lines: {lines}")
                print(f"height: {height}")

                print(f"current height {height}")
                print(f"label height {self.height()}")

            if height < self.height():
                break

            else:
                fontSize -= 1

        font.setPointSize(fontSize)

        super().setFont(font)  # Directly set font without triggering setFont()
        self.resizing = False


class AutoResizingLabel(QLabel, AutoResizingWidget):
    def __init__(self, fontSize, bold, wordWrap=False, text="", parent=None):
        super().__init__(parent)
        self.resizing = False
        self.setText(text)  # Set text properly
        self.setFontParams(fontSize, bold, 5, wordWrap)
        self.adjustFontSize()
        


class AutoResizingRadioButton(QRadioButton, AutoResizingWidget):
    def __init__(self, fontSize, bold, wordWrap=False, text="", parent=None):
        super().__init__(parent)
        self.resizing = False
        self.setText(text)  # Set text properly
        self.setFontParams(fontSize, bold, 20, wordWrap)
        self.adjustFontSize()



class AutoResizingClickableLabel(QLabel, AutoResizingWidget):
    # adds click functionality to QLabel
    clicked = QtCore.pyqtSignal(str)

    def __init__(self, fontSize, bold, wordWrap=False, text="", parent=None):
        super().__init__(parent)
        self.resizing = False
        self.setText(text)  # Set text properly
        self.setFontParams(fontSize, bold, 5, wordWrap)
        self.adjustFontSize()

    def mousePressEvent(self, event):
        # after each mouse press event, clickstate changes to clicked
        self.clickState = "Clicked"

    def mouseReleaseEvent(self, event):
        self.clicked.emit(self.clickState)

    def simulateClick(self):
        self.clicked.emit("Clicked")


class AutoResizingResponsiveClickableLabel(QLabel, AutoResizingWidget):
    # adds click functionality to QLabel
    clicked = QtCore.pyqtSignal(str)

    def __init__(self, fontSize, bold, wordWrap=False, text="", parent=None):
        super().__init__(parent)
        self.resizing = False
        self.setText(text)  # Set text properly
        self.setFontParams(fontSize, bold, 5, wordWrap)
        self.adjustFontSize()
        self.isClicked = False

    def createGroup(self, group):
        self.group = group

    def enterEvent(self, event):
        if not self.isClicked:
            self.setStyleSheet("color: rgb(225, 225, 225)")

    def leaveEvent(self, event):
        if not self.isClicked:
            self.setStyleSheet("color: 255, 255, 255")

    def mousePressEvent(self, event):
        # after each mouse press event, clickstate changes to clicked
        self.clickState = "Clicked"

    def mouseReleaseEvent(self, event):
        self.wipeGroup()
        self.isClicked = True
        self.setStyleSheet("color: rgb(237, 119, 47)")
        self.clicked.emit(self.clickState)

    def simulateClick(self):
        self.wipeGroup()
        self.isClicked = True
        self.setStyleSheet("color: rgb(237, 119, 47)")
        self.clicked.emit("Clicked")

    def wipeGroup(self):
        for label in self.group:
            label.setStyleSheet("color: 255, 255, 255")
            label.isClicked = False
