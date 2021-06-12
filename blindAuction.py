from replit import clear
# HINT: You can call clear() to clear the output in the console.
from art import logo

more_bidders = ""
print(logo)
print("Welcome to the secret auction program.")
bids = {}


def bid_function():
    bidder_name = input("What is your name? ")
    bid_amount = input("How much is your bid? $")
    bids[bidder_name] = bid_amount
    print(bids)
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no' :")
    if more_bidders == "yes":
        clear()
        bid_function()
    elif more_bidders == "no":
        clear()
        max_winner = max(bids, key=bids.get)
        max_bid = max(bids.values())
        print(f"The winner is {max_winner} with a bid of ${max_bid}")

#
bid_function()













