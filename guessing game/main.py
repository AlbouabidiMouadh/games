import random


def play_again():
    reply = input('do u want to play again (Y or N) : ')
    while reply.upper() == "Y":
        game()
        reply = input('do u want to play again (Y or N) : ')


def result(random_number, guess):
    if random_number == guess:
        print("u won")
    elif random_number > guess:
        print("less than the number")
    elif random_number < guess:
        print("bigger than the number")
    print(f"the right answer is = {random_number}")


def hard():
    print("u have chosen the hard mode")
    random_number = random.randint(1, 1000)
    guess = int(input("give a number between 1 and 1000 : "))
    result(random_number, guess)


def easy():
    print("u have chosen the easy mode")
    random_number = random.randint(1, 10)
    guess = int(input("give a number between 1 and 10 : "))
    result(random_number, guess)


def normal():
    print("u have chosen the normal mode")
    random_number = random.randint(1, 100)
    guess = int(input("give a number between 1 and 1000 : "))
    result(random_number, guess)


def game():
    level = input("choose the level u want : n for normal , e for easy and h for hard : ")
    if level.upper() == "E":
        easy()
    elif level.upper() == "N":
        normal()
    elif level.upper() == "H":
        hard()


print("hello in our guessing game !")
game()
play_again()
