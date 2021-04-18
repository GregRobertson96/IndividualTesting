from src.Display.InputConsole import InputConsole

class CharacterSheet:
    input = None

    def __init__(self):
        self.availableStats = ""
        self.charName = ""
        self.charAge = ""
        self.charClass = ""
        self.charStats = []
        self.charAttributes = ["Strength","Endurance", "Agility", "Dexterity", "Intelligence", "Wisdom", "Charisma", "Willpower"]

        if input is None:
            self.input = InputConsole()
        else:
            self.input = input

    def totalStats(self):
        self.maxStats = self.input(int("Please enter the total stats available."))
        return self.maxStats

    def characterProfile(self):
        self.charName = self.input(str("Please enter your character's name: \n"))
        userAge = self.input(int("Please enter your character's age: \n"))
        if userAge > "18":
            self.charAge = "Adult"
        elif userAge < "19":
            self.charAge = "Child"

        return "Your character's name is:" + self.charName + "\nTheir age is :" + userAge + "\nThat would make them an: " + self.charAge

    def characterStats(self, totalStats):
        counter = ""
        stat_points = totalStats
        for item in self.charAttributes:
            statInput = self.input("Please enter a stat for :" + self.charAttributes[0] + "\n You have " + str(stat_points) + "Available")
            self.charStats[counter] = statInput
            stat_points = stat_points - int(statInput)
            if stat_points < 0:
                print("You don't have enough stat points available.")
                break
            counter = counter + 1
        return self.charStats


