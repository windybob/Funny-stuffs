import random

# Convert input values to integers
smallestNumber = int(input("What is the smallest number you want to guess? "))
biggestNumber = int(input("What is the biggest number you want to guess? "))

# Generate a random number within the specified range
x = random.randint(smallestNumber, biggestNumber)

while True:
    print(x)
    # Ask for input
    answer = input(f"Guess a random number ranging from {smallestNumber} to {biggestNumber}: ")
    # Checking answer
    if answer.lower() == "exit" or answer.lower() == "quit" or answer.lower() == "give up":
        print(f"The number was {x}. Bye!")
        break
    elif int(answer) > x:
        print("Smaller!")
    elif int(answer) < x:
        print("Bigger!")
    else:
        print("Correct!")
        replayRequest = input("Would you like to play again? (yes/no): ").lower() # Ask if player want to play again and convert input to lowercase
        if replayRequest == "yes":
            x = random.randint(smallestNumber, biggestNumber)
        elif replayRequest == "no":
            print("Bye!")
            break
        else:
            print("I will take that as a no then.")
            break