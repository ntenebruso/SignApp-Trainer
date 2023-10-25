from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl
from ui.mainwindow import Ui_MainWindow
import os

class MainWindow(QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()
    
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)

    self.ui.openFolderBtn.clicked.connect(self.openFolder)

  def openFolder(self):
    QDesktopServices.openUrl(QUrl.fromLocalFile(os.path.join(os.getcwd(), "rps_data_sample")))
