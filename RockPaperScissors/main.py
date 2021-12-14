import random


rps = ["R", "P", "S"]


def game():
    print("it a new game ! ")
    computer_reply = random.choice(rps)
    reply = input("write s for scissor , p for paper and r for rock  >> ")
    if reply.upper() == "S":
        if computer_reply == "S":
            print("its a draw!")
        elif computer_reply == "P":
            print("u won!")
        else:
            print("u loose")
        print(f"the computer move is {computer_reply}")
    elif reply.upper() == "P":
        if computer_reply == "P":
            print("its a draw!")
        elif computer_reply == "R":
            print("u won!")
        else:
            print("u loose")
        print(f"the computer move is {computer_reply}")
    elif reply.upper() == "R":
        if computer_reply == "R":
            print("its a draw!")
        elif computer_reply == "S":
            print("u won!")
        else:
            print("u loose")
        print(f"the computer move is {computer_reply}")


print("hello in the rsp game !")
new_game = "Y"
while new_game.upper() == "Y":
    game()
    new_game = input("do u want a new game : (y)es or (n)o > ")