"""
A Python Library for taking data from the HexTCG API and making it easy to use.
"""

import os
import ConfigParser
import platform
import subprocess
import shutil
import smtplib

HexCardData = "HexCardData.csv"
ConfigFile = "HexAPIPythonSettings.cfg"
UserHome = os.path.expanduser("~")

class HexAPI():
    def __init__(self):
        self.config = ConfigParser.RawConfigParser()
        if os.path.isfile(ConfigFile):
            self.config.read(ConfigFile)
            if self.config.get("General", "newconfig") == "True":
                self.setupDefaultConfig()
        else:
            shutil.copy("HexAPIPythonSettings-New.cfg", ConfigFile)
            self.setupDefaultConfig()
    
    def setupDefaultConfig(self):
        self.config.set("General", "newconfig", False)
        self.config.set("HexDeck", "outputpath", UserHome)
        self.config.set("HexDeck", "showreserves", "False")
        self.config.set("HexDeck", "lastname", None)
        self.config.set("Alerts", "enabled", False)
        self.config.set("Alerts", "email", None)
        self.config.set("Alerts", "password", None)
        
        with open(ConfigFile, 'wb') as configfileobj:
            self.config.write(configfileobj)
    
    def setConfigValue(self, section, option, value):
        self.config.set(section, option, value)
        
        with open(ConfigFile, 'wb') as configfileobj:
            self.config.write(configfileobj)
    
    def getConfigValue(self, section, option):
        self.config.read(ConfigFile)
        return self.config.get(section, option)
        
    def newCall(self, data):
        #f = open('apioutput.txt', 'a')
        #f.write("%s\n"%data)
        #f.close()
        #print(data["Message"])
        if data["Message"] == "SaveDeck":
            if data["Name"].isdigit():
                data["Name"] = self.config.get("HexDeck", "lastname")
                data["Maindeck"] = False
            else:
                self.setConfigValue("HexDeck", "lastname", data["Name"])
                data["Maindeck"] = True
            
            HexDeck(data, self.config).generateDeckImage()
        elif data["Message"] == "GameEnded":
            #f = open('apioutput.txt', 'a')
            #f.write("%s\n"%data)
            #f.close()
            OutputPath = self.config.get("HexDeck", "outputpath")
            FinalImageLocation = "%s/LastDeckExport.png"%(OutputPath)
            if os.path.isfile(FinalImageLocation):
                os.remove(FinalImageLocation)
            shutil.copy("%s/Maindeck.png"%(OutputPath), FinalImageLocation)
        elif data["Message"] == "GameStarted":
            if self.getConfigValue("Alerts", "enabled") == "True":
                sendRoundStartedEmail(self.getConfigValue("Alerts", "email"), self.getConfigValue("Alerts", "password"))
            #f = open('apioutput.txt', 'a')
            #f.write("%s\n"%data)
            #f.close()
        elif data["Message"] == "CardUpdated":
            if data["Collection"] == 2:
                #print("You drew a %s"%data["Name"])
                pass

def sendRoundStartedEmail(email, password):
    server = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    server.starttls()

    #Next, log in to the server
    server.login(email, password)

    SUBJECT = "Hex Round Alerts - Round Started"
    TEXT = "This is an alert email letting you know your match has started."

    msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

    server.sendmail("%s@gmail.com"%email, "%s@gmail.com"%email, msg)

    server.quit()

