class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)
        
        self.question_bank = [
        ["Is your character male?", 0, "male"],
        ["Is your character female", 0, "female"],
        ["Does your character have black hair?", 0, "black hair"],
        ["Does your character have brown hair?", 0, "brown hair"],
        ["Does your character have blonde hair?", 0, "blonde hair"],
        ["Does your character have white hair?", 0, "white hair"],
        ["Does your character have orange hair?", 0, "orange hair"],
        ["Does your character have short hair?", 0, "short hair"],
        ["Does your character have long hair?", 0, "hair long"],
        ["Does your character have facial hair?", 0, "facial hair"],
        ["Is your character bald?", 0, "bald"],
        ["Does your character have freckles?", 0, "freckles"],
        ["Does your character have dyed hair?", 0, "dyed hair"],
        ["Does your character have braided hair?", 0, "braided hair"],
        ["Does your character have a ponytail?", 0, "ponytail"],
        ["Does your character have any headware?", 0, "headwear"],
        ["Does your character wear earrings?", 0, "earrings"],
        ["Does your character wear glasses?", 0, "glasses"],
        ["Does your character have a beard?", 0, "beard"],
        ["Does your character have a mustache?", 0, "mustache"],
        ["Does your character have blue eyes?", 0, "blue eyes"],
        ["Does your character have green eyes?", 0, "green"],
        ["Does your character have brown eyes?", 0, "eyes brown"],
        ["Is your character smiling with teeth?", 0, "teeth"],
        ["Is your character facing left?", 0, "left"],
        ["Is your character facing right?", 0, "name"],
    ]


    def onLoad(self):
        self.memory.insertListData(self.question_bank)
        pass

    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self):
        questionAsked = False
        while questionAsked == False:
            index = random.randint(0, 25)
            if self.getData(self.question_bank[index][1]) != 1:
                question = self.question_bank[index]
                self.memeory.insertData("questionAsked", question[0])
                self.memory.removeData(question[0])
                self.memory.insertData(question[0], 1)
                self.onStopped(str(question[0])) 
                questionAsked = True
        
        pass

    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box

    
