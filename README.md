# my-project
OVERVIEW OF THIS PROJECT
This is a simple number guessing game where the player tries to guess a randomly generated number between 1 and 100. The player can choose between two difficulty levels, which determine the number of attempts they have to guess the number.
Code Breakdown
1.Imports:
CODE:
            import random
            from art import logo
            print(logo)
  i.The random module is used to generate a random number.
  ii.The logo is imported from an external module (assumed to contain a decorative ASCII art logo) and printed to the console.
2.Game Initialization:
CODE:
            easy_turn = 10
            hard_turn = 5
            print("Welcome to the Number Guessing Game!")
            print("I'm thinking of a number between 1 and 100.")
            answer = random.randint(1, 100)
            # print(f" the correct answer is  {answer} ")
            level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  i.easy_turn and hard_turn variables define the number of attempts based on the difficulty level.
  ii.A random number (the answer) is generated between 1 and 100.
  iii.The player is prompted to select a difficulty level, and their input is converted to lowercase for consistency.
  
3.Function Definitions:

          check_answer(user_guess, actual_answer, turns):

  i.This function checks if the user's guess is higher, lower, or equal to the actual answer.
  ii.It provides feedback ("Too high" or "Too low") and decrements the number of turns remaining.
  iii.If the guess is correct, it congratulates the player but does not return turns (you may want to return turns unchanged for a cleaner structure).
          set_difficulty():
  This function returns the number of turns based on the player's chosen difficulty level (easy or hard).
  
4.Main Game Loop (game() function):

code
      def game():
          turns = set_difficulty()
          guess = 0
      
          while guess != answer:
              print(f"You have {turns} attempts remaining to guess the number.")
              guess = int(input("Make a guess: "))
              turns = check_answer(guess, answer, turns)
              if turns == 0:
                  print("you have run out of guess you lose")
                  return
The game starts by setting the number of turns based on the selected difficulty.
A while loop continues as long as the player has not guessed the answer.
The player is informed of how many attempts remain.
The player is prompted to make a guess, which is converted to an integer.
The check_answer function is called to provide feedback and adjust the number of remaining turns.
If the player runs out of turns, a message is displayed indicating they have lost.
Potential Improvements
Input Validation: Add error handling for non-integer inputs when asking for a guess.
Return Value in check_answer: Ensure that the function always returns the number of turns.
Difficulty Level Handling: Move the difficulty input into the game() function to allow for replayability without restarting the program.
This structure sets up a basic interactive game experience and can be expanded with more features like hints or a scoring system if desired!
