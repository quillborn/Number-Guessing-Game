import random
mystery_number = random.randint(1,100)
attempts_left = 10
guess = 0


def higher_lower(guess,mystery_number):
        """checks input against mystery number"""
        if guess > mystery_number:
            print("Too high..")
            print(f"You have {attempts_left} attempts left.")
            
        elif guess < mystery_number:
            print("Too low")
            print(f"You have {attempts_left} attempts left.")

        elif guess == mystery_number:
            print(f"The number was {mystery_number}! You Win!")
            return("win")
        



# start game
print("Welcome to the Number Guessing Game!\n")




#set difficulty
while True:
    try:
        difficulty = str(input("would you like to play hard or easy mode?").lower())
        
        if difficulty[:1].lower() == "e":
            attempts_left = 10
            print(f"You have {attempts_left} attempts.")
            break

        elif difficulty[:1].lower() == "h":
            attempts_left = 5
            print(f"You have {attempts_left} attempts.")
            break
        else:
            print("invalid input")
    except:
        print("error")



#cheatcode
# print(f"The mystery numer is {mystery_number}.")


#user attempts to guess number
print("I'm thinking of a number 1 - 100..")

while attempts_left > 0:
    try:
        guess = int(input("Guess a number: "))
        if guess < 0 or guess > 100:
            raise Exception("Guess must be between 1 and 100.")
        else:
            attempts_left -= 1

            if higher_lower(guess,mystery_number) == "win":
                break
        
            elif attempts_left == 0:
                print(f"The number I was thinking of was {mystery_number}! Game Over!")
                break
        
    except:
        print("error")

#exit game
exit()


    



            
    
        

