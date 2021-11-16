import random

var1 = (random.randint(1,9))





def main():
    guess = int(input("Guess what number I'm hidding: "))
    if var1 == guess:
        print("You guessed the number")
    elif var1 <= guess:
        print("Your guess is too high!")
        main()
    elif var1 >= guess:
        print("Your guess is too low!")
        main()

main()