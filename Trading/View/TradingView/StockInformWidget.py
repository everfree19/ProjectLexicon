from PyQt4.QtCore import *
from PyQt4.QtGui import *

from AxDynamicTemplate.lexiconDynamicTemplate import *
from Presenter.IPresenter import *


class stockInformWidget:
    def __init__(self, lexiconWindow ):
        #코스피 정보 위젯
        btn_kospi = QPushButton("KOSPI", lexiconWindow)
        btn_kospi.move(10, 80)
        btn_kospi.clicked.connect(self.btn_clicked_getCodeList_kospi)
        self.lexiconAxCtrl = lexiconWindow.lexiconAxCtrl
        self.kospiListCtrl = lexiconWindow.KospiListWidgetCtrl
        self.kospiListCtrl.setGeometry(10, 110, 200, 300)
        # 코스닥 정보 위젯
        btn_kosdaq = QPushButton("KOSDAQ", lexiconWindow)
        btn_kosdaq.move(10, 420)
        btn_kosdaq.clicked.connect(self.btn_clicked_getCodeList_kosdaq)
        self.kosdaqListCtrl = lexiconWindow.KosdaqListWidgetCtrl
        self.kosdaqListCtrl.setGeometry(10, 450, 200, 300)

        # 거래량 급증
        btn_RapidTradingVolumn = QPushButton("거래량 급증", lexiconWindow)
        btn_RapidTradingVolumn.move(220, 80)
        btn_RapidTradingVolumn.clicked.connect(self.btn_clicked_getCodeList_RapidTradingVolumn)  # 거래량 급증 이벤트핸들러
        self.rtvListCtrl = lexiconWindow.RapidHighTradingVolumeListWidgetCtrl
        self.rtvListCtrl.setGeometry(220, 110, 200, 300)
        self.rtvListCtrl.currentRowChanged.connect(self.onRTVCurrentRowChanged)

        #체결정보 요청
        label = QLabel('체결 정보 ', lexiconWindow)
        label.move(450, 80)
        self.conclusionInfoTextCtrl = QTextEdit(lexiconWindow)
        self.conclusionInfoTextCtrl.setGeometry(450, 110, 200, 300)
        self.conclusionInfoTextCtrl.setEnabled(True)

        #이벤트 리스너 등록
        self.registerLexiconEventListener()



    def registerLexiconEventListener(self) :
        lexiconMainpresenter.axDynamicCallback.interfaceBinding (self, lexiconMainpresenter.StockInformDao)
        self.lexiconAxCtrl.connect(
            self.lexiconAxCtrl, SIGNAL("OnReceiveTrData(QString, QString, QString, QString, QString, int, QString, QString, QString)"),
            lexiconMainpresenter.axDynamicCallback.OnReceiveTrData)

    def btn_clicked_getCodeList_kospi(self):
        if self.lexiconAxCtrl is not None:
            ret = self.lexiconAxCtrl.dynamicCall("GetCodeListByMarket(QString)", ["0"])
            if len(ret) != 0:
                kospi_code_list = ret.split(';')
                kospi_code_name_list = []

                for x in kospi_code_list:
                    name = self.lexiconAxCtrl.dynamicCall("GetMasterCodeName(QString)", [x])
                    kospi_code_name_list.append(x + " : " + name)

                self.kospiListCtrl.addItems(kospi_code_name_list)


    def btn_clicked_getCodeList_kosdaq(self):
        if self.lexiconAxCtrl is not None:
            ret = self.lexiconAxCtrl.dynamicCall("GetCodeListByMarket(QString)", ["10"])
            if len(ret) != 0:
                kosdaq_code_list = ret.split(';')
                kosdaq_code_name_list = []

                for x in kosdaq_code_list:
                    name = self.lexiconAxCtrl.dynamicCall("GetMasterCodeName(QString)", [x])
                    kosdaq_code_name_list.append(x + " : " + name)

                self.kosdaqListCtrl.addItems(kosdaq_code_name_list)

    def btn_clicked_getCodeList_RapidTradingVolumn(self):
        #self.kiwoom.dynamicCall("CommRqData(QString, QString, int, QString)", "Request1", "opt10001", 0, "0101")
        self.lexiconAxCtrl.dynamicCall("SetInputValue(QString,QString)", "시장구분","101") #코스닥
        self.lexiconAxCtrl.dynamicCall("SetInputValue(QString,QString)", "정렬구분","2")   #급증률
        self.lexiconAxCtrl.dynamicCall("SetInputValue(QString,QString)", "시간구분","2")   #전일
        self.lexiconAxCtrl.dynamicCall("SetInputValue(QString,QString)", "거래량구분","1000") #거래량 구분 100만주 이상
        self.lexiconAxCtrl.dynamicCall("SetInputValue(QString,QString)", "시간","1")         #시간
        self.lexiconAxCtrl.dynamicCall("SetInputValue(QString,QString)", "종목조건","0")      # 증 100만 보기
        self.lexiconAxCtrl.dynamicCall("SetInputValue(QString,QString)", "가격구분","0")      #가격 전체조회
        self.lexiconAxCtrl.dynamicCall("CommRqData(QString, QString, int, QString)", "RequestRapidVolumnList", "OPT10023", 0, "0101") # 0101 은 화면 번혼데 뭔지 모르겠네



    def onRTVCurrentRowChanged ( self, nRow ) :
        self.conclusionInfoTextCtrl.clear()
        stockItem = lexiconMainpresenter.StockInformDao.getStockItem(nRow)
        self.lexiconAxCtrl.dynamicCall("SetInputValue(QString,QString)", "종목코드",stockItem._code)
        self.lexiconAxCtrl.dynamicCall("CommRqData(QString, QString, int, QString)", "ConclusionInfo", "OPT10003", 0, "0101")
