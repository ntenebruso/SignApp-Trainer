from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl
from ui.mainwindow import Ui_MainWindow

from lib.train import train

import os
from threading import Thread

class MainWindow(QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()
    
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)

    self.ui.openFolderBtn.clicked.connect(self.openFolder)
    self.ui.beginTrainingBtn.clicked.connect(self.train)
    self.ui.trainingInfoLabel.hide()

  def openFolder(self):
    QDesktopServices.openUrl(QUrl.fromLocalFile(os.path.join(os.getcwd(), "rps_data_sample")))

  def train(self):
    self.ui.beginTrainingBtn.setDisabled(True)
    self.ui.trainingInfoLabel.show()
    trainingThread = Thread(target=self.run_thread)
    trainingThread.start()

  def run_thread(self):
    train()
    self.ui.beginTrainingBtn.setDisabled(False)
    self.ui.trainingInfoLabel.hide()

