import pyautogui
import threading
import time
import random
import copy

_GUILocker=threading.Lock()
_isGUILockerAcquired=False

class GUI(object):
    def __init__(self,startX,startY,windowWidth,windowHeight):
        self.__startX=startX
        self.__startY=startY
        self.__windowWidth=windowWidth
        self.__windowHeight=windowHeight
        self.__lastOperationTime=time.time()
#
    def GUIAcquire(self):
        global _GUILocker
        global _isGUILockerAcquired

        _GUILocker.acquire()
        _isGUILockerAcquired=True
#
    def GUIRelease(self):
        global _GUILocker
        global _isGUILockerAcquired

        _GUILocker.release()
        _isGUILockerAcquired=False
#
    def GUIIsAcquired(self):
        global _GUILocker
        global _isGUILockerAcquired

        return _isGUILockerAcquired
#
    def GUITryToAcquire(self):
        global _GUILocker
        global _isGUILockerAcquired

        if _isGUILockerAcquired:
            return False
        else:
            self.GUIAcquire()
            return True
#
    def updateOperationTime(self):
        _GUILocker.acquire()

        self.__lastOperationTime=time.time()

        _GUILocker.release()
#
    def click(self):
        _GUILocker.acquire()

        pyautogui.click()
        self.__lastOperationTime=time.time()

        _GUILocker.release()
#
    def genPositionOffsets(self,position):
        offsetWidth=round(random.uniform(-1,1)*position.width/2,4)
        offsetHeight=round(random.uniform(-1,1)*position.height/2,4)

        return offsetWidth,offsetHeight
#
    def setMouseToRandomPosition(self,duration=0.2):
        _GUILocker.acquire()

        pyautogui.moveTo(self.__startX+random.uniform(0.3,0.7)*self.__windowWidth,
                self.__startY+random.uniform(0.3,0.7)*self.__windowHeight+30,
                duration,
                pyautogui.easeInOutQuad)

        _GUILocker.release()
#
    def clickRandomPosition(self,duration=0.2):
        _GUILocker.acquire()

        pyautogui.moveTo(self.__startX+random.uniform(0.3,0.7)*self.__windowWidth,
            self.__startY+random.uniform(0.4,0.7)*self.__windowHeight,
            duration,
            pyautogui.easeInOutQuad)
        pyautogui.click()
        self.__lastOperationTime=time.time()

        _GUILocker.release()
#
    def clickCoordinate(self,x,y,clicks=1,duration=0.2):
        _GUILocker.acquire()

        pyautogui.moveTo(x,y,duration,pyautogui.easeInOutQuad)
        pyautogui.click(x,y,clicks,random.uniform(0.1,1))
        self.__lastOperationTime=time.time()

        _GUILocker.release()
#
    def clickImageWithOffsets(self,imagePath,clicks=1,duration=0.2,offsetX=0,offsetY=0,accuracy=0.9):
        ret=False

        _GUILocker.acquire()

        position=pyautogui.locateOnScreen(imagePath,
                    region=(self.__startX,self.__startY,self.__windowWidth,self.__windowHeight),
                    confidence=accuracy)
        if position:
            x,y=pyautogui.center(position)
            offsetWidth,offsetHeight=self.genPositionOffsets(position)
            pyautogui.moveTo(x+offsetWidth+offsetX,y+offsetHeight+offsetY,duration,pyautogui.easeInOutQuad)
            pyautogui.click(x+offsetWidth+offsetX,y+offsetHeight+offsetY,clicks,random.uniform(0.1,1))
            self.__lastOperationTime=time.time()
            ret=True
        else:
            ret=False

        _GUILocker.release()

        return ret
#
    def clickPositionWithOffsets(self,position,clicks=1,duration=0.2,offsetX=0,offsetY=0,accuracy=0.9):
        ret=False

        _GUILocker.acquire()

        if position:
            x,y=pyautogui.center(position)
            offsetWidth,offsetHeight=self.genPositionOffsets(position)
            pyautogui.moveTo(x+offsetWidth+offsetX,y+offsetHeight+offsetY,duration,pyautogui.easeInOutQuad)
            pyautogui.click(x+offsetWidth+offsetX,y+offsetHeight+offsetY,clicks,random.uniform(0.1,1))
            self.__lastOperationTime=time.time()
            ret=True
        else:
            ret=False

        _GUILocker.release()

        return ret
#
    def moveToImage(self,imagePath,duration=0.1,accuracy=0.9):
        ret=False

        _GUILocker.acquire()

        position=pyautogui.locateOnScreen(imagePath,
                    region=(self.__startX,self.__startY,self.__windowWidth,self.__windowHeight),
                    confidence=accuracy)
        if position:
            x,y=pyautogui.center(position)
            pyautogui.moveTo(x,y,duration,pyautogui.easeInOutQuad)
            ret=True
        else:
            ret=False

        _GUILocker.release()

        return ret
#
    def moveToCenter(self,duration=0.1):
        pyautogui.moveTo(self.__startX+self.__windowWidth/2,
            self.__startY+self.__windowHeight/2,
            duration,
            pyautogui.easeInOutQuad)
###
    def getScreenshot(self,imagePath=None):
        return pyautogui.screenshot(imagePath,region=(self.__startX,self.__startY,self.__windowWidth,self.__windowHeight))
#
    def getImagePosition(self,imagePath,accuracy=0.9):
        return pyautogui.locateOnScreen(imagePath,
                    region=(self.__startX,self.__startY,self.__windowWidth,self.__windowHeight),
                    confidence=accuracy)
#
    def getImagePositionInScreenshot(self,imagePath,screenshot,accuracy=0.9):
        return pyautogui.locate(imagePath,screenshot,confidence=accuracy)
#
    def dragMouseToRandomPosition(self,directionX,directionY,duration=0.2,interval=0.0):        
        moveX=round(directionX*random.uniform(0.3,0.6)*self.__windowWidth,4)
        moveY=round(directionY*random.uniform(0.3,0.6)*self.__windowHeight,4)

        _GUILocker.acquire()

        pyautogui.mouseDown()
        time.sleep(interval)
        pyautogui.move(moveX,moveY,duration,pyautogui.easeInOutQuad)
        time.sleep(interval)
        pyautogui.mouseUp()
        self.__lastOperationTime=time.time()

        _GUILocker.release()
#
    def dragMouseTo(self,x,y,duration=0.1,interval=0.0):
        _GUILocker.acquire()

        pyautogui.mouseDown()
        time.sleep(interval)
        pyautogui.moveTo(x,y,duration,pyautogui.easeInOutQuad)
        time.sleep(interval)
        pyautogui.mouseUp()
        self.__lastOperationTime=time.time()
        
        _GUILocker.release()
#
    def scroll(self,clicks):
        _GUILocker.acquire()

        pyautogui.scroll(clicks)
        self.__lastOperationTime=time.time()
        
        _GUILocker.release()
#
    def isImageDetected(self,imagePath,accuracy=0.9):
        if (pyautogui.locateOnScreen(imagePath,
                region=(self.__startX,self.__startY,self.__windowWidth,self.__windowHeight),
                confidence=accuracy))==None:
            return False
        else:
            return True