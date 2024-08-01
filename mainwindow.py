# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QListView,
                               QMainWindow, QPushButton, QSizePolicy, QSlider,
                               QWidget, QPlainTextEdit)
import properties


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(properties.Properties.windowWidth, properties.Properties.windowHeight)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        MainWindow.setFixedSize(QSize(properties.Properties.windowWidth, properties.Properties.windowHeight))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_gen = QPushButton(self.centralwidget)
        self.btn_gen.setObjectName(u"btn_gen")
        self.btn_gen.setGeometry(QRect(10, 220, 171, 61))
        self.lst_pswd = QPlainTextEdit(self.centralwidget)
        self.lst_pswd.setObjectName(u"lst_pswd")
        self.lst_pswd.setReadOnly(True)
        self.lst_pswd.setGeometry(QRect(190, 10, 361, 271))
        self.chckbx_abc = QCheckBox(self.centralwidget)
        self.chckbx_abc.setObjectName(u"chckbx_abc")
        self.chckbx_abc.setGeometry(QRect(10, 20, 76, 20))
        self.chckbx_ABC = QCheckBox(self.centralwidget)
        self.chckbx_ABC.setObjectName(u"chckbx_ABC")
        self.chckbx_ABC.setGeometry(QRect(10, 50, 76, 20))
        self.chckbx_spec = QCheckBox(self.centralwidget)
        self.chckbx_spec.setObjectName(u"chckbx_spec")
        self.chckbx_spec.setGeometry(QRect(10, 110, 76, 20))
        self.chckbx_123 = QCheckBox(self.centralwidget)
        self.chckbx_123.setObjectName(u"chckbx_123")
        self.chckbx_123.setGeometry(QRect(10, 80, 76, 20))
        self.sl_qnt = QSlider(self.centralwidget)
        self.sl_qnt.setObjectName(u"sl_qnt")
        self.sl_qnt.setGeometry(QRect(10, 180, 171, 22))
        self.sl_qnt.setOrientation(Qt.Horizontal)
        self.sl_qnt.setRange(0, 30)
        self.sl_qnt.setSingleStep(1)
        self.sl_qnt.setTickInterval(1)
        self.lbl_qnt = QLabel(self.centralwidget)
        self.lbl_qnt.setObjectName(u"lbl_qnt")
        self.lbl_qnt.setGeometry(QRect(10, 160, 49, 16))
        self.lbl_qnt.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PassGen", None))
        self.btn_gen.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.chckbx_abc.setText(QCoreApplication.translate("MainWindow", u"abc", None))
        self.chckbx_ABC.setText(QCoreApplication.translate("MainWindow", u"ABC", None))
        self.chckbx_spec.setText(QCoreApplication.translate("MainWindow", u"/*-+", None))
        self.chckbx_123.setText(QCoreApplication.translate("MainWindow", u"123", None))
        self.lbl_qnt.setText(QCoreApplication.translate("MainWindow", u"0", None))
    # retranslateUi
