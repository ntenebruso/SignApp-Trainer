import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QSplashScreen, QStyleFactory

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("fusion"))

    loading_screen = QSplashScreen(QPixmap("assets/loading.gif"))
    loading_screen.show()

    from widgets.mainwindow import MainWindow

    loading_screen.close()
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
