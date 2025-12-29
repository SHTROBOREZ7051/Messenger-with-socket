from PyQt5 import QtCore, QtMultimedia
#from googletrans import Translator
#import googletrans
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QWidget, QInputDialog
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import PyQt5.QtCore
import sys
import socket
from cryptography.fernet import Fernet
import time
import pickle
import io
import json
import re
import os
import io

from encryption import encrypt_messageRSA, decrypt_messageAES, generate_key_and_iv


def encrypt_all_block_RSA(data):
    encrypted_data = []
    
    for block in data:
        encrypted_data.append(encrypt_messageRSA(block))
        
    return encrypted_data

def decrypt_all_block_AES(data, key, iv):
    encrypted_data = []
    
    for block in data:
        encrypted_data.append(decrypt_messageAES(block, key, iv))
        
    return encrypted_data    


def encode_all_element(*elements):
    elements = list(elements)
    for index in range(len(elements)):
        elements[index] = elements[index].encode()
        
    return elements


class AdditionalInformation(QWidget):
    def __init__(self):
        super().__init__()
        f_additionalInformation = open(r"templates\additionalInformation.ui", "r", encoding="utf-8")
        f = io.StringIO(f_additionalInformation.read())
        uic.loadUi(f, self)
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


class SetWindows(QWidget):
    def __init__(self, parent=None, signal=None):
        self.nickName = None
        self.port = None
        self.ip = None
        self.signal = signal
        super().__init__()
        #set_windows.ui
        f_set_windows = open(r"templates\set_windows.ui", "r", encoding="utf-8")
        f = io.StringIO(f_set_windows.read())
                
        uic.loadUi(f, self)
        self.setWindowTitle("Настройки")
        self.setWindowModality(2)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.center()
        self.pushButtonConfirm.clicked.connect(self.confirm)
        self.pushButtonCancel.clicked.connect(lambda: self.close())
        if os.path.exists(os.path.join("Information", "aboutUser.json")):
            with open(os.path.join("Information", "aboutUser.json")) as f:
                information = json.load(f)
                self.lineEdit.setText(information["nickName"])
                self.lineEdit_2.setText(information["ip"])
                self.lineEdit_3.setText(information["port"])        
    
    def center(self):
            qr = self.frameGeometry()
            cp = QtWidgets.QDesktopWidget().availableGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())
    
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()
    
    def mouseMoveEvent(self, event):
        try:
            delta = QtCore.QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
        except AttributeError:
            pass
        
    def confirm(self):
        self.nickName = self.lineEdit.text()
        self.ip = self.lineEdit_2.text()
        port = self.lineEdit_3.text()
        sampleIp = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
        
        self.lineEdit.setStyleSheet("border-radius: 7px; font: 12pt 'Sitka Small';")
        self.lineEdit_2.setStyleSheet("border-radius: 7px; font: 12pt 'Sitka Small';")
        self.lineEdit_3.setStyleSheet("border-radius: 7px; font: 12pt 'Sitka Small';")        
        
        if 4 <= len(self.nickName) < 15:
            if not re.match(sampleIp, self.ip) is None:
                if port.isdecimal() and int(port) <= 65535:
                    
                    if not os.path.exists(os.path.join("Information", "aboutUser.json")):
                    
                        with open(os.path.join("Information", "aboutUser.json"), "w") as f:
                            information = {"nickName": self.nickName, "ip": self.ip, "port": port}
                            json.dump(information, f, indent=6)
                    else:
                        with open(os.path.join("Information", "aboutUser.json"), "w") as f:
                            information = {"nickName": self.nickName, "ip": self.ip, "port": port}
                            json.dump(information, f, indent=6)
                            
                    self.close()
                    self.signal.emit(['Update configuration'])
                else:
                    self.lineEdit_3.setStyleSheet("border: 2px solid red; border-radius: 7px; font: 12pt 'Sitka Small';")
                    self.lineEdit_3.setText("Некорректный ввод PORT")
            else:
                self.lineEdit_2.setStyleSheet("border: 2px solid red; border-radius: 7px; font: 12pt 'Sitka Small';")
                self.lineEdit_2.setText("Некорректный ввод IP")
        else:
            self.lineEdit.setStyleSheet("border: 2px solid red; border-radius: 7px; font: 12pt 'Sitka Small';")
            self.lineEdit.setText("Слишком длинный либо слишком короткий ник")


