import logic
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
    status = input("Update your status/Press 0 to quit:")
    if status != '0':
        logic.update_status(status)
    

       


