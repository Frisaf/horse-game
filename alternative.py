def input_int(arg):
    while True:
        try:
            return int(input(arg))
        
        except ValueError:
            print("Enter a number instead")

class Horse:
    def __init__(self, name, speed, agility):
        self.name = name
        self.speed = speed
        self.agility = agility
    
    def __str__(self):
        return f"{self.name} {self.speed} {self.agility}"

    def check_speed():
        while True:
            speed = input_int("How FAST is your horse?\n> ")
            
            if speed > 6:
                print("Your horse's SPEED cannot exceed 6!")
            
            elif speed < 1:
                print("Your horse's speed cannot be lower than 1!")
            
            else:
                return speed

    def check_agility():
        while True:
            agility = input_int("How AGILE is your horse?\n> ")

            if agility > 6:
                print("Your horse's AGILITY cannot exceed 6!")
            
            elif agility < 1:
                print("Your horse's AGILITY cannot be lower than 1!")
            
            else:
                return agility
    
    def check_total(speed, agility):
        if speed + agility != 8:
            print("The sum of your SPEED and AGILITY has to be 8. Try again.")
            return False
        
        else:
            return True

horses = {
    "Player Horse": {
        "Name": "",
        "Speed": 0,
        "Agility": 0,
    }
}

name = input("What's your horse's name?\n> ")

while True:
    speed = Horse.check_speed()
    agility = Horse.check_agility()
    check = Horse.check_total(speed, agility)

    if check == True:
        horse_stats = str(Horse(name, speed, agility))
        split_horse_stats = horse_stats.split()
        horses["Player Horse"]["Name"] = split_horse_stats[0]
        horses["Player Horse"]["Speed"] = split_horse_stats[1]
        horses["Player Horse"]["Agility"] = split_horse_stats[2]

        print(f"You've now created your horse!\nName: {split_horse_stats[0]}\nSpeed: {split_horse_stats[1]}\nAgility: {split_horse_stats[2]}")

        break

def main():
    pass