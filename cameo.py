import cv2
from manager import CaptureManager,WindowManager

class Cameo(object):
    def __init__(self) -> None:
        self._windowManager = WindowManager('Cameo',self.onKeyPress)
        self._captureManager = CaptureManager(cv2.VideoCapture(0),self._windowManager,True)
    
    def run(self):
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame

            self._captureManager.exitFrame()
            self._windowManager.processEvents()

    def onKeyPress(self,keycode):
        if keycode == 27:
            self._windowManager.destroyWindow()
        elif keycode == 32:
            self._captureManager.writeImage("screenshoot.png")
        elif keycode == 9:
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo("video.mp4")
        elif keycode == ord('s'):
            self._captureManager.stopWritingVideo()

if __name__=="__main__":
    Cameo().run()