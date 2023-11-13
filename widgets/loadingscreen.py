from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QWidget, QLabel


class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(200, 200)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)

        self.setStyleSheet("background-color: white;")

        self.label_animation = QLabel(self)
        self.movie = QMovie("assets/loading.gif")
        self.label_animation.setMovie(self.movie)
        self.movie.start()
