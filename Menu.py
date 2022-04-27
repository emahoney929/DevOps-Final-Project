# Author: Ethan Mahoney
# Class: CS491 - DevOps
# Poject: Menu class used in conjuction with driver file to
# control flow of the cmd line menu provided in the program
from Player import Player
from Scraper import Scraper

class Menu:
    def __init__(self, choice=0):
        self.choice = choice
        self.scraper = Scraper()
        self.players = []
        self.playerCount = 0

    # Getters
    def getChoice(self):
        return self.choice
    
    def getPlayerCount(self):
        return self.playerCount

    def getPlayers(self):
        return self.players
        
    def getPlayer(self, first, last):
        for player in self.players:
            if player.getFirstName() == first and player.getLastName() == last:
                return player
        return None
    
    # Setter
    def setChoice(self, choice):
        self.choice = choice

    # tracks the amount of unique players searched
    def increaseCount(self):
        self.playerCount += 1

    # checks for player in searched list
    def hasPlayer(self, first, last):
        for player in self.players:
            if player.getFirstName() == first and player.getLastName() == last:
                return True
        return False

    # adds a player to the list of people search
    def addPlayer(self, player):
        self.players.append(player)

    # returns the stats of a player given a defined year
    def getPlayerStats(self, player, year):
        return self.scraper.scrapeInfo(player, year)

