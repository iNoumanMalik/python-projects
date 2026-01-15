def fahren_to_celsius(f):
    celsius = (f-32)*(5/9)
    return celsius
 
def celsius_to_fahren(c):
    fahren = c*(9/5)+32
    return fahren

def main():
    while(True):
        print("Choose an option: \n1.Fahrenheit to Celsius\n2.Celsius to Fahrenheit: ")
        choice = input("Your choice: ").strip()

        if(choice == "1"):
            f = float(input("Enter temperature in fahrenheit: "))
            c = fahren_to_celsius(f)
            print(c,"C")

        elif(choice == "2"):
            c = float(input("Enter temperature in Celsius: "))
            f = celsius_to_fahren(c)
            print(f,"F")
        else:
            print("Invalid Option")

main()