import os

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QApplication, QMainWindow

from lib.util import bundle_dir, train_config
from ui.mainwindow import Ui_MainWindow
from widgets.graphwindow import GraphWindow
from widgets.trainwindow import TrainWindow
from widgets.camerawindow import CameraWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.train_window: TrainWindow = None
        self.graph_window: GraphWindow = None
        self.camera_window: CameraWindow = None

        self.ui.openFolderBtn.clicked.connect(self.open_folder)
        self.ui.beginTrainingBtn.clicked.connect(self.open_train_window)
        self.ui.openCameraBtn.clicked.connect(self.open_camera_window)
        self.ui.plotDataBtn.clicked.connect(self.plot_data)

    def closeEvent(self, event):
        QApplication.closeAllWindows()

    def open_train_window(self):
        if self.train_window is None:
            self.train_window = TrainWindow()
        self.train_window.show()
        self.train_window.activateWindow()
        self.train_window.raise_()

    def open_camera_window(self):
        if self.camera_window is None:
            self.camera_window = CameraWindow()
        self.camera_window.show()
        self.camera_window.activateWindow()
        self.camera_window.raise_()

    def plot_data(self):
        if self.graph_window is None:
            self.graph_window = GraphWindow()
        self.graph_window.show()
        self.graph_window.activateWindow()
        self.graph_window.raise_()

    def open_folder(self):
        QDesktopServices.openUrl(QUrl.fromLocalFile(os.path.join(bundle_dir, train_config.get("data_dir"))))
