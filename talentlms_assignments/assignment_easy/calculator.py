def calculator(a,b,operation):
    if(operation == "+"):
        return a + b
    elif(operation == "-"):
        return a - b
    elif(operation == "*"):
        return a * b
    elif(operation == "/"):
        return a / b
    else:
        print("Invalid Input")
        return
    

while(True):
    num_a = int(input("Enter first number: "))
    num_b = int(input("Enter second number: "))
    operation = input("Enter the operation you want to perform (+,-,*,/): ")
    print(calculator(num_a,num_b, operation))
    