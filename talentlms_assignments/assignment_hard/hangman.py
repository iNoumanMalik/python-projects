import random

def random_secret():
    random_integer = random.randint(0,4)
    SECRET_WORDS = ["cinema","dress","keyboard","fantastic","enthusiastic"]
    return SECRET_WORDS[random_integer]


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
            handle_display(guessed_letters, random_word)
        else:
            print("Wrong")
            attempts = attempts - 1
        
        if guessed_letters != set(random_word):
            continue
        break   
    
    if guessed_letters == set(random_word): # we compare same elements even ordering is changed, it does not affect
        print("You win")
    
    if attempts == 0:
        print("\nYou lost ... Hurray!")



def handle_display(guessed_letters, random_word):
    display_progress(guessed_letters, random_word)
    
    
def display_progress(guessed_letters, random_word):
    print("\n")
    for char in random_word:
        print(char if char in guessed_letters else "_", end=" ")
    if(guessed_letters != set(random_word)):
        print("\n\n____GUESS THE WORD____")
    
    
    

def main():
    ATTEMPTS = 5
    random_word = random_secret()
    guessed_letters = set()
    display_progress(guessed_letters,random_word)
    user_guess_word(random_word,ATTEMPTS)
    

main()