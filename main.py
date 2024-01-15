import random
import keyboard
import time

ActionDuration = 150
CycleCount = 1
SPmax = 7
SP = 3
SeeleSPDbuffupto = 0

class Character:
    def __init__(self, name, SPD):
        self.name = name
        self.SPD = SPD
        self.AV = 10000 / SPD
        self.currentAV = self.AV
        self.NoT = 0

Seele = Character("Seele", 122)
FuXuan = Character("FuXuan", 100)
SilverWolf = Character("SilverWolf", 134)
Sparkle = Character("Sparkle", 160)

Team = [Seele, FuXuan, SilverWolf, Sparkle]

def SortTeam():
    global Team
    sorted_team = sorted(Team, key=lambda x: x.currentAV)
    Team = sorted_team

def PrintStats():
    SortTeam()
    for character in Team:
        print(f"{character.name}: SPD - {character.SPD}, Current AV - {round(character.currentAV)}")
    print(f"AD remaining = {round(ActionDuration)}")
    print(f"SP remaining = {SP}")

def takeTurn(character):
    global ActionDuration, CycleCount, SP, SeeleSPDbuffupto
    print("\n" + "-" * 20)
    print(f"{character.name} takes its turn!")
    print("-" * 20)

    character.NoT += 1

    ActionDuration -= character.currentAV
    if ActionDuration <= 0:
        ActionDuration += 100
        CycleCount += 1

        print("\n" + "-" * 20)
        print(f"Turn {CycleCount}")
        print("-" * 20)

    x = character.currentAV
    for other_char in Team:
        other_char.currentAV = max(0, other_char.currentAV - x)

    character.currentAV = character.AV



    # Check if the character is Sparkle
    if character.name == "Sparkle":
        if SP > 0:
            # Skill
            print("\n" + "-" * 20)
            print(f"Sparkle Skill")
            print("-" * 20)
            SP -= 1

            PrintStats()


            # SeeleBuff
            SeeleRef = next((char for char in Team if char.name == "Seele"), None)
            if SeeleRef:
                action_forward = 0.5 * SeeleRef.AV
                print("\n" + "-" * 20)
                print(f"Action Forwarded to Seele: -{round(action_forward)} from Seele's Current AV")
                print("-" * 20)

                SeeleRef.currentAV = max(0, SeeleRef.currentAV - action_forward)

        else:
            # BasicATK
            print("\n" + "-" * 20)
            print(f"Sparkle BasicATK")
            print("-" * 20)
            SP += 1

        if character.NoT % 3 == 0:
            # Ultimate
            print("\n" + "-" * 20)
            print(f"Sparkle Ultimate")
            print("-" * 20)
            SP = min(SPmax, SP + 4)

    if character.name == "FuXuan":
        if character.NoT % 3 == 1:
            if SP > 0:
                # Skill
                print("\n" + "-" * 20)
                print(f"FuXuan Skill")
                print("-" * 20)
                SP -= 1
            else:
                # Basic ATK
                print("\n" + "-" * 20)
                print(f"FuXuan BasicATK")
                print("-" * 20)
                SP += 1
        else:
            # Basic ATK
            print("\n" + "-" * 20)
            print(f"FuXuan BasicATK")
            print("-" * 20)
            SP += 1

    if character.name == "SilverWolf":
        if character.NoT % 3 == 1:
            if SP > 0:
                # Skill
                print("\n" + "-" * 20)
                print(f"SilverWolf Skill")
                print("-" * 20)
                SP -= 1
            else:
                # Basic ATK
                print("\n" + "-" * 20)
                print(f"SilverWolf BasicATK")
                print("-" * 20)
                SP += 1
        else:
            y = random.choices(["Skill", "BasicATK"], weights=[20, 80])[0]
            if y == "Skill":
                #Skill
                print("\n" + "-" * 20)
                print(f"SilverWolf Skill")
                print("-" * 20)
                SP -= 1
            else:
                #BasicATK
                print("\n" + "-" * 20)
                print(f"SilverWolf BasicATK")
                print("-" * 20)
                SP += 1

    if character.name == "Seele":
        if SP > 1:
            # Skill
            print("\n" + "-" * 20)
            print(f"Seele Skill")
            print("-" * 20)

            SP -= 1
            character.SPD = 150
            character.AV = 10000 / character.SPD
            SeeleSPDbuffupto = character.NoT + 2
        else:
            z = random.choices(["Skill", "BasicATK"], weights=[50, 50])[0]
            if z == "Skill":
                # Skill
                print("\n" + "-" * 20)
                print(f"Seele Skill")
                print("-" * 20)
                SP -= 1
                character.SPD = 150
                character.AV = 10000 / character.SPD
                SeeleSPDbuffupto = character.NoT + 2
            else:
                # BasicATK
                print("\n" + "-" * 20)
                print(f"Seele BasicATK")
                print("-" * 20)
                SP += 1
                character.currentAV = max(0, character.currentAV - 0.2 * character.AV)

        if SeeleSPDbuffupto < character.NoT:
            character.SPD = 122
            character.AV = 10000 / character.SPD

    PrintStats()

    if character.name == "Seele":
        r = random.choices(["Resurgence","Skip"],weights=[33,77])
        if r=="Resurgence":
            print("\n" + "-" * 20)
            print(f"Seele Resurgence")
            print("-" * 20)
            character.currentAV = 0
            PrintStats()

def Enter():
    takeTurn(Team[0])

# Initial display of stats
PrintStats()

# Wait for user input (empty for Enter, "quit" for Space)
while True:
    user_input = input("\n"+"Press Enter for the next turn, or type 'quit' to end: ")

    if user_input.lower() == 'quit':
        break

    # Simulate a turn on Enter key press
    Enter()

