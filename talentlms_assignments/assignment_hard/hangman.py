import random

def random_secret():
    random_integer = random.randint(1,5)
    SECRET_WORDS = ["cinema","dress","keyboard","fantastic","enthusiastic"]
    return SECRET_WORDS[random_integer]


def user_guess_word(random_word, attempts):
    
    guessed_letters = []
    
    while attempts > 0:
        print(f"Remaining attempts: {attempts}")   
        user_guess = input("Your choice: ").lower()
        
        if len(user_guess) != 1 or not user_guess.isalpha():
            print("Enter one character!")
            continue
        
        if user_guess in random_word:
            guessed_letters.append(user_guess)
            print("Correct")
        else:
            print("Wrong")
            attempts = attempts - 1
            
        if len(guessed_letters) != len(random_word):
            continue
        break
    
    print(guessed_letters)       
    
    if guessed_letters == random_word:
        print("You win")


def display_progress(random_word):
    ATTEMPTS = 5
    
    total_words = len(random_word)
    for _ in range(total_words):
        print("_", end=" ")
        
    print("\n\n____GUESS THE WORD____")
    user_guess_word(random_word,ATTEMPTS)
    

def main():
    random_word = random_secret()
    print(random_word)
    display_progress(random_word)
    
main()