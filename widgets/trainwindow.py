from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QProcess
from ui.trainwindow import Ui_TrainWindow

import sys
import os

class TrainWindow(QWidget):
  def __init__(self):
    super().__init__()
    self.ui = Ui_TrainWindow()
    self.ui.setupUi(self)
    
    self.process = QProcess()
    self.process.setProcessChannelMode(QProcess.MergedChannels)
    self.process.readyReadStandardOutput.connect(self.data_ready)
    self.process.started.connect(lambda: self.ui.trainBtn.setEnabled(False))
    self.process.finished.connect(lambda: self.ui.trainBtn.setEnabled(True))

    self.ui.closeBtn.clicked.connect(self.close)
    self.ui.trainBtn.clicked.connect(self.start_program)

  def start_program(self):
    self.process.start(sys.executable, [os.path.join("lib", "train.py")])

  def data_ready(self):
    cursor = self.ui.trainOutput.textCursor()
    cursor.movePosition(cursor.End)
    cursor.insertText(str(self.process.readAllStandardOutput().data(), encoding="utf-8"))
    self.ui.trainOutput.ensureCursorVisible()
