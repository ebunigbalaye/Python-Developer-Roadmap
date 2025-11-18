import random

def greeting():
    """This function prints out a personalized greeting to the screen"""
    player_name = input("What's your name ?")
    print(f"Hello {player_name}")
   
def difficulty():
    """This function queries the user for their desired difficulty
    and returns the chosen difficulty"""
    print("Levels :")
    print("Easy --> 10 tries")
    print("Medium --> 7 tries")
    print ("Hard --> 5 tries")
    difficulty = input("Pick a level ")
    return difficulty.lower()

def number_chosen():
    """This function chooses a number at random between 1 and 100"""
    number = random.randint(1,100)
    return number

def no_of_tries(difficulty): 
    """This function returns the number of tries a player gets based on the difficulty chosen"""
    if difficulty == "easy":
        tries = 10
    elif difficulty == "medium":
        tries = 7
    else:
        tries = 5
    print(f"You're playing in {difficulty} mode. You get {tries} tries to guess the number")
    return tries
 
def user_guess():
    """This function prompts the user to guess and returns the guess an integer"""
    guess = input("Enter a number between 1 and 100 ")
    return int(guess)

def number_check(user_guess,number):
    """This function checks the user's guess against the computer generated random int and prints out feedback"""
    if user_guess > number:
        print("TOO LARGE")
    elif user_guess < number:
        print ("TOO SMALL")
    else :
        print("CORRECT")

def interest():
    """This function queries the user's interest in gameplay"""
    interest = input("Would you like to play 'Y' for yes and any other key for no:").lower()
    if interest =='y':
        return True
    else:
        return False
  
    

    

print("Welcome to Muiz's Number Guessing Game")
greeting()
proceed = interest()
while proceed:
    tries = no_of_tries(difficulty())
    number = number_chosen()
    while tries > 0 :
        player_guess = user_guess()
        if player_guess == number:
             print (f"You guessed the number with {tries} tries left, You win!!")
             break
        else:
            number_check(player_guess,number) 
            tries -= 1
            print (f"You have {tries} tries left")
    else:
        print ("You've run out of tries, You lose ")
        print(f"The number was {number}")
    
    proceed = interest()