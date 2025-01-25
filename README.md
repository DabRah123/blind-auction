# Blind Auction Program

This is a simple Python-based auction bidding program that allows users to place bids and determines the highest bidder. It features an ASCII art logo and a clean, interactive command-line interface.

---

## Features

- Displays a cool ASCII art logo at the start of the program.
- Allows multiple users to place bids.
- Dynamically determines and announces the highest bidder.
- Simple and user-friendly interface.

---

## How It Works

### Algorithm:
1. **Initialize** an empty dictionary to store user names and their bids.
2. **Display the logo** using ASCII art imported from a separate file.
3. Use a loop to:
   - Prompt the user to either add a new bid or end the bidding process.
   - If the user chooses to add a bid:
     - Ask for their name and bid amount.
     - Store the name and bid in the dictionary.
     - Clear the screen for the next user.
   - If the user chooses to end the bidding:
     - Check if there are any bids.
     - If bids exist, find the highest bid and the corresponding user.
     - Print the winner and their bid.
     - Exit the loop.
4. Handle invalid input gracefully.
5. If no bids were placed, print an appropriate message and exit.

---

## File Structure

The program is divided into two files:

1. **`asciiart.py`**: Contains the ASCII art logo.
2. **`main.py`**: Implements the main functionality of the bidding program.

---

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/auction-bidding.git
