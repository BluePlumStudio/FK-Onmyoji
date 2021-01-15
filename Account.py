import threading
import keyboard
import win32gui
import win32con
import win32clipboard
import os

from Util import *
from Config import *
from GUI import *

screenWidth,screenHeight=pyautogui.size()

IMAGE_ACTIVITY_FULL_PATH="./screenshots/activity/full.png"
IMAGE_ACTIVITY_START_PATH="./screenshots/activity/start.png"
IMAGE_ACTIVITY_START_2_PATH="./screenshots/activity/start2.png"
IMAGE_ACTIVITY_START_3_PATH="./screenshots/activity/start3.png"
IMAGE_ACTIVITY_FINISHED_1_PATH="./screenshots/activity/finished1.png"
IMAGE_ACTIVITY_FINISHED_2_PATH="./screenshots/activity/finished2.png"
IMAGE_ACTIVITY_FAILED_PATH="./screenshots/activity/failed.png"
IMAGE_ACTIVITY_CLOSE_PATH="./screenshots/activity/close.png"

IMAGE_FAILED_PATH="./screenshots/failed.png"
IMAGE_SCREENSHOT_PATH="./screenshots/screenshot.png"
IMAGE_CONNECTING_PATH="./screenshots/connecting.png"
IMAGE_ASSISTANCE_PATH="./screenshots/assistance.png"
IMAGE_ASSISTANCE_2_PATH="./screenshots/assistance2.png"
IMAGE_ASSISTANCE_3_PATH="./screenshots/assistance3.png"
IMAGE_ASSISTANCE_4_PATH="./screenshots/assistance4.png"
IMAGE_ACCEPT_PATH="./screenshots/accept.png"
IMAGE_OCCUPIED_PATH="./screenshots/occupied.png"
IMAGE_FOOD_INSUFFICIENCY_PATH="./screenshots/food.png"
IMAGE_CLOSE_DIALOG_PATH="./screenshots/close.png"
IMAGE_DISCONNECTED_PATH="./screenshots/disconnected.png"

IMAGE_MITAMA_INVITE_PATH="./screenshots/Mitama/teamInvite.png"
IMAGE_MITAMA_START_PATH="./screenshots/Mitama/start.png"
IMAGE_MITAMA_FINISHED1_PATH="./screenshots/Mitama/finished1.png"
IMAGE_MITAMA_FINISHED2_PATH="./screenshots/Mitama/finished2.png"
IMAGE_MITAMA_CONFIRM_PATH="./screenshots/Mitama/confirm.png"
IMAGE_MITAMA_CONFIRM2_PATH="./screenshots/Mitama/confirm2.png"
IMAGE_MITAMA_RADIO_PATH="./screenshots/Mitama/radio.png"
IMAGE_MITAMA_RADIO_SELECTED_PATH="./screenshots/Mitama/radioSelected.png"
IMAGE_MITAMA_ACCEPT_PATH="./screenshots/Mitama/accept.png"
IMAGE_MITAMA_FULL_WARNING_PATH="./screenshots/Mitama/fullWarning.png"
IMAGE_MITAMA_FULL_CONFIRM_PATH="./screenshots/Mitama/fullConfirm.png"

IMAGE_STROY_INVITE_PATH="./screenshots/Story/invite.png"
IMAGE_STROY_INVITATION_CONFIRMED_PATH="./screenshots/Story/invitationConfirmed.png"
IMAGE_STROY_START_PATH="./screenshots/Story/start.png"
IMAGE_STROY_EXPLORE_PATH="./screenshots/Story/explore.png"
IMAGE_STROY_FIGHT_PATH="./screenshots/Story/fight.png"
IMAGE_STROY_FIGHT_BOSS_PATH="./screenshots/Story/fightBoss.png"
IMAGE_STROY_FINISHED1_PATH="./screenshots/Story/finished1.png"
IMAGE_STROY_FINISHED2_PATH="./screenshots/Story/finished2.png"
IMAGE_STROY_ACCEPT_PATH="./screenshots/Story/accept.png"
IMAGE_STROY_BACK_PATH="./screenshots/Story/back.png"
IMAGE_STROY_GET_REWARD_PATH="./screenshots/Story/getReward.png"
IMAGE_STROY_REWARD_CONFIRMED_PATH="./screenshots/Story/rewardConfirmed.png"
IMAGE_STROY_READY_PATH="./screenshots/Story/ready.png"
IMAGE_STROY_READY_MARK_PATH="./screenshots/Story/readyMark.png"
IMAGE_STROY_SELECT_LEVEL_PATH="./screenshots/Story/selectLevel.png"
IMAGE_STROY_FULL1_PATH="./screenshots/Story/full1.png"
IMAGE_STROY_FULL2_PATH="./screenshots/Story/full2.png"
IMAGE_STROY_FOOD_PATH="./screenshots/Story/food.png"
IMAGE_STROY_CHERRY_CAKE_PATH="./screenshots/Story/cherryCake.png"

IMAGE_STROY_SHIKIGAMI_SELECTED_PATH="./screenshots/Story/shikigamiSelected.png"
IMAGE_STROY_SELECTED_LEVEL_PATH="./screenshots/Story/selectedLevel.png"

IMAGE_MITAMA_X_START_PATH="./screenshots/MitamaX/start.png"
IMAGE_MITAMA_X_READY_PATH="./screenshots/MitamaX/ready.png"
IMAGE_MITAMA_X_FINISHED1_PATH="./screenshots/MitamaX/finished1.png"
IMAGE_MITAMA_X_FINISHED2_PATH="./screenshots/MitamaX/finished2.png"

IMAGE_BREACH_START_PATH="./screenshots/Breach/start.png"
IMAGE_BREACH_START_2_PATH="./screenshots/Breach/start2.png"
IMAGE_BREACH_SECTION_PATH="./screenshots/Breach/section.png"
IMAGE_BREACH_SECTION_2_PATH="./screenshots/Breach/section2.png"
IMAGE_BREACH_SECTION_3_PATH="./screenshots/Breach/section3.png"
IMAGE_BREACH_FINISHED1_PATH="./screenshots/Breach/finished1.png"
IMAGE_BREACH_FINISHED2_PATH="./screenshots/Breach/finished2.png"
IMAGE_BREACH_SHIKIGAMI_SELECTED_PATH="./screenshots/Breach/shikigamiSelected.png"
IMAGE_BREACH_SELECTION_MARK_PATH="./screenshots/Breach/selectionMark.png"
IMAGE_BREACH_FAILED_PATH="./screenshots/Breach/failed.png"
IMAGE_BREACH_BREACH_PATH="./screenshots/Breach/breach.png"

IMAGE_CLUB_BATTLE_READY_PATH="./screenshots/TeamBattle/ready.png"
IMAGE_CLUB_BATTLE_FINISHED2_PATH="./screenshots/TeamBattle/finished2.png"

