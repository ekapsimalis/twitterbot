import logic
from sys import exit
from tkinter import Tk            #Later implementation for GUI Interface
from tkinter import Label, Entry  #Later implementation for GUI Interface

if __name__ == "__main__":
    print("--------------------------------------------------")
    logic.showChanges()
    followers = logic.totalFollowers()
    print("You have " + str(followers) + " followers")
    print("--------------------------------------------------")
    logic.show_newest_mentions()
    print("--------------------------------------------------")
    print("TOP GREEK TRENDS RIGHT NOW")
    logic.show_trends()
    print("--------------------------------------------------")

    while True:
        print("----------------MAIN MENU-----------------")
        print("1--> UPDATE STATUS")
        print("2--> SHOW YOUR TIMELINE")
        print("3--> SEARCH IN TWITTER")
        print("PRESS ANY KEY TO QUIT")
        choice = input("Select: ")
        if choice == '1':
            tweet = input("What do you want to write? ")
            logic.update_status(tweet)
        elif choice == '2':
            logic.show_timelline()
        elif choice == '3':
            querry = input("Search for: ")
            logic.searchbyNumbers(querry)
        else:
            exit(0)



       


