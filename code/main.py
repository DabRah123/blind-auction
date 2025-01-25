from asciiart import logo

print(logo)

user_bids = {}

def input_bids():
    while True:
        user_choice = input("Type 'yes' to add a new user or 'no' to end the bid: ").lower()
        if user_choice == "yes":
            name = input("What is your name? ")
            bid = int(input("Enter your bid amount: "))
            user_bids[name] = bid  
            print("\n" * 100) 
        elif user_choice == "no":
            if user_bids:
                winner = max(user_bids, key=user_bids.get)
                print(f"The winner is {winner} with a bid of {user_bids[winner]}.")
            else:
                print("No bids were placed.")
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

input_bids()