IMAGE_SEAL_TEAM_PATH="./screenshots/Seal/team.png"
IMAGE_SEAL_GIFT_PATH="./screenshots/Seal/gift.png"
IMAGE_SEAL_ACHIEVEMENT_PATH="./screenshots/Seal/achievement.png"
IMAGE_SEAL_BACK_1_PATH="./screenshots/Seal/back1.png"
IMAGE_SEAL_BACK_2_PATH="./screenshots/Seal/back2.png"
IMAGE_SEAL_CLOSE_PATH="./screenshots/Seal/close.png"
IMAGE_SEAL_SEAL_PATH="./screenshots/Seal/seal.png"
IMAGE_SEAL_MATCH_PATH="./screenshots/Seal/match.png"
IMAGE_SEAL_START_PATH="./screenshots/Seal/start.png"
IMAGE_SEAL_READY_PATH="./screenshots/Seal/ready.png"
IMAGE_SEAL_FINISHED1_PATH="./screenshots/Seal/finished1.png"
IMAGE_SEAL_FINISHED2_PATH="./screenshots/Seal/finished2.png"

IMAGE_INVITE_CLUB_MEMBERS_INVITE="./screenshots/InviteClubMembers/invite.png"
IMAGE_INVITE_CLUB_MEMBERS_REFRESH="./screenshots/InviteClubMembers/refresh.png"

IMAGE_CLUB_BREACH_START_PATH="./screenshots/ClubBreach/start.png"
IMAGE_CLUB_BREACH_SECTION_PATH="./screenshots/ClubBreach/section.png"
IMAGE_CLUB_BREACH_FINISHED1_PATH="./screenshots/ClubBreach/finished1.png"
IMAGE_CLUB_BREACH_FINISHED2_PATH="./screenshots/ClubBreach/finished2.png"
IMAGE_CLUB_BREACH_SHIKIGAMI_SELECTED_PATH="./screenshots/ClubBreach/shikigamiSelected.png"
IMAGE_CLUB_BREACH_SELECTION_MARK_PATH="./screenshots/ClubBreach/selectionMark.png"
IMAGE_CLUB_BREACH_BREACH_REPORT_PATH="./screenshots/ClubBreach/breachReport.png"
IMAGE_CLUB_BREACH_FAILED_PATH="./screenshots/ClubBreach/failed.png"
IMAGE_CLUB_BREACH_EMPTY_PATH="./screenshots/ClubBreach/empty.png"
IMAGE_CLUB_BREACH_COMMUNITY_PATH="./screenshots/ClubBreach/community.png"
IMAGE_CLUB_BREACH_BREACH_PATH="./screenshots/ClubBreach/breach.png"
IMAGE_CLUB_BREACH_CLUB_PATH="./screenshots/ClubBreach/club.png"
IMAGE_CLUB_BREACH_CLOSE_PATH="./screenshots/ClubBreach/close.png"
IMAGE_CLUB_BREACH_SCROLL_BAR_PATH="./screenshots/ClubBreach/scrollBar.png"

IMAGE_CARD_SYNTHESIS_CARD_PATH="./screenshots/CardSynthesis/card.png"
IMAGE_CARD_SYNTHESIS_START_PATH="./screenshots/CardSynthesis/start.png"

IMAGE_DEVILS_NIGHT_ENTER_PATH="./screenshots/DevilsNight/enter.png"
IMAGE_DEVILS_NIGHT_SELECTED_PATH="./screenshots/DevilsNight/selected.png"
IMAGE_DEVILS_NIGHT_START_PATH="./screenshots/DevilsNight/start.png"
IMAGE_DEVILS_NIGHT_BULLET_PATH="./screenshots/DevilsNight/bullet.png"
IMAGE_DEVILS_NIGHT_UP_PATH="./screenshots/DevilsNight/up.png"
IMAGE_DEVILS_NIGHT_SHARE_PATH="./screenshots/DevilsNight/share.png"
IMAGE_DEVILS_NIGHT_OVER_PATH="./screenshots/DevilsNight/over.png"
IMAGE_DEVILS_NIGHT_INVITE_PATH="./screenshots/DevilsNight/invite.png"
IMAGE_DEVILS_NIGHT_SECTION_PATH="./screenshots/DevilsNight/section.png"
IMAGE_DEVILS_NIGHT_CLOSE_PATH="./screenshots/DevilsNight/close.png"
#
_localVariable=threading.local()
_DETECTION_INTERVAL=0.2
_GLOBAL_CONFIG_PATH="./config.ini"
_globalConfig=Config(_GLOBAL_CONFIG_PATH)
_accountCount=0
_fullShikigamiCount=0
_isPaused=False

_detectPauseThread=threading.Thread()
_accountLocker=threading.Lock()
_feedbackerLocker=threading.Lock()
#
class Account(threading.Thread):
    def __init__(self,gameMode,total,startX=0,startY=0,windowWidth=screenWidth,windowHeight=screenHeight,isCaptain=False,feedbackerName=None):
        threading.Thread.__init__(self)
        global _globalConfig
        global _accountCount
        global _detectPauseThread
        global _accountLocker

        self.__startX=startX
        self.__startY=startY
        self.__windowWidth=windowWidth
        self.__windowHeight=windowHeight
        self.__gameMode=gameMode
        self.__total=total
        self.__isCaptain=isCaptain
        self.__feedbackerName=feedbackerName

        self.__gui=GUI(startX,startY,windowWidth,windowHeight)
        self.__id=_accountCount
        _accountCount+=1

        if self.__gameMode!=3 and self.__gameMode!=4 and self.__gameMode!=6 and self.__gameMode!=8 and self.__gameMode!=9 and self.__gameMode!=10 and _globalConfig.closeGamesAfterFailure and _globalConfig.exitAfterFailure:
            self._detectFailureThread=threading.Thread(None,self.detectFailure,args=())
            self._detectFailureThread.start()
        self._detectAssistance=threading.Thread(None,self.detectAssistance,args=())
        self._detectAssistance.start()
        self._detectOccupation=threading.Thread(None,self.detectOccupation,args=())
        self._detectOccupation.start()
        self._detectFoodInsufficiency=threading.Thread(None,self.detectFoodInsufficiency,args=())
        self._detectFoodInsufficiency.start()
        self._detectDisconnection=threading.Thread(None,self.detectDisconnection,args=())
        self._detectDisconnection.start()

        _accountLocker.acquire()

        if not _detectPauseThread.isAlive():
            _detectPauseThread=threading.Thread(None,self.detectPause)
            _detectPauseThread.start()

        _accountLocker.release()
#
    @property
    def accountCount(self):
        return _accountCount
