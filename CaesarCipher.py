class CaesarCipher:

    seedNumber=0
    textToEncript=''
    textEncripted=''
    textToDecript=''
    textDecripted=''

    def __init__(self,seedNumber):
        self.seedNumber=seedNumber

    def encriptString(self,textToEncript):
        self.textToEncript=textToEncript
        self._cleanString()
        self._encription()
        print(self.textEncripted)
        return self.textEncripted
    
    def _cleanString(self):
        accentToRemove='ÁÀÃÂÇáàãâçÉÊéêÍíÑÓÔÕñóôõÚÜúü'
        accentToReplace='AAAACaaaacEEeeIiNOOOnoooUUuu'

        for letter in self.textToEncript:
            positionLetter=accentToRemove.find(letter)
            if positionLetter!=-1:
                self.textToEncript=self.textToEncript.replace(letter,accentToReplace[positionLetter],1)

    def _encription(self):
        for textCharacter in self.textToEncript:
            try:
                numberAscii=ord(textCharacter)+self.seedNumber
                if numberAscii>127:
                    delta=numberAscii % 127
                    self.textEncripted=self.textEncripted+str(chr(delta))
                else:
                    self.textEncripted=self.textEncripted+str(chr(numberAscii))
            except:
                self.textEncripted=self.textEncripted+str(textCharacter)

    def decriptString(self,textToDecript):
        self.textToDecript=textToDecript
        self._decription()
        print(self.textDecripted)
        return self.textDecripted


    def _decription(self):
        for encriptedCharacter in self.textToDecript:
            try:
                numberAscii=ord(encriptedCharacter)-self.seedNumber
                if numberAscii<0:
                    delta=127+numberAscii
                    self.textDecripted=self.textDecripted+str(chr(delta))
                else:
                    self.textDecripted=self.textDecripted+chr(numberAscii)
            except:
                self.textDecripted=self.textDecripted+str(encriptedCharacter)

                
