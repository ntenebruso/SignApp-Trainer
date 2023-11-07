from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl

from ui.graphwindow import Ui_GraphWindow

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.image import imread

import os

DATASET_PATH = os.path.join(os.getcwd(), "rps_data_sample")

class GraphWindow(QWidget):
  def __init__(self):
    super(GraphWindow, self).__init__()

    self.ui = Ui_GraphWindow()
    self.ui.setupUi(self)

    self.get_folders()

    self.figure = Figure()
    self.canvas = FigureCanvas(self.figure)
    self.toolbar = NavigationToolbar(self.canvas)
    self.ui.graphContainer.addWidget(self.toolbar)
    self.ui.graphContainer.addWidget(self.canvas)
    self.ui.plotBtn.clicked.connect(self.plot)

  def get_folders(self):
    for path in os.listdir(DATASET_PATH):
      if os.path.isdir(os.path.join(DATASET_PATH, path)):
        self.ui.fileInput.addItem(path)

  def plot(self):
    self.figure.clear()
    
    current_option = self.ui.fileInput.currentText()
    label_dir = os.path.join(DATASET_PATH, current_option)
    example_filenames = os.listdir(label_dir)[:5]
    axs = self.figure.subplots(1, 5)
    for i in range(5):
      axs[i].imshow(imread(os.path.join(label_dir, example_filenames[i])))
      axs[i].get_xaxis().set_visible(False)
      axs[i].get_yaxis().set_visible(False)
    self.figure.suptitle(f'Showing 5 for {current_option}')

    self.canvas.draw()
