import time
import datetime
from PyQt4 import QtCore

class realDataRequestTimer(QtCore.QThread):
    Signal = QtCore.pyqtSignal([str])
    def __init__(self, realDataWidget):
        super(realDataRequestTimer, self).__init__()
        self.delay = 1
        self.state = True
        self.handler = None
        self.realDataWidget = realDataWidget

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
        pass
        #self.realDataWidget.lexiconAxCtrl.dynamicCall("SetRealReg(QString, QString, QString, QString)", sScreenNo, sCode, '9001;10', sRealType)
        #ret = self.realDataWidget.lexiconAxCtrl.dynamicCall("CommRqData(QString, QString, int, QString)", "RD_StockMarketPrice", "주식시세", 0, "0101") # 0101 은 화면 번혼데 뭔지 모르겠네
        #print ( "error : " , ret )
        #Request to Server
        #self.Signal.emit(test_list[0])


    def startTimer(self):
        self.setHandler(self.onTimer)
        self.setDelay(1)
        self.start()

    def stopTimer(self):
        self.end()