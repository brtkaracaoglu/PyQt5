import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Font, Color, File Dialog")
        self.setGeometry(650,150,600,600)
        self.UI()

    def UI(self):
        verticalBox = QVBoxLayout()
        horizontolBox = QHBoxLayout()
        self.editor = QTextEdit()
        fontButon = QPushButton("Font Değiştir")
        fontButon.clicked.connect(self.fontDegistir)
        colorButon = QPushButton("Color Değiştir")
        colorButon.clicked.connect(self.colorDegistir)
        fileButon = QPushButton("File  Değiştir")
        fileButon.clicked.connect(self.fileOpen)
        horizontolBox.addStretch()
        horizontolBox.addWidget(fontButon)
        horizontolBox.addWidget(colorButon)
        horizontolBox.addWidget(fileButon)
        horizontolBox.addStretch()
        verticalBox.addWidget(self.editor)
        verticalBox.addLayout(horizontolBox)
        self.setLayout(verticalBox)

        self .show()

    def fontDegistir(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.editor.setCurrentFont(font)

    def colorDegistir(self):
        color = QColorDialog.getColor()
        self.editor.setTextColor(color)

    def fileOpen(self):
        url = QFileDialog.getOpenFileName(self, "Dosya Aç", "", "All Files(* );;*txt *py")
        print(url)
        file = open(url[0],"r")
        content = file.read()
        self.editor.setText(content)

def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()