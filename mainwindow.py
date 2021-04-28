# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calculator.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(243, 380)
        MainWindow.setMinimumSize(QtCore.QSize(243, 380))
        MainWindow.setMaximumSize(QtCore.QSize(243, 380))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.disp_screen = QtWidgets.QLabel(self.centralwidget)
        self.disp_screen.setGeometry(QtCore.QRect(0, 0, 243, 61))
        self.disp_screen.setMinimumSize(QtCore.QSize(243, 61))
        self.disp_screen.setMaximumSize(QtCore.QSize(243, 61))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(18)
        font.setBold(False)
        self.disp_screen.setFont(font)
        self.disp_screen.setStyleSheet("QLabel{\n"
"    qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"    border: 1px solid gray;\n"
"    border-radius:10px;\n"
"    background-color:white;\n"
"    color:black;\n"
"}\n"
"")
        self.disp_screen.setObjectName("disp_screen")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(0, 60, 61, 61))
        self.clear.setMinimumSize(QtCore.QSize(61, 61))
        self.clear.setMaximumSize(QtCore.QSize(61, 61))
        font = QtGui.QFont()
        font.setFamily("Semi-Coder")
        font.setPointSize(1)
        self.clear.setFont(font)
        self.clear.setStyleSheet("QPushButton{\n"
"       background-color: rgb(215, 215, 215);\n"
"       border: 1px solid gray;\n"
"    border-radius:10px;\n"
"    color:black;\n"
"    font-family:Semi-Coder;\n"
"    font-size:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.clear.setObjectName("clear")
        self.plus_minus = QtWidgets.QPushButton(self.centralwidget)
        self.plus_minus.setGeometry(QtCore.QRect(60, 60, 61, 61))
        self.plus_minus.setMinimumSize(QtCore.QSize(61, 61))
        self.plus_minus.setMaximumSize(QtCore.QSize(61, 61))
        font = QtGui.QFont()
        font.setFamily("Semi-Coder")
        font.setPointSize(1)
        self.plus_minus.setFont(font)
        self.plus_minus.setStyleSheet("QPushButton{\n"
"       background-color: rgb(215, 215, 215);\n"
"       border: 1px solid gray;\n"
"    border-radius:10px;\n"
"    color:black;\n"
"    font-family:Semi-Coder;\n"
"    font-size:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.plus_minus.setObjectName("plus_minus")
        self.division = QtWidgets.QPushButton(self.centralwidget)
        self.division.setGeometry(QtCore.QRect(180, 60, 61, 61))
        self.division.setMinimumSize(QtCore.QSize(61, 61))
        self.division.setMaximumSize(QtCore.QSize(61, 61))
        font = QtGui.QFont()
        font.setFamily("Semi-Coder")
        font.setPointSize(1)
        self.division.setFont(font)
        self.division.setStyleSheet("QPushButton{\n"
"       background-color: rgb(255, 151, 57);\n"
"       color: white;\n"
"       border: 1px solid gray;\n"
"    border-radius:10px;\n"
"    font-family:Semi-Coder;\n"
"    font-size:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}\n"
"")
        self.division.setObjectName("division")
        self.percent = QtWidgets.QPushButton(self.centralwidget)
        self.percent.setGeometry(QtCore.QRect(120, 60, 61, 61))
        self.percent.setMinimumSize(QtCore.QSize(61, 61))
        self.percent.setMaximumSize(QtCore.QSize(61, 61))
        font = QtGui.QFont()
        font.setFamily("Semi-Coder")
        font.setPointSize(1)
        self.percent.setFont(font)
        self.percent.setStyleSheet("QPushButton{\n"
"       background-color: rgb(215, 215, 215);\n"
"       border: 1px solid gray;\n"
"    border-radius:10px;\n"
"    color:black;\n"
"    font-family:Semi-Coder;\n"
"    font-size:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.percent.setObjectName("percent")
        self.eight = QtWidgets.QPushButton(self.centralwidget)
        self.eight.setGeometry(QtCore.QRect(60, 120, 61, 61))
        self.eight.setMinimumSize(QtCore.QSize(61, 61))
        self.eight.setMaximumSize(QtCore.QSize(61, 61))
        font = QtGui.QFont()
        font.setFamily("Semi-Coder")
        font.setPointSize(1)
        self.eight.setFont(font)
        self.eight.setStyleSheet("QPushButton{\n"
"       border: 1px solid gray;\n"
"    border-radius:10px;\n"
"    color:black;\n"
"    font-family:Semi-Coder;\n"
"    font-size:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.eight.setObjectName("eight")
        self.nine = QtWidgets.QPushButton(self.centralwidget)
        self.nine.setGeometry(QtCore.QRect(120, 120, 61, 61))
        self.nine.setMinimumSize(QtCore.QSize(61, 61))
        self.nine.setMaximumSize(QtCore.QSize(61, 61))
        font = QtGui.QFont()
        font.setFamily("Semi-Coder")
        font.setPointSize(1)
        self.nine.setFont(font)
        self.nine.setStyleSheet("QPushButton{\n"
"       border: 1px solid gray;\n"
"    border-radius:10px;\n"
"    color:black;\n"
"    font-family:Semi-Coder;\n"
"    font-size:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.nine.setObjectName("nine")
        self.seven = QtWidgets.QPushButton(self.centralwidget)
        self.seven.setGeometry(QtCore.QRect(0, 120, 61, 61))
        self.seven.setMinimumSize(QtCore.QSize(61, 61))
        self.seven.setMaximumSize(QtCore.QSize(61, 61))
        font = QtGui.QFont()
        font.setFamily("Semi-Coder")
        font.setPointSize(1)
        self.seven.setFont(font)
        self.seven.setStyleSheet("QPushButton{\n"
"       border: 1px solid gray;\n"
"    border-radius:10px;\n"
"    color:black;\n"
"    font-family:Semi-Coder;\n"
"    font-size:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.seven.setObjectName("seven")
        self.multiply = QtWidgets.QPushButton(self.centralwidget)
        self.multiply.setGeometry(QtCore.QRect(180, 120, 61, 61))
        self.multiply.setMinimumSize(QtCore.QSize(61, 61))
        self.multiply.setMaximumSize(QtCore.QSize(61, 61))
        font = QtGui.QFont()
        font.setFamily("Semi-Coder")
        font.setPointSize(1)
        self.multiply.setFont(font)
        self.multiply.setStyleSheet("QPushButton{\n"
"       background-color: rgb(255, 151, 57);\n"
"       color: white;\n"
"       border: 1px solid gray;\n"
"    border-radius:10px;\n"
"    font-family:Semi-Coder;\n"
"    font-size:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}\n"
"")
        self.multiply.setObjectName("multiply")
        self.five = QtWidgets.QPushButton(self.centralwidget)
        self.five.setGeometry(QtCore.QRect(60, 180, 61, 61))
        self.five.setMinimumSize(QtCore.QSize(61, 61))
        self.five.setMaximumSize(QtCore.QSize(61, 61))
        font = QtGui.QFont()
        font.setFamily("Semi-Coder")
        font.setPointSize(1)
        self.five.setFont(font)
        self.five.setStyleSheet("QPushButton{\n"
"       border: 1px solid gray;\n"
"    border-radius:10px;\n"
"    color:black;\n"
"    font-family:Semi-Coder;\n"
"    font-size:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.five.setObjectName("five")
        self.six = QtWidgets.QPushButton(self.centralwidget)
        self.six.setGeometry(QtCore.QRect(120, 180, 61, 61))
        self.six.setMinimumSize(QtCore.QSize(61, 61))
        self.six.setMaximumSize(QtCore.QSize(61, 61))
        font = QtGui.QFont()
        font.setFamily("Semi-Coder")
        font.setPointSize(1)
        self.six.setFont(font)
        self.six.setStyleSheet("QPushButton{\n"
"       border: 1px solid gray;\n"
"    border-radius:10px;\n"
"    color:black;\n"
"    font-family:Semi-Coder;\n"
"    font-size:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.six.setObjectName("six")
        self.plus = QtWidgets.QPushButton(self.centralwidget)
        self.plus.setGeometry(QtCore.QRect(180, 240, 61, 61))
        self.plus.setMinimumSize(QtCore.QSize(61, 61))
        self.plus.setMaximumSize(QtCore.QSize(61, 61))
        font = QtGui.QFont()
        font.setFamily("Semi-Coder")
        font.setPointSize(1)
        self.plus.setFont(font)
        self.plus.setStyleSheet("QPushButton{\n"
"       background-color: rgb(255, 151, 57);\n"
"       color: white;\n"
"       border: 1px solid gray;\n"
"    border-radius:10px;\n"
"    font-family:Semi-Coder;\n"
"    font-size:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}\n"
"")
        self.plus.setObjectName("plus")
        self.four = QtWidgets.QPushButton(self.centralwidget)
        self.four.setGeometry(QtCore.QRect(0, 180, 61, 61))
        self.four.setMinimumSize(QtCore.QSize(61, 61))
        self.four.setMaximumSize(QtCore.QSize(61, 61))
        font = QtGui.QFont()
        font.setFamily("Semi-Coder")
        font.setPointSize(1)
        self.four.setFont(font)
        self.four.setStyleSheet("QPushButton{\n"
"       border: 1px solid gray;\n"
"    border-radius:10px;\n"
"    color:black;\n"
"    font-family:Semi-Coder;\n"
"    font-size:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.four.setObjectName("four")
        self.one = QtWidgets.QPushButton(self.centralwidget)
        self.one.setGeometry(QtCore.QRect(0, 240, 61, 61))
        self.one.setMinimumSize(QtCore.QSize(61, 61))
        self.one.setMaximumSize(QtCore.QSize(61, 61))
        font = QtGui.QFont()
        font.setFamily("Semi-Coder")
        font.setPointSize(1)
        self.one.setFont(font)
        self.one.setStyleSheet("QPushButton{\n"
"       border: 1px solid gray;\n"
"    border-radius:10px;\n"
"    color:black;\n"
"    font-family:Semi-Coder;\n"
"    font-size:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.one.setObjectName("one")
        self.two = QtWidgets.QPushButton(self.centralwidget)
        self.two.setGeometry(QtCore.QRect(60, 240, 61, 61))
        self.two.setMinimumSize(QtCore.QSize(61, 61))
        self.two.setMaximumSize(QtCore.QSize(61, 61))
        font = QtGui.QFont()
        font.setFamily("Semi-Coder")
        font.setPointSize(1)
        self.two.setFont(font)
        self.two.setStyleSheet("QPushButton{\n"
"       border: 1px solid gray;\n"
"    border-radius:10px;\n"
"    color:black;\n"
"    font-family:Semi-Coder;\n"
"    font-size:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.two.setObjectName("two")
        self.minus = QtWidgets.QPushButton(self.centralwidget)
        self.minus.setGeometry(QtCore.QRect(180, 180, 61, 61))
        self.minus.setMinimumSize(QtCore.QSize(61, 61))
        self.minus.setMaximumSize(QtCore.QSize(61, 61))
        font = QtGui.QFont()
        font.setFamily("Semi-Coder")
        font.setPointSize(1)
        self.minus.setFont(font)
        self.minus.setStyleSheet("QPushButton{\n"
"       background-color: rgb(255, 151, 57);\n"
"       color: white;\n"
"       border: 1px solid gray;\n"
"    border-radius:10px;\n"
"    font-family:Semi-Coder;\n"
"    font-size:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}\n"
"")
        self.minus.setObjectName("minus")
        self.three = QtWidgets.QPushButton(self.centralwidget)
        self.three.setGeometry(QtCore.QRect(120, 240, 61, 61))
        self.three.setMinimumSize(QtCore.QSize(61, 61))
        self.three.setMaximumSize(QtCore.QSize(61, 61))
        font = QtGui.QFont()
        font.setFamily("Semi-Coder")
        font.setPointSize(1)
        self.three.setFont(font)
        self.three.setStyleSheet("QPushButton{\n"
"       border: 1px solid gray;\n"
"    border-radius:10px;\n"
"    color:black;\n"
"    font-family:Semi-Coder;\n"
"    font-size:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.three.setObjectName("three")
        self.zero = QtWidgets.QPushButton(self.centralwidget)
        self.zero.setGeometry(QtCore.QRect(0, 300, 121, 61))
        self.zero.setMinimumSize(QtCore.QSize(121, 61))
        self.zero.setMaximumSize(QtCore.QSize(121, 61))
        font = QtGui.QFont()
        font.setFamily("Semi-Coder")
        font.setPointSize(1)
        self.zero.setFont(font)
        self.zero.setStyleSheet("QPushButton{\n"
"       border: 1px solid gray;\n"
"    border-radius:10px;\n"
"    color:black;\n"
"    font-family:Semi-Coder;\n"
"    font-size:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.zero.setObjectName("zero")
        self.comma = QtWidgets.QPushButton(self.centralwidget)
        self.comma.setGeometry(QtCore.QRect(120, 300, 61, 61))
        self.comma.setMinimumSize(QtCore.QSize(61, 61))
        self.comma.setMaximumSize(QtCore.QSize(61, 61))
        font = QtGui.QFont()
        font.setFamily("Semi-Coder")
        font.setPointSize(1)
        self.comma.setFont(font)
        self.comma.setStyleSheet("QPushButton{\n"
"       background-color: rgb(215, 215, 215);\n"
"       border: 1px solid gray;\n"
"    border-radius:10px;\n"
"    color:black;\n"
"    font-family:Semi-Coder;\n"
"    font-size:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.comma.setObjectName("comma")
        self.equal = QtWidgets.QPushButton(self.centralwidget)
        self.equal.setGeometry(QtCore.QRect(180, 300, 61, 61))
        self.equal.setMinimumSize(QtCore.QSize(61, 61))
        self.equal.setMaximumSize(QtCore.QSize(61, 61))
        font = QtGui.QFont()
        font.setFamily("Semi-Coder")
        font.setPointSize(1)
        self.equal.setFont(font)
        self.equal.setStyleSheet("QPushButton{\n"
"       background-color: rgb(255, 151, 57);\n"
"       color: white;\n"
"       border: 1px solid gray;\n"
"    border-radius:10px;\n"
"    font-family:Semi-Coder;\n"
"    font-size:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}\n"
"")
        self.equal.setObjectName("equal")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 243, 17))
        self.menuBar.setMinimumSize(QtCore.QSize(243, 10))
        self.menuBar.setObjectName("menuBar")
        self.menuMenu = QtWidgets.QMenu(self.menuBar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menuBar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuMenu.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.disp_screen.setText(_translate("MainWindow", "0"))
        self.clear.setText(_translate("MainWindow", "C"))
        self.clear.setShortcut(_translate("MainWindow", "Ctrl+Backspace"))
        self.plus_minus.setText(_translate("MainWindow", "±"))
        self.plus_minus.setShortcut(_translate("MainWindow", "_"))
        self.division.setText(_translate("MainWindow", "÷"))
        self.division.setShortcut(_translate("MainWindow", "/"))
        self.percent.setText(_translate("MainWindow", "%"))
        self.percent.setShortcut(_translate("MainWindow", "%"))
        self.eight.setText(_translate("MainWindow", "8"))
        self.eight.setShortcut(_translate("MainWindow", "8"))
        self.nine.setText(_translate("MainWindow", "9"))
        self.nine.setShortcut(_translate("MainWindow", "9"))
        self.seven.setText(_translate("MainWindow", "7"))
        self.seven.setShortcut(_translate("MainWindow", "7"))
        self.multiply.setText(_translate("MainWindow", "x"))
        self.multiply.setShortcut(_translate("MainWindow", "*"))
        self.five.setText(_translate("MainWindow", "5"))
        self.five.setShortcut(_translate("MainWindow", "5"))
        self.six.setText(_translate("MainWindow", "6"))
        self.six.setShortcut(_translate("MainWindow", "6"))
        self.plus.setText(_translate("MainWindow", "+"))
        self.plus.setShortcut(_translate("MainWindow", "+"))
        self.four.setText(_translate("MainWindow", "4"))
        self.four.setShortcut(_translate("MainWindow", "4"))
        self.one.setText(_translate("MainWindow", "1"))
        self.one.setShortcut(_translate("MainWindow", "1"))
        self.two.setText(_translate("MainWindow", "2"))
        self.two.setShortcut(_translate("MainWindow", "2"))
        self.minus.setText(_translate("MainWindow", "-"))
        self.minus.setShortcut(_translate("MainWindow", "-"))
        self.three.setText(_translate("MainWindow", "3"))
        self.three.setShortcut(_translate("MainWindow", "3"))
        self.zero.setText(_translate("MainWindow", "0"))
        self.comma.setText(_translate("MainWindow", "."))
        self.equal.setText(_translate("MainWindow", "="))
        self.equal.setShortcut(_translate("MainWindow", "Return"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
