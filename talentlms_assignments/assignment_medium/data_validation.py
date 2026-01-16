def validate_input(value, data_type): 
    
    if(data_type == "integer"):
       if value.startswith("-"):
           return value[1:].isdigit()
       return value.isdigit()
        
    elif(data_type == "float"):
       if value.startswith("-"):
           return value[1:]
       return value.replace(".","",1).isdigit() and value.count(".")==1

    elif(data_type == "email"):
        if " " in value:
            return False
        
        if value.count("@") !=1:
            return False
        
        name,domain = value.split("@")
        if not name or not domain:
            return False
        
        if "." not in domain:
            return False
        
        if domain.startswith(".") and domain.endswith("."):
            return False

        return True
    
    else:
        return False
          
    
    

print(validate_input("23","integer"))
print(validate_input("23.3","integer"))

print(validate_input("23.3","float"))
print(validate_input("23","float"))

print(validate_input("23","email"))
print(validate_input("nouman","email"))
print(validate_input("nouman.com","email"))
print(validate_input("@emumba.com","email"))
print(validate_input("nouman@emumba.com","email"))


