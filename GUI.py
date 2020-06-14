import pyautogui
import threading
import time
import random
import copy

_GUILocker=threading.Lock()
#_isGUILockerAcquired=False

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

        _GUILocker.acquire()
#
    def GUIRelease(self):
        global _GUILocker

        _GUILocker.release()
#
    def updateOperationTime(self):
        self.GUIAcquire()

        self.__lastOperationTime=time.time()

        self.GUIRelease()
#
    def click(self):
        self.GUIAcquire()

        pyautogui.click()
        #self.__lastOperationTime=time.time()

        self.GUIRelease()
#
    def genPositionOffsets(self,position):
        offsetWidth=round(random.uniform(-1,1)*position.width/2,4)
        offsetHeight=round(random.uniform(-1,1)*position.height/2,4)

        return offsetWidth,offsetHeight
#
    def setMouseToRandomPosition(self,offsetX=0,offsetY=0,rangeX=0.4,rangeY=0.4,duration=0.2):
        self.GUIAcquire()

        pyautogui.moveTo(offsetX+self.__startX+random.uniform(0.0,rangeX)*self.__windowWidth,
                offsetY+self.__startY+random.uniform(0.0,rangeY)*self.__windowHeight,
                duration,
                pyautogui.easeInOutQuad)

        self.GUIRelease()
#
    def clickRandomPosition(self,duration=0.2):
        self.GUIAcquire()

        pyautogui.moveTo(self.__startX+random.uniform(0.3,0.7)*self.__windowWidth,
            self.__startY+random.uniform(0.4,0.7)*self.__windowHeight,
            duration,
            pyautogui.easeInOutQuad)
        pyautogui.click()
        #self.__lastOperationTime=time.time()

        self.GUIRelease()
#
    def clickCoordinate(self,x,y,clicks=1,duration=0.2):
        self.GUIAcquire()

        pyautogui.moveTo(x,y,duration,pyautogui.easeInOutQuad)
        pyautogui.click(x,y,clicks,random.uniform(0.1,1))
        #self.__lastOperationTime=time.time()

        self.GUIRelease()
#
    def clickImageWithOffsets(self,imagePath,clicks=1,duration=0.2,offsetX=0,offsetY=0,accuracy=0.9):
        ret=False

        self.GUIAcquire()

        position=pyautogui.locateOnScreen(imagePath,
                    region=(self.__startX,self.__startY,self.__windowWidth,self.__windowHeight),
                    confidence=accuracy)
        if position:
            x,y=pyautogui.center(position)
            offsetWidth,offsetHeight=self.genPositionOffsets(position)
            pyautogui.moveTo(x+offsetWidth+offsetX,y+offsetHeight+offsetY,duration,pyautogui.easeInOutQuad)
            pyautogui.click(x+offsetWidth+offsetX,y+offsetHeight+offsetY,clicks,random.uniform(0.1,1))
            #self.__lastOperationTime=time.time()
            ret=True
        else:
            ret=False

        self.GUIRelease()

        return ret
#
    def clickPositionWithOffsets(self,position,clicks=1,duration=0.2,offsetX=0,offsetY=0,accuracy=0.9):
        ret=False

        self.GUIAcquire()

        if position:
            x,y=pyautogui.center(position)
            offsetWidth,offsetHeight=self.genPositionOffsets(position)
            pyautogui.moveTo(x+offsetWidth+offsetX,y+offsetHeight+offsetY,duration,pyautogui.easeInOutQuad)
            pyautogui.click(x+offsetWidth+offsetX,y+offsetHeight+offsetY,clicks,random.uniform(0.1,1))
            #self.__lastOperationTime=time.time()
            ret=True
        else:
            ret=False

        self.GUIRelease()

        return ret
#
    def moveToImage(self,imagePath,duration=0.1,accuracy=0.9):
        ret=False

        self.GUIAcquire()

        position=pyautogui.locateOnScreen(imagePath,
                    region=(self.__startX,self.__startY,self.__windowWidth,self.__windowHeight),
                    confidence=accuracy)
        if position:
            x,y=pyautogui.center(position)
            pyautogui.moveTo(x,y,duration,pyautogui.easeInOutQuad)
            ret=True
        else:
            ret=False

        self.GUIRelease()

        return ret
#
    def moveToCenter(self,duration=0.1):
        self.GUIAcquire()

        pyautogui.moveTo(self.__startX+self.__windowWidth/2,
            self.__startY+self.__windowHeight/2,
            duration,
            pyautogui.easeInOutQuad)

        self.GUIRelease()
#
    def moveTo(self,x,y,duration=0.1):
        self.GUIAcquire()

        pyautogui.moveTo(self.__startX+x,
            self.__startY+y,
            duration,
            pyautogui.easeInOutQuad)
        
        self.GUIRelease()
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

        self.GUIAcquire()

        pyautogui.mouseDown()
        time.sleep(interval)
        pyautogui.move(moveX,moveY,duration,pyautogui.easeInOutQuad)
        time.sleep(interval)
        pyautogui.mouseUp()
        #self.__lastOperationTime=time.time()

        self.GUIRelease()
#
    def dragMouseTo(self,x,y,duration=0.1,interval=0.0):
        self.GUIAcquire()

        pyautogui.mouseDown()
        time.sleep(interval)
        pyautogui.moveTo(x,y,duration,pyautogui.easeInOutQuad)
        time.sleep(interval)
        pyautogui.mouseUp()
        #self.__lastOperationTime=time.time()
        
        self.GUIRelease()
#
    def scroll(self,clicks):
        self.GUIAcquire()

        pyautogui.scroll(clicks)
        #self.__lastOperationTime=time.time()
        
        self.GUIRelease()
#
    def isImageDetected(self,imagePath,accuracy=0.9):
        if (pyautogui.locateOnScreen(imagePath,
                region=(self.__startX,self.__startY,self.__windowWidth,self.__windowHeight),
                confidence=accuracy))==None:
            return False
        else:
            return True