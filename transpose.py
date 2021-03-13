import db


class Transpose:
    def __init__(self):
        self.db = db.DB()
        dbMap = list( self.db.getPropery('transpose_map')[0][2])
        integerMap = map(int, dbMap)
        self.map = list(integerMap)


    def encrypt(self,text):

        returnString=''
        for i in self.map:
            returnString += text[i-1]
        return returnString

    def decrypt(self,text):

        returnString = ''
        counter=0
        for i in self.map:
            returnString += text[self.map[counter] - 1]
            counter += 1
        return returnString



