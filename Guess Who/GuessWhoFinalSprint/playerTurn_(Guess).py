class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)
        self.memory = ALProxy("ALMemory")

    def onLoad(self):
        pass

    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self, p):
        playerGuess = self.memory.getData("userGuess")
        roboCharacter = self.memory.getData("roboCharacter")
        if (playerGuess == roboCharacter[26]):
            self.onStopped("right")
        else:
            self.onStopped("wrong")
        pass

    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box
