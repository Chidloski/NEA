from PyQt5 import QtCore, QtGui, QtWidgets
from widgets.menuWidgets.functions.menuFunctions import *
from widgets.labelClasses import AutoResizingResponsiveClickableLabel, AutoResizingClickableLabel

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

        self.playSection = AutoResizingResponsiveClickableLabel(24, True, parent=self)
        self.playSection.setGeometry(QtCore.QRect(10, 10, 101, 31))
        self.playSection.setFont(font)
        self.playSection.setObjectName("playSection")

        self.playSection.clicked.connect(lambda: goToPlay(dashboard))

        self.puzzleSection = AutoResizingResponsiveClickableLabel(24, True, parent=self)
        self.puzzleSection.setGeometry(QtCore.QRect(10, 50, 101, 31))
        self.puzzleSection.setFont(font)
        self.puzzleSection.setObjectName("puzzleSection")

        self.puzzleSection.clicked.connect(lambda: goToPuzzles(dashboard))

        self.prosSection = AutoResizingResponsiveClickableLabel(24, True, parent=self)
        self.prosSection.setGeometry(QtCore.QRect(10, 90, 111, 31))
        self.prosSection.setFont(font)
        self.prosSection.setObjectName("prosSection")

        self.prosSection.clicked.connect(lambda: goToPros(dashboard))

        font.setBold(False)
        font.setPointSize(16)

        self.accountSection = AutoResizingResponsiveClickableLabel(16, False, parent=self)
        self.accountSection.setGeometry(10, 490, 101, 26)
        self.accountSection.setFont(font)
        self.accountSection.setObjectName("accountSection")
        self.accountSection.clicked.connect(lambda: goToAccount(dashboard))

        self.logOut = AutoResizingResponsiveClickableLabel(16, False, parent=self)
        self.logOut.setGeometry(QtCore.QRect(10, 520, 101, 26))
        self.logOut.setFont(font)
        self.logOut.setObjectName("logOut")
        self.logOut.clicked.connect(lambda: logOut(dashboard))

        self.playSection.createGroup([self.playSection, self.puzzleSection, self.prosSection, self.accountSection, self.logOut])
        self.puzzleSection.createGroup([self.playSection, self.puzzleSection, self.prosSection, self.accountSection, self.logOut])
        self.prosSection.createGroup([self.playSection, self.puzzleSection, self.prosSection, self.accountSection, self.logOut])
        self.accountSection.createGroup([self.playSection, self.puzzleSection, self.prosSection, self.accountSection, self.logOut])
        self.logOut.createGroup([self.playSection, self.puzzleSection, self.prosSection, self.accountSection, self.logOut])

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.playSection.setText(_translate("menuPage", "Play"))
        self.puzzleSection.setText(_translate("menuPage", "Puzzles"))
        self.prosSection.setText(_translate("menuPage", "Pros"))
        self.logOut.setText(_translate("menuPage", "Log Out"))
        self.accountSection.setText(_translate("menuPage", "Account"))
