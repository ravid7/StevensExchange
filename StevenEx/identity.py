from cryptography.fernet import Fernet
import re


class Identity:

    def __init__(self, name, email, password):
        super().__init__()
        self.name = name
        self.email = email
        self.password = password
        self.key = self.keyInitializer()

    def validate(self, secret):
        cipher_suite = Fernet(self.key)
        print(cipher_suite.encrypt())

    def keyInitializer(self):
        file_key = open('keyCryp', 'r')
        x = file_key.readline()
        x = re.search(r"([a-zA-Z0-9]+)", x)
        return x.group(0)


# i.validate(b"ravirathore")
