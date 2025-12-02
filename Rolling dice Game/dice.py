import random


choice = input("roll the dice? (yes/no): ")
if choice == "yes":
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print(f" the first number of the die was {die1} and the second was {die2}")

elif choice == "no":
    print("Thanks for playing")

else:
    print("You entered an Invalid choice, please choose yes or no.")
