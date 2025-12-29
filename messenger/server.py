import socket
import time
import pickle
import threading
import os
import hashlib

from tChats import OrdinarChat, User
from encryption import generate_keys, decrypt_messageRSA, encrypt_messageAES


def hashing_password(psw):
    h = hashlib.sha256()
    h.update(psw.encode('ascii'))
    return h.hexdigest()

def decode_all_element(*elements):
    elements = list(elements)
    for index in range(len(elements)):
        elements[index] = elements[index].decode()
        
    return elements


def decrypt_all_block_RSA(data):
    decrypted_data = []
    #print("len ", len(data))
    print(data)
    index_end = 0
    first_block = ''
    #print("@#$%^&*()_")
    for block in data:
        #print("@#$%^&*()_")
        #print("block ", index_end)
        decrypt_block = decrypt_messageRSA(block)
        #print("END")
        if index_end == 0:
            #print('first')
            first_block = decrypt_block
            #print('first')
            
        elif decrypt_block == first_block:
            #print("break")
            break
        #print("SKIP")
        decrypted_data.append(decrypt_block)
        #print(decrypt_block)
        #print("SKIP_END")
        #print(decrypted_data[index_end])
        #print("SKIP_END_END")
        index_end += 1
    
    #print(decrypted_data + data[index_end-1:], " decrypt_all_block_RSA")
    if index_end == len(data):
        return decrypted_data
    
    return decrypted_data + data[index_end-1:]
    
def encrypt_all_block_AES(data, key, iv):
    decrypted_data = []
    
    for block in data:
        decrypted_data.append(encrypt_messageAES(block, key, iv))
        
    return decrypted_data


