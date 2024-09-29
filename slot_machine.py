import random as rnd
import copy

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100
NUM_OF_ROWS = 3
NUM_OF_COLS = 3

symbol_count = {"A": 2, "B": 4, "C": 6, "D": 8}

symbol_value = {"A": 5, "B": 4, "C": 3, "D": 2}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for i in range(lines):
        symbol = columns[0][i]

        for col in columns:
            symbol_to_check = col[i]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(i + 1)
    
    return winnings, winning_lines

def pick_and_decrement(symbols):
    symbols_keys = list(symbols.keys())
    counts = list(symbols.values())
    
    if sum(counts) == 0:
        print("No symbols left to pick!")
        return None
    
    chosen_symbol = rnd.choices(symbols_keys, counts)[0]
    
    symbols[chosen_symbol] -= 1
    
    if symbols[chosen_symbol] == 0:
        del symbols[chosen_symbol]
    
    return chosen_symbol

def get_slot_machine_spin(rows, cols, symbols):
    columns = []
    for _ in range(rows):
        column = []
        for _ in range(cols):
            value = pick_and_decrement(symbols)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for i in range(NUM_OF_ROWS):
        for j, col in enumerate(columns):
            if j != len(columns) - 1:
                print(col[i], end="|")
            else:
                print(col[i])

def deposit():
    while True:
        amount = input("What would you like to deposit? $")

        if amount.isdigit():
            amount = int(amount)

            if amount > 0:
                break
            else:
                print("Amount must be greater than zero")
        else:
            print("Please input a number. Thank you.")
    
    return amount

def get_number_of_lines():
    while True:
        num_of_lines = input("Enter the amount of lines you would like to bet on (1-" + str(MAX_LINES) + "): ")

        if num_of_lines.isdigit():
            num_of_lines = int(num_of_lines)

            if 1 <= num_of_lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines: (1" + str(MAX_LINES) + ")")
        else:
            print("Please input a number. Thank you.")
    
    return num_of_lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line (" + str(MIN_BET) + "-" + str(MAX_BET) + ")? ")

        if amount.isdigit():
            amount = int(amount)

            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("Amount must be between: (" + str(MIN_BET) + "-" + str(MAX_BET) + ")")
        else:
            print("Please input a number. Thank you.")
    
    return amount

def game(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print("You do not have enough funds to be that amount. Your current balance is: $" + str(balance))
        else:
            break
    
    print("You are betting " + str(bet) + " on " + str(lines) + " lines. Total bet is equal to: " + str(total_bet))

    copied_symbol_count = copy.deepcopy(symbol_count)
    slots = get_slot_machine_spin(NUM_OF_ROWS, NUM_OF_COLS, copied_symbol_count)

    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)

    print("You have won $" + str(winnings))
    print("You won on lines: ", *winning_lines)

    return winnings - total_bet

def main():
    balance = deposit()

    while balance > 0:
        print("Current Balance is: $" + str(balance))
        play = input("Press Enter to Play (q to quit)")

        if play == 'q':
            break

        balance += game(balance)

    print("Your final balance is: $" + str(balance))

main()