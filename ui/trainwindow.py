# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/trainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TrainWindow(object):
    def setupUi(self, TrainWindow):
        TrainWindow.setObjectName("TrainWindow")
        TrainWindow.resize(589, 347)
        self.gridLayout = QtWidgets.QGridLayout(TrainWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.trainOutput = QtWidgets.QPlainTextEdit(TrainWindow)
        font = QtGui.QFont()
        font.setFamily("Andale Mono")
        self.trainOutput.setFont(font)
        self.trainOutput.setReadOnly(True)
        self.trainOutput.setPlainText("")
        self.trainOutput.setObjectName("trainOutput")
        self.gridLayout.addWidget(self.trainOutput, 0, 1, 1, 2)
        self.closeBtn = QtWidgets.QPushButton(TrainWindow)
        self.closeBtn.setObjectName("closeBtn")
        self.gridLayout.addWidget(self.closeBtn, 2, 2, 1, 1)
        self.trainBtn = QtWidgets.QPushButton(TrainWindow)
        self.trainBtn.setObjectName("trainBtn")
        self.gridLayout.addWidget(self.trainBtn, 2, 1, 1, 1)

        self.retranslateUi(TrainWindow)
        QtCore.QMetaObject.connectSlotsByName(TrainWindow)

    def retranslateUi(self, TrainWindow):
        _translate = QtCore.QCoreApplication.translate
        TrainWindow.setWindowTitle(_translate("TrainWindow", "Model Trainer"))
        self.closeBtn.setText(_translate("TrainWindow", "Close"))
        self.trainBtn.setText(_translate("TrainWindow", "Start Training"))