#
    def gameModeActivity(self):
        printWithTime("消息:账户:%s:实时活动"%(str(self.__id)))
        while True:
            screenshot = self.__gui.getScreenshot()
            time.sleep(_DETECTION_INTERVAL*10)

            position=self.__gui.getImagePositionInScreenshot(IMAGE_ACTIVITY_FULL_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_ACTIVITY_FULL_PATH,position.left,position.top))
                continue

            position=self.__gui.getImagePositionInScreenshot(IMAGE_ACTIVITY_START_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_ACTIVITY_START_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                time.sleep(_DETECTION_INTERVAL*8)
                continue

            position=self.__gui.getImagePositionInScreenshot(IMAGE_ACTIVITY_START_2_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_ACTIVITY_START_2_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                continue

            position=self.__gui.getImagePositionInScreenshot(IMAGE_ACTIVITY_START_3_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_ACTIVITY_START_3_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                continue

            position=self.__gui.getImagePositionInScreenshot(IMAGE_ACTIVITY_FINISHED_1_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_ACTIVITY_FINISHED_1_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                
                while True:
                    if not self.__gui.clickImageWithOffsets(IMAGE_ACTIVITY_FINISHED_1_PATH,1,0.2):
                        break
                    printWithTime("消息:账户:%s:检测到图像:%s:位置"%(str(self.__id),IMAGE_ACTIVITY_FINISHED_1_PATH))
                break

            position=self.__gui.getImagePositionInScreenshot(IMAGE_ACTIVITY_FINISHED_2_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_ACTIVITY_FINISHED_2_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                
                while True:
                    if not self.__gui.clickImageWithOffsets(IMAGE_ACTIVITY_FINISHED_2_PATH,1,0.2):
                        break
                    printWithTime("消息:账户:%s:检测到图像:%s:位置"%(str(self.__id),IMAGE_ACTIVITY_FINISHED_2_PATH))
                break

            position=self.__gui.getImagePositionInScreenshot(IMAGE_ACTIVITY_FAILED_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_ACTIVITY_FAILED_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                
                while True:
                    if not self.__gui.clickImageWithOffsets(IMAGE_ACTIVITY_FAILED_PATH,1,0.2):
                        break
                    printWithTime("消息:账户:%s:检测到图像:%s:位置"%(str(self.__id),IMAGE_ACTIVITY_FAILED_PATH))
                break

            position=self.__gui.getImagePositionInScreenshot(IMAGE_ACTIVITY_CLOSE_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_ACTIVITY_CLOSE_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                continue

#
    def gameModeMitama(self):
        printWithTime("消息:账户:%s:多人御魂/觉醒"%(str(self.__id)))
        while True:
            screenshot = self.__gui.getScreenshot()
            #time.sleep(_DETECTION_INTERVAL)
            if _localVariable.isFailureDetected:
                position=self.__gui.getImagePositionInScreenshot(IMAGE_MITAMA_CONFIRM2_PATH,screenshot)
                if position != None:
                    if position.left <= self.__windowWidth*0.145:
                        continue
                    printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_MITAMA_CONFIRM2_PATH,position.left,position.top))
                    self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                    
                    while True:
                        if not self.__gui.clickImageWithOffsets(IMAGE_MITAMA_CONFIRM2_PATH,1,0.2):
                            _localVariable.isFailureDetected=False
                            break
                        printWithTime("消息:账户:%s:检测到图像:%s:位置"%(str(self.__id),IMAGE_MITAMA_CONFIRM2_PATH))
                    continue  

                position=self.__gui.getImagePositionInScreenshot(IMAGE_MITAMA_RADIO_PATH,screenshot)
                if position != None:
                    printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_MITAMA_RADIO_PATH,position.left,position.top))
                    self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                    
                    while True:
                        if not self.__gui.clickImageWithOffsets(IMAGE_MITAMA_RADIO_PATH,1,0.2):
                            _localVariable.isFailureDetected=False
                            break
                        printWithTime("消息:账户:%s:检测到图像:%s:位置"%(str(self.__id),IMAGE_MITAMA_RADIO_PATH))
                    continue  

                position=self.__gui.getImagePositionInScreenshot(IMAGE_MITAMA_ACCEPT_PATH,screenshot)
                if position != None:
                    if position.left <= self.__windowWidth*0.08:
                        continue
                    printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_MITAMA_ACCEPT_PATH,position.left,position.top))
                    self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                    continue

            if self.__isCaptain:
                position=self.__gui.getImagePositionInScreenshot(IMAGE_MITAMA_CONFIRM_PATH,screenshot)
                if position != None:
                    time.sleep(1.0)
                    printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_MITAMA_CONFIRM_PATH,position.left,position.top))
                    self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                    continue

                if _globalConfig.isFullTeam:
                    position=self.__gui.getImagePositionInScreenshot(IMAGE_MITAMA_INVITE_PATH,screenshot)
                    if position == None:
                        position=self.__gui.getImagePositionInScreenshot(IMAGE_MITAMA_START_PATH,screenshot)
                        if position != None:
                            printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_MITAMA_START_PATH,position.left,position.top))
                            self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                            continue
                else:
                    position=self.__gui.getImagePositionInScreenshot(IMAGE_MITAMA_START_PATH,screenshot)
                    if position != None:
                        printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_MITAMA_START_PATH,position.left,position.top))
                        self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                        continue
            
            position=self.__gui.getImagePositionInScreenshot(IMAGE_MITAMA_FINISHED1_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_MITAMA_FINISHED1_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,2,0.2,self.__startX,self.__startY)
                continue

            position=self.__gui.getImagePositionInScreenshot(IMAGE_MITAMA_FINISHED2_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_MITAMA_FINISHED2_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                
                while True:
                    if not self.__gui.clickImageWithOffsets(IMAGE_MITAMA_FINISHED2_PATH,1,0.2):
                        break
                    printWithTime("消息:账户:%s:检测到图像:%s:位置"%(str(self.__id),IMAGE_MITAMA_FINISHED2_PATH))
                break  
            
            position=self.__gui.getImagePositionInScreenshot(IMAGE_FAILED_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_FAILED_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                _localVariable.isFailureDetected=True
                if not _globalConfig.closeGamesAfterFailure and not _globalConfig.exitAfterFailure:
                    message="消息:账户:%s:失败，准备重试"%(str(self.__id))
                    printWithTime(message)
                    threading.Thread(None,self.feedback,str(self.__id),args=(message,)).start()
            
            position=self.__gui.getImagePositionInScreenshot(IMAGE_MITAMA_FULL_WARNING_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_MITAMA_FULL_WARNING_PATH,position.left,position.top))
                message="警告:账户:%s:仓库御魂已满"%(str(self.__id))
                printWithTime(message)
                threading.Thread(None,self.feedback,str(self.__id),args=(message,)).start()
                position=self.__gui.getImagePositionInScreenshot(IMAGE_MITAMA_FULL_CONFIRM_PATH,screenshot)
                if position != None:
                    printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_MITAMA_FULL_CONFIRM_PATH,position.left,position.top))
                    self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                continue

