import random
number_for_guessing = random.randint(1, 100)
no_of_attempts = 0
print("🎯 Welcome to the Number Guessing Game!!!!!")
print("I'm thinking of a number between 1 and 100..........")
while True:
    user_guess = input("Enter your guess: ")
    if not user_guess.isdigit():
        print("❌ Please enter a valid number.")
        continue
    user_guess = int(user_guess)
    no_of_attempts += 1
    if user_guess < number_for_guessing:
        print("📉 Too low. Please try again.....")
    elif user_guess > number_for_guessing:
        print("📈 Too high. Please try again.....")
    else:
        print(f"🎉 Yes correct! The number was {number_for_guessing}.")
        print(f"✅ You guessed the correct number in {no_of_attempts} attempts.")
        break
