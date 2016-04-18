
from AxDynamicTemplate.lexiconDynamicTemplate import *
from Presenter.IPresenter import *


class lexiconDynamicCallback:
    def __init__(self):
        pass

    def interfaceBinding (self, window, dao ) :
        self.mainFrame = window
        self._dao = dao


    def OnReceiveMsg(self, sScrNo, sRQName, sTrCode, sMsg):
        if sRQName == "Order":
            self.mainFrame.orderInfoWidget.contractInfoView.setText(sMsg)
        else :
            print ("On Receive Msg \n ")
            print ( "Screen No : " + sScrNo + "\n")
            print ( "RQName: " + sRQName + "\n")
            print ( "TrCode : " + sTrCode + "\n")
            print ( "Msg : " + sMsg + "\n")

    def OnReceiveTrData(self,  ScrNo, RQName, TrCode, RecordName, PrevNext, DataLength, ErrorCode, Message, SplmMsg):
        if RQName == "RequestRapidVolumnList":
            extractTrData_RapidVolumnListData (self.mainFrame, self._dao, TrCode, RQName)
        elif RQName == "ConclusionInfo":
            extractTrData_ConclusionInfo ( self.mainFrame, self._dao, TrCode, RQName)


    def OnReceiveRealData(self,  stockItemCode, realType, realData):  # 종목 코드, 실시간 타입, 실시간 데이터 전문
        print( "Hello Real Data ")
        if realType == "RD_StockMarketPrice":
            print( stockItemCode + "," + realType + "," + realData)

    def OnReceiveChejanData(self, sGubun, nItemCnt, sFidList):
        print ("= OnReceiveChejanData = \n")
        #self.lineEdit_6.setText(self.GetChjanData(9203))
        #self.textEdit.append("주문번호: "+self.GetChjanData(9203))
        #self.textEdit.append("종 목 명: "+self.GetChjanData(302))
        #self.textEdit.append("주문수량: "+self.GetChjanData(900))
        #self.textEdit.append("주문가격: "+self.GetChjanData(901))
