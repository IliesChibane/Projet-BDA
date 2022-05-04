# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\M1\s2\bda\Projet-BDA\ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(775, 585)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(20, 20, 20);\n"
"background-color: rgb(58, 58, 58);")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.menu = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu.sizePolicy().hasHeightForWidth())
        self.menu.setSizePolicy(sizePolicy)
        self.menu.setMinimumSize(QtCore.QSize(200, 567))
        self.menu.setMaximumSize(QtCore.QSize(200, 16777215))
        self.menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu.setObjectName("menu")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.menu)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.slide = QtWidgets.QFrame(self.menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slide.sizePolicy().hasHeightForWidth())
        self.slide.setSizePolicy(sizePolicy)
        self.slide.setMinimumSize(QtCore.QSize(198, 0))
        self.slide.setMaximumSize(QtCore.QSize(198, 16777215))
        self.slide.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.slide.setFrameShadow(QtWidgets.QFrame.Raised)
        self.slide.setObjectName("slide")
        self.scrollArea = QtWidgets.QScrollArea(self.slide)
        self.scrollArea.setGeometry(QtCore.QRect(-10, -10, 211, 581))
        self.scrollArea.setMinimumSize(QtCore.QSize(211, 581))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 209, 579))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(209, 579))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 12pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 12pt \"Arial\";")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/icons/icons/chevrons-down.svg"))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_14 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_14)
        self.pushButton_5.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 italic 12pt \"Arial\";\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_7.addWidget(self.pushButton_5)
        self.verticalLayout_2.addWidget(self.frame_14)
        self.frame_15 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_15)
        self.pushButton_6.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 italic 12pt \"Arial\";\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_3.addWidget(self.pushButton_6)
        self.verticalLayout_2.addWidget(self.frame_15)
        self.frame_18 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_18)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_18)
        self.pushButton_7.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 italic 12pt \"Arial\";\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_4.addWidget(self.pushButton_7)
        self.verticalLayout_2.addWidget(self.frame_18)
        self.frame_7 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_8.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 italic 12pt \"Arial\";\n"
"")
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_5.addWidget(self.pushButton_8)
        self.verticalLayout_2.addWidget(self.frame_7)
        self.frame_13 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_13)
        self.pushButton_9.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 italic 12pt \"Arial\";\n"
"")
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_6.addWidget(self.pushButton_9)
        self.verticalLayout_2.addWidget(self.frame_13)
        self.frame_19 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_19)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_19)
        self.pushButton_10.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 italic 12pt \"Arial\";\n"
"")
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_7.addWidget(self.pushButton_10)
        self.verticalLayout_2.addWidget(self.frame_19)
        self.frame_16 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_16)
        self.pushButton_11.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 italic 12pt \"Arial\";\n"
"")
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_8.addWidget(self.pushButton_11)
        self.verticalLayout_2.addWidget(self.frame_16)
        self.frame_17 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_17)
        self.pushButton_12.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 italic 12pt \"Arial\";\n"
"")
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_9.addWidget(self.pushButton_12)
        self.verticalLayout_2.addWidget(self.frame_17)
        self.frame_12 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_13.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 italic 12pt \"Arial\";\n"
"")
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout_10.addWidget(self.pushButton_13)
        self.verticalLayout_2.addWidget(self.frame_12)
        self.frame_11 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_14.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 italic 12pt \"Arial\";\n"
"")
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout_11.addWidget(self.pushButton_14)
        self.verticalLayout_2.addWidget(self.frame_11)
        self.frame_8 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_15.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 italic 12pt \"Arial\";\n"
"")
        self.pushButton_15.setObjectName("pushButton_15")
        self.verticalLayout_12.addWidget(self.pushButton_15)
        self.verticalLayout_2.addWidget(self.frame_8)
        self.frame_10 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.pushButton_16 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_16.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 italic 12pt \"Arial\";\n"
