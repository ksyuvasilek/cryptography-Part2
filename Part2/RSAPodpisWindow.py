# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Ksusha\PycharmProjects\Графика1\RSAPodpisWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RSAPodpisWind(object):
    def setupUi(self, RSAPodpisWind):
        RSAPodpisWind.setObjectName("RSAPodpisWind")
        RSAPodpisWind.resize(1557, 1033)
        RSAPodpisWind.setMinimumSize(QtCore.QSize(0, 0))
        RSAPodpisWind.setMaximumSize(QtCore.QSize(4564756, 16777215))
        RSAPodpisWind.setGeometry(200, 50, 1500, 970)
        RSAPodpisWind.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(RSAPodpisWind)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.e1 = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.e1.setFont(font)
        self.e1.setReadOnly(False)
        self.e1.setObjectName("e1")
        self.gridLayout.addWidget(self.e1, 0, 4, 2, 2)
        self.p = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p.setFont(font)
        self.p.setObjectName("p")
        self.gridLayout.addWidget(self.p, 0, 1, 2, 2)
        self.N1 = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.N1.setFont(font)
        self.N1.setReadOnly(False)
        self.N1.setObjectName("N1")
        self.gridLayout.addWidget(self.N1, 2, 4, 2, 2)
        self.q = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.q.setFont(font)
        self.q.setObjectName("q")
        self.gridLayout.addWidget(self.q, 2, 1, 2, 2)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 7, 3, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 6, 3, 1, 1)
        self.N = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.N.setFont(font)
        self.N.setReadOnly(True)
        self.N.setObjectName("N")
        self.gridLayout.addWidget(self.N, 4, 1, 2, 2)
        self.s1 = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.s1.setFont(font)
        self.s1.setReadOnly(False)
        self.s1.setObjectName("s1")
        self.gridLayout.addWidget(self.s1, 4, 4, 2, 2)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 6, 4, 1, 1)
        self.textProverka = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textProverka.setFont(font)
        self.textProverka.setReadOnly(False)
        self.textProverka.setObjectName("textProverka")
        self.gridLayout.addWidget(self.textProverka, 7, 4, 1, 2)
        self.e = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.e.setFont(font)
        self.e.setReadOnly(False)
        self.e.setObjectName("e")
        self.gridLayout.addWidget(self.e, 7, 1, 1, 2)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 11, 1, 1, 1)
        self.auto_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.auto_2.setFont(font)
        self.auto_2.setObjectName("auto_2")
        self.gridLayout.addWidget(self.auto_2, 11, 4, 1, 1)
        self.resVerification = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.resVerification.setFont(font)
        self.resVerification.setReadOnly(True)
        self.resVerification.setObjectName("resVerification")
        self.gridLayout.addWidget(self.resVerification, 9, 4, 2, 2)
        self.checkFile = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkFile.setFont(font)
        self.checkFile.setObjectName("checkFile")
        self.gridLayout.addWidget(self.checkFile, 8, 5, 1, 1)
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        self.gridLayout.addWidget(self.clear, 11, 5, 1, 1)
        self.textToPodpis = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textToPodpis.setFont(font)
        self.textToPodpis.setReadOnly(False)
        self.textToPodpis.setObjectName("textToPodpis")
        self.gridLayout.addWidget(self.textToPodpis, 12, 1, 1, 2)
        self.checkText = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkText.setFont(font)
        self.checkText.setObjectName("checkText")
        self.gridLayout.addWidget(self.checkText, 8, 4, 1, 1)
        self.signText = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.signText.setFont(font)
        self.signText.setObjectName("signText")
        self.gridLayout.addWidget(self.signText, 13, 1, 1, 1)
        self.signFile = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.signFile.setFont(font)
        self.signFile.setObjectName("signFile")
        self.gridLayout.addWidget(self.signFile, 13, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 12, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 11, 0, 1, 1)
        self.d = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.d.setFont(font)
        self.d.setReadOnly(False)
        self.d.setBackgroundVisible(False)
        self.d.setObjectName("d")
        self.gridLayout.addWidget(self.d, 9, 1, 2, 2)
        self.s = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.s.setFont(font)
        self.s.setReadOnly(True)
        self.s.setObjectName("s")
        self.gridLayout.addWidget(self.s, 14, 1, 1, 2)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 14, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 12, 4, 4, 2)
        self.genPQ = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.genPQ.setFont(font)
        self.genPQ.setObjectName("genPQ")
        self.gridLayout.addWidget(self.genPQ, 6, 1, 1, 1)
        self.calcCD = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.calcCD.setFont(font)
        self.calcCD.setObjectName("calcCD")
        self.gridLayout.addWidget(self.calcCD, 6, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 9, 0, 2, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 2, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 2, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 2, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 3, 2, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 3, 2, 1)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 4, 3, 2, 1)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 9, 3, 2, 1)
        RSAPodpisWind.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RSAPodpisWind)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1557, 26))
        self.menubar.setObjectName("menubar")
        RSAPodpisWind.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RSAPodpisWind)
        self.statusbar.setObjectName("statusbar")
        RSAPodpisWind.setStatusBar(self.statusbar)

        self.retranslateUi(RSAPodpisWind)
        QtCore.QMetaObject.connectSlotsByName(RSAPodpisWind)

    def retranslateUi(self, RSAPodpisWind):
        _translate = QtCore.QCoreApplication.translate
        RSAPodpisWind.setWindowTitle(_translate("RSAPodpisWind", "КМЗИ"))
        self.label_12.setText(_translate("RSAPodpisWind", "Введите текст:"))
        self.label_15.setText(_translate("RSAPodpisWind", "Хэш-функция:"))
        self.comboBox_2.setItemText(0, _translate("RSAPodpisWind", "MD5"))
        self.comboBox_2.setItemText(1, _translate("RSAPodpisWind", "SHA-1"))
        self.comboBox_2.setItemText(2, _translate("RSAPodpisWind", "ГОСТ Р 34.11-94"))
        self.comboBox.setItemText(0, _translate("RSAPodpisWind", "MD5"))
        self.comboBox.setItemText(1, _translate("RSAPodpisWind", "SHA-1"))
        self.comboBox.setItemText(2, _translate("RSAPodpisWind", "ГОСТ Р 34.11-94"))
        self.auto_2.setText(_translate("RSAPodpisWind", "Автозаполнение"))
        self.checkFile.setText(_translate("RSAPodpisWind", "Проверить файл"))
        self.clear.setText(_translate("RSAPodpisWind", "Очистить"))
        self.checkText.setText(_translate("RSAPodpisWind", "Проверить"))
        self.signText.setText(_translate("RSAPodpisWind", "Подписать"))
        self.signFile.setText(_translate("RSAPodpisWind", "Подписать файл"))
        self.label_9.setText(_translate("RSAPodpisWind", "Введите текст:"))
        self.label_8.setText(_translate("RSAPodpisWind", "Хэш-функция:"))
        self.label_10.setText(_translate("RSAPodpisWind", "Подпись:"))
        self.genPQ.setText(_translate("RSAPodpisWind", "Сгенерировать p и q"))
        self.calcCD.setText(_translate("RSAPodpisWind", "Вычисление ключей"))
        self.label_3.setText(_translate("RSAPodpisWind", "Открытый ключ e ="))
        self.label_4.setText(_translate("RSAPodpisWind", "Закрытый ключ d ="))
        self.label_5.setText(_translate("RSAPodpisWind", "N = "))
        self.label_2.setText(_translate("RSAPodpisWind", "Простое число q = "))
        self.label.setText(_translate("RSAPodpisWind", "Простое число p = "))
        self.label_6.setText(_translate("RSAPodpisWind", "Открытый ключ e ="))
        self.label_7.setText(_translate("RSAPodpisWind", "N = "))
        self.label_13.setText(_translate("RSAPodpisWind", "Подпись:"))
        self.label_14.setText(_translate("RSAPodpisWind", "Результат проверки:"))
