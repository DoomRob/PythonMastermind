import random

# The .randrange() function generates a random number
number = str(random.randrange(1000, 10000))

guess = input("Guess the 4 digit number: ")

# The ctr variable keeps a count of the number of tires the player takes to guess the number
tries = 1

if(guess == number):
    print("You're the Matermind!, Great Job! You guessed in 1 try")
else:

    # The game keeps going as long the Player fails to guess the correct number
    while(guess != number):
        #
        tries += 1
        court = 0
        guess = str(guess)
        number = str(number)
        correct = []
        for i in range(4):
            if guess[i] == number[i]:
                count += 1
                correct.append(guess[i])
            else:
                continue
        if(count < 4) and (count != 0):
            print("Not quite the number. But you did get ", count, " dights counted")
            print("Also these numbers in your input were correct.")

            for n in correct:
                print(n, end=' ')

            print('\n')
            print('\n')
            guess = int(input("Please enter your next set numbers: "))

        elif(count == 0):
            print("None of the numbers in your input match.")
            guess = int(input("Please enter your next set numbers: "))

if guess == number:
    print("You're become a Mastermind!")
    print("It took you only", tries, "tries")
