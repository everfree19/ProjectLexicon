from PyQt4.QtGui import *

class StockItemWidget:
     def __init__(self, lexiconWindow ):
        self.clientLeftBase = 220
        self.clientTopBase = 50
        self.clientRightBase = 70
        self.defaultCode = "041020"   # infraware item code
        self.lexiconMainFrame = lexiconWindow

       # itemLabel = QLabel('종목코드: ', self.lexiconMainFrame )
       # itemLabel.move(self.clientLeftBase + 10, self.clientTopBase + 10)

