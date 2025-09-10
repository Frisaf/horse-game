# first_name = ""
# last_name = ""

# while len(first_name) <= 2 and len(last_name) <= 2:
#     first_name = input("What is your FIRST name?\n> ")
#     last_name = input("What is your LAST name?\n> ")

#     if len(first_name) < 2 or len(last_name) < 2:
#         print("Your first name and last name both have to be at least 2 characters long.")
    
#     else:
#         print(f"Great, welcome {last_name} {first_name} ({first_name} {last_name}).\nYour names backwards are: {last_name[::-1]} {first_name[::-1]}")

def name(first: str, last: str) -> str:
    return f"{last[::-1]} {first[::-1]}"
        
print(name(input("What is your FIRST name?\n> "), input("What is your LAST name?\n> ")))