# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Ksusha\PycharmProjects\Графика1\GOST94window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GOST94(object):
    def setupUi(self, GOST94):
        GOST94.setObjectName("GOST94")
        GOST94.resize(987, 572)
        self.centralwidget = QtWidgets.QWidget(GOST94)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 1, 1, 1)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.gridLayout.addWidget(self.plainTextEdit_2, 5, 0, 1, 2)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 1, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 6, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)


        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.plainTextEdit_3.setFont(font)
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.gridLayout.addWidget(self.plainTextEdit_3, 3, 0, 1, 2)


        GOST94.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GOST94)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 987, 26))
        self.menubar.setObjectName("menubar")
        GOST94.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GOST94)
        self.statusbar.setObjectName("statusbar")
        GOST94.setStatusBar(self.statusbar)

        self.retranslateUi(GOST94)
        QtCore.QMetaObject.connectSlotsByName(GOST94)

    def retranslateUi(self, GOST94):
        _translate = QtCore.QCoreApplication.translate
        GOST94.setWindowTitle(_translate("GOST94", "ГОСТ Р 34.11-94"))
        self.pushButton_2.setText(_translate("GOST94", "Вычислить из файла"))
        self.pushButton.setText(_translate("GOST94", "Вычислить"))
        self.pushButton_3.setText(_translate("GOST94", "Очистить"))
        self.label.setText(_translate("GOST94", "Введите текст:"))
        self.label_2.setText(_translate("GOST94", "Введите вектор инициализации:"))
