from tkinter import *
from functools import partial # To prevent unwanted windows
import random


class Game:
    def __init__(self):
        # Formatting variables..
        self.game_stats_list = [50, 6]

        # In actual program this is blank and is populated with user calculations
        self.round_stats_list = ['silver ($4)']

        self.game_frame = Frame()
        self.game_frame.grid()

        # Heading row
        self.heading_label = Label(self.game_frame, text="Play..",
                                   font="Arial 24 bold", padx=10, pady=10)
        self.heading_label.grid(row=0)

        # History button (row 1)
        self.stats_button = Button(self.game_frame,
                                   text="Game Stats",
                                   font="arial 14", padx=10, pady=10,
                                   command=lambda: self.to_stats(self.round_stats_list))
        self.stats_button.grid(row=1)

    def reveal_boxes(self):
        # Retrieve the balance from the initial function..
        current_balance = self.balance.get()
        stakes_multiplier = self.multiplier.get()

        round_winnings = 0
        prizes = []
        stats_prizes = []
        for item in range(0, 3):
            prize_num = random.randint(1, 100)

            if 0 < prize_num <= 5:
                prize = PhotoImage(file="Mystery_box_images\gold_low.gif")
                prize_list = "gold (${})".format(5 * stakes_multiplier)
                round_winnings += 5 * stakes_multiplier
            elif 5 < prize_num <= 25:
                prize = PhotoImage(file="Mystery_box_images\silver_low.gif")
                prize_list = "silver (${})".format(2 * stakes_multiplier)
                round_winnings += 2 * stakes_multiplier
            elif 25 < prize_num <= 65:
                prize = PhotoImage(file="Mystery_box_images\copper_low.gif")
                prize_list = "copper (${})".format(1 * stakes_multiplier)
                round_winnings += stakes_multiplier
            else:
                prize = PhotoImage(file="lead_low.gif")
                prize_list = "lead ($0)"

            prizes.append(prize)
            stats_prizes.append(prize_list)

        photo1 = prizes[0]
        photo2 = prizes[1]
        photo3 = prizes[2]

        # Display prizes & edit background..
        self.prize1_label.config(image=photo1)
        self.prize1_label.photo = photo1
        self.prize2_label.config(image=photo2)
        self.prize2_label.photo = photo2
        self.prize3_label.config(image=photo3)
        self.prize3_label.photo = photo3

        # Deduct cost of game
        current_balance -= 5 * stakes_multiplier

        # Add winnings
        current_balance += round_winnings

        # Set balance to new balance
        self.balance.set(current_balance)

        balance_statement = "Game Cost: ${}\nPayback: ${} \n" \
                            "Current Balance: ${}".format(5 * stakes_multiplier, round_winnings, current_balance)

        # Add round results to statistics list
        round_summary = "{} | {} | {} - Cost: ${} | " \
                        "Payback: ${} | Current Balance: " \
                        "${}".format(stats_prizes[0], stats_prizes[1],
                                     stats_prizes[2],
                                     5 * stakes_multiplier, round_winnings,
                                     current_balance)
        self.round_stats_list.append(round_summary)
        print(self.round_stats_list)
        # Edit label so user can see their balance
        self.balance_label.config(text=balance_statement)

        if current_balance < 5 * stakes_multiplier:
            self.play_button.config(state=DISABLED)
            self.game_box.focus()
            self.play_button.config(text="Game Over")

            balance_statement = "Current Balance: ${}\n " \
                                "Your balance is too low. You can only quit " \
                                "or view yours stats. Sorry about that.".format(current_balance)
            self.balance_label.config(fg="#660000", font="arial 10 bold",
                                      text=balance_statement)

    def to_quit(self):
        root.destroy()


class Start:
    def __init__(self, parent):

        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Mystery Heading(row 0)
        self.mystery_box_label = Label(self.start_frame, text="Mystery Box Game",
                                       font="Arial 19 bold")
        self.mystery_box_label.grid(row=1)

        # Help button (row 2)
        self.help_button = Button(self.start_frame, text="Help",
                                  command=self.to_help)
        self.help_button.grid(row=2, pady=10)

    def to_help(self):
        get_help = Help(self)


class Help:
    def __init__(self, partner):

        # Disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.help_box = Toplevel()

        # If users press cross at top, closes help and 'released' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300)
        self.help_frame.grid()

        # Set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                 font="arial 14 bold")
        self.how_heading.grid(row=0)

        help_text="Choose an amount to play with and then choose the stakes. " \
                  "Higher stakes cost more per round but you can win more as well.\n\n" \
                  "When you enter the play area, you will see three mystery " \
                  "boxes. To reveal the contents of the boxes, click the " \
                  "'Open Boxes' button. If you don't have enough money to play, " \
                  "the button will turn red and you will need to quit the game.\n\n" \
                  "The contents of the boxes will be added to your balance. " \
                  "The boxes could contain..\n\n" \
                  "Low: Lead ($0) | Copper ($1) | Silver ($2) | Gold($10)\n" \
                  "Medium: Lead($0) | Copper ($2) | Silver ($4) | Gold ($25)\n" \
                  "High: Lead($0) | Copper ($5) | Silver ($10) | Gold ($50)\n\n" \
                  "If each box contains gold you earn $30 (low stakes). If " \
                  "they contained copper, silver and gold, you would receive " \
                  "$14 ($1 + $2 + $10) and so on."

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text=help_text,
                               justify=LEFT, wrap=400, padx=10, pady=10)
        self.help_text.grid(row=1)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("title goes here")
    something = Start(root)
    root.mainloop()
