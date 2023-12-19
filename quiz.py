print("Welcome to the quiz, gamer!")

playing = input("Would you like to play? ")

#ensure input by the user is changed into lowercase so that it can always be recognised
if playing.lower() != "yes":
    quit()

print("Okay! Let's play the game :)")
score = 0

#In Python, variables can be reassigned with new values without any problem. 
#The previous value of the variable is simply overwritten, 
#and the variable now holds the new value. 
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("That's correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("That's correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("That's correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ").lower()
if answer == "power supply":
    print("That's correct!")
    score += 1 
else:
    print("Incorrect!")

percentage_scores = (score / 4)*100
print("That is a score of {percentage}%!".format(percentage = percentage_scores))