class MyClass(GeneratedClass):
    def __init__(self):
    # Initialize the base class
        GeneratedClass.__init__(self)
        # Create ALMemory proxy to read/write robot memory
        self.memory = ALProxy("ALMemory")
        # Define character features:
        # Each inner list represents a character's features (Booleans) + their name at the end
        self.characterFeatures =[
        [False, True, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, True, "Amy"],

        [True, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False, False, True, True, True, False, True, False, False, True, False, "Al"],

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

        [True, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False, False, True, False, True, False, False, True, True, True, False, "Jo"],

        [True, False, True, False, False, False, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False, False, True, False, True, False, "Gabe"],

        [True, False, True, False, False, False, False, True, False, False, False, True, True, False, False, False, False, False, False, False, True, False, False, False, False, True, "Eric"],

        [False, True, False, False, False, False, True, False, True, False, False, True, False, True, False, False, False, False, False, False, False, False, True, False, False, True, "Emma"],

        [False, True, False, False, False, True, False, True, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, True, False, True, "Carmen"],

        [True, False, False, False, False, False, True, False, True, True, False, True, False, False, True, False, False, False, True, True, False, True, False, False, False, True, "Daniel"],

        [False, True, False, True, False, False, False, False, True, False, False, False, False, False, False, False, True, True, False, False, True, False, False, False, True, False, "Rachel"],

        [False, True, False, False, True, False, False, False, True, False, False, False, False, False, True, True, False, False, False, False, True, False, False, False, False, True, "Caity"]
        ]

        # Define a dictionary mapping feature names to their index in the characterFeatures list
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
        "green": 21,
        "eyes brown": 22,
        "brown eyes": 22,
        "teeth": 23,
        "left": 24,
        "right": 25,
        "name": 26
        }

        # Human-readable feature list (optional usage)
        self.features = [
            'male',          # 0
            'female',        # 1
            'black hair',    # 2
            'brown hair',    # 3
            'hair blonde',   # 4
            'white hair',    # 5
            'orange hair',   # 6
            'short hair',    # 7
            'hair long',     # 8
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
            'green',         # 21
            'eyes brown',    # 22
            'teeth',         # 23
            'left',          # 24
            'right',         # 25
            'name'           # 26
        ]

        # List of character names
        self.name = ["Amy", "Al", "Sam", "Sofia", "Olivia", "Mike", "David", "Farah", "Ben", "Jordan", "Laura", "Leo", "Liz", "Mia", "Nick", "Lily", "Joe", "Gabe", "Eric", "Emma", "Carmen", "Daniel", "Rachel", "Katie"]

    def onLoad(self):
        #put initialization code here
        pass

    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self, p):
        # This method is called when the input is triggered
        userResponse = p # Read the input parameter
        # Depending on the user's "yes" or "no" answer, eliminate characters
        if userResponse.toUpper() == "YES":
            self.elim(
        # (Incomplete - would call self.elim() differently for NO)
        elif userResponse.toUpper() == "NO":
        
        pass

    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box

    def elim(self, feat, ans):
        # Eliminate characters based on feature `feat` and answer `ans`
        self.logger.info(feat)  # Log the feature being evaluated

        # Get the feature index based on the string (e.g., "black hair" → 2)
        feat_idx = self.featureToInt[feat]

        # Loop through all characters
        for i, person in enumerate(self.characterFeatures):
            if person[feat_idx] != ans:
                # If the character's feature does not match the answer, eliminate
                self.memory.removeData(self.name[i])  # Remove old data for the character
                self.memory.insertData(self.name[i], 0)  # Set character's state to eliminated (0)
                
                # Log which character was eliminated
                self.logger.info(str(self.name[i]) + " " + str(self.memory.getData(self.name[i])))

                # (Old code you commented out about gState row/column updating)
                # row = i // 8  # Would calculate grid row
                # col = i % 8   # Would calculate grid column
                # gState[row][col] = "0"
