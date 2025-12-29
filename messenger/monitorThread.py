from PyQt5 import QtCore
from cryptography.fernet import Fernet
import pickle
import time
import sys


class ThreadMonitor(QtCore.QThread):
    getSignal = QtCore.pyqtSignal(list)
    serverSocket = None
    symetricKey = None
        
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        
    def start(self):
        print(f"the server was started {self.symetricKey}")
        while True:
            if self.symetricKey != None:
                message = self.symetricKey.recv(1024)
                decodeMessage = pickle.load(message)
            if decodeMessage[0] == "200_OK":
                self.symetricKey = decodeMessage[-1]
                self.cipher = Fernet(self.symetricKey)
                self.mysignal.emit(decodeMessage)
            elif decodeMessage[0] == "100_CONTINUE":
                decryptedMessage = self.cipher.decrypt(decrypt[-1]).decode()
                decryptedload = ["100_CONTINUE", decodeMessage[1], decodeMessage[2], decryptedMessage]
                self.mysignal.emit(decryptedload)
            time.sleep(2)
            
    def sendEncryptMessage(self, information):
        if information[0] == "100_CONTINUE":
            encryptMessage = self.cipher.encrypt(information[-1])
            pickLoad = ["100_CONTINUE", information[1], information[2], encryptMessage]
            self.serverSocket.send(pickle.dumps(pickLoad))
        elif information[0] == "500_INTERNAL_SERVER_ERROR":
            encryptMessage = self.cipher.encrypt(information[-1])
            pickLoad = ["500_INTERNAL_SERVER_ERROR", information[1], encryptMessage]
            self.serverSocket.send(pickle.dumps(pickLoad))