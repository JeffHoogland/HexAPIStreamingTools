import os

#sampleData = {u'Sideboard': [{u'Gems': [], u'Guid': {u'm_Guid': u'd3d0da9e-3f67-4129-94a6-0a3c8f1ea931'}, u'Flags': u'', u'Id': 131578836}, {u'Gems': [], u'Guid': {u'm_Guid': u'd3d0da9e-3f67-4129-94a6-0a3c8f1ea931'}, u'Flags': u'', u'Id': 131579086}, {u'Gems': [], u'Guid': {u'm_Guid': u'd3d0da9e-3f67-4129-94a6-0a3c8f1ea931'}, u'Flags': u'', u'Id': 131579336}, {u'Gems': [], u'Guid': {u'm_Guid': u'6e13ec0a-4b77-465b-b205-7d6b687b103f'}, u'Flags': u'', u'Id': 147553698}, {u'Gems': [], u'Guid': {u'm_Guid': u'00f99de4-842e-41cd-86a7-1fe71cc75b62'}, u'Flags': u'', u'Id': 157847860}, {u'Gems': [], u'Guid': {u'm_Guid': u'6e13ec0a-4b77-465b-b205-7d6b687b103f'}, u'Flags': u'', u'Id': 157847919}, {u'Gems': [], u'Guid': {u'm_Guid': u'00f99de4-842e-41cd-86a7-1fe71cc75b62'}, u'Flags': u'', u'Id': 163617878}, {u'Gems': [], u'Guid': {u'm_Guid': u'00f99de4-842e-41cd-86a7-1fe71cc75b62'}, u'Flags': u'', u'Id': 163617909}, {u'Gems': [], u'Guid': {u'm_Guid': u'00f99de4-842e-41cd-86a7-1fe71cc75b62'}, u'Flags': u'', u'Id': 163617943}, {u'Gems': [], u'Guid': {u'm_Guid': u'735bd7ec-1b7b-4e5a-aa8b-63773e9e3ebc'}, u'Flags': u'', u'Id': 173548476}, {u'Gems': [], u'Guid': {u'm_Guid': u'735bd7ec-1b7b-4e5a-aa8b-63773e9e3ebc'}, u'Flags': u'', u'Id': 173548477}, {u'Gems': [], u'Guid': {u'm_Guid': u'04b7d8f0-7a0a-4cb7-9f7c-2880d98cd9dd'}, u'Flags': u'', u'Id': 210683765}, {u'Gems': [], u'Guid': {u'm_Guid': u'7c94b87b-c575-464c-b47d-f9082d24e3c2'}, u'Flags': u'', u'Id': 210683984}, {u'Gems': [], u'Guid': {u'm_Guid': u'eba0cba5-7512-45df-bfed-ca36d7593866'}, u'Flags': u'', u'Id': 210684112}, {u'Gems': [], u'Guid': {u'm_Guid': u'061c070a-6591-4b22-9dd8-92d725210ea1'}, u'Flags': u'', u'Id': 216281518}], u'Champion': u'Bishop Elijah', u'Deck': [{u'Gems': [], u'Guid': {u'm_Guid': u'6865d8d5-bd2e-43c6-8a68-53d1bde6bc28'}, u'Flags': u'', u'Id': 12287}, {u'Gems': [], u'Guid': {u'm_Guid': u'6865d8d5-bd2e-43c6-8a68-53d1bde6bc28'}, u'Flags': u'', u'Id': 12288}, {u'Gems': [], u'Guid': {u'm_Guid': u'6865d8d5-bd2e-43c6-8a68-53d1bde6bc28'}, u'Flags': u'', u'Id': 12289}, {u'Gems': [], u'Guid': {u'm_Guid': u'6865d8d5-bd2e-43c6-8a68-53d1bde6bc28'}, u'Flags': u'', u'Id': 12290}, {u'Gems': [], u'Guid': {u'm_Guid': u'6865d8d5-bd2e-43c6-8a68-53d1bde6bc28'}, u'Flags': u'', u'Id': 12291}, {u'Gems': [], u'Guid': {u'm_Guid': u'6865d8d5-bd2e-43c6-8a68-53d1bde6bc28'}, u'Flags': u'', u'Id': 12292}, {u'Gems': [], u'Guid': {u'm_Guid': u'6865d8d5-bd2e-43c6-8a68-53d1bde6bc28'}, u'Flags': u'', u'Id': 12293}, {u'Gems': [], u'Guid': {u'm_Guid': u'6865d8d5-bd2e-43c6-8a68-53d1bde6bc28'}, u'Flags': u'', u'Id': 12294}, {u'Gems': [], u'Guid': {u'm_Guid': u'6865d8d5-bd2e-43c6-8a68-53d1bde6bc28'}, u'Flags': u'', u'Id': 12295}, {u'Gems': [], u'Guid': {u'm_Guid': u'6865d8d5-bd2e-43c6-8a68-53d1bde6bc28'}, u'Flags': u'', u'Id': 12296}, {u'Gems': [], u'Guid': {u'm_Guid': u'6865d8d5-bd2e-43c6-8a68-53d1bde6bc28'}, u'Flags': u'', u'Id': 12297}, {u'Gems': [], u'Guid': {u'm_Guid': u'6865d8d5-bd2e-43c6-8a68-53d1bde6bc28'}, u'Flags': u'', u'Id': 12298}, {u'Gems': [], u'Guid': {u'm_Guid': u'6865d8d5-bd2e-43c6-8a68-53d1bde6bc28'}, u'Flags': u'', u'Id': 12299}, {u'Gems': [], u'Guid': {u'm_Guid': u'6865d8d5-bd2e-43c6-8a68-53d1bde6bc28'}, u'Flags': u'', u'Id': 12300}, {u'Gems': [], u'Guid': {u'm_Guid': u'6865d8d5-bd2e-43c6-8a68-53d1bde6bc28'}, u'Flags': u'', u'Id': 12301}, {u'Gems': [], u'Guid': {u'm_Guid': u'6865d8d5-bd2e-43c6-8a68-53d1bde6bc28'}, u'Flags': u'', u'Id': 12302}, {u'Gems': [], u'Guid': {u'm_Guid': u'6865d8d5-bd2e-43c6-8a68-53d1bde6bc28'}, u'Flags': u'', u'Id': 12303}, {u'Gems': [], u'Guid': {u'm_Guid': u'6865d8d5-bd2e-43c6-8a68-53d1bde6bc28'}, u'Flags': u'', u'Id': 12304}, {u'Gems': [], u'Guid': {u'm_Guid': u'6865d8d5-bd2e-43c6-8a68-53d1bde6bc28'}, u'Flags': u'', u'Id': 12305}, {u'Gems': [], u'Guid': {u'm_Guid': u'6865d8d5-bd2e-43c6-8a68-53d1bde6bc28'}, u'Flags': u'', u'Id': 12306}, {u'Gems': [], u'Guid': {u'm_Guid': u'6865d8d5-bd2e-43c6-8a68-53d1bde6bc28'}, u'Flags': u'', u'Id': 12307}, {u'Gems': [], u'Guid': {u'm_Guid': u'95e3c817-6924-427d-87ee-ccedeb5d6c8d'}, u'Flags': u'', u'Id': 131577570}, {u'Gems': [], u'Guid': {u'm_Guid': u'95e3c817-6924-427d-87ee-ccedeb5d6c8d'}, u'Flags': u'', u'Id': 131577820}, {u'Gems': [], u'Guid': {u'm_Guid': u'95e3c817-6924-427d-87ee-ccedeb5d6c8d'}, u'Flags': u'', u'Id': 131578070}, {u'Gems': [], u'Guid': {u'm_Guid': u'95e3c817-6924-427d-87ee-ccedeb5d6c8d'}, u'Flags': u'', u'Id': 131578320}, {u'Gems': [], u'Guid': {u'm_Guid': u'e76c081e-224c-4cf0-9417-04013e9f372f'}, u'Flags': u'', u'Id': 131578687}, {u'Gems': [], u'Guid': {u'm_Guid': u'37e0e097-4bd0-43b9-a181-c3bd47ba2c0f'}, u'Flags': u'', u'Id': 131578689}, {u'Gems': [], u'Guid': {u'm_Guid': u'ffc42641-a189-43c8-95ff-8a909b30b32c'}, u'Flags': u'', u'Id': 131578844}, {u'Gems': [], u'Guid': {u'm_Guid': u'e76c081e-224c-4cf0-9417-04013e9f372f'}, u'Flags': u'', u'Id': 131578937}, {u'Gems': [], u'Guid': {u'm_Guid': u'37e0e097-4bd0-43b9-a181-c3bd47ba2c0f'}, u'Flags': u'', u'Id': 131578939}, {u'Gems': [], u'Guid': {u'm_Guid': u'ffc42641-a189-43c8-95ff-8a909b30b32c'}, u'Flags': u'', u'Id': 131579094}, {u'Gems': [], u'Guid': {u'm_Guid': u'e76c081e-224c-4cf0-9417-04013e9f372f'}, u'Flags': u'', u'Id': 131579187}, {u'Gems': [], u'Guid': {u'm_Guid': u'37e0e097-4bd0-43b9-a181-c3bd47ba2c0f'}, u'Flags': u'', u'Id': 131579189}, {u'Gems': [], u'Guid': {u'm_Guid': u'ffc42641-a189-43c8-95ff-8a909b30b32c'}, u'Flags': u'', u'Id': 131579344}, {u'Gems': [], u'Guid': {u'm_Guid': u'e76c081e-224c-4cf0-9417-04013e9f372f'}, u'Flags': u'', u'Id': 131579437}, {u'Gems': [], u'Guid': {u'm_Guid': u'37e0e097-4bd0-43b9-a181-c3bd47ba2c0f'}, u'Flags': u'', u'Id': 131579439}, {u'Gems': [], u'Guid': {u'm_Guid': u'e0bfc238-3443-4738-a452-6ba2f18463cb'}, u'Flags': u'', u'Id': 173548816}, {u'Gems': [], u'Guid': {u'm_Guid': u'e0bfc238-3443-4738-a452-6ba2f18463cb'}, u'Flags': u'', u'Id': 173548817}, {u'Gems': [], u'Guid': {u'm_Guid': u'f346bde5-b461-4b99-b27a-2df4e8740c92'}, u'Flags': u'', u'Id': 210683830}, {u'Gems': [], u'Guid': {u'm_Guid': u'f346bde5-b461-4b99-b27a-2df4e8740c92'}, u'Flags': u'', u'Id': 210683831}, {u'Gems': [], u'Guid': {u'm_Guid': u'f346bde5-b461-4b99-b27a-2df4e8740c92'}, u'Flags': u'', u'Id': 210683832}, {u'Gems': [], u'Guid': {u'm_Guid': u'f346bde5-b461-4b99-b27a-2df4e8740c92'}, u'Flags': u'', u'Id': 210683833}, {u'Gems': [], u'Guid': {u'm_Guid': u'4db8ed15-284d-4ff1-b536-9d53a2011562'}, u'Flags': u'', u'Id': 210683930}, {u'Gems': [], u'Guid': {u'm_Guid': u'4db8ed15-284d-4ff1-b536-9d53a2011562'}, u'Flags': u'', u'Id': 210683931}, {u'Gems': [], u'Guid': {u'm_Guid': u'4db8ed15-284d-4ff1-b536-9d53a2011562'}, u'Flags': u'', u'Id': 210683932}, {u'Gems': [], u'Guid': {u'm_Guid': u'4db8ed15-284d-4ff1-b536-9d53a2011562'}, u'Flags': u'', u'Id': 210683933}, {u'Gems': [], u'Guid': {u'm_Guid': u'eba0cba5-7512-45df-bfed-ca36d7593866'}, u'Flags': u'', u'Id': 210684113}, {u'Gems': [{u'Guid': {u'm_Guid': u'05914943-3bd7-4768-ae39-d5223519c45c'}, u'Name': u'Minor Diamond of Wind'}], u'Guid': {u'm_Guid': u'e82e25c5-7f4b-49d1-9e12-68d716393124'}, u'Flags': u'', u'Id': 213281175}, {u'Gems': [{u'Guid': {u'm_Guid': u'05914943-3bd7-4768-ae39-d5223519c45c'}, u'Name': u'Minor Diamond of Wind'}], u'Guid': {u'm_Guid': u'e82e25c5-7f4b-49d1-9e12-68d716393124'}, u'Flags': u'', u'Id': 214597980}, {u'Gems': [], u'Guid': {u'm_Guid': u'a4e6d649-8f06-4024-be63-0bd497a8fcba'}, u'Flags': u'', u'Id': 215603973}, {u'Gems': [], u'Guid': {u'm_Guid': u'a4e6d649-8f06-4024-be63-0bd497a8fcba'}, u'Flags': u'', u'Id': 215914820}, {u'Gems': [], u'Guid': {u'm_Guid': u'1b771946-8f90-47bb-8e35-26bd657e173c'}, u'Flags': u'', u'Id': 216463453}, {u'Gems': [], u'Guid': {u'm_Guid': u'1b771946-8f90-47bb-8e35-26bd657e173c'}, u'Flags': u'', u'Id': 216593686}, {u'Gems': [], u'Guid': {u'm_Guid': u'1b771946-8f90-47bb-8e35-26bd657e173c'}, u'Flags': u'', u'Id': 216800225}, {u'Gems': [], u'Guid': {u'm_Guid': u'061c070a-6591-4b22-9dd8-92d725210ea1'}, u'Flags': u'', u'Id': 217025686}, {u'Gems': [], u'Guid': {u'm_Guid': u'061c070a-6591-4b22-9dd8-92d725210ea1'}, u'Flags': u'', u'Id': 217025789}, {u'Gems': [], u'Guid': {u'm_Guid': u'a4e6d649-8f06-4024-be63-0bd497a8fcba'}, u'Flags': u'', u'Id': 217025875}, {u'Gems': [], u'Guid': {u'm_Guid': u'a4e6d649-8f06-4024-be63-0bd497a8fcba'}, u'Flags': u'', u'Id': 217060498}, {u'Gems': [], u'Guid': {u'm_Guid': u'1b771946-8f90-47bb-8e35-26bd657e173c'}, u'Flags': u'', u'Id': 217138555}, {u'Gems': [], u'Guid': {u'm_Guid': u'061c070a-6591-4b22-9dd8-92d725210ea1'}, u'Flags': u'', u'Id': 217147547}], u'CampaignDeck': False, u'Equipment': [{u'm_Guid': u'00000000-0000-0000-0000-000000000000'}, {u'm_Guid': u'00000000-0000-0000-0000-000000000000'}, {u'm_Guid': u'00000000-0000-0000-0000-000000000000'}, {u'm_Guid': u'00000000-0000-0000-0000-000000000000'}, {u'm_Guid': u'00000000-0000-0000-0000-000000000000'}, {u'm_Guid': u'00000000-0000-0000-0000-000000000000'}], u'Version': u'Live', u'User': u'JeffHoogland', u'Message': u'SaveDeck', u'TournamentDeck': False, u'Name': u'[ATK][DIAMOND][DIAMOND][DIAMOND][DIAMOND][DIAMOND]'}

