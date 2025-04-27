import os
import sys
import time
from naoqi import ALProxy
#Creates the class to run the Choregraphe block
class MyClass(GeneratedClass):
    #initializes the class
    def __init__(self):
        GeneratedClass.__init__(self)
    #code to run in the block during runtime of the program
    def onLoad(self):
        #start of the try block
        try:
            #assign a variable to the ALPhotoCapture library
            self.photoCaptureProxy = ALProxy("ALPhotoCapture")
        #start of the except block
        except Exception, e:
            #set the photo capture vairable to none
            self.photoCaptureProxy = None
            #print the error in the terminal
            self.logger.error(e)
    #function to run when the block unloads
    def onUnload(self):
        #put clean-up code here
        #skips this block
        pass
    #function to run when the block is activated, takes in an integer
    def onInput_onStart(self, number):
        #sets a variable equal to the integer the function took in
        roboGesture = number
        #sets the path for the taken image to be saved to
        NAO_IMAGE_PATH = "/home/nao/recordings/cameras/"
        #sets the format of the photo to be taken
        self.photoCaptureProxy.setPictureFormat("jpg")
        #takes the image and saves it to the set path under the name "gesutre"
        rpsImage = self.photoCaptureProxy.takePicture(NAO_IMAGE_PATH, "gesture")
        #calls the output of the block and outputs the variable it first received
        self.onStopped(roboGesture) #activate the output of the box

    #function to run when the block outputs
    def onInput_onStop(self):
        #calls the unload function to run any clean up code
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
