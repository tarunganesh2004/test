import random

def game():
    chosen = random.randint(1, 10)
    #print(chosen)
    count = 0
    while True:
        guess = input("Enter the guess: ")
        count+=1
        if guess.isdigit():
            guess = int(guess)
        else:
            print("Enter an integer")
            
        if guess== chosen:
            print("YOu won")
            break
        else:
            print("Try again")
    print(f"you took {count} chances")
game()   