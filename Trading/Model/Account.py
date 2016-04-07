

class Account:
    def __init__(self):
        pass

    def setAccount ( self,  accountNumber ) :
        self.accountNumber = accountNumber
        print (self.getAccount())

    def getAccount (self) :
        return self.accountNumber
