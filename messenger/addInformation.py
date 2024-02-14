from PyQt5.QtWidgets import QWidget
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import Qt


class AdditionalInformation(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("templates/addInformation.ui", self)
        self.setWindowTitle("Информация")
        self.setWindowModality(2)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)        
        self.center()
        icon1 = QtGui.QIcon()
        icon2 = QtGui.QIcon()
        self.pushButton_7.move(345, 5)
        self.pushButton_8.move(315, 5)
        icon1.addPixmap(QtGui.QPixmap(r"button_Icon\x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(r"button_Icon\-.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon1)
        self.pushButton_8.setIcon(icon2)
        self.pushButton_7.clicked.connect(lambda: self.close())
        self.pushButton_8.clicked.connect(lambda: self.showMinimized())        
        
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
