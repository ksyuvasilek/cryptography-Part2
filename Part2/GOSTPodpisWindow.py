# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Ksusha\PycharmProjects\Графика1\GOSTPodpisWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GOSTPodpisWind(object):
    def setupUi(self, GOSTPodpisWind):
        GOSTPodpisWind.setObjectName("GOSTPodpisWind")
        GOSTPodpisWind.resize(1557, 1045)
        GOSTPodpisWind.setMinimumSize(QtCore.QSize(0, 0))
        GOSTPodpisWind.setMaximumSize(QtCore.QSize(4564756, 16777215))
        GOSTPodpisWind.setGeometry(200, 40, 1500, 970)
        font = QtGui.QFont()
        font.setPointSize(12)
        GOSTPodpisWind.setFont(font)
        GOSTPodpisWind.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(GOSTPodpisWind)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.q = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.q.setFont(font)
        self.q.setObjectName("q")
        self.gridLayout.addWidget(self.q, 2, 1, 2, 2)
        self.a1 = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.a1.setFont(font)
        self.a1.setReadOnly(False)
        self.a1.setObjectName("a1")
        self.gridLayout.addWidget(self.a1, 4, 4, 2, 2)
        self.q1 = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.q1.setFont(font)
        self.q1.setReadOnly(False)
        self.q1.setObjectName("q1")
        self.gridLayout.addWidget(self.q1, 2, 4, 2, 2)
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
        self.p1 = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p1.setFont(font)
        self.p1.setReadOnly(False)
        self.p1.setObjectName("p1")
        self.gridLayout.addWidget(self.p1, 0, 4, 2, 2)
        self.p = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p.setFont(font)
        self.p.setObjectName("p")
        self.gridLayout.addWidget(self.p, 0, 1, 2, 2)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 3, 2, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 14, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 11, 3, 2, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 11, 0, 2, 1)
        self.Ya1 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Ya1.setObjectName("Ya1")
        self.gridLayout.addWidget(self.Ya1, 9, 4, 1, 2)
        self.r1 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.r1.setObjectName("r1")
        self.gridLayout.addWidget(self.r1, 11, 4, 1, 2)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 4, 3, 2, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 3, 2, 1)
        self.a = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.a.setFont(font)
        self.a.setReadOnly(False)
        self.a.setObjectName("a")
        self.gridLayout.addWidget(self.a, 4, 1, 2, 2)
        self.signFile = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.signFile.setFont(font)
        self.signFile.setObjectName("signFile")
        self.gridLayout.addWidget(self.signFile, 15, 2, 1, 1)
        self.signText = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.signText.setFont(font)
        self.signText.setObjectName("signText")
        self.gridLayout.addWidget(self.signText, 15, 1, 1, 1)
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        self.gridLayout.addWidget(self.clear, 17, 5, 1, 1)
        self.resVerification = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.resVerification.setFont(font)
        self.resVerification.setReadOnly(True)
        self.resVerification.setObjectName("resVerification")
        self.gridLayout.addWidget(self.resVerification, 16, 4, 1, 2)
        self.textProverka = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textProverka.setFont(font)
        self.textProverka.setReadOnly(False)
        self.textProverka.setObjectName("textProverka")
        self.gridLayout.addWidget(self.textProverka, 14, 4, 1, 2)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 16, 0, 1, 1)
        self.s = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.s.setFont(font)
        self.s.setReadOnly(True)
        self.s.setObjectName("s")
        self.gridLayout.addWidget(self.s, 17, 1, 1, 2)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 16, 3, 1, 1)
        self.checkText = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkText.setFont(font)
        self.checkText.setObjectName("checkText")
        self.gridLayout.addWidget(self.checkText, 15, 4, 1, 1)
        self.textToPodpis = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textToPodpis.setFont(font)
        self.textToPodpis.setReadOnly(False)
        self.textToPodpis.setObjectName("textToPodpis")
        self.gridLayout.addWidget(self.textToPodpis, 14, 1, 1, 2)
        self.checkFile = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkFile.setFont(font)
        self.checkFile.setObjectName("checkFile")
        self.gridLayout.addWidget(self.checkFile, 15, 5, 1, 1)
        self.r = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.r.setReadOnly(True)
        self.r.setObjectName("r")
        self.gridLayout.addWidget(self.r, 16, 1, 1, 2)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 14, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 17, 0, 1, 1)
        self.k = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.k.setReadOnly(True)
        self.k.setObjectName("k")
        self.gridLayout.addWidget(self.k, 13, 1, 1, 2)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 13, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 13, 0, 1, 1)
        self.s1 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.s1.setObjectName("s1")
        self.gridLayout.addWidget(self.s1, 13, 4, 1, 2)
        self.Xa = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Xa.setFont(font)
        self.Xa.setReadOnly(False)
        self.Xa.setBackgroundVisible(False)
        self.Xa.setObjectName("Xa")
        self.gridLayout.addWidget(self.Xa, 11, 1, 2, 2)
        self.genPQ = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.genPQ.setFont(font)
        self.genPQ.setObjectName("genPQ")
        self.gridLayout.addWidget(self.genPQ, 6, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 2, 1)
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
        self.gridLayout.addWidget(self.label_3, 9, 0, 1, 1)
        self.auto_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.auto_2.setFont(font)
        self.auto_2.setObjectName("auto_2")
        self.gridLayout.addWidget(self.auto_2, 17, 4, 1, 1)
        self.Ya = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Ya.setFont(font)
        self.Ya.setReadOnly(False)
        self.Ya.setObjectName("Ya")
        self.gridLayout.addWidget(self.Ya, 9, 1, 1, 2)
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 9, 3, 1, 1)
        GOSTPodpisWind.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GOSTPodpisWind)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1557, 26))
        self.menubar.setObjectName("menubar")
        GOSTPodpisWind.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GOSTPodpisWind)
        self.statusbar.setObjectName("statusbar")
        GOSTPodpisWind.setStatusBar(self.statusbar)

        self.retranslateUi(GOSTPodpisWind)
        QtCore.QMetaObject.connectSlotsByName(GOSTPodpisWind)

    def retranslateUi(self, GOSTPodpisWind):
        _translate = QtCore.QCoreApplication.translate
        GOSTPodpisWind.setWindowTitle(_translate("GOSTPodpisWind", "КМЗИ"))
        self.label_2.setText(_translate("GOSTPodpisWind", "q = "))
        self.label.setText(_translate("GOSTPodpisWind", "p = "))
        self.label_6.setText(_translate("GOSTPodpisWind", "p = "))
        self.label_9.setText(_translate("GOSTPodpisWind", "Введите текст:"))
        self.label_18.setText(_translate("GOSTPodpisWind", "r ="))
        self.label_4.setText(_translate("GOSTPodpisWind", "Закрытый ключ x ="))
        self.label_13.setText(_translate("GOSTPodpisWind", "a ="))
        self.label_7.setText(_translate("GOSTPodpisWind", "q ="))
        self.signFile.setText(_translate("GOSTPodpisWind", "Подписать файл"))
        self.signText.setText(_translate("GOSTPodpisWind", "Подписать"))
        self.clear.setText(_translate("GOSTPodpisWind", "Очистить"))
        self.label_17.setText(_translate("GOSTPodpisWind", "r = "))
        self.label_14.setText(_translate("GOSTPodpisWind", "Результат проверки:"))
        self.checkText.setText(_translate("GOSTPodpisWind", "Проверить"))
        self.checkFile.setText(_translate("GOSTPodpisWind", "Проверить файл"))
        self.label_12.setText(_translate("GOSTPodpisWind", "Введите текст:"))
        self.label_10.setText(_translate("GOSTPodpisWind", "s = "))
        self.label_16.setText(_translate("GOSTPodpisWind", "s ="))
        self.label_11.setText(_translate("GOSTPodpisWind", "k = "))
        self.genPQ.setText(_translate("GOSTPodpisWind", "Сгенерировать p и q"))
        self.label_5.setText(_translate("GOSTPodpisWind", "a = "))
        self.calcCD.setText(_translate("GOSTPodpisWind", "Вычисление параметров"))
        self.label_3.setText(_translate("GOSTPodpisWind", "Открытый ключ y ="))
        self.auto_2.setText(_translate("GOSTPodpisWind", "Автозаполнение"))
        self.label_19.setText(_translate("GOSTPodpisWind", "Открытый ключ y ="))
