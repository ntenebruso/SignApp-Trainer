from PyQt5.QtWidgets import QWidget
from ui.trainwindow import Ui_TrainWindow

class TrainWindow(QWidget):
  def __init__(self):
    super().__init__()
    self.ui = Ui_TrainWindow()
    self.ui.setupUi(self)
