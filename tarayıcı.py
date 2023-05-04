from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys
import PyQt5
class AnaEkran (QMainWindow):
    def __init__(self):
        super (AnaEkran, self).__init__()

        #Tarayıcının iskeleti
        self.tarayıcı = QWebEngineView()
        google='www.google.com'
        qurl=QUrl(google)
        self.tarayıcı.setUrl(qurl)

        self.setCentralWidget(self.tarayıcı)
        self.showMaximized()

        #Navigasyon tuşları-İleri,Geri,Yenile,Ana Sayfa
        navbar = QToolBar()
        self.addToolBar (navbar)

        #Geri Buton
        geriButon = QAction('Geri', self)
        geriButon.triggered.connect(self.tarayıcı.back)
        navbar.addAction(geriButon)

        #İleri Buton
        ileriButon = QAction('İleri', self)
        ileriButon.triggered.connect(self.tarayıcı.forward)
        navbar.addAction(ileriButon)

        #Yenile Buton
        yenileButon = QAction('Yenile', self)
        yenileButon.triggered.connect(self.tarayıcı.reload)
        navbar.addAction(yenileButon)

        #Ana Sayfa Buton
        anaSayfaButon = QAction('Ana Sayfa', self)
        anaSayfaButon.triggered.connect(self.AnaEkranaGit)
        navbar.addAction(anaSayfaButon)

        #Arama Çubuğu
        self.aramaCubugu = QLineEdit()
        self.aramaCubugu.returnPressed.connect(self.LinkeGit)
        navbar.addWidget(self.aramaCubugu)
        self.tarayıcı.urlChanged.connect(self.LinkiAra)

    def AnaEkranaGit (self):
        google='http://google.com'
        self.tarayıcı.setUrl(QUrl(google))
    def LinkeGit(self):
        url = self.aramaCubugu.text()
        self.tarayıcı.setUrl(QUrl(url))
    def LinkiAra(self, link):
        self.aramaCubugu.setText(link.toString())



#    *  Yeni özellikler bu kısımda kazandırılacak-Fonksiyonlar
#    *  __init__ metodu içine butonlar eklenip fonksiyonlar çağrılmalıdır
#    !! Geliştirmek isteyenler için yapılacak listesi:
#           * Ayarlar Menusu(Geçmiş-Ana Ekranı Değiştirme-Yeni Sekme-Yer İşaretleri)
#           * Sayfaları, sekmelere ayırma


Tarayıcı=QApplication(sys.argv)
QApplication.setApplicationName("Dünyanın En Kötü Web Tarayıcısı")
ekran=AnaEkran()
Tarayıcı.exec_()
# pip3 install pyqt5-tools

