from exp8 import *


class Calculator:
    def __init__(self):
        ui.clear2.clicked.connect(self.clear)
        ui.calculate.clicked.connect(self.add)
        ui.calculate.clicked.connect(self.sub)
        ui.calculate.clicked.connect(self.mul)
        ui.calculate.clicked.connect(self.div)

    def clear(self):
        ui.resultline.setText("")

    def add(self):
        first = float(ui.First_lineEdit.text())
        second = float(ui.Second_lineEdit.text())
        try:
            addition = first + second
            if ui.addbtn.isChecked():
                ui.resultline.setText(str(addition))
        except:
            pass

    def sub(self):
        first = float(ui.First_lineEdit.text())
        second = float(ui.Second_lineEdit.text())
        try:
            subtract = first - second
            if ui.subbtn.isChecked():
                ui.resultline.setText(str(subtract))
        except:
            pass

    def mul(self):
        first = float(ui.First_lineEdit.text())
        second = float(ui.Second_lineEdit.text())
        try:
            multiply = first * second
            if ui.mulbtn.isChecked():
                ui.resultline.setText(str(multiply))
        except:
            pass

    def div(self):
        first = float(ui.First_lineEdit.text())
        second = float(ui.Second_lineEdit.text())
        try:
            divide = first / second
            if ui.divbtn.isChecked():
                ui.resultline.setText(str(divide))
        except:
            pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    File = open("Combinear.qss", 'r')
    with File:
        qss = File.read()
        app.setStyleSheet(qss)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    Calculator = Calculator()
    sys.exit(app.exec_())
