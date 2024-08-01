# This Python file uses the following encoding: utf-8
import sys, random
from PySide6.QtWidgets import QApplication, QMainWindow

import charsets
import properties
from mainwindow import Ui_MainWindow

buffer = ""


class PassGen(QMainWindow):

    def __init__(self):
        super(PassGen, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.sl_qnt.valueChanged.connect(self.sl_value_changed)
        self.ui.btn_gen.clicked.connect(self.generatePass)

    def sl_value_changed(self):
        self.ui.lbl_qnt.setText(str(self.ui.sl_qnt.value()))

    def generatePass(self):
        global buffer
        for i in range(10):
            self.empty_master()
            self.check_boxes()
            buffer += str(self.create_pass()) + "\n"
        self.print_passwords()
        buffer = ""

    def check_boxes(self):
        if self.ui.chckbx_123.isChecked():
            charsets.master_chset.composition += str(charsets.digits_chset.composition)
        if self.ui.chckbx_abc.isChecked():
            charsets.master_chset.composition += str(charsets.lowercase_chset.composition)
        if self.ui.chckbx_ABC.isChecked():
            charsets.master_chset.composition += str(charsets.uppercase_chset.composition)
        if self.ui.chckbx_spec.isChecked():
            charsets.master_chset.composition += str(charsets.special_chset.composition)

    def empty_master(self):
        charsets.master_chset.composition = ""

    def count_master(self):
        return charsets.master_chset.count()

    def pick_char(self):
        gen_char = charsets.master_chset.composition[random.randrange(0, charsets.master_chset.count() - 1)]
        return gen_char

    def create_pass(self):
        password = ""
        for i in range(0, self.ui.sl_qnt.value()):
            password += self.pick_char()
        return password

    def print_passwords(self):
        self.ui.lst_pswd.setPlainText(buffer)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = PassGen()
    window.show()

    sys.exit(app.exec())
