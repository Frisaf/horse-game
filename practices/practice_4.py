weapons = [
    {
        "Name": "Ancient Sword",
        "Damage": 4,
        "Description": "An ancient sword, probably found in an old graveyard. It isn't very good."
    },
    {
        "Name": "Celestial Spear",
        "Damage": 15,
        "Description": "A spear made out of an angel's hair. It isn't very ethically made, but it does large amounts of damage."
    },
    {
        "Name": "Wooden Club",
        "Damage": 10,
        "Description": "The go to weapon for a barbarian. You don't come off as very intelligent if you use this."
    }
]

def print_weapon_info(arg):
    print(f"{weapon["Name"]} deals {weapon["Damage"]} damage. This is what the experts say about the weapon:\n'{weapon["Description"]}'\n")

# for weapon in weapons:
#     print(f"{weapon["Name"]} deals {weapon["Damage"]} damage. This is what the experts say about the weapon:\n'{weapon["Description"]}'\n")

for weapon in weapons:
    print_weapon_info(weapon)