from random import randint

print("Nhap Dam, La, Keo: ")
player = input()
computer= randint(0,2)
if computer == 0:
    computer = "Dam"
if computer == 1:
    computer = "Keo"
if computer == 2:
    computer = "La"
print("---")
print("you choose: " + player)
print("Computer chooses: "+ computer)
print("---")

if player == computer:
    print("Draw")
else:
    if player == "Keo":
        if computer == "La":
            print("Win!")
        else:
            print("Lose")

    elif player == "La":
        if computer == "Keo":
            print("Win!")
        else:
            print("Lose")
    
    elif player == "Dam":
        if computer == "Keo":
            print("Win!")
        else:
            print("Lose")
    else:
        print("Nhap sai!")