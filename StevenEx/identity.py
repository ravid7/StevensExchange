from cryptography.fernet import Fernet
import re
import os

class Identity:

    def __init__(self):
        super().__init__()
        self.key = self.keyInitializer().encode('UTF-8')
        self.cipher = Fernet(self.key)
    #encrypt password
    def encrypt(self, password):
        password = password.encode('UTF-8')
        return self.cipher.encrypt(password)

    #decrypt and match password
    def match(self, db_key, passed):
        return self.cipher.decrypt(db_key.encode()).decode() == passed

    def keyInitializer(self):
        path = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(path, 'credentials/keyCryp')
        file_key = open(path, 'r')
        x = file_key.readline()
        x = re.search(r"([a-zA-Z0-9=]+)", x)
        return x.group(0)

