def find_vowels(str):
    count_vowels = 0
    vowels = ["a","e","i","o","u"]
    for char in str:
        if char in vowels:
            count_vowels +=count_vowels
    
    return count_vowels

print(find_vowels("Nouman"))