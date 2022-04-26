from Menu import Menu
from Player import Player
import scraperTests

if __name__ == "__main__":
    print("Welcome To The Baseball Player Information Program")
    print("---------------------------------------------------")
    print("This program provides player statistics based on the name of the player entered!\n")


    menu = Menu()

    while True:
        print("Please select an option:")
        print("1. Retrieve Player Stats")
        print("2. Save Player Stats to File")
        print("3. Exit")
        choice = input()
        menu.setChoice(choice)

        if menu.getChoice() == "1":
            first, last = input("\nEnter the full name of a Baseball Player (first last): ").split()
            year = input("Enter the year in which you would like there stats: ")

            try:
                player = menu.getPlayerStats(Player(first, last), year)

                if menu.hasPlayer(player.getFirstName(), player.getLastName()):
                    play = menu.getPlayer(player.getFirstName(), player.getLastName())
                    play.addStats(player.getStats()[1])
                    print(play)
                else:
                    menu.addPlayer(player)
                    menu.increaseCount()
                    print(menu.players[menu.getPlayerCount()-1])
            except:
                print("\nError: Could not get player stats! (Could be misspelled name or invalid year)\n")
        elif menu.getChoice() == "2":
            first, last = input("\nWhich player would you like to save stats for (first last): ").split()
            if menu.hasPlayer(first, last):
                try:
                    with open(first + last + ".txt", "w") as outfile: 
                        player = menu.getPlayer(first, last)
                        outfile.write(player.__str__())
                        print("\n")
                except:
                    print("\nError: Could not open a text file for output!\n")
            else:
                print("\nError: Must retrieve a player's stats or spelt player name incorrectly!\n")
        elif menu.getChoice() == "3":
            break
        else:
            print("\nError: Please enter a valid option!")



