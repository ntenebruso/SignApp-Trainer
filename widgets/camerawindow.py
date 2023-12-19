import os

from PyQt5.QtMultimedia import QCameraInfo, QCamera, QCameraImageCapture
from PyQt5.QtWidgets import QWidget

from lib.util import bundle_dir, train_config
from ui.camerawindow import Ui_CameraWindow

data_dir = os.path.join(bundle_dir, train_config.get("data_dir"))


class CameraWindow(QWidget):
    def __init__(self):
        super(CameraWindow, self).__init__()

        self.ui = Ui_CameraWindow()
        self.ui.setupUi(self)

        self.available_cameras: list[QCameraInfo] = None
        self.camera: QCamera = None

        self.get_available_cameras()
        self.select_camera(0)

        self.capture = QCameraImageCapture(self.camera)
        self.capture.setCaptureDestination(QCameraImageCapture.CaptureToFile)

        self.ui.cameraInput.currentIndexChanged.connect(self.select_camera)
        self.ui.captureBtn.clicked.connect(self.capture_image)

    def get_available_cameras(self):
        self.available_cameras = QCameraInfo.availableCameras()
        for i in self.available_cameras:
            self.ui.cameraInput.addItem(i.description())

    def select_camera(self, index):
        self.camera = QCamera(self.available_cameras[index])
        self.camera.setViewfinder(self.ui.cameraOutput)
        self.camera.start()

    def capture_image(self):
        if self.capture.isReadyForCapture():
            self.capture.capture(os.path.join(data_dir, self.ui.objectInput.text()))
            self.ui.statusLabel.setText("Successfully saved image")
        else:
            self.ui.statusLabel.setText("Error")

    def showEvent(self, event):
        self.camera.start()

    def closeEvent(self, event):
        self.camera.stop()
