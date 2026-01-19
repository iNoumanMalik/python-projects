import random

def random_secret():
    SECRET_WORDS = ["cinema","dress","keyboard","fantastic","enthusiastic"]
    return random.choice(SECRET_WORDS)
    # random_integer = random.randint(0,len(SECRET_WORDS)-1)
    # return SECRET_WORDS[random_integer]

def display_progress(guessed_letters, secret_word):
    print("\n")
    for char in secret_word:
        print(char if char in guessed_letters else "_", end=" ")
    print("\n\n____GUESS THE WORD____")
        

def play_game(secret_word, attempts):  
    guessed_letters = set()
    wrong_guessed = set()
    
    display_progress(guessed_letters, secret_word)
    
    while attempts > 0:
        print(f"Remaining attempts: {attempts}")   
        user_guess = input("Enter a letter: ").lower()
        
        if len(user_guess) != 1 or not user_guess.isalpha():
            print("Enter one alphabet character!")
            continue
        
        if user_guess in guessed_letters or user_guess in wrong_guessed:
            print("You already guessed this word")
            continue
        
        if user_guess in secret_word:
            guessed_letters.add(user_guess)
            print("Correct")
        else:
            wrong_guessed.add(user_guess)
            attempts = attempts - 1
            print("Wrong")

        display_progress(guessed_letters, secret_word)
        
        if set(secret_word) == guessed_letters: # we compare same elements even ordering is changed, it does not affect
            print("\nYou WIN! The word was:", secret_word)
            return True
    
    print("\nYou LOST! The word was:", secret_word)
    return False

def main():
    ATTEMPTS = 5
    
    while True:
        secret_word = random_secret()
        play_game(secret_word,ATTEMPTS)
        
        choice = input("\nReplay? (y/n)").lower()
        if choice !="y":
            print("Thanks for playing")
            break   
    
main()