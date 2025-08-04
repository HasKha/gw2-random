import random

wing_names = [
    "W1: Spirit Vale",
    "W2: Salvation pass",
    "W3: Stronghold of the Faithful",
    "W4: Bastion of the Penitent (all CMs!)",
    "W5: Hall of Chains",
    "W6: Mythwright Gambit",
    "W7: The Key of Ahdashim",
    "W8: Mount Balrior"
]
available_wings = [1, 2, 3, 4, 5, 6, 7, 8]

instability_names = [
    "1. Don't Trip - /gg when downstate",
    "2. A bit Extra - One extra ban",
    "3. Unlimited Power - No bans",
    "4. Alienate - Two players must play core",
    "5. Weightly - Ban a weight class instead",
    "6. Safari - Everyone in one subgroup",
    "7. Rainbow - Play at least one of each profession, no bans",
    "8. Bounty - CM kills grant additional points"
]
available_instabilities = [1, 2, 3, 4, 5, 6, 7, 8]

# 1. Select a raid wing
print("Rolling the wing...")
wing = random.choice(available_wings)
print(wing_names[wing - 1])
print("")

print("Rolling instability...")
instab = random.choice(available_instabilities)
print(instability_names[instab - 1])
print()

if instab == 3 or instab == 7:
    print("No bans!")
elif instab == 5:
    print("Rolling a weight class instead...")
    weight = random.choice(["Heavy", "Medium", "Light"])
    print(weight + " is banned!")
else:
    print("Rolling bans...")
    heavy_ban = random.choice(["Guardian", "Revenant", "Warrior"])
    medium_ban = random.choice(["Engineer", "Ranger", "Thief"])
    light_ban = random.choice(["Elementalist", "Mesmer", "Necromancer"])
    print(heavy_ban + " is banned!")
    print(medium_ban + " is banned!")
    print(light_ban + " is banned!")
    extra_ban = ""
    if instab == 2:
        while extra_ban == "" or extra_ban == heavy_ban or extra_ban == medium_ban or extra_ban == light_ban:
            extra_ban = random.choice(["Guardian", "Revenant", "Warrior", "Engineer", "Ranger", "Thief", "Elementalist", "Mesmer", "Necromancer"])
        print("  " + extra_ban + " is also banned!")
