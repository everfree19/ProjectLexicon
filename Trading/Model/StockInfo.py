from Model.ConclusionInfo import *

#종목 정보
class StockInfo:
    m_nConclusionInfo = ConclusionInfo()

    def __init__(self, code, name,  price, fluctuation, leapRate):
        self._code = code   #종목 코드
        self._name = name   #종목명
        self._price = price #현재가
        self._fluctuation = fluctuation   #등락률
        self._leapRate = leapRate         #급증률
