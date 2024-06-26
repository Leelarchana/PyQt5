# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\pyqt5\calci.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(379, 632)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 351, 161))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setLineWidth(2)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.clear = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("C"))
        self.clear.setGeometry(QtCore.QRect(10, 190, 80, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(24)
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        self.back = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.remove())
        self.back.setGeometry(QtCore.QRect(100, 190, 80, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(24)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.percent = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("%"))
        self.percent.setGeometry(QtCore.QRect(190, 190, 80, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(24)
        self.percent.setFont(font)
        self.percent.setObjectName("percent")
        self.divide = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("/"))
        self.divide.setGeometry(QtCore.QRect(280, 190, 80, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(24)
        self.divide.setFont(font)
        self.divide.setObjectName("divide")
        self.eight = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("8"))
        self.eight.setGeometry(QtCore.QRect(100, 270, 80, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(24)
        self.eight.setFont(font)
        self.eight.setObjectName("eight")
        self.seven = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("7"))
        self.seven.setGeometry(QtCore.QRect(10, 270, 80, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(24)
        self.seven.setFont(font)
        self.seven.setObjectName("seven")
        self.multiply = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("*"))
        self.multiply.setGeometry(QtCore.QRect(280, 270, 80, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(24)
        self.multiply.setFont(font)
        self.multiply.setObjectName("multiply")
        self.nine = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("9"))
        self.nine.setGeometry(QtCore.QRect(190, 270, 80, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(24)
        self.nine.setFont(font)
        self.nine.setObjectName("nine")
        self.five = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("5"))
        self.five.setGeometry(QtCore.QRect(100, 350, 80, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(24)
        self.five.setFont(font)
        self.five.setObjectName("five")
        self.four = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("4"))
        self.four.setGeometry(QtCore.QRect(10, 350, 80, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(24)
        self.four.setFont(font)
        self.four.setObjectName("four")
        self.minus = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("-"))
        self.minus.setGeometry(QtCore.QRect(280, 350, 80, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(24)
        self.minus.setFont(font)
        self.minus.setObjectName("minus")
        self.six = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("6"))
        self.six.setGeometry(QtCore.QRect(190, 350, 80, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(24)
        self.six.setFont(font)
        self.six.setObjectName("six")
        self.two = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("2"))
        self.two.setGeometry(QtCore.QRect(100, 430, 80, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(24)
        self.two.setFont(font)
        self.two.setObjectName("two")
        self.one = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("1"))
        self.one.setGeometry(QtCore.QRect(10, 430, 80, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(24)
        self.one.setFont(font)
        self.one.setObjectName("one")
        self.add = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("+"))
        self.add.setGeometry(QtCore.QRect(280, 430, 80, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(24)
        self.add.setFont(font)
        self.add.setObjectName("add")
        self.three = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("3"))
        self.three.setGeometry(QtCore.QRect(190, 430, 80, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(24)
        self.three.setFont(font)
        self.three.setObjectName("three")
        self.zero = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("0"))
        self.zero.setGeometry(QtCore.QRect(100, 510, 80, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(24)
        self.zero.setFont(font)
        self.zero.setObjectName("zero")
        self.plusminus = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.plus_minus())
        self.plusminus.setGeometry(QtCore.QRect(10, 510, 80, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(24)
        self.plusminus.setFont(font)
        self.plusminus.setObjectName("plusminus")
        self.equal = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.math_it())
        self.equal.setGeometry(QtCore.QRect(280, 510, 80, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(24)
        self.equal.setFont(font)
        self.equal.setObjectName("equal")
        self.decimal = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.dot())
        self.decimal.setGeometry(QtCore.QRect(190, 510, 80, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(24)
        self.decimal.setFont(font)
        self.decimal.setObjectName("decimal")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 379, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def math_it(self):
        screen = self.label.text()
        try:
            answer = eval(screen)
            self.label.setText(str(answer))
        except:
            self.label.setText("ERROR")
    
    def plus_minus(self):
        screen = self.label.text()
        if "-" in screen:
            self.label.setText(screen.replace("-",""))
        else:
            self.label.setText(f'-{screen}')   


    def remove(self):
        screen = self.label.text()
        screen = screen[:-1]
        self.label.setText(screen)


    def dot(self):
        screen = self.label.text()
        if "." in screen:
            pass
        else:
            self.label.setText(f'{screen}.')

    
    def press_it(self,pressed):
        if pressed == "C":
            self.label.setText("0")
        else:
            if self.label.text() == "0":
                self.label.setText("")
            self.label.setText(f'{self.label.text()}{pressed}') 


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.label.setText(_translate("MainWindow", "0"))
        self.clear.setText(_translate("MainWindow", "AC"))
        self.back.setText(_translate("MainWindow", "<<"))
        self.percent.setText(_translate("MainWindow", "%"))
        self.divide.setText(_translate("MainWindow", "/"))
        self.eight.setText(_translate("MainWindow", "8"))
        self.seven.setText(_translate("MainWindow", "7"))
        self.multiply.setText(_translate("MainWindow", "X"))
        self.nine.setText(_translate("MainWindow", "9"))
        self.five.setText(_translate("MainWindow", "5"))
        self.four.setText(_translate("MainWindow", "4"))
        self.minus.setText(_translate("MainWindow", "-"))
        self.six.setText(_translate("MainWindow", "6"))
        self.two.setText(_translate("MainWindow", "2"))
        self.one.setText(_translate("MainWindow", "1"))
        self.add.setText(_translate("MainWindow", "+"))
        self.three.setText(_translate("MainWindow", "3"))
        self.zero.setText(_translate("MainWindow", "0"))
        self.plusminus.setText(_translate("MainWindow", "+/-"))
        self.equal.setText(_translate("MainWindow", "="))
        self.decimal.setText(_translate("MainWindow", "."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
