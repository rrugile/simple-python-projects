import random

top_of_range = input("Type a number: ")

#must ensure top_of_range is a number and that it is greater than zero:
#ensure it is number using .isdigit()
#if not digit then converting it to integer will return an error
if top_of_range.isdigit():
    #since the returned number of top_of_range will be a string: "25"
    #we must convert to integer
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number larger than 0")
        quit()
else:
    print("Please type a number")
    quit()

#stop, start, step
#random.randrange(1, 11, 2)

#or can just input the stop number so randrange starts from 0 
#randrange goes up to but does not include 11
#random.randrange(11)

#if must include the stop number use randint
#random.randit(10)

random_number = random.randint(0, top_of_range)
#add a counter of guesses
guesses_made = 0

while True:
    guesses_made += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number.")
        #use continue to bring the user back to the top of the loop
        continue

    if user_guess == random_number:
        print("Correct!")
        #ensure to stop the loop soon as user makes a correct guess
        break
    else:
        print("Incorrect!")

    if user_guess == random_number:
        break
    #can have multiple elif statements
    elif user_guess > random_number:
        print("The number was too high!")
    else:
        print("The number was too low!")


#could also just use commas as that will add additional spaces:
#print("You got it in", guesses, "guesses")
if guesses_made == 1:
    print("You got it in {guesses} guess!".format(guesses=guesses_made))
else:
    print("You got it in {guesses} guesses!".format(guesses=guesses_made))