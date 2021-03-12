import transpose
import replace
import string

class Handler:

    def __init__(self):
        self.n = 10
        self.behavior = [1 ,0 , 0, 1, 0, 1]

    def execute(self,text, type):

        text = self.__processText(text)
        chunks = self.__seperate(text)
        returnString=''
        counter = 0
        transposeObject = transpose.Transpose()
        replaceObject = replace.Replace()
        for i in chunks:
            try:
                 action = self.behavior[counter]
            except:
                print(i)
                exit()

            if type =='encrypt':
                if action:
                    returnString += transposeObject.encrypt(i)
                else:
                    returnString += replaceObject.encrypt(i)
            else:
                if action:
                    returnString += transposeObject.decrypt(i)
                else:
                    returnString += replaceObject.decrypt(i)

            if counter == len(self.behavior)-1:
                counter = 0
            else:
                counter +=1
        return returnString

    def __processText(self,text):
        return text.lower()





    def __seperate(self,text):

        chunks = [text[i:i + self.n] for i in range(0, len(text), self.n)]
        chunks[len(chunks) - 1] = chunks[len(chunks) - 1].ljust(self.n, ' ')
        return chunks









