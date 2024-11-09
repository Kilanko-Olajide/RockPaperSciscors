import random

starter = True
listing = ["rock", "paper", "sciscors"]


win = 0
loss = 0
tie = 0

print("Play the game of rock, paper and sciscors with Mr. Computer.")
while starter:
    index = random.randint(0,2)
    computer_input = listing[index]

    if win == 1:
        wintimes = "time"
    else:
        wintimes = "times"


    if loss == 1:
        losstimes = "time"
    else:
        losstimes = "times"


    if win+loss+tie == 1:
        alltime = "time"
    else:
        alltime = "times"


    if tie == 1:
        tietimes = "time"
    else:
        tietimes = "times"


    user_input = input("Enter either rock paper or sciscors: ").lower()

    if user_input == "quit":
        if win == 0:
            print("You did not win at all.")
            print(f"You played against Mr. Computer {win+loss+tie} {alltime} and won none.")
            break

        elif win > loss:
            print("You won Mr. Computer!!!")

        elif win == loss:
            print("This game was a tie between you and Mr. Computer!!!")
            continue

        else:
            print("You lost to Mr. Computer")

        print(f"You played against Mr. Computer {win+loss+tie} {alltime}.")
        print(f"You won {win} {wintimes}, lost {loss} {losstimes} and tied with the computer {tie} {tietimes} .")
        break


    elif user_input not in listing:
        print("You must enter either rock paper or sciscors")


    else:
        if user_input == "rock" and computer_input == "sciscors":
            win +=1
            print("You are correct!!!")
            print("The computer chose sciscors!!!")

        elif user_input == "sciscors" and computer_input == "paper":
            win +=1
            print("You are correct!!!")
            print("The computer chose paper!!!")

        elif user_input == "paper" and computer_input  == "rock":
            win +=1
            print("You are correct!!!")
            print("The computer chose rock!!!")
        
        elif user_input == computer_input:
            print("You and the computer chose the same thing, lol..")
            tie += 1

        else:
            print("You are incorrect!!!")
            print(f"The computer chose {computer_input} ")
            loss +=1
