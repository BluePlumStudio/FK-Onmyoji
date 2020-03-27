import pathlib
import configparser

class newConfigparser(configparser.ConfigParser):
    def __init__(self,defaults=None):
        configparser.ConfigParser.__init__(self,defaults=None)
        
    def optionxform(self, optionstr):
        return optionstr
#
class Config(object):
    def __init__(self):
        self.exitAfterFinish=False
        self.closeGamesAfterFinish=False
        self.exitAfterFailure=False
        self.closeGamesAfterFailure=True
        self.exitIfOccupied=False
        self.closeGamesIfOccupied=True
        self.exitIfFoodNotEnough=False
        self.closeGamesIfFoodNotEnough=True
        self.isFullTeam=False
        self.replaceShikigamiIfFull=True
#
    def __init__(self,configFilePath):
        self.exitAfterFinish=False
        self.closeGamesAfterFinish=False
        self.exitAfterFailure=False
        self.closeGamesAfterFailure=True
        self.exitIfOccupied=False
        self.closeGamesIfOccupied=True
        self.exitIfFoodNotEnough=False
        self.closeGamesIfFoodNotEnough=True
        self.isFullTeam=False
        self.replaceShikigamiIfFull=True
        configPraser=newConfigparser()
        
        if (pathlib.Path(configFilePath).exists())==False:
            configPraser["Options"]={"ExitAfterfinish":"False",
                                    "CloseGamesAfterFinish":"False",
                                    "ExitAfterFailure":"False",
                                    "CloseGamesAfterFailure":"True",
                                    "ExitIfOccupied":"False",
                                    "CloseGamesIfOccupied":"True",
                                    "ExitIfFoodNotEnough":"False",
                                    "CloseGamesIfFoodNotEnough":"True",
                                    "ExitIfDisconnected":"False",
                                    "CloseGamesIfDisconnected":"True",
                                    "IsFullTeam":"False",
                                    "ReplaceIfShikigamiFull":"True"}
            
            with open(configFilePath, 'w') as configFile:
                configPraser.write(configFile)

            return
                
        configPraser.read(configFilePath)
        if configPraser.has_section("Options"):
            options=configPraser["Options"]
            if configPraser.has_option("Options","ExitAfterfinish"):
                self.exitAfterFinish=options.getboolean("ExitAfterfinish")
            if configPraser.has_option("Options","CloseGamesAfterFinish"):
                self.closeGamesAfterFinish=options.getboolean("CloseGamesAfterFinish")
            if configPraser.has_option("Options","ExitAfterFailure"):
                self.exitAfterFailure=options.getboolean("ExitAfterFailure")
            if configPraser.has_option("Options","CloseGamesAfterFailure"):
                self.closeGamesAfterFailure=options.getboolean("CloseGamesAfterFailure")
            if configPraser.has_option("Options","ExitIfOccupied"):
                self.exitIfOccupied=options.getboolean("ExitIfOccupied")
            if configPraser.has_option("Options","CloseGamesIfOccupied"):
                self.closeGamesIfOccupied=options.getboolean("CloseGamesIfOccupied")
            if configPraser.has_option("Options","ExitIfFoodNotEnough"):
                self.exitIfFoodNotEnough=options.getboolean("ExitIfFoodNotEnough")
            if configPraser.has_option("Options","CloseGamesIfFoodNotEnough"):
                self.closeGamesIfFoodNotEnough=options.getboolean("CloseGamesIfFoodNotEnough")
            if configPraser.has_option("Options","ExitIfDisconnected"):
                self.exitIfDisconnected=options.getboolean("ExitIfDisconnected")
            if configPraser.has_option("Options","CloseGamesIfDisconnected"):
                self.closeGamesIfDisconnected=options.getboolean("CloseGamesIfDisconnected")
            if configPraser.has_option("Options","IsFullTeam"):
                self.isFullTeam=options.getboolean("IsFullTeam")
            if configPraser.has_option("Options","ReplaceIfShikigamiFull"):
                self.replaceShikigamiIfFull=options.getboolean("ReplaceIfShikigamiFull")