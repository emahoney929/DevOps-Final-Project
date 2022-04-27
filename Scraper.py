# Author: Ethan Mahoney
# Class: CS491 - DevOps
# Project: Scraper class used to webscrape player information from 
# Baseball Reference website using Beautiful Soup
from bs4 import BeautifulSoup
from requests import get

class Scraper:
    def __init__(self):
        self.link = ""
        self.html = None

    # Constructs a link based off the name of the baseball player provided
    def constructLink(self, first, last):
        if len(last) > 5:
            last = last[:5]
        first = first[0:2]

        # Link is similar for all players except for sublte differnces depending on last and first name
        return "https://www.baseball-reference.com/players/" + last[0] + "/" + last + first + "01.shtml"


    # Uses beautiful soup to scrape information from the web link and add the stats to a list
    def scrapeInfo(self, player, year):
        self.link = self.constructLink(player.getFirstName(), player.getLastName())
        html = get(self.link).text
        soup = BeautifulSoup(html, "html.parser")
        table = soup.find("tbody")
        rows = table.find_all("tr")
        stats = []
        stats.append(year)

        for row in rows:
            if row["class"][0] == "full" and row.th.text == year:
                data = row.find_all("td")
                for datum in data:
                    stats.append(datum.text)
                    
        player.playerStats.append(stats)
        return player   # Returns a player object that will be added to the list of searched players
        
