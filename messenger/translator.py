from PyQt5.QtWidgets import QWidget
from PyQt5 import uic, QtWidgets, QtGui, QtCore
from googletrans import Translator
import googletrans


class TranslatorWindows(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("templates/translateWindows.ui", self)
        self.setWindowTitle("Переводчик")
        self.setWindowModality(2)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)        
        self.center()
        self.listOfLang = list(googletrans.LANGUAGES.values())
        for i in self.listOfLang:
            self.comboBox.addItem(i)
            self.comboBox_2.addItem(i)
            
        icon1 = QtGui.QIcon()
        icon2 = QtGui.QIcon()
        self.pushButton_13.move(345, 5)
        self.pushButton_14.move(315, 5)
        icon1.addPixmap(QtGui.QPixmap(r"button_Icon\x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(r"button_Icon\-.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_13.setIcon(icon1)
        self.pushButton_14.setIcon(icon2)
        self.pushButton_13.clicked.connect(lambda: self.close())
        self.pushButton_14.clicked.connect(lambda: self.showMinimized())
        self.pushButton.clicked.connect(self.translate)

    def get_key(self, d, value):
        for k, v in d.items():
            if v == value:
                return k    
    
    def translate(self):
        trl = self.comboBox.currentText()
        trrl = self.comboBox_2.currentText()
        trt = str(self.lineEdit.text())
        translator = Translator()
        lenguageForTr = googletrans.LANGUAGES.get(self.get_key(googletrans.LANGUAGES, trrl))
        translation = translator.translate(trt, dest=lenguageForTr)
        self.lineEdit_2.setText(translation.text) 
        
    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
            
    def mouseMoveEvent(self, event):
        try:
            delta = QtCore.QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
        except AttributeError:
            pass
            
    def mousePressEvent(self, event):
            self.oldPos = event.globalPos()        
