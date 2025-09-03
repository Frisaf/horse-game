# name_ok = False

# while name_ok == False:
#     user_name = input("What's your name? It has to be at least 2 characters long.")

#     if len(user_name) <= 2:
#         print("Your name needs to be at least 2 characters long.")
    
#     else:
#         print("Name ok")
#         name_ok = True

## Försök göra det till en funktion

def length_check(prompt: str, clamp: int) -> str:
    value = ""
    
    while len(value) < clamp:
        value = input(prompt)

        if len(value) < clamp:
            print(f"It has to be at least {clamp}")
        
        else:
            print("OK")
            
            return value
        
name = length_check("Your name?\n> ", 2)
print(f"Your name is {name}")