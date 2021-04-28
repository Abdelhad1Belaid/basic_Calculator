import sys
from PyQt5 import QtWidgets
import mainwindow
from PyQt5.QtWidgets import QMessageBox

class MainWindow(QtWidgets.QMainWindow):
    first_num = None
    second_num = None
    typing = False
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Connecting Buttons
        # About Button 
        self.ui.actionAbout.triggered.connect(self.about_pressed)


        # Digits
        self.ui.zero.clicked.connect(self.digit_pressed)
        self.ui.one.clicked.connect(self.digit_pressed)
        self.ui.two.clicked.connect(self.digit_pressed)
        self.ui.three.clicked.connect(self.digit_pressed)
        self.ui.four.clicked.connect(self.digit_pressed)
        self.ui.five.clicked.connect(self.digit_pressed)
        self.ui.six.clicked.connect(self.digit_pressed)
        self.ui.seven.clicked.connect(self.digit_pressed)
        self.ui.eight.clicked.connect(self.digit_pressed)
        self.ui.nine.clicked.connect(self.digit_pressed)

        # Decimal point 
        self.ui.comma.clicked.connect(self.comma_pressed)

        # Operations

        # Unary Operations
        self.ui.plus_minus.clicked.connect(self.unary_op_pressed)
        self.ui.percent.clicked.connect(self.unary_op_pressed)

        # Arithmetic operations
        self.ui.division.clicked.connect(self.binary_op_pressed)
        self.ui.multiply.clicked.connect(self.binary_op_pressed)
        self.ui.minus.clicked.connect(self.binary_op_pressed)
        self.ui.plus.clicked.connect(self.binary_op_pressed)
        # 
        self.ui.division.setCheckable(True)
        self.ui.multiply.setCheckable(True)
        self.ui.minus.setCheckable(True)
        self.ui.equal.setCheckable(True)
        self.ui.plus.setCheckable(True)

        # Clear Button
        self.ui.clear.clicked.connect(self.clear_pressed)

        # Equal Button
        self.ui.equal.clicked.connect(self.equals_pressed)

    # Defining Functions 
    # Digits function
    def digit_pressed(self):
        button = self.sender()
        if(self.ui.plus.isChecked() or self.ui.minus.isChecked() or self.ui.multiply.isChecked() or self.ui.division.isChecked()) and (not self.typing):
            content = format(float(button.text()), '.15g')
            self.typing = True
        else:
            if(('.' in self.ui.disp_screen.text()) and (button.text()=="0")):
                content = format(self.ui.disp_screen.text() + button.text(), '.15')
            else:
                content = format(float(self.ui.disp_screen.text() + button.text()), '.15g')
        self.ui.disp_screen.setText(content)

    # Comma Function
    def comma_pressed(self):
        content = self.ui.disp_screen.text()
        if('.' in content):
            pass
        else:
            self.ui.disp_screen.setText(content + '.')

    # Unary Operations
    def unary_op_pressed(self):
        button = self.sender()
        content = float(self.ui.disp_screen.text())
        if button.text() == chr(177):
            content*=-1
        else:
            content*=0.01
        content = format(content, '.15g')
        self.ui.disp_screen.setText(content)

    # Arithmetic Operations
    def binary_op_pressed(self):
        button = self.sender()
        self.first_num = float(self.ui.disp_screen.text())
        button.setChecked(True)

    def equals_pressed(self):
        self.second_num = float(self.ui.disp_screen.text())
        if self.ui.plus.isChecked():
            content = self.first_num + self.second_num
            self.ui.disp_screen.setText(format(content, '.15g'))
            self.ui.plus.setChecked(False)

        elif self.ui.minus.isChecked():
            content = self.first_num - self.second_num
            self.ui.disp_screen.setText(format(content, '.15g'))
            self.ui.minus.setChecked(False)

        elif self.ui.multiply.isChecked():
            content = self.first_num * self.second_num
            self.ui.disp_screen.setText(format(content, '.15g'))
            self.ui.multiply.setChecked(False)

        elif self.ui.division.isChecked():
            content = self.first_num / self.second_num
            self.ui.disp_screen.setText(format(content, '.15g'))
            self.ui.division.setChecked(False)
        self.typing = False

    # Clear Function
    def clear_pressed(self):
        self.ui.plus.setChecked(False)
        self.ui.minus.setChecked(False)
        self.ui.multiply.setChecked(False)
        self.ui.division.setChecked(False)
        self.typing = False
        self.ui.disp_screen.setText("0")

    # About Function
    def about_pressed(self):
	    msg = QMessageBox()
	    msg.setWindowTitle("About")
	    msg.setText("""@project: \tBasic Calculator
						@author: \tBelaid Abdelhadi
						@email: \tbelaidabdelhadi@gmail.com
						@social: \thttps://web.facebook.com/belaid.B.D.T.A.2010/
						@github: \thttps://github.com/Abdelhad1Belaid
						@linkedin: \thttps://www.linkedin.com/in/abdelhadi-belaid/""")
	    msg.setIcon(QMessageBox.Information)
	    x = msg.exec_()
