from Player import Player
from Scraper import Scraper

class Menu:
    def __init__(self, choice=0):
        self.choice = choice
        self.scraper = Scraper()
        self.players = []
        self.playerCount = 0


    def setChoice(self, choice):
        self.choice = choice

    def getChoice(self):
        return self.choice

    def increaseCount(self):
        self.playerCount += 1

    def getPlayerCount(self):
        return self.playerCount

    def getPlayers(self):
        return self.players
        
    def getPlayer(self, first, last):
        for player in self.players:
            if player.getFirstName() == first and player.getLastName() == last:
                return player
        return None

    def hasPlayer(self, first, last):
        for player in self.players:
            if player.getFirstName() == first and player.getLastName() == last:
                return True
        return False

    def addPlayer(self, player):
        self.players.append(player)

    def getPlayerStats(self, player, year):
        return self.scraper.scrapeInfo(player, year)

