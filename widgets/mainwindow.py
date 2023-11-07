from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl

from ui.mainwindow import Ui_MainWindow

from widgets.trainwindow import TrainWindow
from widgets.graphwindow import GraphWindow

from lib.plot import plot

import os

class MainWindow(QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()
    
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)

    self.train_window = TrainWindow()
    self.graph_window = GraphWindow()

    self.ui.openFolderBtn.clicked.connect(self.open_folder)
    self.ui.beginTrainingBtn.clicked.connect(self.open_train_window)

    self.ui.plotDataBtn.clicked.connect(self.plot_data)

  def closeEvent(self, event):
    QApplication.closeAllWindows()

  def open_train_window(self):
    self.train_window.show()
    self.train_window.activateWindow()
    self.train_window.raise_()

  def plot_data(self):
    self.graph_window.show()
    self.graph_window.activateWindow()
    self.graph_window.raise_()

  def open_folder(self):
    QDesktopServices.openUrl(QUrl.fromLocalFile(os.path.join(os.getcwd(), "rps_data_sample")))

