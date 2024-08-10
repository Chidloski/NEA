from PyQt5 import QtCore, QtGui, QtWidgets
from widgets.utilityWidgets.functions.proFunctions import *


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


class Ui_infoBoard(QtWidgets.QWidget):
    def setupUi(self, dashboard):
        self.setObjectName("infoBoard")
        self.resize(560, 560)

        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(28)
        font.setBold(True)

        self.proNameLabel = QtWidgets.QLabel(self)
        self.proNameLabel.setGeometry(QtCore.QRect(10, 10, 531, 31))
        self.proNameLabel.setFont(font)
        self.proNameLabel.setObjectName("proNameLabel")

        self.imageLabel = QtWidgets.QLabel(self)
        self.imageLabel.setGeometry(QtCore.QRect(10, 50, 271, 251))
        self.imageLabel.setFont(font)
        self.imageLabel.setText("")
        self.imageLabel.setObjectName("imageLabel")
        self.imageLabel.setScaledContents(True)

        font.setPointSize(16)
        font.setBold(False)

        self.overviewLabel = QtWidgets.QLabel(self)
        self.overviewLabel.setGeometry(QtCore.QRect(300, 50, 221, 20))
        self.overviewLabel.setFont(font)
        self.overviewLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.overviewLabel.setObjectName("overviewLabel")

        self.majorWinsLabel = QtWidgets.QLabel(self)
        self.majorWinsLabel.setGeometry(QtCore.QRect(300, 210, 221, 20))
        self.majorWinsLabel.setFont(font)
        self.majorWinsLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.majorWinsLabel.setObjectName("majorWinsLabel")

        font.setPointSize(11)

        self.peakRatingLabel = QtWidgets.QLabel(self)
        self.peakRatingLabel.setGeometry(QtCore.QRect(310, 170, 211, 16))
        self.peakRatingLabel.setFont(font)
        self.peakRatingLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.peakRatingLabel.setObjectName("peakRatingLabel")

        self.titleLabel = QtWidgets.QLabel(self)
        self.titleLabel.setGeometry(QtCore.QRect(310, 150, 211, 16))
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.titleLabel.setObjectName("titleLabel")

        self.birthLabel = QtWidgets.QLabel(self)
        self.birthLabel.setGeometry(QtCore.QRect(310, 120, 211, 16))
        self.birthLabel.setFont(font)
        self.birthLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.birthLabel.setObjectName("birthLabel")

        self.genderLabel = QtWidgets.QLabel(self)
        self.genderLabel.setGeometry(QtCore.QRect(310, 100, 211, 16))
        self.genderLabel.setFont(font)
        self.genderLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.genderLabel.setObjectName("genderLabel")

        self.nationalityLabel = QtWidgets.QLabel(self)
        self.nationalityLabel.setGeometry(QtCore.QRect(310, 80, 211, 16))
        self.nationalityLabel.setFont(font)
        self.nationalityLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.nationalityLabel.setObjectName("nationalityLabel")

        self.major1Label = QtWidgets.QLabel(self)
        self.major1Label.setGeometry(QtCore.QRect(310, 240, 211, 16))
        self.major1Label.setFont(font)
        self.major1Label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.major1Label.setObjectName("major1Label")

        self.major2Label = QtWidgets.QLabel(self)
        self.major2Label.setGeometry(QtCore.QRect(310, 260, 211, 16))
        self.major2Label.setFont(font)
        self.major2Label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.major2Label.setObjectName("major2Label")

        self.major3Label = QtWidgets.QLabel(self)
        self.major3Label.setGeometry(QtCore.QRect(310, 280, 211, 16))
        self.major3Label.setFont(font)
        self.major3Label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.major3Label.setObjectName("major3Label")

        font.setPointSize(12)

        self.descriptionLabel = QtWidgets.QLabel(self)
        self.descriptionLabel.setGeometry(QtCore.QRect(10, 310, 521, 231))
        self.descriptionLabel.setFont(font)
        self.descriptionLabel.setWordWrap(True)
        self.descriptionLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.descriptionLabel.setObjectName("descriptionLabel")

        font.setPointSize(18)

        self.backLabel = clickableLabel(self)
        self.backLabel.setGeometry(QtCore.QRect(20, 168, 16, 16))
        self.backLabel.setFont(font)
        self.backLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.backLabel.setObjectName("backLabel")
        self.backLabel.clicked.connect(lambda: switchPhoto(self, -1))

        self.forwardLabel = clickableLabel(self)
        self.forwardLabel.setGeometry(QtCore.QRect(260, 168, 16, 16))
        self.forwardLabel.setFont(font)
        self.forwardLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.forwardLabel.setObjectName("forwardLabel")
        self.forwardLabel.clicked.connect(lambda: switchPhoto(self, 1))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        populateForPlayer(dashboard, "Magnus Carlsen")

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.proNameLabel.setText(_translate("infoBoard", "Magnus Carlsen"))
        self.overviewLabel.setText(_translate("infoBoard", "Overview:"))
        self.majorWinsLabel.setText(_translate("infoBoard", "Major Wins:"))
        self.peakRatingLabel.setText(_translate("infoBoard", "• Peak Rating: 2882"))
        self.titleLabel.setText(_translate("infoBoard", "• Title: Grandmaster (GM) "))
        self.birthLabel.setText(_translate("infoBoard", "• Born: 30 November, 1990 "))
        self.genderLabel.setText(_translate("infoBoard", "• Gender: Male"))
        self.nationalityLabel.setText(_translate("infoBoard", "• Nationality: Norwegian"))
        self.major1Label.setText(_translate("infoBoard", "• 5x World Chess Champion"))
        self.major2Label.setText(_translate("infoBoard", "• Triple Crown Winner"))
        self.major3Label.setText(_translate("infoBoard", "• Highest ever FIDE Rating"))
        self.descriptionLabel.setText(_translate("infoBoard", "Magnus Carlsen is a Norwegian chess grandmaster and one of the greatest players in history. He became a grandmaster at 13, quickly challenging the world\'s best with his sharp intuition. His deep understanding of chess and consistent top-level performance have made him a dominant force since 2010, setting numerous records in the process.\n"
"\n"
"Carlsen\'s playstyle is marked by versatility and adaptability, thriving in any position. He excels in all phases of the game — openings, middlegames, and endgames — and is known for squeezing wins from seemingly drawn positions with exceptional precision. His legendary endgame skills, combined with an uncanny ability to maintain focus under pressure, make him incredibly difficult to beat, often outlasting opponents in long, grueling battles."))
        self.backLabel.setText(_translate("infoBoard", "<"))
        self.forwardLabel.setText(_translate("infoBoard", ">"))

