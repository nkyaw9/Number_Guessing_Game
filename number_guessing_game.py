import random

def main():

    while True:
        try:
            # Gets the range from user
            lowerBound = int(input("Lower bound: ")) 
            upperBound = int(input("Upper bound: ")) 
            if lowerBound == upperBound: # invalid if user type same bounds
                raise Exception("Lower and upper bound cannot be the same")
            break
        except ValueError: # invalid if its not an integer
            print("Please type in an integer value")
        except Exception as e:
            print(e)

    # random number in the range
    number = random.randrange(lowerBound, upperBound + 1)
    counter = 1 # track number of guesses

    while True:
        try:
            # takes in user's guess
            guess = int(input(f"Guess {counter}: "))
            counter += 1
        except ValueError: # nvalid if its not an integer
            print("Please type in an integer value")

        # calculate high and low distance from the number
        result = prox(number, guess, lowerBound, upperBound)
        if result == 1:
            print("Correct!")
            print("Total Guesses: ", counter - 1)
            break
        print(result)

# calculate high and low distance from the number
def prox(number, guess, lowerBound, upperBound):

    if guess < lowerBound or guess > upperBound:
        return "Out of range"
    elif guess > number:
        return "Too high"
    elif guess < number:
        return "Too low"
   
    return 1 # if user guess correct

main()
