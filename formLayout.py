import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Layout")
        self.setGeometry(650,150,600,600)
        self.UI()

    def UI(self):
        form = QFormLayout()
        form.setRowWrapPolicy(QFormLayout.WrapAllRows)
        name_text = QLabel("İsminiz :")
        name_input = QLineEdit()
        pass_text = QLabel("Şifreniz :")
        pass_input = QLineEdit()
        form.addRow(name_text,name_input)
        form.addRow(pass_text,pass_input)
        form.addRow(QLabel("Şehir"),QComboBox())

        self.setLayout(form)
        self .show()




def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()