from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
import base64


# Генерация пары ключей RSA
def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    # Сохранение закрытого ключа
    with open("keys/private_key.pem", "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ))

    # Сохранение открытого ключа
    with open("keys/public_key.pem", "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

# Загрузка закрытого ключа
def load_private_key():
    with open("keys/private_key.pem", "rb") as f:
        return serialization.load_pem_private_key(
            f.read(),
            password=None,
            backend=default_backend()
        )

# Загрузка открытого ключа
def load_public_key():
    with open("keys/public_key.pem", "rb") as f:
        return serialization.load_pem_public_key(
            f.read(),
            backend=default_backend()
        )

# Шифрование сообщения
def encrypt_messageRSA(message):
    print("encrypt_messageRSA", message)
    
    if isinstance(message, bytes):
        return message        
    
    public_key = load_public_key()
    encrypted = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )#.encode()
    return encrypted

# Дешифрование сообщения
def decrypt_messageRSA(encrypted_message):
    private_key = load_private_key()
    decrypted = private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted.decode()



# Функция для генерации ключа и инициализационного вектора
def generate_key_and_iv():
    key = os.urandom(32)  # 256-битный ключ
    iv = os.urandom(16)   # 128-битный IV
    return key, iv

# Функция для добавления паддинга
def pad(data):
    padding_length = 16 - len(data) % 16
    return data + bytes([padding_length] * padding_length)

# Функция для удаления паддинга
def unpad(data):
    padding_length = data[-1]
    return data[:-padding_length]

# Функция для шифрования сообщения
def encrypt_messageAES(plaintext, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Добавление паддинга к сообщению
    padded_plaintext = pad(plaintext.encode())
    
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    return base64.b64encode(ciphertext).decode()

# Функция для дешифрования сообщения
def decrypt_messageAES(ciphertext, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    decrypted_padded = decryptor.update(base64.b64decode(ciphertext)) + decryptor.finalize()
    
    # Убираем дополнение
    return unpad(decrypted_padded).decode()




if __name__ == "__main__":
    # Генерация ключей (раскомментируйте, если ключи еще не созданы)
    #generate_keys() 100_VALID_PASSWORD
     
    # Пример использования
    original_message = "qwerty"
    
    print(load_private_key())
    print(load_public_key())
    
    print(f"Оригинальное сообщение: {original_message}")

    encrypted = encrypt_messageRSA(original_message)
    print(f"Зашифрованное сообщение: {encrypted}")

    decrypted = decrypt_messageRSA(encrypted)
    print(f"Дешифрованное сообщение: {decrypted}")