import random
easy_turn=10
hard_turn=5
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer=random.randint(1,100)
# print(f", the correct answer is  {answer} ")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
def check_answer(user_guess, actual_answer,turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("Too high.")
        print("guess again")
        return turns-1
    
        # return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        print("guess again")
        return turns-1
        # return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")

def set_difficulty():
   
        if level=="easy":
            return easy_turn
        else:
            return hard_turn

def game():
    turns=set_difficulty()
    guess=0
    while guess!=answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))
        turns=check_answer(guess,answer,turns)
        if turns==0:
            print("you have run out of guess you lose")
            return
        # elif guess!=answer:
        #     print("guess again")
game()


    