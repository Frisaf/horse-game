def input_int(arg):
    while True:
        try:
            return int(input(arg))
        
        except ValueError:
            print("Skriv in en siffra")

def check_speed():
    while True:
        speed = input_int("::: ")
        
        if speed > 6:
            print("Din hästs SPEED kan inte överstiga ett värde på 6!")
        
        elif speed < 1:
            print("Din hästs SPEED kan inte vara mindre än 1!")
        
        else:
            return speed

print(check_speed())