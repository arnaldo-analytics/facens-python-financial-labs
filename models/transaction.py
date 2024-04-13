from utils.utils import Utils

class Transaction():

    def __init__(self, _type=None, value=None, description=None):
        self.__utils = Utils()
        
        self.__type = _type
        self.__value = value
        self.__description = description

    def save(self):
        self.__utils.write_file(self.__type, self.__value, self.__description)
    
    def view(self):
        for transaction in self.__utils.read_file():
            print(transaction)
    