# Author: Ethan Mahoney
# Class: CS491 - DevOps
# Project: Player class used to hold information regarding a baseball player
class Player:
    def __init__(self, first="", last=""):
        self.firstName = first
        self.lastName = last
        self.playerStats = [["Year", "Age", "Tm", "Lg", "G", "PA", "AB", "R", "H", "2B",	
                             "3B", "HR", "RBI", "SB", "CS", "BB", "SO", "BA", "OBP", "SLG", 
                             "OPS", "OPS+", "TB", "GDP", "HBP",	"SH", "SF",	"IBB", "Pos", "Awards"]]

    # Setter
    def setFullName(self, first, last):
        self.firstName = first.lower()
        self.lastName = last.lower()

    # Getters
    def getFirstName(self):
        return self.firstName 
        
    def getLastName(self):
        return self.lastName
    
    def getStats(self):
        return self.playerStats

    def addStats(self, stats):
        self.playerStats.append(stats)

    # formats the string output of a player object for printing
    def __str__(self):
        output = ""
        for col in self.playerStats[0]:
            output += col + " | "

        output += "\n"

        for rows in self.playerStats[1:]:
            for cols in rows:
                output += cols + " | "
            output += "\n"
        return output
