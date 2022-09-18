import random


def guess(range):
    random_number = random.randint(0,range)
    x = 0
    while x != random_number:
        x = int(input("Enter The Number: "))
        if x > random_number:
            print("The guessed number is larger than the original number!")
        elif x < random_number:
            print("The guessed number is smaller than the original number!")
    print("you guessed correctly!")



def computerguess(y):
    answer = "w"
    already_showed = set()
    computerguesses = 0
    
    while True:
        computerguessed = random.randint(0,y)
        if (computerguessed in already_showed):
            if len(already_showed) == y+1:
                print("Invalid input you gave!, please try again!")
                break
            else:
                pass
        else:
            
        
            print(f"The number you guessed was {computerguessed}.")
            already_showed.add(computerguessed)
            print("computer Guessed values are ", already_showed)
            answer = input("enter the answer('c' or 'w'): ")
            if (answer == "c"):
                print(f"the number of computer guesses is {computerguesses + 1}.")
                break
            else:
                computerguesses += 1
                pass
                


while True:

    try:
        opinion = input("will you guess or the you want computer to guess?('me' or 'computer'): ")
        original_range = int(input("highest range: ")) 
        
        if opinion == "me":
            guess(original_range)
        elif opinion == "computer":
            computerguess(original_range)
        elif opinion == "quit":
            break
        else:
            print("Invalid Input, Please try again.")
    except:
        print("Invalid Range, Please try again")
