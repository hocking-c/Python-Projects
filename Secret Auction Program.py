from art import logo
print(logo)
print("Welcome to the Secret Auction Program")

bids = {}
bidding_finished = False

def highest_bidder(bidding_record):
    highest_bid = 0
    #{"Angela": 123, "James": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    should_continue = input("Are there any other users who would like to place a bid? Type 'yes' or 'no'\n").lower()
    if should_continue == "no":
        bidding_finished = True
        highest_bidder(bids)
    elif should_continue == "yes":
        clear()
