print("Welcome to my game!")
play = input("do you want to play? ")
if play.lower() != "yes" :
    quit()

print("okay let's play!")
score = 0

a1 = input("which is the longest river in the world? ")
if a1.lower() == "nile":
    print("correct!")
    score +=1
else:
    print("incorrect")

a2 = input("what does RAM stands for? ")
if a2.lower() == "random access memory":
    print("correct!")
    score +=1
else:
    print("incorrect")

a3 = input("what is the value of pie? ")
if a3.lower() == "3.14":
    print("correct!")
    score +=1
else:
    print("incorrect")

a4 = input("what does PSU stands for? ")
if a4.lower() == "power supply unit":
    print("correct!")
    score +=1
else:
    print("incorrect")

print(f"your score is {score}")
print("you got "+ str((score/4)*100) +" %.")
print("thanks for playing! ")



    