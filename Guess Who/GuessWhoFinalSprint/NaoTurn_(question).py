class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)
        self.memory = ALProxy("ALMemory")
        self.question_bank = [["male", 0],["female", 0], ["black hair", 0], ["brown hair", 0],["blonde hair", 0],["white hair", 0],["orange hair", 0],["short hair", 0],["long hair", 0],["facial hair", 0],["bald", 0],["freckles", 0],["dyed hair", 0],["braided hair", 0],["ponytail", 0],["headwear", 0], ["earrings", 0],["glasses", 0],["beard", 0],["mustache", 0],["blue eyes", 0],["green eyes", 0],["brown eyes", 0],["showing teeth", 0],["facing left", 0],["facing right", 0]]

        self.name = ["Amy", "Al", "Sam", "Sofia", "Olivia", "Mike", "David", "Farah", "Ben", "Jordan", "Laura", "Leo", "Liz", "Mia", "Nick", "Lily", "Joe", "Gabe", "Eric", "Emma", "Carmen", "Daniel", "Rachel", "Katie"]


    def onLoad(self):
        self.memory.insertListData(self.question_bank)

        pass

    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self):
        if self.checkIfCanGuess():
            return
        questionAsked = False
        while questionAsked == False:
            index = random.randint(0, 25)
            if self.memory.getData(self.question_bank[index][0]) != 1:
                question = self.question_bank[index]
                self.memory.insertData("questionAsked", question[0])
                self.memory.removeData(question[0])
                self.memory.insertData(question[0], 1)
                if question[0] == "male" or question[0] == "female" or question[0] == "bald" or question[0] == "showing teeth" or question[0] == "facing left" or question[0] == "facing right":
                    phrase = ("Is your character " + str(question[0]))
                    self.onStopped(phrase)
                else:
                    phrase = ("Does your character have " + str(question[0]))
                    self.onStopped(phrase)
                questionAsked = True

        pass

    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box

    def checkIfCanGuess(self):
        remaining = 0
        lastName = ""
        for name in self.name:
            if (self.memory.getData(name)):
                lastName = name
                remaining += 1
                if (remaining >= 2):
                    return False

        self.guess(lastName)
        return True
