def input_int(arg):
    while True:
        try:
            return int(input(arg))
        
        except ValueError:
            print("Skriv in en siffra")

class Horse:
    def __init__(self, name, speed, agility):
        self.name = name
        self.speed = speed
        self.agility = agility
    
    def __str__(self):
        return f"{self.name} {self.speed} {self.agility}"

# def check_speed(speed):
#     while True:
#         if speed > 6:
#             return 

print("Skapa din häst!")

player_horse = {
    "Name": "",
    "Speed": 0,
    "Agility": 0,
}
player_horse["Name"] = input("Vad ska din häst heta?\n> ")

print("Din häst har speed och agility, max 6 på varje, men max 8 totalt.")

while player_horse["Speed"] + player_horse["Agility"] != 8:
    player_horse["Speed"] = input_int("Hur SNABB är din häst?\n> ")
    player_horse["Agility"] = input_int("Hur SMIDIG är din häst?\n> ")

    if player_horse["Speed"] + player_horse["Agility"] != 8:
        print("Nä det måste vara exakt 8 totalt. Försök igen.")

horse_1 = Horse(player_horse["Name"], player_horse["Speed"], player_horse["Agility"])

print(horse_1)