class Server():
    def __init__(self, ip, port):
        self.port = port
        self.ip = ip
        self.server_password = "65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5"
        self.symetricKey = None
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.ip, self.port))
        self.server.listen(0)
        self.allClients = []
        self.users_key_IV = {}
        
        
        #!!!!!! Сохранять и выгружать инфориацию о чатах из json файла
        self.chatDict = {}
        
        
        if not self.keys_exists():
            generate_keys()
        
        
        self.public_key = None
        with open("keys/public_key.pem", 'rb') as f:
            self.public_key = f.read()
        
        print("Сервер запущен!")
        threading.Thread(target=self.checkNewJoined).start()
    
    def keys_exists(self):
        return os.path.exists("keys/private_key.pem") and os.path.exists("keys/public_key.pem")
    
    #Проверка на подключение к чату
    def checkNewJoined(self):
        while True:
            user, road = self.server.accept()
            if user not in self.allClients:    #Проверка на наличие пользователя в чате
                self.allClients.append(user)
                #self.newKey()
                answer = ["200_CONNECTION_ESTAB", self.public_key] #Успешное подключение к чату
                user.send(pickle.dumps(answer))
                print(f"{road} - joined the chat")
                #self.checkMassage(user)
                threading.Thread(target=self.checkMassage, args=(user, )).start()
            time.sleep(2)
    
    def verifyUser(self, chat_name, password, user_name):
        chat = self.chatDict.get(chat_name, 0)
        if chat:
            if chat.chatname_isCorrect(chat_name) and chat.password_isCorrect(password) and not chat.user_includeChat(user_name):
                return True
        return False

    #Генератор симметричного шифра
    def newKey(self):
        if self.symetricKey is None:
            self.symetricKey = Fernet.generate_key()

    #Проверка на наличие новых сообщений    
    def checkMassage(self, user):
        while True:
            #Попытка принять сообщение от пользователя
            try:
                #print("checkMassage")
                message = user.recv(2048) #, "100_VALID_PASSWORD"
                #print("---------------")
                #print(pickle.loads(message))
                decodeMessage = decrypt_all_block_RSA(pickle.loads(message))
                #print("---------------")
                #print(decodeMessage)
            
            #В случае неудачи, оборвать с ним соединение
            except:
                self.allClients.remove(user)
                break
            
            #Отправка сообщения в чат
            
            #"100_SEND_MESSAGE", *encode_all_element(self.name_thisChat, self.nickName,  self.password_thisChat, messageText)
            ################################################################################################
            if decodeMessage[0] == "100_SEND_MESSAGE":
                #decodeMessage = [decodeMessage[0], *decode_all_element(*decodeMessage[1:])]
                this_chat = self.chatDict[decodeMessage[1]]
                for client in this_chat.get_userList():
                    if client.name != decodeMessage[2]:
                        decodeMessage[0] = "100_TAKE_MESSAGE"
                        user_key, user_iv = self.users_key_IV[id(client.socket_address)]
                        encode_message = encrypt_all_block_AES(decodeMessage, user_key, user_iv)
                        new_message = pickle.dumps(encode_message)
                        client.socket_address.send(new_message)
            
            
            if decodeMessage[0] == "100_VALID_PASSWORD":
                print("password: ", decodeMessage[2])
                self.users_key_IV[id(user)] = [decodeMessage[-2], decodeMessage[-1]]
                if hashing_password(decodeMessage[2]) != self.server_password:
                    answer = ["400_WRONG_PASSWORD", "Соединение разорвано, пароль сервера неверный"]
                    del self.users_key_IV[id(user)]
                    print(answer)
                    
                else:
                    answer = ["200_CORRECT_PASSWORD"]
                    print(answer)
                
                encode_answer = encrypt_all_block_AES(answer, decodeMessage[-2], decodeMessage[-1])
                user.send(pickle.dumps(encode_answer))                    
            
            
            elif decodeMessage[0] == "100_MAKE_NEW_CHAT":
            
                decodeMessage = [decodeMessage[0], decodeMessage[1], decodeMessage[2], decodeMessage[3]]#*decode_all_element(*decodeMessage[1:3])
            
                print(decodeMessage, "100_MAKE_NEW_CHAT")
                
                user_key, user_iv = self.users_key_IV[id(user)]
                
                #######################################################################################################
                if self.chatDict.get(decodeMessage[1], 0) == 0:
                    new_chat = OrdinarChat(decodeMessage[1], decodeMessage[2])
                    new_chat.add_user(User(decodeMessage[3], user))
                    self.chatDict[decodeMessage[1]] = new_chat
                    print(self.chatDict)
                    answer = ["200_CHAT_BE_MAKED"]
                else:
                    # Случай когда чат с таким именем уже есть
                    answer = ["403_WRONG_CONNECT_CHAT", ""]
                    
                user.send(pickle.dumps(encrypt_all_block_AES(answer, user_key, user_iv)))                    
            
            elif decodeMessage[0] == "100_VALID_CHAT_INFORMATION":

                decodeMessage = [decodeMessage[0], decodeMessage[1], decodeMessage[2], decodeMessage[3]]#*decode_all_element(*decodeMessage[1:3])
                
                user_key, user_iv = self.users_key_IV[id(user)]
                
                print(decodeMessage, "100_VALID_CHAT_INFORMATION")                
                ###################################################################################################               
                if self.verifyUser(decodeMessage[1], decodeMessage[2], decodeMessage[3]):
                    self.chatDict[decodeMessage[1]].add_user(User(decodeMessage[3], user))
                    answer = ["200_JOIN_CHAT"]
                else:
                    answer = ["403_WRONG_CONNECT_CHAT", "Такого чата нет"]
                    
                user.send(pickle.dumps(encrypt_all_block_AES(answer, user_key, user_iv)))                    
            
            #Участник покинул чат
            elif decodeMessage[0] == "500_INTERNAL_SERVER_ERROR":
                print(f"{decodeMessage[1]} - left the chat")
                #self.allClients.remove(user)
            
            elif decodeMessage[0] == "EXIT":
 
                decodeMessage = [decodeMessage[0], *decode_all_element(*decodeMessage[1:])]
                
                print(decodeMessage)
                
                print(f"{decodeMessage[1]}  - Разорвал соединение")
                #self.allClients.remove(user)
                
                user.close()
                #########################################################################################################################
                if self.chatDict.get(decodeMessage[2], 0):
                    if self.chatDict[decodeMessage[2]].user_includeChat(decodeMessage[1]):
                        self.chatDict[decodeMessage[2]].del_user(decodeMessage[1])
            
            time.sleep(1)
    
        
if __name__ == "__main__":
    # 192.168.1.1
    newServer = Server("192.168.1.1", 1234)