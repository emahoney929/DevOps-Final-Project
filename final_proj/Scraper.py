from bs4 import BeautifulSoup
from requests import get

class Scraper:
    def __init__(self):
        self.link = ""
        self.html = None

    def constructLink(self, first, last):
        if len(last) > 5:
            last = last[:5]
        first = first[0:2]

        return "https://www.baseball-reference.com/players/" + last[0] + "/" + last + first + "01.shtml"


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
        return player
        
