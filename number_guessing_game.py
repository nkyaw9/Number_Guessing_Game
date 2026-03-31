import random

def main():
# Gets the range from user
    while True:
        try:
            lowerBound = int(input("Lower bound: "))
            upperBound = int(input("Upper bound: "))
            if lowerBound == upperBound:
                raise Exception("Lower and upper bound cannot be the same")
            break
        except ValueError:
            print("Please type in an integer value")
        except Exception as e:
            print(e)


    number = random.randrange(lowerBound, upperBound + 1)
    counter = 1


    while True:
        try:
            guess = int(input(f"Guess {counter}: "))
            counter += 1
           
        except ValueError:
            print("Please type in an integer value")


        result = prox(number, guess, lowerBound, upperBound)
        if result == 1:
            print("Correct!")
            print("Total Guesses: ", counter - 1)
            break
        print(result)




def prox(number, guess, lowerBound, upperBound):


    if guess < lowerBound or guess > upperBound:
        return "Out of range"
    elif guess > number:
        return "Too high"
    elif guess < number:
        return "Too low"
   
    return 1

main()
