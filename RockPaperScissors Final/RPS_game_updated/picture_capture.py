import os
import sys
import time
from naoqi import ALProxy

class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)

    def onLoad(self):
        try:
            self.photoCaptureProxy = ALProxy("ALPhotoCapture")
        except Exception, e:
            self.photoCaptureProxy = None
            self.logger.error(e)

    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self, number):
        roboGesture = number
        NAO_IMAGE_PATH = "/home/nao/recordings/cameras/"
        self.photoCaptureProxy.setPictureFormat("jpg")
        rpsImage = self.photoCaptureProxy.takePicture(NAO_IMAGE_PATH, "gesture")
        self.onStopped(roboGesture) #activate the output of the box


    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