class ThreadMonitor(QtCore.QThread):
    getSignal = QtCore.pyqtSignal(list)
    serverSocket = None
    
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.symetricKey = None
        self.IV = None
        self.public_key = None
                
    
    def set_value_AES(self, key, iv):
        self.symetricKey = key
        self.IV = iv
    
    def set_value_RSA(self, public_key):
        self.public_key = public_key
    
    def run(self):
        print(f"the server was started {self.serverSocket}")
        while True:
            print("while True")
            if self.serverSocket != None:
                print("if")
                print('ifffffffffff')
                message = self.serverSocket.recv(1024)
                
                print(message, "||||||||||||||||message")
                raw_message = pickle.loads(message)
                print(raw_message, "||||||||||||||||raw_message")
                                
                
                if raw_message[0] != "200_CONNECTION_ESTAB":
                    
                    decodeMessage = decrypt_all_block_AES(raw_message, self.symetricKey, self.IV)
                    
                    print(decodeMessage, "ThreadMonitor")
                    """
                    if decodeMessage[0] == "200_OK":
                    
                    self.symetricKey = decodeMessage[-1]
                    self.cipher = Fernet(self.symetricKey)
                    self.getSignal.emit(decodeMessage)
                    """ 
                    if decodeMessage[0] == "100_SEND_MESSAGE":
                        #decryptedMessage = self.cipher.decrypt(decodeMessage[-1]).decode()
                        #decryptedload = ["100_CONTINUE", decodeMessage[1], decryptedMessage]
                        print("??????????????????????????????????")
                        ###########################################################################################################
                        self.getSignal.emit(decodeMessage)
                
                    elif decodeMessage[0] == "100_TAKE_MESSAGE":
                        print(decodeMessage, "100_TAKE_MESSAGE")
                        self.getSignal.emit(decodeMessage)
                
                    elif decodeMessage[0] == "200_CORRECT_PASSWORD":
                        decryptedload = ["200_CORRECT_PASSWORD"]
                        self.getSignal.emit(decryptedload)
                
                    elif decodeMessage[0] == "200_JOIN_CHAT":
                        decryptedload = ["200_JOIN_CHAT"]
                        self.getSignal.emit(decryptedload)                    
                
                    elif decodeMessage[0] == "200_CHAT_BE_MAKED":
                        decryptedload = ["200_CHAT_BE_MAKED"]
                        self.getSignal.emit(decryptedload)                      
                
                    elif decodeMessage[0] == "400_WRONG_PASSWORD":
                        decryptedload = ["400_WRONG_PASSWORD"]
                        self.getSignal.emit(decryptedload)
                    
                    elif decodeMessage[0] == "403_WRONG_CONNECT_CHAT":
                        decryptedload = ["403_WRONG_CONNECT_CHAT", decodeMessage[1]]
                        self.getSignal.emit(decryptedload)  
                else:
                    pickLoad = ["200_CONNECTION_ESTAB", raw_message[1]]
                    print(pickLoad)
                    self.getSignal.emit(pickLoad)                              
                        
            time.sleep(2)
                        
    def send_encrypt(self, information):
        if information[0] == "100_SEND_MESSAGE":
            #encryptMessage = self.cipher.encrypt(information[-1])
            #pickLoad = ["100_CONTINUE", information[1], encryptMessage]
            encode_pickLoad = encrypt_all_block_RSA(information)
            self.serverSocket.send(pickle.dumps(encode_pickLoad))
            
        elif information[0] == "100_VALID_PASSWORD":
            #pickLoad = ["100_VALID_PASSWORD", information[1], information[2]] //
            print(information, "information")
            encode_pickLoad = encrypt_all_block_RSA(information)
            self.serverSocket.send(pickle.dumps(encode_pickLoad)) #["100_VALID_PASSWORD", self.nickName, self.sym_key, self.IV, self.server_password]
        
        elif information[0] == "100_MAKE_NEW_CHAT":
            #                                   name           password       usersList=[]
            pickLoad = ["100_MAKE_NEW_CHAT", information[1], information[2], information[3]]
            print("send_encrypt 100_MAKE_NEW_CHAT", pickLoad)
            encode_pickLoad = encrypt_all_block_RSA(pickLoad)
                        
            self.serverSocket.send(pickle.dumps(encode_pickLoad))            
            
            
        elif information[0] == "100_VALID_CHAT_INFORMATION":
            pickLoad = ["100_VALID_CHAT_INFORMATION", information[1], information[2], information[3]]
            
            encode_pickLoad = encrypt_all_block_RSA(pickLoad)
                        
            self.serverSocket.send(pickle.dumps(encode_pickLoad))            
                        
        elif information[0] == "EXIT":
            #encryptMessage = self.cipher.encrypt(information[-1])
            pickLoad = ["EXIT", *information[1:]]
            encode_pickLoad = encrypt_all_block_RSA(pickLoad)
                        
            self.serverSocket.send(pickle.dumps(encode_pickLoad))
                


