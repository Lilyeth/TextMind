
import sys,os
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets

import SearchFunction as sf
import layout

class Window(layout.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        # self.m_ui = layout.Ui_Dialog()
        self.setupUi(self)


        # self.pushButton.clicked.connect(self.searchText)
        self.SearchBar.textChanged.connect(self.searchText)
        self.ResultsBox.itemSelectionChanged.connect(self.searchResults)



    def change_name(self):
        if self.pushButton.text() == 'PushMe':
            self.pushButton.setText("Auts")
        else:
            self.pushButton.setText("PushMe")

    def searchText(self):
        result = sf.searchFunc(self.SearchBar.text())
        self.ResultsBox.clear()
        self.ResultsBox.addItems(result)

    def searchResults(self):
        name = self.ResultsBox.selectedItems()[0].text()
        fileName = name.replace(' ','%20')
        #fileName = name
        # print('file://%s/Processed/%s.html'%(os.getcwd(),fileName))
        self.DocView.setSource(QtCore.QUrl('file://%s/Processed/%s.html'%(os.getcwd(),fileName)))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Window()
    ex.setGeometry(100,100,900,600)
    ex.show()
    sys.exit(app.exec_())
