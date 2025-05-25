import random

NUM_ROUNDS = 5
score = 0

print("Welcome to the High-Low Game!")
print("--------------------------------")

for round_num in range(1, NUM_ROUNDS + 1):
    print(f"Round {round_num}")

    user_num = random.randint(1, 100)
    computer_num = random.randint(1, 100)

    print(f"Your number is {user_num}")
    guess = input("Do you think your number is higher or lower than the computer's?: ").lower()

    # Extension #1: Validate input
    while guess != "higher" and guess != "lower":
        guess = input("Please enter either 'higher' or 'lower': ").lower()

    # Game logic
    correct = False
    if guess == "higher" and user_num > computer_num:
        correct = True
    elif guess == "lower" and user_num < computer_num:
        correct = True

    if correct:
        print(f"You were right! The computer's number was {computer_num}")
        score += 1
    else:
        print(f"Aww, that's incorrect. The computer's number was {computer_num}")

    print(f"Your score is now {score}\n")

# Extension #2: Ending messages
print("Thanks for playing!")

if score == NUM_ROUNDS:
    print("Wow! You played perfectly!")
elif score >= NUM_ROUNDS // 2:
    print("Good job, you played really well!")
else:
    print("Better luck next time!")
