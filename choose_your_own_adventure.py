name=input("What is your name? ")
print("Welcome", name, "to this adventure!")

answer=input("You are in a forest. There are to ways out of this place. One of them is dark the other one is light. From which way do you want to go?(light/dark) ").lower()

if answer=="light":
    answer=input("You came to a village. There are barking dogs in  one way and a house in the other side. where will you go? (house/dog): ").lower()
    if answer=="dog":
        print("You come across with people and survivied! YOU WON!")
    elif answer=="house":
        answer=input("You find out it is the house of an creepy monster. Will you stay here for a night or kill the monster? (stay/kill)): ")
        if answer=="stay":
            print("Monster ate you, you are dead! You lost!")
        elif answer=="kill":
            answer=input("You have killed the monster! You won!")
        else: 
            print("Undefined way.You lost!")
    else: 
        print("Undefined way.You lost!")
elif answer=="dark":
    answer=input("You came across with two men. One of them is young and dodgy face boy. another one is old man with smiling face. From which one you ask help? boy/man: ")
    if answer=="boy":
        print("Boy helped you and you go safely home. You won!")
    elif answer=="man":
        print("The man robbed your everything you have and beat you. You are dying. You lost!")
    else: 
        print("Undefined way.You lost!")
else: 
    print("Undefined way.You lost!")