#
    def gameModeStory(self):
        global _fullShikigamiCount
        global _isPaused
        printWithTime("消息:账户:%s:章节探索"%(str(self.__id)))

        while True:
            screenshot = self.__gui.getScreenshot()
            time.sleep(_DETECTION_INTERVAL)

            if self.__isCaptain:
                if not self.__gui.getImagePositionInScreenshot(IMAGE_STROY_CHERRY_CAKE_PATH,screenshot):
                    position=self.__gui.getImagePositionInScreenshot(IMAGE_STROY_INVITE_PATH,screenshot)
                    '''
                    if position != None:
                        winsound.Beep(500,1000)
                    '''
                    if position != None:
                        _localVariable.isBossDetected=False
                        printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_STROY_INVITE_PATH,position.left,position.top))
                        self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                        continue

                    position=self.__gui.getImagePositionInScreenshot(IMAGE_STROY_INVITATION_CONFIRMED_PATH,screenshot)
                    if position != None:
                        time.sleep(3.0)
                        _localVariable.isBossDetected=False
                        printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_STROY_INVITATION_CONFIRMED_PATH,position.left,position.top))
                        self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                        continue

                    position=self.__gui.getImagePositionInScreenshot(IMAGE_STROY_START_PATH,screenshot)
                    if position != None:
                        _localVariable.isBossDetected=False
                        printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_STROY_START_PATH,position.left,position.top))
                        self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                        continue

                    position=self.__gui.getImagePositionInScreenshot(IMAGE_STROY_EXPLORE_PATH,screenshot)
                    if position != None:
                        _localVariable.isBossDetected=False
                        printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_STROY_EXPLORE_PATH,position.left,position.top))
                        self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                        continue

                #检测目标
                if not _localVariable.isBossDetected and self.__gui.getImagePositionInScreenshot(IMAGE_STROY_CHERRY_CAKE_PATH,screenshot) and _localVariable.detectCount:
                    _localVariable.detectCount-=1
                    if (not self.__gui.isImageDetected(IMAGE_STROY_FIGHT_PATH)
                        and not self.__gui.isImageDetected(IMAGE_STROY_FIGHT_BOSS_PATH)):
                        self.__gui.setMouseToRandomPosition(self.__windowWidth*0.3,self.__windowHeight*0.3,0.4,0.4)
                        self.__gui.dragMouseToRandomPosition(_localVariable.xDirection,random.uniform(0.01,0.1))
                        printWithTime("账户:%s:第%s次检测:%s"
                                    %(str(self.__id),str(10-_localVariable.detectCount),IMAGE_STROY_FIGHT_PATH))
                        printWithTime("账户:%s:第%s次检测:%s"
                                    %(str(self.__id),str(10-_localVariable.detectCount),IMAGE_STROY_FIGHT_BOSS_PATH))
                        if _localVariable.detectCount==0:
                            _localVariable.detectCount=10
                            _localVariable.xDirection=-_localVariable.xDirection
                            
                position=self.__gui.getImagePositionInScreenshot(IMAGE_STROY_FIGHT_PATH,screenshot)
                if position != None:
                    printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_STROY_FIGHT_PATH,position.left,position.top))
                    self.__gui.clickPositionWithOffsets(position,1,0.101,self.__startX,self.__startY)
                    continue

                position=self.__gui.getImagePositionInScreenshot(IMAGE_STROY_FIGHT_BOSS_PATH,screenshot)
                if position != None:
                    printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_STROY_FIGHT_BOSS_PATH,position.left,position.top))
                    self.__gui.clickPositionWithOffsets(position,1,0.101,self.__startX,self.__startY)
                    _localVariable.isBossDetected=True
                    continue

                position=self.__gui.getImagePositionInScreenshot(IMAGE_STROY_FINISHED1_PATH,screenshot)
                if position != None:
                    printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_STROY_FINISHED1_PATH,position.left,position.top))
                    self.__gui.clickPositionWithOffsets(position,2,0.2,self.__startX,self.__startY)
                    continue

                position=self.__gui.getImagePositionInScreenshot(IMAGE_STROY_FINISHED2_PATH,screenshot)
                if position != None:
                    printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_STROY_FINISHED2_PATH,position.left,position.top))
                    self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                    
                    while True:
                        if not self.__gui.clickImageWithOffsets(IMAGE_STROY_FINISHED2_PATH,1,0.2):
                            break
                        printWithTime("消息:账户:%s:检测到图像:%s:位置"%(str(self.__id),IMAGE_STROY_FINISHED2_PATH))
                    break  
            else:

                if _globalConfig.replaceShikigamiIfFull and self.__gui.isImageDetected(IMAGE_STROY_FULL1_PATH,accuracy=0.7):
                    printWithTime("消息:账户:%s:已完成%d个满经验式神"%(str(self.__id),_fullShikigamiCount))

                    def inner():
                        global _fullShikigamiCount 
                        while not self.__gui.isImageDetected(IMAGE_STROY_READY_MARK_PATH):
                            time.sleep(0.1)
                            continue

                        self.__gui.clickCoordinate(self.__startX+self.__windowWidth/3,self.__startY+self.__windowHeight*2/3,1,0.1)
                        while not self.__gui.isImageDetected(IMAGE_STROY_SELECT_LEVEL_PATH,accuracy=0.5):
                            time.sleep(0.1)
                            self.__gui.clickCoordinate(self.__startX+self.__windowWidth/3,self.__startY+self.__windowHeight*2/3,1,0.1)

                        position=self.__gui.getImagePosition(IMAGE_STROY_SELECT_LEVEL_PATH,accuracy=0.5)
                        while True:
                            if not position:
                                position=self.__gui.getImagePosition(IMAGE_STROY_SELECT_LEVEL_PATH,accuracy=0.5)
                                continue
                            
                            self.__gui.clickPositionWithOffsets(position,1,0.2)
                            if self.__gui.isImageDetected(IMAGE_STROY_SELECTED_LEVEL_PATH,accuracy=0.7):
                                break
                        
                        position=self.__gui.getImagePosition(IMAGE_STROY_SELECTED_LEVEL_PATH,accuracy=0.7)
                        while True:
                            if not position:
                                position=self.__gui.getImagePosition(IMAGE_STROY_SELECTED_LEVEL_PATH,accuracy=0.7)
                                continue          

                            self.__gui.clickPositionWithOffsets(position,1,0.2)    
                            if not self.__gui.isImageDetected(IMAGE_STROY_SELECT_LEVEL_PATH,accuracy=0.5):
                                break      
                        
                        count=0
                        while count<3:
                            count+=1

                            while True:
                                position=self.__gui.getImagePosition(IMAGE_STROY_SHIKIGAMI_SELECTED_PATH)
                                if position:
                                    break
                                #self.__gui.moveToCenter()
                                self.__gui.moveTo(self.__startX+self.__windowWidth/2,self.__startY+self.__windowHeight*4/5,0.11)
                                self.__gui.scroll(-200)
                            
                            self.__gui.moveToImage(IMAGE_STROY_SHIKIGAMI_SELECTED_PATH)
                            
                            position=self.__gui.getImagePosition(IMAGE_STROY_FULL2_PATH,accuracy=0.7)
                            if position:
                                position=self.__gui.dragMouseTo(position.left,position.top+position.height*8,duration=1.0,interval=1.0)

                            positionTmp=self.__gui.getImagePosition(IMAGE_STROY_FULL2_PATH,accuracy=0.7)
                            if position!=positionTmp:
                                printWithTime("消息:账户:%s:已替换1名满经验式神"%(str(self.__id)))
                                _fullShikigamiCount+=1

                            if not self.__gui.isImageDetected(IMAGE_STROY_FULL2_PATH,accuracy=0.7):
                                break
                    
                    innerThread=threading.Thread(None,inner,str(self.__id))
                    innerThread.start()
                    winsound.Beep(1000,3000)
                    seconds=30
                    while seconds and not innerThread.isAlive():
                        time.sleep(1.0)
                        seconds-=1

                    seconds=30
                    while seconds and innerThread.isAlive():
                        printWithTime("消息:账户:%s:等待式神替换结束"%(str(self.__id)))
                        time.sleep(1.0)
                        seconds-=1
                    stopThread(innerThread)
                
                position=self.__gui.getImagePositionInScreenshot(IMAGE_STROY_READY_PATH,screenshot)
                if position != None:
                    printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_STROY_READY_PATH,position.left,position.top))
                    self.__gui.clickPositionWithOffsets(position,2,0.2,self.__startX,self.__startY)
                    continue

                position=self.__gui.getImagePositionInScreenshot(IMAGE_STROY_FINISHED1_PATH,screenshot)
                if position != None:
                    printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_STROY_FINISHED1_PATH,position.left,position.top))
                    self.__gui.clickPositionWithOffsets(position,2,0.2,self.__startX,self.__startY)
                    continue

                position=self.__gui.getImagePositionInScreenshot(IMAGE_STROY_FINISHED2_PATH,screenshot)
                if position != None:
                    printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_STROY_FINISHED2_PATH,position.left,position.top))
                    self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                    
                    while True:
                        if not self.__gui.clickImageWithOffsets(IMAGE_STROY_FINISHED2_PATH,1,0.2):
                            break
                        printWithTime("消息:账户:%s:检测到图像:%s:位置"%(str(self.__id),IMAGE_STROY_FINISHED2_PATH))
                    break  

                position=self.__gui.getImagePositionInScreenshot(IMAGE_STROY_ACCEPT_PATH,screenshot)
                if position != None:
                    if position.left <= self.__windowWidth*0.08:
                        continue
                    message="消息:账户:%s:已尝试接受新一轮章节探索"%(str(self.__id))
                    printWithTime(message)
                    threading.Thread(None,self.feedback,str(self.__id),args=(message,)).start()
                    printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_STROY_ACCEPT_PATH,position.left,position.top))
                    self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                    continue
            #奖励结算
            if (self.__gui.getImagePositionInScreenshot(IMAGE_STROY_BACK_PATH,screenshot) 
                or self.__gui.getImagePositionInScreenshot(IMAGE_STROY_REWARD_CONFIRMED_PATH,screenshot)):
                position=self.__gui.getImagePositionInScreenshot(IMAGE_STROY_GET_REWARD_PATH,screenshot)
                if position != None:
                    printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_STROY_GET_REWARD_PATH,position.left,position.top))
                    self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)

                position=self.__gui.getImagePositionInScreenshot(IMAGE_STROY_REWARD_CONFIRMED_PATH,screenshot)
                if position != None:
                    printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_STROY_REWARD_CONFIRMED_PATH,position.left,position.top))
                    self.__gui.clickCoordinate(self.__startX+self.__windowWidth/4+random.uniform(0.1,1)*self.__windowWidth/20,
                                            self.__startY+self.__windowHeight/8+random.uniform(0.1,1)*self.__windowHeight/20)