class HexDeck():
    def __init__(self, DeckData, configFile):
        self.OutputPath = configFile.get("HexDeck", "outputpath")
        self.ShowReserves = configFile.getboolean("HexDeck", "showreserves")
        
        self.isMainDeck = DeckData["Maindeck"]
        
        self.DeckName = DeckData["Name"]
        self.DeckChampion = DeckData["Champion"]
        
        self.CardKey = {}
        self.CardTypes = ["Troop","Action","other","Resource"]
        
        ShardTypes = ["Wild Shard", "Ruby Shard", "Sapphire Shard", "Diamond Shard", "Blood Shard"]
        DeckShards = []

        self.ReadableDeck = {}
        self.DeckOrder = {"Troop":[],"Action":[],"other":[],"Resource":[]}
        
        self.ReadableReserves = {}
        self.ReservesOrder = {"Troop":[],"Action":[],"other":[],"Resource":[]}

        with open(HexCardData) as f:
            for line in f:
               (cardname, uuid, cardtype) = line.split("|")
               cardname = cardname.strip()
               uuid = uuid.strip()
               cardtype = cardtype.strip().split(",")[0]
               self.CardKey[uuid] = {"name":cardname, "type":cardtype}
        
        for d in DeckData["Deck"]:
            CardName = self.CardKey[d["Guid"]["m_Guid"]]["name"]
            CardType = self.CardKey[d["Guid"]["m_Guid"]]["type"]
            if CardName in ShardTypes and CardName.split(" ")[0] not in DeckShards:
                DeckShards.append(CardName.split(" ")[0])
            #print(CardName)
            if CardType not in self.CardTypes:
                CardType = "other"
            
            if CardName in self.ReadableDeck:
                self.ReadableDeck[CardName] += 1
            else:
                self.ReadableDeck[CardName] = 1
                self.DeckOrder[CardType].append(CardName)

        if len(DeckData["Deck"]) < 60:
            self.DeckName = ""
            for s in DeckShards:
                self.DeckName = "%s[%s]"%(self.DeckName, s.upper())
            self.DeckName = "%sLimited"%(self.DeckName)

        for d in self.DeckOrder:
            self.DeckOrder[d].sort()
        
        for d in DeckData["Sideboard"]:
            CardName = self.CardKey[d["Guid"]["m_Guid"]]["name"]
            CardType = self.CardKey[d["Guid"]["m_Guid"]]["type"]
            #print(CardName)
            if CardType not in self.CardTypes:
                CardType = "other"
            
            if CardName in self.ReadableReserves:
                self.ReadableReserves[CardName] += 1
            else:
                self.ReadableReserves[CardName] = 1
                self.ReservesOrder[CardType].append(CardName)

        for d in self.ReservesOrder:
            self.ReservesOrder[d].sort()
    
    def setOutputPath(self, OutputPath):
        self.OutputPath = OutputPath

    def generateDeckImage(self):
        f = open('%s/%s.txt'%(self.OutputPath, self.DeckName), 'w')
        f.write("Champion: %s\n"%self.DeckChampion)
        for ourtype in self.CardTypes:
            for card in self.DeckOrder[ourtype]:
                f.write("%sx %s\n"%(self.ReadableDeck[card], card))
        if self.ShowReserves:
            f.write("Reserves\n")
            for ourtype in self.CardTypes:
                for card in self.ReservesOrder[ourtype]:
                    f.write("%sx %s\n"%(self.ReadableReserves[card], card))
        f.close()

        #StackIt broke their windows EXE so always try to use the local python version
        #if "windows" in platform.platform().lower():
            #subprocess.call(["StackIt.exe", "%s/%s.txt"%(self.OutputPath, self.DeckName)])
        #else:
        os.system('cd StackIt && python StackIt.py "%s/%s.txt"'%(self.OutputPath, self.DeckName))
        FinalImageLocation = "%s/LastDeckExport.png"%(self.OutputPath)
        if os.path.isfile(FinalImageLocation):
            os.remove(FinalImageLocation)
        if "windows" in platform.platform().lower():
            shutil.copy("%s/%s.png"%(self.OutputPath, self.DeckName), FinalImageLocation)
        else:
            os.symlink("%s/%s.png"%(self.OutputPath, self.DeckName), FinalImageLocation)
        
        if self.isMainDeck:
            FinalImageLocation = "%s/Maindeck.png"%(self.OutputPath)
            if os.path.isfile(FinalImageLocation):
                os.remove(FinalImageLocation)
            shutil.copy("%s/%s.png"%(self.OutputPath, self.DeckName), FinalImageLocation)
