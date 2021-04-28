#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 03:57:20 2021
@project : Basic Calculator
@author  : Belaid Abdelhadi
@email   : belaidabdelhadi@gmail.com
@social  : https://web.facebook.com/belaid.B.D.T.A.2010/
@github  : https://github.com/Abdelhad1Belaid
@linkedin: https://www.linkedin.com/in/abdelhadi-belaid/
"""
from Calculator import *

def main():
    app = QtWidgets.QApplication(sys.argv)

    Calculator = MainWindow()
    Calculator.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()