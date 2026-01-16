# this is part I - calculate average
def find_average(): 
    with open("students.csv") as f:
        header = f.readline()
    
        for line in f:  
            total = 0
            average = 0
            data = line.strip()
            for marks in data[1:]:
                total = total + int(marks)
                
            average = total/(len(data)-1)
            print(f"Average marks of {data[0]} are {average}")

# following is part II - store and find contact
def show_menu():
    print("\nChoose and option from below: ")
    print("1. Add contact")
    print("2. Search existing contact")  
    
    
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter contact number: ").strip()
    
    with open("contactbook.txt","a") as f:
        f.write(f"{name},{phone}\n")
        
    # if name and phone:
    #     data[name] = phone
    # else:
    #     print("Please provide both")
    # return data


def search_contact():
    username = input("Enter the name of user: ")
    with open("contactbook.txt") as f:
        for line in f:
            line = line.split(",")
            if line[0] == username:
                return print(f"The contact number of {line[0]} is {line[1]}")
    
    print("Incorrect Name")
            
    # for key,value in data.items():
    #     if key == username:
    #         print(value)
        


def contact_book(choice):
    if(choice == "1"):
        add_contact()
    elif(choice == "2"):
        search_contact()
    else:
        print("Invalid option!")
    
    
def main():
    # find_average()
     
    # data = {} - I was doing with dict first
    while(True):
        show_menu()
        choice = input("Your choice: ")  
        contact_book(choice)
    
main()