#
    def gameModeMitamaX(self):
        printWithTime("消息:账户:%s:单人御魂/业原火/御灵"%(str(self.__id)))
        while True:
            screenshot = self.__gui.getScreenshot()
            time.sleep(_DETECTION_INTERVAL)

            position=self.__gui.getImagePositionInScreenshot(IMAGE_MITAMA_X_START_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_MITAMA_X_START_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                continue

            position=self.__gui.getImagePositionInScreenshot(IMAGE_MITAMA_X_READY_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_MITAMA_X_READY_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                continue
            
            position=self.__gui.getImagePositionInScreenshot(IMAGE_MITAMA_X_FINISHED1_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_MITAMA_X_FINISHED1_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,2,0.2,self.__startX,self.__startY)
                continue

            position=self.__gui.getImagePositionInScreenshot(IMAGE_MITAMA_X_FINISHED2_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_MITAMA_X_FINISHED2_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                
                while True:
                    if not self.__gui.clickImageWithOffsets(IMAGE_MITAMA_X_FINISHED2_PATH,1,0.2):
                        break
                    printWithTime("消息:账户:%s:检测到图像:%s:位置"%(str(self.__id),IMAGE_MITAMA_X_FINISHED2_PATH))
                break 

            position=self.__gui.getImagePositionInScreenshot(IMAGE_FAILED_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_FAILED_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                continue
#
    def gameModeBreach(self):
        printWithTime("消息:账户:%s:结界突破"%(str(self.__id)))
        isShikigamiSelected=False
        while True:
            screenshot = self.__gui.getScreenshot()
            time.sleep(_DETECTION_INTERVAL)

            position=self.__gui.getImagePositionInScreenshot(IMAGE_BREACH_START_PATH,screenshot,0.8)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_BREACH_START_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                continue

            position=self.__gui.getImagePositionInScreenshot(IMAGE_BREACH_START_2_PATH,screenshot,0.8)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_BREACH_START_2_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                continue

            position=self.__gui.getImagePositionInScreenshot(IMAGE_BREACH_SECTION_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_BREACH_SECTION_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                continue
            
            '''
            position=self.__gui.getImagePositionInScreenshot(IMAGE_BREACH_SECTION_2_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_BREACH_SECTION_2_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                position=self.__gui.getImagePositionInScreenshot(IMAGE_BREACH_START_PATH,screenshot,0.8)
                if position != None:
                    printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_BREACH_START_PATH,position.left,position.top))
                    self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                continue

            position=self.__gui.getImagePositionInScreenshot(IMAGE_BREACH_SECTION_3_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_BREACH_SECTION_3_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                position=self.__gui.getImagePositionInScreenshot(IMAGE_BREACH_START_PATH,screenshot,0.8)
                if position != None:
                    printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_BREACH_START_PATH,position.left,position.top))
                    self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                continue
            '''
            ''''''
            '''
            position=self.__gui.getImagePositionInScreenshot(IMAGE_BREACH_SELECTION_MARK_PATH,screenshot)
            if position != None:
                continue
            '''
            ''''''
            position=self.__gui.getImagePositionInScreenshot(IMAGE_BREACH_FINISHED1_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_BREACH_FINISHED1_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,2,0.2,self.__startX,self.__startY)
                continue

            position=self.__gui.getImagePositionInScreenshot(IMAGE_BREACH_FINISHED2_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_BREACH_FINISHED2_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                
                while True:
                    if not self.__gui.clickImageWithOffsets(IMAGE_BREACH_FINISHED2_PATH):
                        isShikigamiSelected=False
                        break
                    printWithTime("消息:账户:%s:检测到图像:%s"%(str(self.__id),IMAGE_BREACH_FINISHED2_PATH))
                break
            
            position=self.__gui.getImagePositionInScreenshot(IMAGE_BREACH_FAILED_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_BREACH_FAILED_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                isShikigamiSelected=False
                continue

            position=self.__gui.getImagePositionInScreenshot(IMAGE_BREACH_BREACH_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_BREACH_BREACH_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                continue

            if isShikigamiSelected:
                continue

            position=self.__gui.getImagePositionInScreenshot(IMAGE_BREACH_SELECTION_MARK_PATH,screenshot)
            if position != None:
                isShikigamiSelected=True
                continue

            position=self.__gui.getImagePositionInScreenshot(IMAGE_BREACH_SHIKIGAMI_SELECTED_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_BREACH_SHIKIGAMI_SELECTED_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                continue
#
    def gameModeTeamBattle(self):
        printWithTime("消息:账户:%s:道馆"%(str(self.__id)))
        while True:
            screenshot = self.__gui.getScreenshot()
            time.sleep(_DETECTION_INTERVAL*4)

            position=self.__gui.getImagePositionInScreenshot(IMAGE_CLUB_BATTLE_READY_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_CLUB_BATTLE_READY_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                time.sleep(_DETECTION_INTERVAL*4)

                while True:
                    if not self.__gui.clickImageWithOffsets(IMAGE_CLUB_BATTLE_READY_PATH):
                        break
                    printWithTime("消息:账户:%s:检测到图像:%s"%(str(self.__id),IMAGE_CLUB_BATTLE_READY_PATH))
                break  
#
    def gameModeSeal(self):
        printWithTime("消息:账户:%s:妖气封印"%(str(self.__id)))
        while True:
            screenshot = self.__gui.getScreenshot()
            time.sleep(_DETECTION_INTERVAL*3)

            position=self.__gui.getImagePositionInScreenshot(IMAGE_FAILED_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:失败，准备重试"%(str(self.__id)))
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_FAILED_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,2,0.2,self.__startX,self.__startY)
                continue

            position=self.__gui.getImagePositionInScreenshot(IMAGE_SEAL_TEAM_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_SEAL_TEAM_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                continue

            position=self.__gui.getImagePositionInScreenshot(IMAGE_SEAL_ACHIEVEMENT_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_SEAL_ACHIEVEMENT_PATH,position.left,position.top))
                position=self.__gui.getImagePositionInScreenshot(IMAGE_SEAL_BACK_2_PATH,screenshot)
                if position != None:
                    printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_SEAL_BACK_2_PATH,position.left,position.top))
                    self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                continue

            position=self.__gui.getImagePositionInScreenshot(IMAGE_SEAL_CLOSE_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_SEAL_CLOSE_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                continue

            position=self.__gui.getImagePositionInScreenshot(IMAGE_SEAL_GIFT_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_SEAL_GIFT_PATH,position.left,position.top))
                position=self.__gui.getImagePositionInScreenshot(IMAGE_SEAL_BACK_1_PATH,screenshot)
                if position != None:
                    printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_SEAL_BACK_1_PATH,position.left,position.top))
                    self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                continue

            position=self.__gui.getImagePositionInScreenshot(IMAGE_SEAL_SEAL_PATH,screenshot)
            if position != None:
                position=self.__gui.getImagePositionInScreenshot(IMAGE_SEAL_MATCH_PATH,screenshot)
                if position != None:
                    printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_SEAL_MATCH_PATH,position.left,position.top))
                    self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                continue

            position=self.__gui.getImagePositionInScreenshot(IMAGE_SEAL_START_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_SEAL_START_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                continue

            position=self.__gui.getImagePositionInScreenshot(IMAGE_SEAL_READY_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_SEAL_READY_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                continue

            position=self.__gui.getImagePositionInScreenshot(IMAGE_SEAL_FINISHED1_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_SEAL_FINISHED1_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,2,0.2,self.__startX,self.__startY)
                continue

            position=self.__gui.getImagePositionInScreenshot(IMAGE_SEAL_FINISHED2_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_SEAL_FINISHED2_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                
                while True:
                    if not self.__gui.clickImageWithOffsets(IMAGE_SEAL_FINISHED2_PATH,1,0.2):
                        break
                    printWithTime("消息:账户:%s:检测到图像:%s:位置"%(str(self.__id),IMAGE_SEAL_FINISHED2_PATH))
                break  
#
    def gameModeInviteClubMembers(self):
        printWithTime("消息:账户:%s:邀请寮成员"%(str(self.__id)))
        while True:
            screenshot = self.__gui.getScreenshot()
            #time.sleep(_DETECTION_INTERVAL*4)

            position=self.__gui.getImagePositionInScreenshot(IMAGE_INVITE_CLUB_MEMBERS_INVITE,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_INVITE_CLUB_MEMBERS_INVITE,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.105,self.__startX,self.__startY)
                continue

            position=self.__gui.getImagePositionInScreenshot(IMAGE_INVITE_CLUB_MEMBERS_REFRESH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_INVITE_CLUB_MEMBERS_REFRESH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.105,self.__startX,self.__startY)
                
                while True:
                    if not self.__gui.clickImageWithOffsets(IMAGE_INVITE_CLUB_MEMBERS_REFRESH,1,0.2):
                        break
                    printWithTime("消息:账户:%s:检测到图像:%s:位置"%(str(self.__id),IMAGE_INVITE_CLUB_MEMBERS_REFRESH))
                break
#
    def gameModeClubBreach(self):
        printWithTime("消息:账户:%s:寮结界突破"%(str(self.__id)))
        isShikigamiSelected=False
        while True:
            screenshot = self.__gui.getScreenshot()
            time.sleep(_DETECTION_INTERVAL*4)

            if _localVariable.isInfoDelayed==True:
                message="消息:账户:%s:寮结界信息滞后，尝试刷新"%(str(self.__id))
                printWithTime(message)
                position=self.__gui.getImagePositionInScreenshot(IMAGE_CLUB_BREACH_CLOSE_PATH,screenshot,0.7)
                _localVariable.isInfoDelayed=False
                _localVariable.startClickCount=0
                if position != None:
                    printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_CLUB_BREACH_CLOSE_PATH,position.left,position.top))
                    self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                    while True:
                        if not self.__gui.clickImageWithOffsets(IMAGE_CLUB_BREACH_CLOSE_PATH,1,0.2):
                            break
                        printWithTime("消息:账户:%s:检测到图像:%s:位置"%(str(self.__id),IMAGE_CLUB_BREACH_CLOSE_PATH))
                    continue
            
            position=self.__gui.getImagePositionInScreenshot(IMAGE_CLUB_BREACH_CLUB_PATH,screenshot,0.95)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_CLUB_BREACH_CLUB_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                continue

            position=self.__gui.getImagePositionInScreenshot(IMAGE_CLUB_BREACH_EMPTY_PATH,screenshot)
            if position != None:
                if not _localVariable.isEmpty:
                    _localVariable.isEmpty=True
                    printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_CLUB_BREACH_EMPTY_PATH,position.left,position.top))
                    message="消息:账户:%s:剩余次数不足，冷却中"%(str(self.__id))
                    printWithTime(message)
                    threading.Thread(None,self.feedback,str(self.__id),args=(message,)).start()
                continue

            position=self.__gui.getImagePositionInScreenshot(IMAGE_CLUB_BREACH_START_PATH,screenshot)
            if position != None:
                _localVariable.isEmpty=False
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_CLUB_BREACH_START_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                _localVariable.startClickCount+=1
                if _localVariable.startClickCount>=10:
                    _localVariable.isInfoDelayed=True
                    _localVariable.startClickCount=0
                continue

            position=self.__gui.getImagePositionInScreenshot(IMAGE_CLUB_BREACH_SECTION_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_CLUB_BREACH_SECTION_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                continue
            ''''''
            position=self.__gui.getImagePositionInScreenshot(IMAGE_CLUB_BREACH_FINISHED1_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_CLUB_BREACH_FINISHED1_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,2,0.2,self.__startX,self.__startY)
                continue

            position=self.__gui.getImagePositionInScreenshot(IMAGE_CLUB_BREACH_FINISHED2_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_CLUB_BREACH_FINISHED2_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                
                while True:
                    if not self.__gui.clickImageWithOffsets(IMAGE_CLUB_BREACH_FINISHED2_PATH):
                        isShikigamiSelected=False
                        break
                    printWithTime("消息:账户:%s:检测到图像:%s"%(str(self.__id),IMAGE_CLUB_BREACH_FINISHED2_PATH))
                break
            ''''''
            position=self.__gui.getImagePositionInScreenshot(IMAGE_CLUB_BREACH_FAILED_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_CLUB_BREACH_FAILED_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                isShikigamiSelected=False
                continue
            '''
            position=self.__gui.getImagePositionInScreenshot(IMAGE_CLUB_BREACH_CLUB_PATH,screenshot,0.95)
            if not position:
                position=self.__gui.getImagePositionInScreenshot(IMAGE_CLUB_BREACH_BREACH_REPORT_PATH,screenshot)
                position2=self.__gui.getImagePositionInScreenshot(IMAGE_CLUB_BREACH_COMMUNITY_PATH,screenshot)
                if position and not position2:
                    self.__gui.setMouseToRandomPosition(self.__windowWidth*0.4,self.__windowHeight*0.4,0.2,0.3)
                    self.__gui.dragMouseToRandomPosition(0.0,random.uniform(-0.01,-0.1))
                    #self.__gui.scroll(-50)
            else:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_CLUB_BREACH_CLUB_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                continue
            '''
            position=self.__gui.getImagePositionInScreenshot(IMAGE_CLUB_BREACH_BREACH_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_CLUB_BREACH_BREACH_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                continue

            if isShikigamiSelected:
                continue

            position=self.__gui.getImagePositionInScreenshot(IMAGE_CLUB_BREACH_SELECTION_MARK_PATH,screenshot)
            if position != None:
                isShikigamiSelected=True
                continue

            position=self.__gui.getImagePositionInScreenshot(IMAGE_CLUB_BREACH_SHIKIGAMI_SELECTED_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_CLUB_BREACH_SHIKIGAMI_SELECTED_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                continue
#
    def gameModeCardSynthesis(self):
        printWithTime("消息:账户:%s:结界卡合成"%(str(self.__id)))
        while True:
            screenshot = self.__gui.getScreenshot()
            #time.sleep(_DETECTION_INTERVAL*4)\
            '''
            position=self.__gui.getImagePositionInScreenshot(IMAGE_CARD_SYNTHESIS_CARD_PATH,screenshot,0.97)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_CARD_SYNTHESIS_CARD_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.15,self.__startX,self.__startY)
                continue
            '''
            self.__gui.clickCoordinate(self.__windowWidth*random.uniform(0.3,0.4),self.__windowHeight*random.uniform(0.35,0.45),1,0.105)
            self.__gui.clickCoordinate(self.__windowWidth*random.uniform(0.3,0.4),self.__windowHeight*random.uniform(0.55,0.65),1,0.105)
            self.__gui.clickCoordinate(self.__windowWidth*random.uniform(0.3,0.4),self.__windowHeight*random.uniform(0.8,0.85),1,0.105)
            position=self.__gui.getImagePositionInScreenshot(IMAGE_CARD_SYNTHESIS_START_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_CARD_SYNTHESIS_START_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.15,self.__startX,self.__startY)
                break
#
    def gameModeDevilsNight(self):
        sectionClickCount=0
        printWithTime("消息:账户:%s:百鬼夜行"%(str(self.__id)))
        while True:
            screenshot = self.__gui.getScreenshot()

            position=self.__gui.getImagePositionInScreenshot(IMAGE_DEVILS_NIGHT_UP_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_DEVILS_NIGHT_UP_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.101,self.__startX,self.__startY)
                continue

            position=self.__gui.getImagePositionInScreenshot(IMAGE_DEVILS_NIGHT_BULLET_PATH,screenshot)
            if position != None:
                self.__gui.clickCoordinate(self.__windowWidth*random.uniform(0.1,0.9),self.__windowHeight*random.uniform(0.7,0.8),1,0.101)
                self.__gui.clickCoordinate(self.__windowWidth*random.uniform(0.1,0.9),self.__windowHeight*random.uniform(0.7,0.8),1,0.101)
                continue

            position=self.__gui.getImagePositionInScreenshot(IMAGE_DEVILS_NIGHT_SECTION_PATH,screenshot)
            if position != None:
                sectionClickCount+=1
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_DEVILS_NIGHT_SECTION_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                if(sectionClickCount>=3):
                    sectionClickCount=0
                    self.__gui.moveToCenter(0.15)
                    self.__gui.dragMouseToRandomPosition(0.1,-1.0)
                continue

            position=self.__gui.getImagePositionInScreenshot(IMAGE_DEVILS_NIGHT_INVITE_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_DEVILS_NIGHT_INVITE_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                time.sleep(2.0)
                continue

            position=self.__gui.getImagePositionInScreenshot(IMAGE_DEVILS_NIGHT_ENTER_PATH,screenshot)
            if position != None:
                sectionClickCount=0
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_DEVILS_NIGHT_ENTER_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                continue

            position=self.__gui.getImagePositionInScreenshot(IMAGE_DEVILS_NIGHT_SELECTED_PATH,screenshot)
            if not position:
                printWithTime("消息:账户:%s:尝试随机选择式神"%(str(self.__id)))
                self.__gui.clickCoordinate(self.__windowWidth*random.uniform(0.16,0.84),self.__windowHeight*random.uniform(0.66,0.8),1,0.105)

            position=self.__gui.getImagePositionInScreenshot(IMAGE_DEVILS_NIGHT_START_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_DEVILS_NIGHT_START_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)
                continue

            position=self.__gui.getImagePositionInScreenshot(IMAGE_DEVILS_NIGHT_OVER_PATH,screenshot)
            if position != None:
                printWithTime("消息:账户:%s:检测到图像:%s:位置:X=%.4f,Y=%.4f"%(str(self.__id),IMAGE_DEVILS_NIGHT_OVER_PATH,position.left,position.top))
                self.__gui.clickPositionWithOffsets(position,1,0.2,self.__startX,self.__startY)

                while True:
                    if not self.__gui.clickImageWithOffsets(IMAGE_DEVILS_NIGHT_OVER_PATH,1,0.2):
                        break
                    printWithTime("消息:账户:%s:检测到图像:%s:位置"%(str(self.__id),IMAGE_DEVILS_NIGHT_OVER_PATH))
                break  

#
    def detectPause(self):
        global _isPaused
        while True:
            keyboard.wait(hotkey='f12')
            printWithTime("消息:F12被按下")
            if _isPaused:
                _isPaused=False
                self.__gui.GUIRelease()
                printWithTime("已继续")
            else:
                _isPaused=True
                self.__gui.GUIAcquire()
                printWithTime("已暂停")
#
    def detectFailure(self):
        while True:
            time.sleep(_DETECTION_INTERVAL*15)
            if not self.__gui.isImageDetected(IMAGE_FAILED_PATH):
                continue

            message="错误:账户:%s:失败，请重新运行!"%(str(self.__id))
            printWithTime(message)

            def inner():
                winsound.Beep(800,30000)
                
                if _globalConfig.closeGamesAfterFailure:
                    os.system("taskkill /IM onmyoji.exe /F")
                if _globalConfig.exitAfterFailure:
                    sys.exit()

                winsound.Beep(800,1000)

            threading.Thread(None,inner,str(str(self.__id))).start()
#
    def detectAssistance(self):
        while True:
            time.sleep(_DETECTION_INTERVAL*10)
            if (not self.__gui.isImageDetected(IMAGE_ASSISTANCE_PATH)) and (not self.__gui.isImageDetected(IMAGE_ASSISTANCE_2_PATH)) and (not self.__gui.isImageDetected(IMAGE_ASSISTANCE_3_PATH)) and (not self.__gui.isImageDetected(IMAGE_ASSISTANCE_4_PATH)):
                continue

            message="消息:账户:%s:检测到悬赏封印邀请"%(str(self.__id))
            printWithTime(message)
            threading.Thread(None,self.feedback,str(self.__id),args=(message,)).start()

            winsound.Beep(1000,100)
            self.__gui.clickImageWithOffsets(IMAGE_ACCEPT_PATH)

            message="消息:账户:%s:已尝试接受悬赏封印邀请"%(str(self.__id))
            printWithTime(message)
            threading.Thread(None,self.feedback,str(self.__id),args=(message,)).start()
#
    def detectOccupation(self):
        while True:
            time.sleep(_DETECTION_INTERVAL*16)
            if not self.__gui.isImageDetected(IMAGE_OCCUPIED_PATH):
                continue

            message="错误:账户:%s:检测到账户在其他设备登录"%(str(self.__id))
            printWithTime(message)
            threading.Thread(None,self.feedback,str(self.__id),args=(message,)).start()
            
            def inner():
                winsound.Beep(1000,10000)

                if _globalConfig.closeGamesIfOccupied:
                    os.system("taskkill /IM onmyoji.exe /F")
                if _globalConfig.exitIfOccupied:
                    sys.exit()
            
            threading.Thread(None,inner,str(str(self.__id))).start()
#
    def detectFoodInsufficiency(self):
        while True:
            time.sleep(_DETECTION_INTERVAL*20)
            if not self.__gui.isImageDetected(IMAGE_FOOD_INSUFFICIENCY_PATH):
                continue

            message="错误:账户:%s:检测到体力不足"%(str(self.__id))
            printWithTime(message)
            threading.Thread(None,self.feedback,str(self.__id),args=(message,)).start()
            self.__gui.clickImageWithOffsets(IMAGE_CLOSE_DIALOG_PATH)

            def inner():
                winsound.Beep(1000,5000)

                if _globalConfig.closeGamesIfFoodNotEnough:
                    os.system("taskkill /IM onmyoji.exe /F")
                if _globalConfig.closeGamesIfFoodNotEnough:
                    sys.exit()
                
                winsound.Beep(1000,1000)
            
            threading.Thread(None,inner,str(str(self.__id))).start()
#
    def detectDisconnection(self):
        while True:
            time.sleep(_DETECTION_INTERVAL*20)
            if not self.__gui.isImageDetected(IMAGE_DISCONNECTED_PATH):
                continue

            message="错误:账户:%s:检测到已断开连接"%(str(self.__id))
            printWithTime(message)
            threading.Thread(None,self.feedback,str(self.__id),args=(message,)).start()

            def inner():
                winsound.Beep(1000,3000)

                if _globalConfig.closeGamesIfDisconnected:
                    os.system("taskkill /IM onmyoji.exe /F")
                if _globalConfig.closeGamesIfDisconnected:
                    sys.exit()
                
                winsound.Beep(1000,1000)
                
            threading.Thread(None,inner,str(str(self.__id))).start()
#
    def feedback(self,message):
        global _feedbackerLocker

        printWithTime("账户:%s:反馈者:%s"%(str(self.__id),self.__feedbackerName))
        qqWindow = win32gui.FindWindow(None, self.__feedbackerName)
        if qqWindow==0:
            printWithTime("账户:%s:无法定位到反馈者:%s"%(str(self.__id),self.__feedbackerName))
            return
        _feedbackerLocker.acquire()

        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, message)
        win32clipboard.CloseClipboard()

        win32gui.SendMessage(qqWindow, 258, 22, 2080193)
        win32gui.SendMessage(qqWindow, 770, 0, 0)
        
        win32gui.SendMessage(qqWindow, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
        win32gui.SendMessage(qqWindow, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

        _feedbackerLocker.release()
#
    def run(self):
        _localVariable.isBossDetected=False
        _localVariable.isFailureDetected=False
        _localVariable.detectCount=10
        _localVariable.xDirection=-1.0

        _localVariable.isEmpty=False
        _localVariable.startClickCount=0
        _localVariable.isInfoDelayed=False
        count=0
        while self.__total-count>0:
            seconds=0
            while seconds:
                printWithTime("账户:%s:"%(str(self.__id))+str(seconds)+"s后开始")
                time.sleep(1)
                seconds-=1
            printWithTime("账户:%s:"%(str(self.__id))+"开始")
            printWithTime("账户:%s:"%(str(self.__id))+"\n"
                +"\t窗口起始位置X:"+str(self.__startX)+"\n"
                +"\t窗口起始位置Y:"+str(self.__startY)+"\n"
                +"\t窗口宽度:"+str(self.__windowWidth)+"\n"
                +"\t窗口高度:"+str(self.__windowHeight)+"\n"
                +"\t局数:"+str(self.__total)+"\n"
                +"\t是否为房主(Y/N):"+str(self.__isCaptain))
            if self.__gameMode==0:
                self.gameModeActivity()
            elif self.__gameMode==1:
                self.gameModeMitama()
            elif self.__gameMode==2:
                _localVariable.detectCount=10
                _localVariable.xDirection=-1.0
                self.gameModeStory()
            elif self.__gameMode==3:
                self.gameModeMitamaX()
            elif self.__gameMode==4:
                self.gameModeBreach()
            elif self.__gameMode==5:
                self.gameModeTeamBattle()
            elif self.__gameMode==6:
                self.gameModeSeal()
            elif self.__gameMode==7:
                self.gameModeInviteClubMembers()
            elif self.__gameMode==8:
                _localVariable.startClickCount=0
                self.gameModeClubBreach()
            elif self.__gameMode==9:
                self.gameModeCardSynthesis()
            elif self.__gameMode==10:
                self.gameModeDevilsNight() 
            count+=1
            message="%s:账户:%s:游戏类型:%s,已完成%s局,还剩余%s局"%(getTimeFormatted(),str(self.__id),str(self.__gameMode),str(count),str(self.__total-count))
            threading.Thread(None,self.feedback,str(self.__id),args=(message,)).start()
            printWithTime(message)

        message="%s:账户:%s:游戏类型:%s,已完成"%(getTimeFormatted(),str(self.__id),str(self.__gameMode))
        threading.Thread(None,self.feedback,str(self.__id),args=(message,)).start()
        winsound.Beep(800,1000)
        if _globalConfig.closeGamesAfterFinish:
            os.system("taskkill /IM onmyoji.exe /F")
        if _globalConfig.exitAfterFinish:
            sys.exit()
