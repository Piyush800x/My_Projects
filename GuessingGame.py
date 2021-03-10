import random


def main():
    number = random.randint(1, 20)
    guess = int(input("Enter a number between 1 to 20: "))

    while True:
        if number != guess:
            if guess > number:
                print("You guessed higher!"
                      " Guess lower: ")
                guess = int(input("Enter a number between 1 to 20: "))
            elif guess < number:
                print("You guessed lower"
                      " Guess higher: ")
                guess = int(input("Enter a number between 1 to 20: "))
        else:
            print("You guessed it!")
            break


def play_or_quit():
    while True:
        input_result = input("Do you want to play again? "
                             "Y to continue,Q to quit: ".casefold())
        if input_result == "y".casefold():
            return main()
        elif input_result == "q".casefold():
            break


main()
play_or_quit()
