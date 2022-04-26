import unittest
from Menu import Menu
from Player import Player
from Scraper import Scraper

class ScraperIntegrationTest(unittest.TestCase):
    def test_getting_player(self):
        self.menu = Menu()
        self.menu.players.append(Player("yogi", "berra"))
        player = self.menu.getPlayer("yogi", "berra")
        self.assertEqual(player.getFirstName(), "yogi")

    def test_has_player(self):
        self.menu = Menu()
        self.menu.players.append(Player("yogi", "berra"))
        isPlayer = self.menu.hasPlayer("yogi", "berra")
        self.assertTrue(isPlayer)

    def test_scrape_info(self):
        self.scraper = Scraper()
        player = self.scraper.scrapeInfo(Player("yogi", "berra"), "1946")
        self.assertEqual(player.getFirstName(), "yogi")

    def test_get_player_stats(self):
        self.menu = Menu()
        self.menu.getPlayerStats(Player("yogi", "berra"), "1946")
        self.assertEqual(player.getFirstName(), "yogi")



if __name__ == "__main__":
    unittest.main()