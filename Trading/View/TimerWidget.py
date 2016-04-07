import time
import datetime
from PyQt4 import QtCore

class stockTimer(QtCore.QThread):
    TimerSignal = QtCore.pyqtSignal([str])
    def __init__(self, lexiconWnd):
        super(stockTimer, self).__init__()
        self.delay = 1
        self.state = True
        self.handler = None

    def setDelay(self, delay):
        self.delay = delay

    def run(self):
        while self.state:
            time.sleep( self.delay )
            if self.handler is not None:
                self.handler()
    def end(self):
        self.state = False

    def setHandler(self, handler):
        self.handler = handler

    def onTimer(self):
        now = datetime.datetime.now()
        strdate = now.strftime("%Y-%m-%d")
        strtime = now.strftime(" [%H:%M:%S]")
        self.TimerSignal.emit(strdate+strtime)

    def startTimer(self):
        self.setHandler(self.onTimer)
        self.setDelay(1)
        self.start()

