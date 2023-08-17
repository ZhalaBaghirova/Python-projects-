print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() =="no":
    quit()

print("Let's start our quiz!")
score=0

answer= input("What does LAN stand for? ").lower()
if answer=="local area network":
    print("Correct")
    score+=1
else:
    print("False")

answer= input("What does CPU stand for? ").lower()
if answer=="central processing unit":
    print("Correct")
    score+=1
else:
    print("False")

answer= input("What does GPU stand for? ").lower()
if answer=="graphics processing unit":
    print("Correct")
    score+=1
else:
    print("False")

answer= input("What does RAM stand for? ").lower()
if answer=="random access memory":
    score+=1
    print("Correct")
else:
    print("False")

answer= input("What does PSU stand for? ").lower()
if answer=="power supply":
    print("Correct")
    score+=1
else:
    print("False")

print("You got "+str(score*5)+" points and "+str(score)+" questions correct! ")
print(str((score/5)*100)+"%")