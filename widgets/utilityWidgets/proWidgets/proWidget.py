from PyQt5 import QtCore, QtGui, QtWidgets
from widgets.utilityWidgets.functions.proFunctions import *
from widgets.labelClasses import AutoResizingLabel, AutoResizingClickableLabel, AutoResizingResponsiveClickableLabel

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


class Ui_proWidget(QtWidgets.QWidget):
    def setupUi(self, dashboard):
        self.setObjectName("proWidget")
        self.resize(230, 560)

        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(24)
        font.setBold(True)

        self.prosLabel = AutoResizingLabel(24, True, parent = self)
        self.prosLabel.setGeometry(QtCore.QRect(10, 10, 201, 21))
        self.prosLabel.setFont(font)
        self.prosLabel.setObjectName("prosLabel")

        font.setPointSize(13)
        font.setBold(False)

        self.pro1Label = AutoResizingResponsiveClickableLabel(13, False, parent = self)
        self.pro1Label.setGeometry(QtCore.QRect(10, 50, 201, 16))
        self.pro1Label.setFont(font)
        self.pro1Label.setAlignment(QtCore.Qt.AlignCenter)
        self.pro1Label.setObjectName("pro1Label")
        self.pro1Label.clicked.connect(lambda: populateForPlayer(dashboard, "Magnus Carlsen"))

        self.pro2Label = AutoResizingResponsiveClickableLabel(13, False, parent = self)
        self.pro2Label.setGeometry(QtCore.QRect(10, 70, 201, 16))
        self.pro2Label.setFont(font)
        self.pro2Label.setAlignment(QtCore.Qt.AlignCenter)
        self.pro2Label.setObjectName("pro2Label")
        self.pro2Label.clicked.connect(lambda: populateForPlayer(dashboard, "Garry Kasparov"))

        self.pro3Label = AutoResizingResponsiveClickableLabel(13, False, parent = self)
        self.pro3Label.setGeometry(QtCore.QRect(10, 90, 201, 16))
        self.pro3Label.setFont(font)
        self.pro3Label.setAlignment(QtCore.Qt.AlignCenter)
        self.pro3Label.setObjectName("pro3Label")
        self.pro3Label.clicked.connect(lambda: populateForPlayer(dashboard, "Bobby Fischer"))

        self.pro4Label = AutoResizingResponsiveClickableLabel(13, False, parent = self)
        self.pro4Label.setGeometry(QtCore.QRect(10, 110, 201, 16))
        self.pro4Label.setFont(font)
        self.pro4Label.setAlignment(QtCore.Qt.AlignCenter)
        self.pro4Label.setObjectName("pro4Label")
        self.pro4Label.clicked.connect(lambda: populateForPlayer(dashboard, "José Raúl Capablanca"))

        self.pro5Label = AutoResizingResponsiveClickableLabel(13, False, parent = self)
        self.pro5Label.setGeometry(QtCore.QRect(10, 130, 201, 16))
        self.pro5Label.setFont(font)
        self.pro5Label.setAlignment(QtCore.Qt.AlignCenter)
        self.pro5Label.setObjectName("pro5Label")
        self.pro5Label.clicked.connect(lambda: populateForPlayer(dashboard, "Judit Polgár"))

        self.pro1Label.createGroup([self.pro1Label, self.pro2Label, self.pro3Label, self.pro4Label, self.pro5Label])
        self.pro2Label.createGroup([self.pro1Label, self.pro2Label, self.pro3Label, self.pro4Label, self.pro5Label])
        self.pro3Label.createGroup([self.pro1Label, self.pro2Label, self.pro3Label, self.pro4Label, self.pro5Label])
        self.pro4Label.createGroup([self.pro1Label, self.pro2Label, self.pro3Label, self.pro4Label, self.pro5Label])
        self.pro5Label.createGroup([self.pro1Label, self.pro2Label, self.pro3Label, self.pro4Label, self.pro5Label])

        self.pro1Label.isClicked = True
        self.pro1Label.setStyleSheet("color: rgb(237, 119, 47)")

        self.infoLabel = AutoResizingResponsiveClickableLabel(13, False, parent = self)
        self.infoLabel.setGeometry(QtCore.QRect(10, 470, 201, 16))
        self.infoLabel.setFont(font)
        self.infoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.infoLabel.setObjectName("infoLabel")
        self.infoLabel.clicked.connect(lambda: goToInfo(dashboard))

        self.match1Label = AutoResizingResponsiveClickableLabel(13, False, parent = self)
        self.match1Label.setGeometry(QtCore.QRect(10, 490, 201, 16))
        self.match1Label.setFont(font)
        self.match1Label.setAlignment(QtCore.Qt.AlignCenter)
        self.match1Label.setObjectName("match1Label")
        self.match1Label.clicked.connect(lambda: populateForMatch(dashboard, 1))

        self.match2Label = AutoResizingResponsiveClickableLabel(13, False, parent = self)
        self.match2Label.setGeometry(QtCore.QRect(10, 510, 201, 16))
        self.match2Label.setFont(font)
        self.match2Label.setAlignment(QtCore.Qt.AlignCenter)
        self.match2Label.setObjectName("match2Label")
        self.match2Label.clicked.connect(lambda: populateForMatch(dashboard, 2))

        self.match3Label = AutoResizingResponsiveClickableLabel(13, False, parent = self)
        self.match3Label.setGeometry(QtCore.QRect(10, 530, 201, 16))
        self.match3Label.setFont(font)
        self.match3Label.setAlignment(QtCore.Qt.AlignCenter)
        self.match3Label.setObjectName("match3Label")
        self.match3Label.clicked.connect(lambda: populateForMatch(dashboard, 3))

        self.infoLabel.createGroup([self.infoLabel, self.match1Label, self.match2Label, self.match3Label])
        self.match1Label.createGroup([self.infoLabel, self.match1Label, self.match2Label, self.match3Label])
        self.match2Label.createGroup([self.infoLabel, self.match1Label, self.match2Label, self.match3Label])
        self.match3Label.createGroup([self.infoLabel, self.match1Label, self.match2Label, self.match3Label])

        self.infoLabel.isClicked = True
        self.infoLabel.setStyleSheet("color: rgb(237, 119, 47)")

        font.setPointSize(18)
        font.setBold(True)

        self.matchLabel = AutoResizingLabel(18, True, parent = self)
        self.matchLabel.setGeometry(QtCore.QRect(10, 200, 201, 16))
        self.matchLabel.setFont(font)
        self.matchLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.matchLabel.setObjectName("matchLabel")
        self.matchLabel.setHidden(True)

        font.setPointSize(10)
        font.setBold(False)

        self.yearLabel = AutoResizingLabel(10, False, parent = self)
        self.yearLabel.setGeometry(QtCore.QRect(20, 230, 191, 16))
        self.yearLabel.setFont(font)
        self.yearLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.yearLabel.setObjectName("yearLabel")
        self.yearLabel.setHidden(True)

        self.tournamentLabel = AutoResizingLabel(10, False, parent = self)
        self.tournamentLabel.setGeometry(QtCore.QRect(20, 250, 191, 16))
        self.tournamentLabel.setFont(font)
        self.tournamentLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tournamentLabel.setObjectName("tournamentLabel")
        self.tournamentLabel.setHidden(True)

        self.matchupLabel = AutoResizingLabel(10, False, parent = self)
        self.matchupLabel.setGeometry(QtCore.QRect(20, 270, 191, 16))
        self.matchupLabel.setFont(font)
        self.matchupLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.matchupLabel.setObjectName("matchupLabel")
        self.matchupLabel.setHidden(True)

        self.outcomeLabel = AutoResizingLabel(10, False, parent = self)
        self.outcomeLabel.setGeometry(QtCore.QRect(20, 290, 191, 16))
        self.outcomeLabel.setFont(font)
        self.outcomeLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.outcomeLabel.setObjectName("outcomeLabel")
        self.outcomeLabel.setHidden(True)
        
        self.matchDescriptionLabel = AutoResizingLabel(10, False, wordWrap=True, parent = self)
        self.matchDescriptionLabel.setGeometry(QtCore.QRect(20, 310, 191, 55))
        self.matchDescriptionLabel.setFont(font)
        self.matchDescriptionLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.matchDescriptionLabel.setObjectName("matchDescriptionLabel")
        self.matchDescriptionLabel.setWordWrap(True)
        self.matchDescriptionLabel.setHidden(True)

        self.fullBackButton = AutoResizingClickableLabel(10, False, parent = self)
        self.fullBackButton.setGeometry(QtCore.QRect(20, 380, 51, 41))
        self.fullBackButton.setFont(font)
        self.fullBackButton.setObjectName("fullBackButton")
        self.fullBackButton.setHidden(True)
        self.fullBackButton.clicked.connect(lambda: fullBackMove(dashboard))

        self.backButton = AutoResizingClickableLabel(10, False, parent = self)
        self.backButton.setGeometry(QtCore.QRect(70, 380, 51, 41))
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")
        self.backButton.setHidden(True)
        self.backButton.clicked.connect(lambda: backwardMove(dashboard))

        self.forwardButton = AutoResizingClickableLabel(10, False, parent = self)
        self.forwardButton.setGeometry(QtCore.QRect(120, 380, 51, 41))
        self.forwardButton.setFont(font)
        self.forwardButton.setObjectName("forwardButton")
        self.forwardButton.setHidden(True)
        self.forwardButton.clicked.connect(lambda: forwardMove(dashboard))

        self.fullForwardButton = AutoResizingClickableLabel(10, False, parent = self)
        self.fullForwardButton.setGeometry(QtCore.QRect(170, 380, 51, 41))
        self.fullForwardButton.setFont(font)
        self.fullForwardButton.setObjectName("fullForwardButton")
        self.fullForwardButton.setHidden(True)
        self.fullForwardButton.clicked.connect(lambda: fullForwardMove(dashboard))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.prosLabel.setText(_translate("proWidget", "Pros"))
        self.pro1Label.setText(_translate("proWidget", "Magnus Carlsen"))
        self.pro2Label.setText(_translate("proWidget", "Garry Kasparov"))
        self.pro3Label.setText(_translate("proWidget", "Bobby Fischer"))
        self.pro4Label.setText(_translate("proWidget", "José Raúl Capablanca"))
        self.pro5Label.setText(_translate("proWidget", "Judit Polgár"))
        self.infoLabel.setText(_translate("proWidget", "Info"))
        self.match1Label.setText(_translate("proWidget", "Match 1"))
        self.match2Label.setText(_translate("proWidget", "Match 2"))
        self.match3Label.setText(_translate("proWidget", "Match 3"))
        self.matchLabel.setText(_translate("proWidget", "Match 1:"))
        self.yearLabel.setText(_translate("proWidget", "2018"))
        self.tournamentLabel.setText(_translate("proWidget", "World Championship"))
        self.matchupLabel.setText(_translate("proWidget", "Carlsen vs Niemann"))
        self.outcomeLabel.setText(_translate("proWidget", "Win by checkmate"))
        self.matchDescriptionLabel.setText(_translate("proWidget", "Final of the tournament"))
        self.fullBackButton.setText(_translate("proWidget", "<<-"))
        self.backButton.setText(_translate("proWidget", "<-"))
        self.forwardButton.setText(_translate("proWidget", "->"))
        self.fullForwardButton.setText(_translate("proWidget", "->>"))
