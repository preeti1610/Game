import random
# import pygame
list = ["rock", "paper","scissor"]
comp = 0
user = 0
no_of_chance = 3


while(True):
    com = random.choice(list)
    print("Enter your choice")
    u = input()
    if u == "paper" and com == "rock":
        print("you are the winner")
        user = user+1
        print("computer=",comp,"and","you=",user)
        no_of_chance = no_of_chance-1
        print("no of chances left",no_of_chance)
        if no_of_chance ==0:
            if (comp > user):
                print("GAME OVER")
                print("You are the looser")
                break
            else:
                print("GAME OVER")
                print("you are the Winner")
                break
    elif u == "rock" and com == "paper":
        comp = comp+1
        print("computer=",comp,"and","you=",user)
        print("you are the losser")
        no_of_chance = no_of_chance-1
        print("no of chances left",no_of_chance)
        if no_of_chance ==0:
            if (comp > user):
                print("GAME OVER")
                print("You are the looser")
                break
            else:
                print("GAME OVER")
                print("you are the Winner")
                break

    elif u == "rock" and com == "scissor":
        user = user+1
        print("computer=",comp,"and","you=",user)
        print("you are the winner")
        no_of_chance = no_of_chance - 1
        print("no of chances left",no_of_chance)
        if no_of_chance ==0:
            if (comp > user):
                print("GAME OVER")
                print("You are the looser")
                break
            else:
                print("GAME OVER")
                print("you are the Winner")
                break
    elif u == "scissor" and com == "rock":
        comp = comp+1
        print("computer=",comp,"and","you=",user)
        print("you are the losser")
        no_of_chance = no_of_chance - 1
        print("no of chances left",no_of_chance)
        if no_of_chance ==0:
            if (comp > user):
                print("GAME OVER")
                print("You are the looser")
                break
            else:
                print("GAME OVER")
                print("you are the Winner")
                break
    elif u == "scissor" and com == "paper":
        user = user+1
        print("computer=",comp,"and","you=",user)
        print("you are the winner")
        no_of_chance = no_of_chance - 1
        print("no of chances left",no_of_chance)
        if no_of_chance ==0:
            if (comp > user):
                print("GAME OVER")
                print("You are the looser")
                break
            else:
                print("GAME OVER")
                print("you are the Winner")
                break
    elif u == "paper" and com == "scissor":
        comp = comp+1
        print("computer=",comp,"and","you=",user)
        print("you are the losser")
        no_of_chance = no_of_chance - 1
        print("no of chances left",no_of_chance)
        if no_of_chance ==0:
            if (comp > user):
                print("GAME OVER")
                print("You are the looser")
                break
            else:
                print("GAME OVER")
                print("you are the Winner")
                break
    elif u ==com:
        print("No one win please try again")
        print("computer=",comp,"and","you=",user)
    else:
        print("try again")
        continue