class InputInterface(QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        f_input_template = open(r"templates\input_frame.ui", "r", encoding="utf-8")
        self.f = io.StringIO(f_input_template.read())
        
        self.initui()
        self.nickName = None
        self.ip = None
        self.port = None
        self.server_password = None
        self.AbilityToConnect = False
        self.public_key = None
        
        self.sym_key, self.IV = generate_key_and_iv()
        
        self.connectMonitor = ThreadMonitor()
        self.connectMonitor.getSignal.connect(self.signalHandler)
        self.signal = self.connectMonitor.getSignal
        
                
        if os.path.exists(os.path.join("Information", "aboutUser.json")):
            with open(os.path.join("Information", "aboutUser.json")) as f:
                information = json.load(f)
                self.name_line.setText(information["nickName"])
                self.ip_line.setText(information["ip"])
                self.port_line.setText(information["port"])        
            
        
        
    def initui(self):
        uic.loadUi(self.f, self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) 
        self.center()
        
        self.push_data.clicked.connect(self.confirm)
        self.setWindowTitle("Чат-мессенджер: Подключение к серверу")
    
    
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
        
      
    def join(self):
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((self.ip, self.port))
            self.connectMonitor.serverSocket = self.client
            self.connectMonitor.start()
            
        except Exception as error:
            message = "Проверьте соединение с сервером: 'Ошибка с соединением'"
            QtWidgets.QMessageBox.about(self, "Оповещение", message)            
            
        
    def updateConfigure(self):
        if os.path.exists(os.path.join("Information", "aboutUser.json")):
            with open(os.path.join("Information", "aboutUser.json")) as file:
                data = json.load(file)
                self.nickName = data['nickName']
                self.ip = data['ip']
                self.port = int(data['port'])    
        
    def signalHandler(self, value:list):
        print(value)
        if value[0] == 'Update configuration':
            print("UPD")
            self.updateConfigure()
            
        elif value[0] == "200_CONNECTION_ESTAB" and len(value) == 2:
            print("signalHandler don't work")
            
            self.public_key = value[1]
            #print("self.public_key ", self.public_key)
            self.connectMonitor.set_value_RSA(self.public_key)
            self.AbilityToConnect = True
            ####################################################################################################
            
            pickLoad = ["100_VALID_PASSWORD", self.nickName, self.server_password, "100_VALID_PASSWORD", self.sym_key, self.IV]
            print(pickLoad)
            self.connectMonitor.set_value_AES(self.sym_key, self.IV)
            self.connectMonitor.send_encrypt(pickLoad)            
            print("================================================")
            #self.AbilityToConnect = True
            #cellMessage = QtWidgets.QListWidgetItem()
            #cellMessage.setTextAlignment(QtCore.Qt.AlignHCenter)
            #cellMessage.setText(f"Server{value[1]}\n")
            #self.listWidget.addItem(cellMessage)
            #print(value)            
    
        elif value[0] == "200_CORRECT_PASSWORD":
            print(value)
            self.close()
            print([self.nickName, self.ip, self.port, self.server_password, self.connectMonitor])
            """
            self.public_key = None
            
            self.sym_key, self.IV = generate_key_and_iv()            
            """
            usr = UserInterface(self.nickName, self.ip, self.port, self.server_password, self.connectMonitor, self.client, self.public_key, self.sym_key, self.IV)##################################################
            usr.show()
    
        elif value[0] == "100_CONTINUE":
            print("signalHandler don't work1")
            #cellMessage = QtWidgets.QListWidgetItem()
            #cellMessage.setTextAlignment(QtCore.Qt.AlignRight)
            #cellMessage.setText(f"{value[1]}:\n {value[-1]}")
            #self.listWidget.addItem(cellMessage)
            print(value)
        
        elif value[0] == "400_WRONG_PASSWORD":
            self.server_password_line.setStyleSheet("border: 2px solid red; border-radius: 7px; font: 12pt 'Sitka Small';")
            self.server_password_line.setText("Пароль неверный")
                        
            print(value, 'QWERTYUIOP')
            #Пропадает окно ввода, добавить обработку сигналов
        print("END")
            
            
        
        
    def confirm(self):
        print("confirm")
        self.nickName = self.name_line.text()
        self.ip = self.ip_line.text()
        self.port = self.port_line.text()
        self.server_password = self.server_password_line.text()
        sampleIp = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
        
        self.name_line.setStyleSheet("border-radius: 7px; font: 12pt 'Sitka Small';")
        self.ip_line.setStyleSheet("border-radius: 7px; font: 12pt 'Sitka Small';")
        self.port_line.setStyleSheet("border-radius: 7px; font: 12pt 'Sitka Small';")        
        self.server_password_line.setStyleSheet("border-radius: 7px; font: 12pt 'Sitka Small';")        
                
        if 4 <= len(self.nickName) < 15:
            if not re.match(sampleIp, self.ip) is None:
                if self.port.isdecimal() and int(self.port) <= 65535:
                    if self.server_password:
                        if not os.path.exists(os.path.join("Information", "aboutUser.json")):
                    
                            with open(os.path.join("Information", "aboutUser.json"), "w") as f:
                                information = {"nickName": self.nickName, "ip": self.ip, "port": self.port}
                                json.dump(information, f, indent=6)
                        else:
                            with open(os.path.join("Information", "aboutUser.json"), "w") as f:
                                information = {"nickName": self.nickName, "ip": self.ip, "port": self.port}
                                json.dump(information, f, indent=6)
                            
                        #self.close()
                        self.signal.emit(['Update configuration'])
                        
                        if not self.AbilityToConnect:
                            self.join()
                        else:
                            self.signal.emit(['200_CONNECTION_ESTAB', self.public_key])
                            
                    else:
                        self.server_password_line.setStyleSheet("border: 2px solid red; border-radius: 7px; font: 12pt 'Sitka Small';")
                        self.server_password_line.setText("Введите пароль")                        
                else:
                    self.port_line.setStyleSheet("border: 2px solid red; border-radius: 7px; font: 12pt 'Sitka Small';")
                    self.port_line.setText("Некорректный ввод PORT")
            else:
                self.ip_line.setStyleSheet("border: 2px solid red; border-radius: 7px; font: 12pt 'Sitka Small';")
                self.ip_line.setText("Некорректный ввод IP")
        else:
            self.name_line.setStyleSheet("border: 2px solid red; border-radius: 7px; font: 12pt 'Sitka Small';")
            self.name_line.setText("Слишком длинный либо слишком короткий ник")

    
class JoinChatForm(QWidget):
    def __init__(self, parent=None, signal=None):
        self.group_name = None
        self.password = None
        self.signal = signal
        super().__init__()
        
        f_set_windows = open(r"templates\join_chat_windows.ui", "r", encoding="utf-8")
        f = io.StringIO(f_set_windows.read())
                
        uic.loadUi(f, self)
        self.setWindowTitle("Присоедениться к чату")
        self.setWindowModality(2)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.center()
        self.group_name_line.setStyleSheet("border-radius: 7px; font: 12pt 'Sitka Small';")
        self.password_line.setStyleSheet("border-radius: 7px; font: 12pt 'Sitka Small';")
                
        self.confirm_Button.clicked.connect(self.confirm)
        self.close_Button.clicked.connect(lambda: self.close())          
           
     
    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()
    
    def mouseMoveEvent(self, event):
        try:
            delta = QtCore.QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
        except AttributeError:
            pass
        
    def confirm(self):
        self.group_name = self.group_name_line.text()
        self.password = self.password_line.text()
        
        if 4 <= len(self.group_name) < 15:
            if 7 <= len(self.password):
                        
                print("Join new chat     JoinChatForm")
                self.signal.emit(['100_VALID_CHAT_INFORMATION', self.group_name, self.password])
                self.close()
            else:
                self.password_line.setStyleSheet("border: 2px solid red; border-radius: 7px; font: 12pt 'Sitka Small';")
                self.password_line.setText("Пароль должен быть не менее 7 символов")
        else:
            self.group_name_line.setStyleSheet("border: 2px solid red; border-radius: 7px; font: 12pt 'Sitka Small';")
            self.group_name_line.setText("Слишком длинное либо слишком короткое название группы")
    

class MakeNewChat(QWidget):
    def __init__(self, parent=None, signal=None):
        self.group_name = None
        self.password = None
        self.rep_password = None
        self.register_group_over = False
        self.signal = signal
        super().__init__()
        
        f_set_windows = open(r"templates\make_chat_windows.ui", "r", encoding="utf-8")
        f = io.StringIO(f_set_windows.read())
                
        uic.loadUi(f, self)
        self.setWindowTitle("Создать чат")
        self.setWindowModality(2)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.center()
        self.group_name_line.setStyleSheet("border-radius: 7px; font: 12pt 'Sitka Small';")
        self.password_line.setStyleSheet("border-radius: 7px; font: 12pt 'Sitka Small';")
        self.rep_password_line.setStyleSheet("border-radius: 7px; font: 12pt 'Sitka Small';")                
        
        self.confirm_Button.clicked.connect(self.confirm)
        self.close_Button.clicked.connect(lambda: self.close())          
           
     
    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()
    
    def mouseMoveEvent(self, event):
        try:
            delta = QtCore.QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
        except AttributeError:
            pass
        
    def confirm(self):
        self.group_name = self.group_name_line.text()
        self.password = self.password_line.text()
        self.rep_password = self.rep_password_line.text()
        
        if 4 <= len(self.group_name) < 15:
            if 7 <= len(self.password):
                if self.password == self.rep_password:
                    
                    print("self.register_group_over = True")
                    self.signal.emit(['100_MAKE_NEW_CHAT', self.group_name, self.password])
                    self.close()
                else:
                    self.rep_password_line.setStyleSheet("border: 2px solid red; border-radius: 7px; font: 12pt 'Sitka Small';")
                    self.rep_password_line.setText("Введенные пароли не совпадают")
            else:
                self.password_line.setStyleSheet("border: 2px solid red; border-radius: 7px; font: 12pt 'Sitka Small';")
                self.password_line.setText("Пароль должен быть не менее 7 символов")
        else:
            self.group_name_line.setStyleSheet("border: 2px solid red; border-radius: 7px; font: 12pt 'Sitka Small';")
            self.group_name_line.setText("Слишком длинное либо слишком короткое название группы")
    


class UserInterface(QMainWindow):
    def __init__(self, nickName, ip, port, server_password, connectMonitor, client, public_key, sym_key, IV, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        f_template = open(r"templates\main_frame.ui", "r", encoding="utf-8")
        self.f = io.StringIO(f_template.read())
        self.initui()
        self.nickName = nickName
        self.ip = ip
        self.port = port
        self.client = client
        self.public_key = public_key
        self.sym_key = sym_key
        self.IV = IV
        self.AbilityToConnect = False
        
        self.name_thisChat = None
        self.password_thisChat = None
        
        self.server_password = server_password
        self.connectMonitor = connectMonitor
        self.connectMonitor.getSignal.connect(self.signalHandler)
        
    def initui(self):
        uic.loadUi(self.f, self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) 
        self.center()
        self.close_window.move(940, 5)
        self.minimize_window.move(900, 5)
        icon = QtGui.QIcon()
        icon1 = QtGui.QIcon()
        icon2 = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("button_Icon\mn1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(r"button_Icon\x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(r"button_Icon\-.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send_message.setIcon(icon)
        self.send_message.setIconSize(QtCore.QSize(40, 64))
        self.close_window.setIcon(icon1)
        self.close_window.setIconSize(QtCore.QSize(20, 20))          
        self.minimize_window.setIcon(icon2)
        self.minimize_window.setIconSize(QtCore.QSize(25, 20))
        self.make_group_Button.clicked.connect(self.make_group)
        self.join_Button.clicked.connect(self.join)
        #self.pushButton_3.clicked.connect(self.translate)
        #self.pushButton_4.clicked.connect(self.configure)
        self.clear_chat.clicked.connect(self.clear_window)
        self.send_message.clicked.connect(self.sendMessage)
        self.close_window.clicked.connect(lambda: self.close())
        self.minimize_window.clicked.connect(lambda: self.showMinimized())
        self.pushButton_4.clicked.connect(self.getInfo)
        self.setWindowTitle("Чат-мессенджер")
        
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
            
    def updateConfigure(self):
        if os.path.exists(os.path.join("Information", "aboutUser.json")):
            with open(os.path.join("Information", "aboutUser.json")) as file:
                data = json.load(file)
                self.nickName = data['nickName']
                self.ip = data['ip']
                self.port = int(data['port'])    
    
    
    def sendMessage(self):
        
        if self.AbilityToConnect:
            messageText = self.lineEdit.text()
            if len(messageText) > 0:
                pickLoad = ["100_SEND_MESSAGE", self.name_thisChat, self.nickName,  self.password_thisChat, messageText] # "100_CONTINUE" -> "100_SEND_MESSAGE"
                print(pickLoad)
                self.connectMonitor.send_encrypt(pickLoad)
                
                item = QtWidgets.QListWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignLeft)
                item.setText(f"{self.nickName} (ВЫ):\n{messageText}")
                self.listWidget.addItem(item)
                self.lineEdit.setText("")
            else:
                message = "Проверьте соединение с сервером"
                QtWidgets.QMessageBox.about(self, "Оповещение", message)            
    
    def signalHandler(self, value:list):
        
        print("New signalHandler")
        
        if value[0] == 'Update configuration':
            self.updateConfigure()
        
        elif value[0] == "200_OK":
            print("signalHandler don't work")
            cellMessage = QtWidgets.QListWidgetItem()
            cellMessage.setTextAlignment(QtCore.Qt.AlignHCenter)
            cellMessage.setText(f"Server{value[1]}\n")
            self.listWidget.addItem(cellMessage)
            print(value)            
        
        elif value[0] == "200_JOIN_CHAT":
            self.AbilityToConnect = True
            cellMessage = QtWidgets.QListWidgetItem()
            cellMessage.setTextAlignment(QtCore.Qt.AlignHCenter)
            cellMessage.setText(f"Вы подключены к чату\n")
            self.listWidget.addItem(cellMessage)
                        
                        
            print("you be added to chat")
        
        elif value[0] == "200_CHAT_BE_MAKED":
            self.AbilityToConnect = True
            cellMessage = QtWidgets.QListWidgetItem()
            cellMessage.setTextAlignment(QtCore.Qt.AlignHCenter)
            cellMessage.setText(f"Вы создали чат\n")
            self.listWidget.addItem(cellMessage)
                        
                        
        # "100_SEND_MESSAGE", *encode_all_element(self.name_thisChat, self.nickName,  self.password_thisChat, messageText)            
        elif value[0] == "100_TAKE_MESSAGE":
            print(value, "signalHandler      100_TAKE_MESSAGE")
            print("signalHandler don't work1")
            cellMessage = QtWidgets.QListWidgetItem()
            cellMessage.setTextAlignment(QtCore.Qt.AlignRight)
            cellMessage.setText(f"{value[2]}:\n {value[-1]}")
            self.listWidget.addItem(cellMessage)
            print(value)            
        
        elif value[0] == "100_MAKE_NEW_CHAT":
            #                  name   password  usersList=[]
            print("100_MAKE_NEW_CHAT", value[1:])
            self.name_thisChat = value[1]
            self.password_thisChat = value[2]            
            self.connectMonitor.send_encrypt(["100_MAKE_NEW_CHAT", value[1], value[2], self.nickName])# *encode_all_element(*value[1:])
            
        
        elif value[0] == "100_VALID_CHAT_INFORMATION":
            print("100_VALID_CHAT_INFORMATION", value[1:])
            
            self.name_thisChat = value[1]
            self.password_thisChat = value[2]
            
            self.connectMonitor.send_encrypt(["100_VALID_CHAT_INFORMATION", *value[1:], self.nickName])
            
        elif value[0] == "403_WRONG_CONNECT_CHAT":
            self.name_thisChat = None
            self.password_thisChat = None
            
            self.notification_Label.setStyleSheet("border: 2px solid red; color: #fff; border-radius: 7px; font: 12pt 'Sitka Small';")
            self.notification_Label.setText('Такой группы не существует')
                        
                        
    def clear_notification_Label(self):
        self.notification_Label.setText('')
        self.notification_Label.setStyleSheet("border-radius: 15px; background-color: #073759;font: 14pt 'Sitka Small'; color: rgb(200, 0, 0); opacity: 1; transition: opacity 2s ease;")
    
    def clear_window(self):
        self.clear_notification_Label()
        self.listWidget.clear()
                
    
    def getInfo(self):
        self.info = AdditionalInformation()
        self.info.show()
    
    def configure(self):
        self.setWn = SetWindows(self, self.connectMonitor.getSignal)
        self.setWn.show()     
    
    def make_group(self):
        self.clear_notification_Label()
        
        self.make_chat = MakeNewChat(self, self.connectMonitor.getSignal)
        self.make_chat.show()
        
    
    def join(self):
        self.clear_notification_Label()
                
        self.joinChat = JoinChatForm(self, self.connectMonitor.getSignal)
        self.joinChat.show()
        
    """
    self.updateConfigure()
        if self.nickName != None:
            try:
                self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.client.connect((self.ip, self.port))
                self.connectMonitor.serverSocket = self.client
                self.connectMonitor.start()
            except Exception as error:
                message = "Проверьте соединение с сервером: 'Ошибка с соединением'"
                QtWidgets.QMessageBox.about(self, "Оповещение", message)            
        else:
            message = "Введите имя во фкладке 'Настройки'!"
            QtWidgets.QMessageBox.about(self, "Оповещение", message)
    """
    
    def translate(self):
        self.tr = TranslatorWindows()
        self.tr.show()
    
    def closeEvent(self, value:QtGui.QCloseEvent):#, 
        try:
            
            if self.name_thisChat:
                payload = ["EXIT", *encode_all_element(self.nickName, self.name_thisChat)]
                self.connectMonitor.send_encrypt(payload)
            
            self.hide()
            time.sleep(3)
            self.client.close()
            self.close()
        except Exception as err:
            print(err)
            
    
def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = InputInterface()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())