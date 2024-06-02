import random

def generate_number(num_digits):
    return [random.randint(0, 9) for _ in range(num_digits)]

def get_guess(num_digits):
    while True:
        guess = input(f"Enter your {num_digits}-digit guess: ")
        if len(guess) == num_digits and guess.isdigit():
            return [int(d) for d in guess]
        print("Invalid input. Please try again!")

def check_guess(number, guess):
    correct_digits = [d1 == d2 for d1, d2 in zip(number, guess)]
    correct_positions = sum([d1 == d2 for d1, d2 in zip(number, guess)])
    return correct_positions, correct_digits

def play_mastermind(num_digits):
    player1_number = generate_number(num_digits)
    print("Player 1 has set the number. Player 2, start guessing!")

    attempts = 0
    while True:
        guess = get_guess(num_digits)
        attempts += 1
        correct_positions, correct_digits = check_guess(player1_number, guess)
        print(f"Correct positions: {correct_positions}, Correct digits: {correct_digits}")
        if correct_positions == num_digits:
            print("Player 2 wins! Congratulations!")
            break

    print("Now it's Player 1's turn to guess.")
    player2_number = generate_number(num_digits)
    attempts2 = 0
    while True:
        guess = get_guess(num_digits)
        attempts2 += 1
        correct_positions, correct_digits = check_guess(player2_number, guess)
        print(f"Correct positions: {correct_positions}, Correct digits: {correct_digits}")
        if correct_positions == num_digits:
            if attempts2 < attempts:
                print("Player 1 wins! Congratulations!")
            else:
                print("Player 2 wins! Congratulations!")
            break

play_mastermind(4)  # Play with 4-digit numbers