import sys
from PyQt5.QtWidgets import *  # * işareti kütüphanenin hepsini import etmeyi sağlar

# Window sınıfı, QWidget sınıfından kalıtım alarak oluşturuluyor.
class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(50, 50, 800, 500)  # Pencerenin konumunu belirtir: (x, y, genişlik, yükseklik)
        self.setWindowTitle("PyQt Dersleri Pencere Oluşturma")  # Pencerenin başlığını belirtir

        self.show()  # Oluşturulan pencerenin gösterilmesi için kullanılır


app = QApplication(sys.argv)  # PyQt uygulaması oluşturuluyor
window = Window()  # Window sınıfından bir pencere örneği oluşturuluyor
sys.exit(app.exec_())  # Uygulama döngüsünü başlatıyor ve çıkış yapana kadar çalışmasını sağlıyor
