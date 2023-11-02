from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl

from ui.mainwindow import Ui_MainWindow

from widgets.trainwindow import TrainWindow

from lib.train import train
from lib.plot import plot

import os
from threading import Thread

class MainWindow(QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()
    
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)

    self.ui.openFolderBtn.clicked.connect(self.open_folder)
    self.ui.beginTrainingBtn.clicked.connect(self.open_train_window)
    self.ui.trainingInfoLabel.hide()

    self.ui.plotDataBtn.clicked.connect(self.plot_data)

  def open_train_window(self):
    self.train_window = TrainWindow()
    self.train_window.show()

  def plot_data(self):
    plot()

  def open_folder(self):
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

