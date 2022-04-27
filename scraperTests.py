# Author: Ethan Mahoney
# Class: CS491 - DevOps
# Project: Unit test class used to test functionality
# of modularized functions
import unittest
from Menu import Menu
from Player import Player
from Scraper import Scraper

class ScraperUnitTest(unittest.TestCase):
    def test_instance_menu(self):
        self.menu = Menu()
        self.assertIsInstance(self.menu, Menu)

    def test_correct_choice(self):
        self.menu = Menu()
        self.menu.setChoice("1")
        self.assertEqual(self.menu.getChoice(), "1")
        
    def test_wrong_choice(self):
        self.menu = Menu()
        self.menu.setChoice("2")
        self.assertNotEqual(self.menu.getChoice(), "1")

    def test_correct_first_name(self):
        self.player = Player()
        self.player.setFullName("Henry", "Aaron")
        self.assertEqual(self.player.getFirstName(), "henry")
        
    def test_wrong_first_name(self):
        self.player = Player()
        self.player.setFullName("Henry", "Aaron")
        self.assertNotEqual(self.player.getFirstName(), "Henry")

    def test_correct_last_name(self):
        self.player = Player()
        self.player.setFullName("Henry", "Aaron")
        self.assertEqual(self.player.getLastName(), "aaron")
        
    def test_wrong_last_name(self):
        self.player = Player()
        self.player.setFullName("Henry", "Aaron")
        self.assertNotEqual(self.player.getFirstName(), "Aaron")

    def test_correct_player_count(self):
        self.menu = Menu()
        self.menu.increaseCount()
        self.assertEqual(self.menu.getPlayerCount(), 1)
      
    def test_wrong_player_count(self):
        self.menu = Menu()
        self.menu.increaseCount()
        self.assertNotEqual(self.menu.getPlayerCount(), 0)

    def test_correct_stats(self):
        self.player = Player()
        stats = ["1948", "23", "NYY", "AL", "125", "497", "469", "70", "143", "24", "10", "14", 
        "98", "3", "3", "25", "24", ".305", ".341", ".488", ".830", "120", "229", "9", "1", "2", 
        "", "5", "29H", "AS,MVP-29"]

        self.player.addStats(stats)
        self.assertIs(stats, self.player.getStats()[1])
        
    def test_wrong_stats(self):
        self.player = Player()
        stats = ["1948", "23", "NYY", "AL", "125", "497", "469", "70", "143", "24", "10", "14", 
        "98", "3", "3", "25", "24", ".305", ".341", ".488", ".830", "120", "229", "9", "1", "2", 
        "", "5", "29H", "AS,MVP-29"]

        self.player.addStats(stats)
        self.assertIsNot(stats, self.player.getStats())

    def test_correct_output(self):
        self.player = Player()
        stats = ["1948", "23", "NYY", "AL", "125", "497", "469", "70", "143", "24", "10", "14", 
        "98", "3", "3", "25", "24", ".305", ".341", ".488", ".830", "120", "229", "9", "1", "2", 
        "", "5", "29H", "AS,MVP-29"]

        self.player.addStats(stats)
        output = "Year | Age | Tm | Lg | G | PA | AB | R | H | 2B | 3B | HR | RBI | SB | CS | BB | SO | BA | OBP | SLG | OPS | OPS+ | TB | GDP | HBP | SH | SF | IBB | Pos | Awards | \n1948 | 23 | NYY | AL | 125 | 497 | 469 | 70 | 143 | 24 | 10 | 14 | 98 | 3 | 3 | 25 | 24 | .305 | .341 | .488 | .830 | 120 | 229 | 9 | 1 | 2 |  | 5 | 29H | AS,MVP-29 | \n"
        self.assertEqual(self.player.__str__(), output)

    def test_add_player(self):
        self.menu = Menu()
        self.menu.addPlayer(Player("yogi", "berra"))
        self.assertEqual(len(self.menu.players), 1)

    def test_correct_link(self):
        self.scraper = Scraper()
        self.scraper.link = self.scraper.constructLink("yogi", "berra")
        link = "https://www.baseball-reference.com/players/b/berrayo01.shtml"
        self.assertEqual(self.scraper.link, link)
        
    def test_correct_link(self):
        self.scraper = Scraper()
        self.scraper.link = self.scraper.constructLink("yogi", "berra")
        link = "https://www.baseball-reference.com/players/b/berrayogi01.shtml"
        self.assertNotEqual(self.scraper.link, link)

    def test_scrape_enough_info(self):
        self.scraper = Scraper()
        player = self.scraper.scrapeInfo(Player("yogi", "berra"), 1946)
        self.assertEqual(len(player.playerStats), 2)


if __name__ == "__main__":
    unittest.main()
