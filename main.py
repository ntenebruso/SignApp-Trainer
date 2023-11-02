import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QSplashScreen
from PyQt5.QtGui import QPixmap

if __name__ == "__main__":
  app = QApplication(sys.argv)
  loading_screen = QSplashScreen(QPixmap("assets/loading.gif"))
  loading_screen.show()

  from widgets.mainwindow import MainWindow

  loading_screen.close()
  window = MainWindow()
  window.show()

  sys.exit(app.exec_())

