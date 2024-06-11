import random as rd

def spin_row():
    symbols = ['💰', '🪙', '💲', '💎', '❌']
    results = [rd.choice(symbols) for _ in range(3)]
    return results

def print_row(row):
    print("****************")
    print("  |  ".join(row))
    print("****************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '💰':
            return bet * 4
        elif row[0] == '💎':
            return bet * 6
        elif row[0] == '🪙':
            return bet * 3
        elif row[0] == '💲':
            return bet * 5
        elif row[0] == '❌':
            return bet * 2
    elif row[0] == row[1] or row[1] == row[2] or row[0] == row[2]:
        return int(bet * 1.5)
    else:
        return 0

def add_money():
    while True:
        try:
            money = int(input("How much do you want to add? "))
            if money > 1000:
                print("Enter a smaller amount (less than or equal to 1000).")
            else:
                return money
        except ValueError:
            print("Please enter a valid number.")

def main():
    balance = 100

    print("*************************")
    print("Welcome to the slot game")
    print("Symbols: 💰   🪙   💲   💎   ❌")
    print("*************************")

    while balance > 0:
        print(f'Current balance: Rs.{balance}')
        if balance < 20:
            add_balance = input("Do you want to add more money? (Y/N): ").upper()
            if add_balance != 'N':
                sum = add_money()
                balance += sum
                print(f"Money added successfully. Updated balance is Rs.{balance}")
            else:
                break

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a correct number.")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient balance.")
            continue

        if bet <= 0:
            print("Bet must be greater than zero.")
            continue

        balance -= bet

        print("Spinning....")
        row = spin_row()
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won Rs.{payout}!")
        else:
            print("Better luck next time.")

        balance += payout

        play_again = input("Do you want to play again? (Y/N): ").upper()
        if play_again != 'Y':
            print("Thank you for playing.")
            break
    
    print("****************************************")
    print(f'Game over. Your final balance is Rs.{balance}')
    print("****************************************")

if __name__ == "__main__":
    main()
