import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TableWindget")
        self.setGeometry(50,50,400,400)
        self.UI()
# dizany elemanlarını yan yan kullanılması için horizontol alt alt ise vertical
    def UI(self):
        self.table = QTableWidget(self)
        self.table.setRowCount(5)
        self.table.setColumnCount(5)
        self.table.resize(380,380)
        self.table.setHorizontalHeaderItem(0,QTableWidgetItem("İsim"))
        #self.table.verticalHeader().hide()
        self.table.setItem(0,0,QTableWidgetItem("birinci"))
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.doubleClicked.connect(self.getItem)
        self.show()
    def getItem(self):
        for item in self.table.selectedItems():
            print(item.text(),item.row(),item.column())
def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()