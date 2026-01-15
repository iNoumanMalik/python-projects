def calculate_value(list):
    sum = 0
    multiply = 1
    
    for item in list:
        sum += item
        multiply *=item
        
    average = sum/len(list)
    print(f"Sum: {sum}, Muliply: {multiply}, Average: {average}")
    

def reverse_list(list):
    rev_str = []
    for char in reversed(list):
        rev_str.append(char)
    print(rev_str)
    
    
def main():
    numbers = [1,3,4,5,7]
    print(numbers)
    calculate_value(numbers)
    reverse_list(numbers)
    
main()