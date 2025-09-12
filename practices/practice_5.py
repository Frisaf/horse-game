import random

def input_int(prompt) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def number_guess(guess) -> int:
    if guess == answer:
        print("Correct! Good job.")
        return guess
    else:
        print("Nope, try again.")
        return guess

answer = random.randint(1, 10)
total_score = 0

def main() -> int:
    amount_of_guessess = input_int("How many times do you think you will have to guess until you get the right answer?\n> ")
    guessess = 0

    while True:
        user_guess = number_guess(input_int("Guess a number between 1-10!\n> "))
        guessess += 1

        if user_guess == answer:
            break

        else:
            if user_guess > answer:
                print("Your guess was too high.")
            
            else:
                print("Your guess was too low.")

    final_score = abs(amount_of_guessess - guessess)

    print(f"You estimated that you would be able to guess the number in {amount_of_guessess} attempt(s). You guessed the number after {guessess} attempt(s).")
    print("Your final score was " + str(final_score))

    return final_score

while True:
    print("NUMBER GUESS!\nGuess a random number between 1-10!")

    total_score += main()

    print(f"You have a total of {total_score} points.")

    play_again_answer = input("Play again? [Y/n]\n> ")

    if play_again_answer.lower() == "n":
        print("Okay, goodbye!")
        break

    elif play_again_answer == "Y" or play_again_answer == "":
        print("Let's go again!")

    else:
        print("Please answer Y or n.")