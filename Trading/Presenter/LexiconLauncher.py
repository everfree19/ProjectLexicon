import sys

from View.MainWindow.LexiconMainFrame import *
import LexiconPresenter

# run mainFrame
if __name__ == "__main__":

    app = QApplication(sys.argv)
    lexiconMainView = LexiconMainFrame()
    exiconMainpresenter = LexiconPresenter.lexiconPresenter()
    lexiconMainView.show()
    app.exec_()


