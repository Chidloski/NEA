from PyQt5 import QtCore, QtGui, QtWidgets
from widgets.menuWidgets.functions.menuFunctions import *

# makes a clickable label
class clickableLabel(QtWidgets.QLabel):

    # adds click functionality to QLabel
    clicked = QtCore.pyqtSignal(str)

    # initialises the QLabel parent
    def __init__(self, *args, **kwargs):
        QtWidgets.QLabel.__init__(self, *args, **kwargs)

    def mousePressEvent(self, event):
        # after each mouse press event, clickstate changes to clicked
        self.clickState = "Clicked"

    def mouseReleaseEvent(self, event):
            self.clicked.emit(self.clickState)



class Ui_Menu(QtWidgets.QWidget):
    def setupUi(self, dashboard):
        self.setObjectName("menuPage")
        self.resize(130, 560)

        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(24)
        font.setBold(True)

        self.playSection = clickableLabel(self)
        self.playSection.setGeometry(QtCore.QRect(10, 10, 101, 31))
        self.playSection.setFont(font)
        self.playSection.setObjectName("playSection")

        self.playSection.clicked.connect(lambda: goToPlay(dashboard))

        self.puzzleSection = clickableLabel(self)
        self.puzzleSection.setGeometry(QtCore.QRect(10, 50, 101, 31))
        self.puzzleSection.setFont(font)
        self.puzzleSection.setObjectName("puzzleSection")

        self.puzzleSection.clicked.connect(lambda: goToPuzzles(dashboard))

        self.prosSection = clickableLabel(self)
        self.prosSection.setGeometry(QtCore.QRect(10, 90, 101, 31))
        self.prosSection.setFont(font)
        self.prosSection.setObjectName("prosSection")

        font.setBold(False)

        self.logOut = clickableLabel(self)
        self.logOut.setGeometry(QtCore.QRect(10, 520, 101, 26))
        self.logOut.setFont(font)
        self.logOut.setObjectName("logOut")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.playSection.setText(_translate("menuPage", "Play"))
        self.puzzleSection.setText(_translate("menuPage", "Puzzles"))
        self.prosSection.setText(_translate("menuPage", "Pros"))
        self.logOut.setText(_translate("menuPage", "Log Out"))
