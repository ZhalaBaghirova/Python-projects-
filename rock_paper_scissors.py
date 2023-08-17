import random

choices=["rock", "scissors", "paper"]

user_wins=0
computer_wins=0

while True:
    user_input= input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input =="q":
        break   
    if user_input not in choices:
        continue

    random_number=random.randint(0,2)
    # rock:0, paper:2 , scissors:1
    computer_guess=choices[random_number]
    print("Computer picked",computer_guess+".")

    if user_input=="rock" and computer_guess=="scissors":
        print("You won!")
        user_wins+=1

    
    elif user_input=="paper" and computer_guess=="rock":
        print("You won!")
        user_wins+=1

        
    elif user_input=="scissors" and computer_guess=="paper":
        print("You won!")
        user_wins+=1

    elif user_input==computer_guess:
        print("null!")

    else:
        print("You lost!")
        computer_wins+=1

print("You won", user_wins,"times.")
print("The computer won", computer_wins,"times.")
print("Good bye!")
    