"")
        self.pushButton_16.setObjectName("pushButton_16")
        self.verticalLayout_13.addWidget(self.pushButton_16)
        self.verticalLayout_2.addWidget(self.frame_10)
        self.frame_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.pushButton_17 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_17.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 italic 12pt \"Arial\";\n"
"")
        self.pushButton_17.setObjectName("pushButton_17")
        self.verticalLayout_14.addWidget(self.pushButton_17)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_9 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.pushButton_18 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_18.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 italic 12pt \"Arial\";\n"
"")
        self.pushButton_18.setObjectName("pushButton_18")
        self.verticalLayout_15.addWidget(self.pushButton_18)
        self.verticalLayout_2.addWidget(self.frame_9)
        self.frame_6 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.pushButton_19 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_19.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 italic 12pt \"Arial\";\n"
"")
        self.pushButton_19.setObjectName("pushButton_19")
        self.verticalLayout_16.addWidget(self.pushButton_19)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.slide, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout.addWidget(self.menu)
        self.corps = QtWidgets.QFrame(self.centralwidget)
        self.corps.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.corps.setFrameShadow(QtWidgets.QFrame.Raised)
        self.corps.setObjectName("corps")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.corps)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.head = QtWidgets.QFrame(self.corps)
        self.head.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.head.setFrameShadow(QtWidgets.QFrame.Raised)
        self.head.setObjectName("head")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.head)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame = QtWidgets.QFrame(self.head)
        self.frame.setMinimumSize(QtCore.QSize(50, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 0, 41, 41))
        self.pushButton_4.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButton_4.setMaximumSize(QtCore.QSize(41, 41))
        self.pushButton_4.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/align-center.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.frame, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.frame_2 = QtWidgets.QFrame(self.head)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/corner-left-down.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_5.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/x-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.horizontalLayout_3.addWidget(self.frame_2, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.head, 0, QtCore.Qt.AlignTop)
        self.main = QtWidgets.QFrame(self.corps)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy)
        self.main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main.setObjectName("main")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.main)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_17.addWidget(self.plainTextEdit)
        self.textEdit = QtWidgets.QTextEdit(self.main)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_17.addWidget(self.textEdit)
        self.verticalLayout.addWidget(self.main)
        self.foot = QtWidgets.QFrame(self.corps)
        self.foot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.foot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.foot.setObjectName("foot")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.foot)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_4 = QtWidgets.QFrame(self.foot)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 12pt \"Arial\";")
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 12pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.horizontalLayout_4.addWidget(self.frame_4, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.foot, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout.addWidget(self.corps)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Questions"))
        self.pushButton_5.setText(_translate("MainWindow", "QST 1"))
        self.pushButton_6.setText(_translate("MainWindow", "QST 2"))
        self.pushButton_7.setText(_translate("MainWindow", "QST 3"))
        self.pushButton_8.setText(_translate("MainWindow", "QST 4"))
        self.pushButton_9.setText(_translate("MainWindow", "QST 5"))
        self.pushButton_10.setText(_translate("MainWindow", "QST 6"))
        self.pushButton_11.setText(_translate("MainWindow", "QST 7"))
        self.pushButton_12.setText(_translate("MainWindow", "QST 8"))
        self.pushButton_13.setText(_translate("MainWindow", "QST 9"))
        self.pushButton_14.setText(_translate("MainWindow", "QST 10"))
        self.pushButton_15.setText(_translate("MainWindow", "QST 11"))
        self.pushButton_16.setText(_translate("MainWindow", "QST 12"))
        self.pushButton_17.setText(_translate("MainWindow", "QST 13"))
        self.pushButton_18.setText(_translate("MainWindow", "QST 14"))
        self.pushButton_19.setText(_translate("MainWindow", "QST 15"))
        self.label.setText(_translate("MainWindow", "BOUROUINA Rania"))
        self.label_2.setText(_translate("MainWindow", "CHIBANE Ilies"))
import icons_rc
