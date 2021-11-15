
guess = input("Guess what number I'm hidding: ")

var1 = "5"


if var1 == guess:
    print("You guessed the number")
elif var1 <= guess:
    print("Your guess is too high!")
elif var1 >= guess:
    print("Your guess is too low!")