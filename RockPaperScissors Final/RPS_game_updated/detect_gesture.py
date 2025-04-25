from naoqi import ALProxy
import os
import time

class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)

    def onLoad(self):
        pass

    def onUnload(self):
        pass

    def onInput_onStart(self, number):
        self.logger.info("Reading gesture_result.txt...")
        roboGesture = number
        time.sleep(3)
        try:
            gesture_file = "/home/nao/gesture_result.txt"

            # Check if the file exists
            if os.path.exists(gesture_file):
                with open(gesture_file, "r") as f:
                    gesture = f.read().strip()

                self.logger.info("Gesture read: '{}'".format(gesture))

                # Trigger the appropriate output
                if gesture == "rock":
                    self.logger.info("Gesture is ROCK")
                    if roboGesture == 1:
                        self.logger.info("Robot threw scissors")
                        self.onStopped(1)
                    elif roboGesture == 2:
                        self.logger.info("Robot threw paper")
                        self.onStopped(2)
                    elif roboGesture == 3:
                        self.logger.info("Robot threw rock")
                        self.onStopped(3)
                    #self.rock()
                elif gesture == "paper":
                    self.logger.info("Gesture is PAPER")
                    if roboGesture == 1:
                        self.logger.info("Robot threw scissors")
                        self.onStopped(2)
                    elif roboGesture == 2:
                        self.logger.info("Robot threw paper")
                        self.onStopped(3)
                    elif roboGesture == 3:
                        self.logger.info("Robot threw rock")
                        self.onStopped(1)
                    #self.paper()
                elif gesture == "scissors":
                    self.logger.info("Gesture is SCISSORS")
                    if roboGesture == 1:
                        self.logger.info("Robot threw scissors")
                        self.onStopped(3)
                    elif roboGesture == 2:
                        self.logger.info("Robot threw paper")
                        self.onStopped(1)
                    elif roboGesture == 3:
                        self.logger.info("Robot threw rock")
                        self.onStopped(2)
                    #self.scissors()
                else:
                    self.logger.warning("⚠️ Unrecognized gesture: '{}'".format(gesture))
                    #self.error()
                    self.onStopped(4)
            else:
                self.logger.warning("gesture_result.txt not found.")
                #self.error()

        except Exception as e:
            self.logger.error("Error reading gesture: " + str(e))
            #self.error()
            self.onStopped(4)

        self.logger.info("Gesture reader completed.")
