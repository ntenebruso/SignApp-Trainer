# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(641, 407)
        MainWindow.setMinimumSize(QtCore.QSize(295, 330))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(10, 10, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.openFolderBtn = QtWidgets.QPushButton(self.centralwidget)
        self.openFolderBtn.setGeometry(QtCore.QRect(10, 90, 261, 51))
        self.openFolderBtn.setObjectName("openFolderBtn")
        self.beginTrainingBtn = QtWidgets.QPushButton(self.centralwidget)
        self.beginTrainingBtn.setGeometry(QtCore.QRect(10, 160, 261, 51))
        self.beginTrainingBtn.setObjectName("beginTrainingBtn")
        self.plotDataBtn = QtWidgets.QPushButton(self.centralwidget)
        self.plotDataBtn.setGeometry(QtCore.QRect(10, 230, 261, 51))
        self.plotDataBtn.setObjectName("plotDataBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 641, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titleLabel.setText(_translate("MainWindow", "SignApp Trainer"))
        self.openFolderBtn.setText(_translate("MainWindow", "Open Training Folder"))
        self.beginTrainingBtn.setText(_translate("MainWindow", "Begin Training!"))
        self.plotDataBtn.setText(_translate("MainWindow", "Plot Data"))
