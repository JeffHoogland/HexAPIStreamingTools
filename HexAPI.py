"""
A Python Library for taking data from the HexTCG API and making it easy to use.
"""

import os
import ConfigParser
import platform
import subprocess

HexCardData = "HexCardData.csv"
ConfigFile = "HexAPIPythonSettings.cfg"
UserHome = os.path.expanduser("~")

class HexAPI():
    def __init__(self):
        self.config = ConfigParser.RawConfigParser()
        if os.path.isfile(ConfigFile):
            self.config.read(ConfigFile)
        else:
            self.setupDefaultConfig()
    
    def setupDefaultConfig(self):
        self.config.add_section("HexDeck")
        self.config.set("HexDeck", "outputpath", UserHome)
        self.config.set("HexDeck", "showreserves", "False")
        self.config.set("HexDeck", "lastname", None)
        
        with open(ConfigFile, 'wb') as configfileobj:
            self.config.write(configfileobj)
    
    def setConfigValue(self, section, option, value):
        self.config.set(section, option, value)
        
        with open(ConfigFile, 'wb') as configfileobj:
            self.config.write(configfileobj)
        
    def newCall(self, data):
        if data["Message"] == "SaveDeck":
            if data["Name"].isdigit():
                data["Name"] = self.config.get("HexDeck", "lastname")
            else:
                self.setConfigValue("HexDeck", "lastname", data["Name"])
            
            HexDeck(data, self.config).generateDeckImage()

class HexDeck():
    def __init__(self, DeckData, configFile):
        self.OutputPath = configFile.get("HexDeck", "outputpath")
        self.ShowReserves = configFile.getboolean("HexDeck", "showreserves")
        
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
            for ourtype in self.CardTypes:
                for card in self.ReservesOrder[ourtype]:
                    f.write("%sx %s\n"%(self.ReadableReserves[card], card))
        f.close()

        if "windows" in platform.platform().lower():
            subprocess.call(["StackIt.exe", "%s/%s.txt"%(self.OutputPath, self.DeckName)])
        else:
            os.system('cd StackIt && python StackIt.py "%s/%s.txt"'%(self.OutputPath, self.DeckName))
        FinalImageLocation = "%s/LastDeckExport.png"%(self.OutputPath)
        if os.path.isfile(FinalImageLocation):
            os.remove(FinalImageLocation)
        os.symlink("%s/%s.png"%(self.OutputPath, self.DeckName), FinalImageLocation)
