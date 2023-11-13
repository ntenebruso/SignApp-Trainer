from contextlib import redirect_stdout, redirect_stderr
from threading import Thread

from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QWidget

from ui.trainwindow import Ui_TrainWindow


class WriteProcessor(QObject):
    data_ready = pyqtSignal(str, name="dataReady")

    def __init__(self):
        super(WriteProcessor, self).__init__()
        self.buf = ""

    def write(self, buf):
        while buf:
            try:
                newline_index = self.buf.index("\n")
            except ValueError:
                self.buf += buf
                break

            data = self.buf + buf[:newline_index + 1]
            self.buf = ""
            buf = buf[newline_index + 1:]
            self.data_ready.emit(data)

    def flush(self):
        pass


class TrainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TrainWindow()
        self.ui.setupUi(self)

        self.ui.closeBtn.clicked.connect(self.close)
        self.ui.trainBtn.clicked.connect(self.run_thread)

        self.write_processor = WriteProcessor()
        self.write_processor.data_ready.connect(self.data_ready)

    def run_thread(self):
        t = Thread(target=self.run_train)
        t.start()
        self.ui.trainBtn.setEnabled(False)

    def run_train(self):
        from lib.train import main as train
        with redirect_stdout(self.write_processor), redirect_stderr(self.write_processor):
            train()
            self.ui.trainBtn.setEnabled(True)

    def data_ready(self, data):
        cursor = self.ui.trainOutput.textCursor()
        cursor.movePosition(cursor.End)
        cursor.insertText(data)
        self.ui.trainOutput.ensureCursorVisible()
