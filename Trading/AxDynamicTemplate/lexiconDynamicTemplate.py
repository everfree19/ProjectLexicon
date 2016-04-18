
from Presenter.IPresenter import *
#dynamic call tempate method
# 급등락 정보 api
def extractTrData_RapidVolumnListData ( lexiconWindow , StockDao, TrCode, RQName) :
        VolumnList_list = []
        for i in range(0, 10):
            code = lexiconWindow.lexiconAxCtrl.dynamicCall("CommGetData(QString, QString, QString, int, QString)", TrCode, "", RQName, i, "종목코드")
            name = lexiconWindow.lexiconAxCtrl.dynamicCall("CommGetData(QString, QString, QString, int, QString)", TrCode, "", RQName, i, "종목명")
            price = lexiconWindow.lexiconAxCtrl.dynamicCall("CommGetData(QString, QString, QString, int, QString)", TrCode, "", RQName, i, "현재가")
            thanYesterday = lexiconWindow.lexiconAxCtrl.dynamicCall("CommGetData(QString, QString, QString, int, QString)", TrCode, "", RQName, i, "전일대비")
            fluctuation = lexiconWindow.lexiconAxCtrl.dynamicCall("CommGetData(QString, QString, QString, int, QString)", TrCode, "", RQName, i, "등락률")
            prevVolumn = lexiconWindow.lexiconAxCtrl.dynamicCall("CommGetData(QString, QString, QString, int, QString)", TrCode, "", RQName, i, "이전거래량")
            curVolumn = lexiconWindow.lexiconAxCtrl.dynamicCall("CommGetData(QString, QString, QString, int, QString)", TrCode, "", RQName, i, "현재거래량")
            leapQuantity = lexiconWindow.lexiconAxCtrl.dynamicCall("CommGetData(QString, QString, QString, int, QString)", TrCode, "", RQName, i, "급증량")
            leapRate = lexiconWindow.lexiconAxCtrl.dynamicCall("CommGetData(QString, QString, QString, int, QString)", TrCode, "", RQName, i, "급증률")
            #update model list
            StockDao.addStockItem(code.strip(), name.strip(), price.strip(), fluctuation.strip(), leapRate.strip())
            VolumnList_list.append("종목코드 : " + code.strip() + "\n" +
                                   "종목명 : "+ name.strip() + "\n" +
                                   "현재가 : " + price.strip() + "\n" +
                                   "전일대비 : " + thanYesterday.strip() + "\n" +
                                   "등락률 : " + fluctuation.strip() + "\n" +
                                    "이전거래량 : " + prevVolumn.strip() + "\n" +
                                   "현재거래량 : " + curVolumn.strip() + "\n" +
                                   "급증량 : " + leapQuantity.strip() + "\n" +
                                   "급증률 : " + leapRate.strip() + "\n"
                                   )

        lexiconWindow.rtvListCtrl.addItems(VolumnList_list)



def extractTrData_ConclusionInfo ( lexiconWindow , StockDao, TrCode, RQName) :
        conclusion_list = []
        for i in range(0, 10): # 수치 동적 변경 필요
            time = lexiconWindow.lexiconAxCtrl.dynamicCall("CommGetData(QString, QString, QString, int, QString)", TrCode, "", RQName, i, "시간")
            price = lexiconWindow.lexiconAxCtrl.dynamicCall("CommGetData(QString, QString, QString, int, QString)", TrCode, "", RQName, i, "현재가")
            conclVol = lexiconWindow.lexiconAxCtrl.dynamicCall("CommGetData(QString, QString, QString, int, QString)", TrCode, "", RQName, i, "체결거래량")
            accumVol  = lexiconWindow.lexiconAxCtrl.dynamicCall("CommGetData(QString, QString, QString, int, QString)", TrCode, "", RQName, i, "누적거래량")
            conclusionStrength = lexiconWindow.lexiconAxCtrl.dynamicCall("CommGetData(QString, QString, QString, int, QString)", TrCode, "", RQName, i, "체결강도")

            lexiconWindow.conclusionInfoTextCtrl.append("시간 : " + time.strip())
            lexiconWindow.conclusionInfoTextCtrl.append("현재가 : "+ price.strip() )
            lexiconWindow.conclusionInfoTextCtrl.append("체결거래량 : " + conclVol.strip())
            lexiconWindow.conclusionInfoTextCtrl.append("누적거래량 : " + accumVol.strip())
            lexiconWindow.conclusionInfoTextCtrl.append("체결강도 : " + conclusionStrength.strip()  + "\n" )
            #conclusion_list.append("시간 : " + time.strip() + "\n" +
            #                   "현재가 : "+ price.strip() + "\n" +
            #                   "체결거래량 : " + conclVol.strip() + "\n" +
            #                    "누적거래량 : " + accumVol.strip() + "\n" +
            #                   "체결강도 : " + conclusionStrength.strip() + "\n"
            #                   )

#체결정보 extract



