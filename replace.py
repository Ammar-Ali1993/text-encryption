import string
import db


class Replace:

    def __init__(self):

        self.db = db.DB()
        self.spaceReplacement = self.db.getPropery('space_replacement')[0][2]
        self.map = self.db.getPropery('replace_map')[0][2]

    def encrypt(self,text):
        returnString=''
        for i in text:
            encryptedChar = self.__encryptLetter(i)
            returnString += encryptedChar
        return returnString


    def decrypt(self,text):
        returnString = ''
        for i in text:
            decryptedLetter = self.__decryptLetter(i)
            returnString += decryptedLetter
        return returnString

    def __getLetterIndex(self, letter):

        try:
            return string.ascii_lowercase.index(letter)
        except:
            return self.spaceReplacement

    def __encryptLetter(self,letter):

        letterIndex=self.__getLetterIndex(letter)
        try:
            return self.map[letterIndex]
        except:
            return self.spaceReplacement

    def __decryptLetter(self, letter):

        try:
            index = self.map.index(letter)
            return string.ascii_lowercase[index]
        except:
            return ' '





