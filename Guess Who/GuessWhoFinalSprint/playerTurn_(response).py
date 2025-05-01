import random

class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)
        self.memory = ALProxy("ALMemory")
        self.gState = [['Amy', 1], ['Al', 1], ['Sam', 1], ['Sofia', 1], ['Olivia', 1], ['Mike', 1],
        ['David', 1], ['Farah', 1], ['Ben', 1], ['Jordan', 1], ['Laura', 1], ['Leo', 1], ['Liz', 1], ['Mia', 1], ['Nick', 1], ['Lily', 1], ['Joe', 1], ['Gabe', 1], ['Eric', 1], ['Emma', 1], ['Carmen', 1], ['Daniel', 1], ['Rachel', 1], ['Katie', 1]]
        self.characterFeatures =[
        [False, True, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, True, "Amy"],


        [True, False, False, False, False, True, False, False, False, True, True, False, False, False, False, False, False, True, True, True, False, True, False, False, True, False, "Al"],

        [True, False, True, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, True, "Sam"],

        [False,True, False, True, False, False, False, True, False, False, False, False, False, False, False, False, True, False, False, False, False, True, False, True, True, False, "Sofia"],

        [False, True, True, False, False, False, False, False, True, False, False, False, True, True, True, False, False, False, False, False, False, False, True, False, False, True, "Olivia"],

        [True, False, True, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, True, True, True, False, "Mike"],

        [True, False, False, False, True, False, False, True, False, True, False, False, False, False, False, True, False, False, False, True, False, False, True, True, True, False, "David"],

        [False, True, True, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, True, False, "Farah"],

        [True, False, False, True, False, False, False, True, False, False, False, False, False, False, False, False, True, True, False, False, False, False, True, False, False, True, "Ben"],

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

        self.name = [
                 "Amy",
                 "Al",
                 "Sam",
                 "Sofia",
                 "Olivia",
                 "Mike",
                 "David",
                 "Farah",
                 "Ben",
                 "Jordan",
                 "Laura",
                 "Leo",
                 "Liz",
                 "Mia",
                 "Nick",
                 "Lily",
                 "Joe",
                 "Gabe",
                 "Eric",
                 "Emma",
                 "Carmen",
                 "Daniel",
                 "Rachel",
                 "Katie"
            ]


    def onLoad(self):
        cInt = random.randint(0,23)
        if (cInt == 7) or (cInt == 13):
            cInt += 1
        self.roboCharacter = self.characterFeatures[cInt]
        roboCharacter = self.roboCharacter
        self.memory.insertData("roboCharacter", roboCharacter)
        self.memory.insertListData(self.gState)
        self.logger.info(roboCharacter)
        pass

    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self):
        self.logger.info(self.roboCharacter)
        userInput = self.memory.getData("userInput")
        userInput = str(userInput.strip("<...>"))
        userInput = userInput.strip()
        self.logger.info(type(userInput))
        self.logger.info(userInput)
        if userInput == "ready":
            self.onStopped("ready")
            return
        feat_idx = self.featureToInt[userInput]
        if self.roboCharacter[feat_idx] == True:
            self.onStopped("Yes")
        elif self.roboCharacter[feat_idx] == False:
            self.onStopped("No")
        #add another elif for name guessing
        else:
            self.onStopped("Error")
        pass

    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box
