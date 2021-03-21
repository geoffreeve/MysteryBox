from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Start:
    def __init__(self, parent):
        self.starting_funds = IntVar()
        self.starting_funds.set(0)

        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=5, pady=10)
        self.start_frame.grid()

        # Mystery Heading(row 0)
        self.mystery_box_label = Label(self.start_frame, text="Play...",
                                       font="Arial 20 bold")
        self.mystery_box_label.grid(row=0)

        # Initial Instructions (row 1)
        self.mystery_instructions = Label(self.start_frame, font="Arial 9 italic",
                                          text="Press <enter> or click the 'Open Boxes' button"
                                               " to reveal the contents of the mystery boxes.",
                                          wrap=275, justify=LEFT, pady=10)
        self.mystery_instructions.grid(row=1)

        self.value_frame = Frame(self.start_frame)
        self.value_frame.grid()

        # Three labels, (row 2, column 0)
        self.silver_label = Label(self.value_frame, font="Arial 13 bold", bg="light green",
                                  padx=15, pady=10, text="Silver\n(${})".format("?"))
        self.silver_label.grid(row=2, column=0)
        # (row 2, column 1)
        self.lead_label = Label(self.value_frame, font="Arial 13 bold", bg="light green",
                                padx=20, pady=10, text="lead\n(${})".format("?"))
        self.lead_label.grid(row=2, column=1, padx=10)
        # (row 2, column 2)
        self.copper_label = Label(self.value_frame, font="Arial 13 bold", bg="light green",
                                  padx=10, pady=10, text="copper\n(${})".format("?"))
        self.copper_label.grid(row=2, column=2)

        # Open boxes button (row 3)
        self.open_box = Button(self.start_frame, font="arial 13 bold", bg="yellow", padx=70,
                               pady=10, text="Open Boxes")
        self.open_box.grid(row=3, pady=10)

        self.info_frame = Frame(self.start_frame)
        self.info_frame.grid()

        # Game cost info (row 4)
        self.game_cost = Label(self.info_frame, font="arial 13 bold", fg="green",
                               text="Game Cost: {}".format("?"))
        self.game_cost.grid()
        # Payback info (row 5)
        self.payback_info = Label(self.info_frame, font="arial 13 bold", fg="green",
                                  text="Payback: {}".format("?"))
        self.payback_info.grid()
        # Payback info (row 5)
        self.current_balance_label = Label(self.info_frame, font="arial 13 bold", fg="green",
                                           text="Current Balance: {}".format("?"))
        self.current_balance_label.grid()

        # Help/Rules | GameStats Buttons (row 8)
        self.help_button = Button(self.start_frame, font="Arial 13 bold", bg="light grey",
                                  text="Help / Rules")
        self.help_button.grid(row=6, column=0)


class Game:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)

        # Initialise variables
        self.balance = IntVar()

        # Set starting balance to amount entered by user at start of game
        self.balance.set(starting_balance)

        # GUI Setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Heading row
        self.heading_label = Label(self.game_frame, text="Heading",
                                   font="Arial 24 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game")
    something = Start(root)
    root.mainloop()
