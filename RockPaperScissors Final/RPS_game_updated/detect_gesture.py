from naoqi import ALProxy
import os
import time

#creates the class for the Choregraphe block
class MyClass(GeneratedClass):
    #initializes the block
    def __init__(self):
        GeneratedClass.__init__(self)
    #code to run in the block during runtime of the program
    def onLoad(self):
        #skips this block
        pass
    #an unload function to clean up the block
    def onUnload(self):
        #skips this block
        pass
    #function that is called when the block receives an input, takes an int
    def onInput_onStart(self, number):
        #prints a message to the terminal showing the block has been called
        self.logger.info("Reading gesture_result.txt...")
        #sets a variable equal to the input received by the function
        roboGesture = number
        #waits three seconds
        time.sleep(3)
        #start of the try block
        try:
            #gets the path of the gesture files
            gesture_file = "/home/nao/gesture_result.txt"

            # Check if the file exists
            if os.path.exists(gesture_file):
                #opens the file if it exists
                with open(gesture_file, "r") as f:
                    #reads the text from the file and strips and blank space
                    gesture = f.read().strip()
                #prints the text taken from the gesture file to the terminal
                self.logger.info("Gesture read: '{}'".format(gesture))

                # Trigger the appropriate output
                if gesture == "rock":
                    #prints that the user gesture was rock
                    self.logger.info("Gesture is ROCK")
                    #prints that the robot threw scissors and outputs an int that corresponds to the outcome of the game.
                    if roboGesture == 1:
                        self.logger.info("Robot threw scissors")
                        self.onStopped(1)
                    #prints that the robot threw paper and outputs an int that corresponds to the outcome of the game
                    elif roboGesture == 2:
                        self.logger.info("Robot threw paper")
                        self.onStopped(2)
                    #prints that the robot threw rock and outputs and int that corresponds to the outcome of the game
                    elif roboGesture == 3:
                        self.logger.info("Robot threw rock")
                        self.onStopped(3)
                #code for if the user threw paper
                elif gesture == "paper":
                    #prints that the user gesture was paper
                    self.logger.info("Gesture is PAPER")
                    #prints that the robot threw scissors and outputs an int that corresponds to the outcome of the game
                    if roboGesture == 1:
                        self.logger.info("Robot threw scissors")
                        self.onStopped(2)
                    #prints that the robot threw paper and outputs an int that corresponds to the outcome of the game
                    elif roboGesture == 2:
                        self.logger.info("Robot threw paper")
                        self.onStopped(3)
                    #prints that the robot threw rock and outputs an int that corresponds to the outcome of the game
                    elif roboGesture == 3:
                        self.logger.info("Robot threw rock")
                        self.onStopped(1)
                #code for if the user threw scissors
                elif gesture == "scissors":
                    #prints that the user threw scissors
                    self.logger.info("Gesture is SCISSORS")
                    #prints that the robot threw scissors and outputs an int that corresponds to the outcome of the game
                    if roboGesture == 1:
                        self.logger.info("Robot threw scissors")
                        self.onStopped(3)
                    #prints that the robot threw paper and outputs an int that corresponds to the outcome of the game
                    elif roboGesture == 2:
                        self.logger.info("Robot threw paper")
                        self.onStopped(1)
                    #prints that the robot threw rock and outputs an int that corresponds to the outcome of the game
                    elif roboGesture == 3:
                        self.logger.info("Robot threw rock")
                        self.onStopped(2)
                    #self.scissors()
                #else statement in case the text in the file was not one of the three gestures
                else:
                    #prints that contents of the gesture file
                    self.logger.warning("⚠️ Unrecognized gesture: '{}'".format(gesture))
                    #outputs an int showing that the program errored
                    self.onStopped(4)
            #else for if the file could not be read
            else:
                #throws a warning in the terminal
                self.logger.warning("gesture_result.txt not found.")       
        #code to catch an exception 
        except Exception as e:
            #prints the error caught to the terminal
            self.logger.error("Error reading gesture: " + str(e))
            #outputs an int to show that the program errored
            self.onStopped(4)
        #prints to the terminal that the whole program ran
        self.logger.info("Gesture reader completed.")
