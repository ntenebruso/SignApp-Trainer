import math
import os

from PyQt5.QtWidgets import QWidget
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.image import imread

from lib.util import bundle_dir
from ui.graphwindow import Ui_GraphWindow

DATASET_PATH = os.path.join(bundle_dir, "rps_data_sample")


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
        num_images = self.ui.numInput.value()

        num_cols = 5
        num_rows = math.ceil(num_images / num_cols)

        label_dir = os.path.join(DATASET_PATH, current_option)
        example_filenames = os.listdir(label_dir)[:num_images]
        axs = self.figure.subplots(num_rows, num_cols, squeeze=False)

        count = 0
        for i in range(num_rows):
            for j in range(num_cols):
                if count <= num_images - 1:
                    axs[i][j].imshow(imread(os.path.join(label_dir, example_filenames[i + j])))
                axs[i][j].get_xaxis().set_visible(False)
                axs[i][j].get_yaxis().set_visible(False)
                count += 1

        self.figure.suptitle(f'Showing {num_images} for {current_option}')

        self.canvas.draw()
