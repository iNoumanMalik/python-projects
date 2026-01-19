import random

def random_secret():
    SECRET_WORDS = ["cinema","dress","keyboard","fantastic","enthusiastic"]
    random_integer = random.randint(0,len(SECRET_WORDS))
    return SECRET_WORDS[random_integer]


def user_guess_word(random_word, attempts):  
    guessed_letters = set()
    wrong_guessed = set()
    finish = False
    while attempts > 0:
        print(f"Remaining attempts: {attempts}")   
        user_guess = input("Your choice: ").lower()
        
        if len(user_guess) != 1 or not user_guess.isalpha():
            print("Enter one character!")
            continue
        
        if user_guess in random_word and user_guess in guessed_letters:
            print("You already guessed this word")
        
        if user_guess in random_word:
            guessed_letters.add(user_guess)
            print("Correct")
            handle_display(guessed_letters, random_word)
        else:
            print("Wrong")
            if user_guess not in wrong_guessed:
                attempts = attempts - 1
                wrong_guessed.add(user_guess)
            else:
                print("You are guessing the wrong word again")
        
        if guessed_letters != set(random_word):
            continue
        break   

    
    if guessed_letters == set(random_word): # we compare same elements even ordering is changed, it does not affect
        print("\nYou win... Hurray")
        choice = input("Replay? Enter Y/N to continue: ").lower()
        if(choice == 'y'):
            finish = True
    
    if attempts == 0:
        print("\nYou lost ... Sad!")
        choice = input("Replay? Enter Y/N to continue: ").lower()
        if(choice == 'y'):
            finish = True
        
    return finish


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
    replay = user_guess_word(random_word,ATTEMPTS)
    if replay:
        main()
        
    

main()