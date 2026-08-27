# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
print(art.logo)


def highest_bidder(bidder_record):
    highest_bid = 0
    winner = ''
    for bidder in bidder_record:
        big_amount = bidder_record[bidder]
        if big_amount > highest_bid:
            highest_bid = big_amount

            winner = bidder
        print(f"The winner is {winner} and the bid price is ${highest_bid}")


#from art import logo
#print(logo) #it is also possible
bids={}
user_continue=True
while user_continue:
    name=input("What is your name? ")
    price=int(input("what is your bid price: $"))
    bids[name]=price
    should_continue=input("Are there any bidders?Type 'yes' or 'no.\n").lower()
    if should_continue=='no':
        user_continue=False
        highest_bidder(bids)
    elif should_continue=='yes':
        print("\n"*20)
# def condition is always above the code

