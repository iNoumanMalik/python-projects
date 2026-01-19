import random

def random_secret():
    random_integer = random.randint(0,4)
    SECRET_WORDS = ["cinema","dress","keyboard","fantastic","enthusiastic"]
    return SECRET_WORDS[random_integer]

def find_char_position(user_guess, random_word):
    positions = []
    for index,value in enumerate(random_word):
        if value == user_guess:
            positions.append(index)
    
    print(positions)
    return positions

def user_guess_word(random_word, attempts):  
    guessed_letters = set()
    while attempts > 0:
        print(f"Remaining attempts: {attempts}")   
        user_guess = input("Your choice: ").lower()
        
        if len(user_guess) != 1 or not user_guess.isalpha():
            print("Enter one character!")
            continue
        
        if user_guess in random_word:
            guessed_letters.add(user_guess)
            print("Correct")
            find_char_position(user_guess, random_word)
        else:
            print("Wrong")
            attempts = attempts - 1
        
        if guessed_letters != set(random_word):
            continue
        break
    
    print(guessed_letters)       
    
    if guessed_letters == set(random_word): # we compare same elements even ordering is changed, it does not affect
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