from PyQt4.QAxContainer import *
from PyQt4.QtGui import *

from View import TimerWidget, AuthenticateModule
from View.TradingView import StockInformWidget
from View.TradingView import StockItemWidget


class LexiconMainFrame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.staticInit()

    def staticInit(self):
        self.setWindowTitle("LexiconMainFrame")
        self.setGeometry(100, 100, 1280, 800)
        self.loginCtrl = QTextEdit(self)
        self.KospiListWidgetCtrl = QListWidget(self)
        self.KosdaqListWidgetCtrl = QListWidget(self)
        self.RapidHighTradingVolumeListWidgetCtrl = QListWidget(self)  # 거래량 급증 ctrl

        #Timer Control
        self.timerTextCtrl = QTextEdit(self)
        self.timerTextCtrl.setGeometry(200, 10, 150, 50)
        self.timerTextCtrl.setEnabled(False)
        self.bindingViews()

    def bindingViews(self):
        #bind system regist
        self.lexiconAxCtrl = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")

        #register Timer
        self.stockTimer = TimerWidget.stockTimer(self)
        self.stockTimer.TimerSignal.connect(self.timerTextCtrl.setText)
        self.stockTimer.startTimer()
        self.bindingTradingView()

        #login control
        self.authenticateWidget = AuthenticateModule.authenticateWidget(self.loginCtrl)
        self.authenticateWidget.authenticate(self.lexiconAxCtrl)


    def bindingTradingView(self):
         #stockinformation control
        self.stockInformSerivice = StockInformWidget.stockInformWidget(self)
        self.stockItemWidget = StockItemWidget.StockItemWidget(self)
