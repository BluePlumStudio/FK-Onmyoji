'''
Project:FK-Onmyoji-Renew

Powered By BluePlum Studio:lzycc234
https://github.com/BluePlumStudio/FK-Onmyoji
'''

import winsound

from Util import *
from Account import *

accounts=[]

def main():
    winsound.Beep(500,100)
    printWithTime("警告:请务必使用'管理员权限'运行!")
    accountCount=int(inputWithTimePrompt("账户数:"))
    while accountCount:
        accountCount-=1

        gameMode=int(inputWithTimePrompt("游戏类型:\n(0.实时活动 1.多人御魂/觉醒 2.章节探索 3.单人御魂/业原火/御灵 4.结界突破 5.道馆 6.妖气封印 7.邀请寮成员 8.阴阳寮突破 9.结界卡合成 10.百鬼夜行):"))
        count=int(inputWithTimePrompt("局数:"))
        startX=int(inputWithTimePrompt("窗口起始位置X:"))
        startY=int(inputWithTimePrompt("窗口起始位置Y:"))
        windowWidth=int(inputWithTimePrompt("窗口宽度:"))
        windowHeight=int(inputWithTimePrompt("窗口高度:"))
        isCaptainChar=inputWithTimePrompt("是否为房主(Y/N):")
        feedbackerName=inputWithTimePrompt("QQ反馈者名称:")
        isCaptain=False
        if isCaptainChar=='y' or isCaptainChar=="Y":
            isCaptain=True
        else:
            isCaptain=False
        
        accounts.append(Account(gameMode,count,startX,startY,windowWidth,windowHeight,isCaptain,feedbackerName))
    
    for account in accounts:
        account.start()

    #threading.Thread(None,detectOccupation).start()
    #threading.Thread(None,detectPause).start()

    #printWithTime("over")

main()
'''
im1 = pyautogui.screenshot()
print(pyautogui.locate(IMAGE_MITAMA_START_PATH,im1,confidence=0.9))
'''