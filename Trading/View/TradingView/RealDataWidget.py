from PyQt4.QtCore import *
from PyQt4.QtGui import *

from AxDynamicTemplate.lexiconDynamicTemplate import *
from Presenter.IPresenter import *
from TradingUtil import RealDataRequestTimer
#base X : 450
#base Y : 80

class realDataWidget:
    def __init__(self, lexiconWindow ):
        #실시간 데이터 위젯
        label = QLabel('실시간 데이터', lexiconWindow)
        label.move(450, 80)
        self.lexiconWindow = lexiconWindow
        self.realDataListWidget = QListWidget(lexiconWindow)
        self.realDataListWidget.setGeometry(450, 110, 800, 300)


        btn_RealDataStart = QPushButton("수집 시작", lexiconWindow) #실시간 데이터 수집 시작
        btn_RealDataStart.move(550, 80)
        btn_RealDataStart.clicked.connect(self.startRealDataCollect)
        self.startButton = btn_RealDataStart
        self.m_bRunning = False

    def registerLexiconEventListener(self) :
        lexiconMainpresenter.axDynamicCallback.interfaceBinding (self.lexiconWindow, lexiconMainpresenter.StockInformDao)
        #실시간데이터 이벤트핸들러 등록
        # self.lexiconAxCtrl.connect(
        #    self.lexiconAxCtrl, SIGNAL("OnReceiveRealData(QString, QString, QString)"),
        #   lexiconMainpresenter.axDynamicCallback.OnReceiveRealData)
        self.lexiconAxCtrl.connect(
            self.lexiconAxCtrl, SIGNAL("OnReceiveRealData(QString, QString, QString)"),
           self.OnReceiveRealData)

    def startRealDataCollect(self):
        if self.m_bRunning == False :  # 수집 시작 버튼눌렀을 때
            self.startButton.setText("수집 중지")
            self.m_bRunning  = True
            self.runRealDataRequest()
        elif self.m_bRunning == True  : # 수집 중지 버튼눌렀을 때
            self.startButton.setText("수집 시작")
            self.m_bRunning = False
            self.stopRealDataRequest()


    def runRealDataRequest(self):
        self.lexiconAxCtrl.dynamicCall("SetRealReg(QString, QString, QString, QString )", "0101","090150", "10", "0" ) #화면 번호 , 종목 코드, Fid list, opt
        self.lexiconAxCtrl.dynamicCall("CommRqData(QString, QString, int, QString)", "RD_StockMarketPrice", "현재가", 0, "0101") # 0101 은 화면 번혼데 뭔지 모르겠네

        #self.RequestTimer = RealDataRequestTimer.realDataRequestTimer(self)
        #self.RequestTimer.Signal.connect(self.realDataListWidget.addItem)
        #self.RequestTimer.startTimer()



    def stopRealDataRequest(self):
        pass
        #self.RequestTimer.stopTimer()

    def OnReceiveRealData(self,  stockItemCode, realType, realData):  # 종목 코드, 실시간 타입, 실시간 데이터 전문
        print( "Hello Real Data ")
        if realType == "RD_StockMarketPrice":
            print( stockItemCode + "," + realType + "," + realData)