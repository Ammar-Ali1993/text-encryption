class Transpose:

    def __init__(self):
        self.map = [5, 10, 6, 8, 1, 3, 9, 4, 7, 2]

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



