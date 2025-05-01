class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)
        self.memory = ALProxy("ALMemory")
        self.characterFeatures =[
        [False, True, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, True, "Amy"],

        [True, False, False, False, False, True, False, False, False, True, True, False, False, False, False, False, False, True, True, True, False, True, False, False, True, False, "Al"],

        [True, False, True, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, True, "Sam"],

        [False,True, False, True, False, False, False, True, False, False, False, False, False, False, False, False, True, False, False, False, False, True, False, True, True, False, "Sofia"],

        [False, True, True, False, False, False, False, False, True, False, False, False, True, True, True, False, False, False, False, False, False, False, True, False, False, True, "Olivia"],

        [True, False, True, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, True, True, True, False, "Mike"],

        [True, False, False, False, True, False, False, True, False, True, False, False, False, False, False, True, False, False, False, True, False, False, True, True, True, False, "David"],

        [False, True, True, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, True, False, "Farah"],

        [True, False, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, False, False, False, True, False, False, True, "Ben"],

        [True, False, True, False, False, False, False, True, False, False, False, False, True, True, False, False, True, False, False, False, False, False, True, False, True, False, "Jordan"],

        [False, True, True, False, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, True, False, True, True, False, "Laura"],

        [True, False, False, False, False, True, False, True, False, True, False, False, False, False, False, False, False, False, False, True, False, False, True, True, True, False, "Leo"],

        [False, True, False, False, False, True, False, False, True, False, False, False, False, False, False, False, False, True, False, False, True, False, False, True, False, True, "Liz"],

        [False, True, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, False, True, "Mia"],

        [True, False, False, False, True, False, False, True, False, False, False, True, False, False, False, False, True, False, False, False, False, False, True, False, False, True, "Nick"],

        [False, True, False, True, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, True, False, True, True, False, "Lily"],

        [True, False, False, False, False, True, False, False, False, True, True, False, False, False, False, False, False, True, False, True, False, False, True, True, True, False, "Joe"],

        [True, False, True, False, False, False, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False, False, True, False, True, False, "Gabe"],

        [True, False, True, False, False, False, False, True, False, False, False, True, True, False, False, False, False, False, False, False, True, False, False, False, False, True, "Eric"],

        [False, True, False, False, False, False, True, False, True, False, False, True, False, True, False, False, False, False, False, False, False, False, True, False, False, True, "Emma"],

        [False, True, False, False, False, True, False, True, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, True, False, True, "Carmen"],

        [True, False, False, False, False, False, True, False, True, True, False, True, False, False, True, False, False, False, True, True, False, True, False, False, False, True, "Daniel"],

        [False, True, False, True, False, False, False, False, True, False, False, False, False, False, False, False, True, True, False, False, True, False, False, False, True, False, "Rachel"],

        [False, True, False, False, True, False, False, False, True, False, False, False, False, False, True, True, False, False, False, False, True, False, False, False, False, True, "Caity"]
        ]
        self.featureToInt = {
        "male": 0,
        "female": 1,
        "black hair": 2,
        "hair black": 2,
        "brown hair": 3,
        "hair brown": 3,
        "hair blonde": 4, #Carmen
        "blonde hair": 4,
        "white hair": 5,
        "hair white": 5,
        "orange hair": 6,
        "hair orange": 6,
        "short hair": 7,
        "hair short": 7,
        "hair long": 8,
        "long hair": 8,
        "facial hair": 9,
        "bald": 10,
        "freckles": 11,
        "dyed hair": 12,
        "hair dyed": 12,
        "braided hair": 13,
        "hair braided": 13,
        "ponytail": 14,
        "headwear": 15,
        "earrings": 16,
        "glasses": 17,
        "beard": 18,
        "mustache": 19,
        "blue eyes": 20,
        "eyes blue": 20,
        "green eyes": 21,
        "eyes green": 21,
        "eyes brown": 22,
        "brown eyes": 22,
        "showing teeth": 23,
        "facing left": 24,
        "facing right": 25,
        "name": 26
        }

        self.features = [
            'male',          # 0
            'female',        # 1
            'black hair',    # 2
            'brown hair',    # 3
            'hair blonde',   # 4
            'white hair',    # 5
            'orange hair',   # 6
            'short hair',    # 7
            'long hair',     # 8
            'facial hair',   # 9
            'bald',          # 10
            'freckles',      # 11
            'dyed hair',     # 12
            'braided hair',  # 13
            'ponytail',      # 14
            'headwear',      # 15
            'earrings',      # 16
            'glasses',       # 17
            'beard',         # 18
            'mustache',      # 19
            'blue eyes',     # 20
            'green eyes',         # 21
            'eyes brown',    # 22
            'showing teeth', # 23
            'facing left',   # 24
            'facing right',  # 25
            'name'           # 26
        ]
        self.name = ["Amy", "Al", "Sam", "Sofia", "Olivia", "Mike", "David", "Farah", "Ben", "Jordan", "Laura", "Leo", "Liz", "Mia", "Nick", "Lily", "Joe", "Gabe", "Eric", "Emma", "Carmen", "Daniel", "Rachel", "Katie"]

    def onLoad(self):
        #put initialization code here
        pass

    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self, p):
        userResponse = p
        featureAsked = self.memory.getData("questionAsked")
        self.questionLogic(featureAsked, userResponse)
        if userResponse == "yes":
            self.logger.info("Player Eliminated")
            self.elim(featureAsked, True)
        elif userResponse == "no":
            self.logger.info("Player Eliminated")
            self.elim(featureAsked, False)
        else:
            self.logger.info("Didnt work")
        self.onStopped()

        pass

    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box

    def elim(self, feat, ans):
        self.logger.info(feat)
        feat_idx = self.featureToInt[feat]  # Get the feature index from string
        for i, person in enumerate(self.characterFeatures):
            if person[feat_idx] != ans:
                self.memory.removeData(self.name[i])
                self.memory.insertData(self.name[i], 0)
                self.logger.info((str(self.name[i])) + " " + str(self.memory.getData(self.name[i])))
                #row = i // 8/ #possible issue
                #col = i % 8
                #gState[row][col] = "0"

    def questionLogic(self, question, answer):
        if question == "male" or question == "female":
            self.memory.removeData("female")
            self.memory.insertData("female", 1)
            self.memory.removeData("male")
            self.memory.insertData("male", 1)
        elif question == "left" or question == "right":
            self.memory.removeData("left")
            self.memory.insertData("left", 1)
            self.memory.removeData("right")
            self.memory.insertData("right", 1)
        elif question == "bald" and answer == "yes":
            self.memory.removeData("short hair")
            self.memory.insertData("short hair", 1)
            self.memory.removeData("long hair")
            self.memory.insertData("long hair", 1)
            self.memory.removeData("brown hair")
            self.memory.insertData("brown hair", 1)
            self.memory.removeData("black hair")
            self.memory.insertData("black hair", 1)
            self.memory.removeData("dyed hair")
            self.memory.insertData("dyed hair", 1)
            self.memory.removeData("blonde hair")
            self.memory.insertData("blonde hair", 1)
            self.memory.removeData("orange hair")
            self.memory.insertData("orange hair", 1)
            self.memory.removeData("white hair")
            self.memory.insertData("white hair", 1)
            self.memory.removeData("braided")
            self.memory.insertData("braided", 1)
            self.memory.removeData("ponytail")
            self.memory.insertData("ponytail", 1)
            self.memory.removeData("female")
            self.memory.insertData("female", 1)
        elif question == "short hair" or question == "long hair":
            self.memory.removeData("long hair")
            self.memory.insertData("long hair", 1)
            self.memory.removeData("short hair")
            self.memory.insertData("short hair", 1)
            self.memory.removeData("bald")
            self.memory.insertData("bald", 1)
        elif question == ("brown hair" or "black hair" or "orange hair" or "white hair" or "blonde hair" or "dyed hair") and answer == "yes":
            self.memory.removeData("brown hair")
            self.memory.insertData("brown hair", 1)
            self.memory.removeData("black hair")
            self.memory.insertData("black hair", 1)
            self.memory.removeData("white hair")
            self.memory.insertData("white hair", 1)
            self.memory.removeData("orange hair")
            self.memory.insertData("orange hair", 1)
            self.memory.removeData("blonde hair")
            self.memory.insertData("blonde hair", 1)
            self.memory.removeData("dyed hair")
            self.memory.insertData("dyed hair", 1)
        elif question == ("brown eyes" or "green eyes" or "blue eyes") and answer == "yes":
            self.memory.removeData("green eyes")
            self.memory.insertData("green eyes", 1)
            self.memory.removeData("blue eyes")
            self.memory.insertData("blue eyes", 1)
            self.memory.removeData("brown eyes")
            self.memory.insertData("brown eyes", 1)
        elif question == ("ponytail" or "braided") and answer == "yes":
            self.memory.removeData("bald")
            self.memory.insertData("bald", 1)
        elif question == ("facial hair" or "beard" or "mustache") and answer == "yes":
            self.memory.removeData("male")
            self.memory.insertData("male", 1)
            self.memory.removeData("male")
            self.memory.insertData("male", 1)
        elif question == ("beard" or "mustache") and answer == "yes":
            self.memory.removeData("facial hair")
            self.memory.insertData("facial hair", 1)
