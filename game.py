import random, time

def input_int(arg):
    while True:
        try:
            return int(input(arg))
        
        except ValueError:
            print("Skriv in en siffra")

def create_computer_horse():
    speed = random.randint(2, 6)
    names = ["blub", "glub", "clanker", "mupp", "ai", "guh", "huh", "gato", "horse", "big", "small"]
    first_name = random.choice(names).capitalize()
    last_name = random.choice(names).capitalize()
    horse = {
        "Name": first_name + " " + last_name,
        "Speed": speed,
        "Agility": 8 - speed,
    }

    return horse

def clamp(stat_name, prompt, clamp) -> int:
    while player_horse[stat_name] < 1:
        player_horse[stat_name] = input_int(prompt)

        if player_horse[stat_name] > clamp:
            player_horse[stat_name] = 0
            print(f"Det måste vara mindre än {clamp}")

print("Skapa din häst!")

player_horse = {
    "Name": "",
    "Speed": 0,
    "Agility": 0,
}
computer_horse = create_computer_horse()
player_horse["Name"] = input("Vad ska din häst heta?\n> ")
stats_ok = True

print("Din häst har speed och agility, max 6 på varje, men max 8 totalt.")

while stats_ok == True:
    # player_horse["Speed"] = input_int("Hur SNABB är din häst?\n> ")
    # player_horse["Agility"] = input_int("Hur SMIDIG är din häst?\n> ")
    clamp("Speed", "Hur SNABB är din häst?\n> ", 6)
    clamp("Agility", "Hur SMIDIG är din häst?\n> ", 6)

    if player_horse["Speed"] + player_horse["Agility"] == 8:
        stats_ok = False
    
    else:
        print("Nä det måste vara totalt 8. Försök igen.")
        player_horse["Speed"] = 0
        player_horse["Agility"] = 0

print(f"Din motståndare är {computer_horse["Name"]}")

def game_turn():
    player_speed = player_horse["Speed"] + random.randint(1, 6)
    player_agility = random.randint(1, 6) - player_horse["Agility"]

    if player_agility <= 0:
        player_speed -= player_agility
    
    computer_speed = computer_horse["Speed"] + random.randint(1, 6)
    computer_agility = random.randint(1, 6) - computer_horse["Agility"]

    if computer_agility >= 0:
        computer_speed -= computer_agility
    
    print(f"{player_horse["Name"]} springer {player_speed} steg!")
    time.sleep(1)
    print(f"{computer_horse["Name"]} springer {computer_speed} steg!")

    return [player_speed, computer_speed]

player_steps = 0
computer_steps = 0

for i in range(10):
    steps = game_turn()

    player_steps += steps[0]
    computer_steps += steps[1]

print(f"{player_horse["Name"]} tog {player_steps} steg\n{computer_horse["Name"]} tog {computer_steps} steg")

if player_steps > computer_steps:
    print(f"{player_horse["Name"]} vann!")

elif player_steps == computer_steps:
    print("Det blev lika!")

else:
    print(f"{computer_horse["Name"]} vann!")