FinalImageLocation = "/home/jeff/StreamDeck.png"

class deckFormater():
    def __init__(self):
        self.CardKey = {}
        self.CardTypes = ["Troop","Action","other","Resource"]

        self.ReadableDeck = {}
        self.DeckOrder = {"Troop":[],"Action":[],"other":[],"Resource":[]}

        with open("HexCardData.csv") as f:
            for line in f:
               (cardname, uuid, cardtype) = line.split("|")
               cardname = cardname.strip()
               uuid = uuid.strip()
               cardtype = cardtype.strip().split(",")[0]
               self.CardKey[uuid] = {"name":cardname, "type":cardtype}

    def generateImage(self, DeckData):
        for d in DeckData["Deck"]:
            CardName = self.CardKey[d["Guid"]["m_Guid"]]["name"]
            CardType = self.CardKey[d["Guid"]["m_Guid"]]["type"]
            #print(CardName)
            if CardType not in self.CardTypes:
                CardType = "other"
            
            if CardName in self.ReadableDeck:
                self.ReadableDeck[CardName] += 1
            else:
                self.ReadableDeck[CardName] = 1
                self.DeckOrder[CardType].append(CardName)

        for d in self.DeckOrder:
            self.DeckOrder[d].sort()

        f = open('%s.txt'%DeckData["Name"], 'w')
        f.write("Champion: %s\n"%DeckData["Champion"])
        for ourtype in self.CardTypes:
            for card in self.DeckOrder[ourtype]:
                f.write("%sx %s\n"%(self.ReadableDeck[card], card))
        f.close()

        os.system('cd ../StackIt && python StackIt.py "../HexAPIStreamingTools/%s.txt"'%(DeckData["Name"]))
        if os.path.isfile(FinalImageLocation):
            os.remove(FinalImageLocation)
        os.symlink("/media/Storage/GitHub/HexAPIStreamingTools/%s.png"%(DeckData["Name"]), FinalImageLocation)
        

#deckFormater().generateImage(sampleData)

#for s in sampleData:
#    print(s)
