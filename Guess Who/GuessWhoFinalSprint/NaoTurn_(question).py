# Define the main class for the behavior box
class MyClass(GeneratedClass):
    def __init__(self):
        # Initialize the base GeneratedClass
        GeneratedClass.__init__(self)
        
        # Define the question bank:
        # Each item is a list: [question string, whether it was asked (0 = not asked), feature keyword]
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
        # Insert the full question bank into ALMemory at load time (so it can be shared across boxes if needed)
        self.memory.insertListData(self.question_bank)
        pass

    def onUnload(self):
        # Clean-up logic if needed (not used here, but structure is required)
        pass

    def onInput_onStart(self):
        # Called when this box is triggered
        
        # Initialize a flag to track if a question has been asked
        questionAsked = False
        
        # Loop until a valid question is asked
        while questionAsked == False:
            # Randomly pick an index from 0 to 25
            index = random.randint(0, 25)
            
            # Check if this question has NOT already been asked (status 0)
            if self.getData(self.question_bank[index][1]) != 1:
                question = self.question_bank[index]  # Get the selected question

                # Insert the selected question into ALMemory under "questionAsked"
                self.memeory.insertData("questionAsked", question[0])

                # Remove old data (if needed) to reset before inserting
                self.memory.removeData(question[0])

                # Mark the question as asked by setting it to 1
                self.memory.insertData(question[0], 1)

                # Stop this box and output the selected question string
                self.onStopped(str(question[0]))

                # Mark that a question has been successfully asked
                questionAsked = True
        
        pass  # End of onStart

    def onInput_onStop(self):
        # Standard procedure to call clean-up and stop the box
        self.onUnload()
        self.onStopped()
