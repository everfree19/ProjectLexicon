from Model.StockInfo import *


class StockInformDao:

    StockInfoList = []
    def __init__(self):
        pass

    def addStockItem(self, code, name,  price, fluctuation, leapRate):
        newItem = StockInfo (code, name,  price, fluctuation, leapRate)
        self.StockInfoList.append(newItem)

    def getStockItem (self, index) :
        if len ( self.StockInfoList ) is not 0 :
            return self.StockInfoList[index]