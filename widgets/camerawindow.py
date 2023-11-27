from PyQt5.QtWidgets import QWidget
from PyQt5.QtMultimedia import QCameraInfo, QCamera
from PyQt5.QtCore import Qt

from ui.camerawindow import Ui_CameraWindow


class CameraWindow(QWidget):
    def __init__(self):
        super(CameraWindow, self).__init__()

        self.ui = Ui_CameraWindow()
        self.ui.setupUi(self)

        self.available_cameras: list[QCameraInfo] = None
        self.camera: QCamera = None

        self.get_available_cameras()
        self.select_camera(0)

        self.ui.cameraInput.currentIndexChanged.connect(lambda index: self.select_camera(index))

    def get_available_cameras(self):
        self.available_cameras = QCameraInfo.availableCameras()
        for i in self.available_cameras:
            self.ui.cameraInput.addItem(i.description())

    def select_camera(self, index):
        self.camera = QCamera(self.available_cameras[index])
        self.camera.setViewfinder(self.ui.cameraOutput)
        self.camera.start()

    def showEvent(self, event):
        self.camera.start()

    def closeEvent(self, event):
        self.camera.stop()
