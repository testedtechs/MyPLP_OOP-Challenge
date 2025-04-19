# This is the Pet class
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5       # 0 = full, 10 = very hungry
        self.energy = 5       # 0 = tired, 10 = fully rested
        self.happiness = 5    # 0 = sad, 10 = very happy
        self.tricks = []      # list to store learned tricks

    def eat(self):
        # Eating reduces hunger and increases happiness
        if self.hunger >= 3:
            self.hunger -= 3
        else:
            self.hunger = 0
        if self.happiness < 10:
            self.happiness += 1
        print(self.name + " ate some food and feels better!")

    def sleep(self):
        # Sleeping increases energy
        if self.energy <= 5:
            self.energy += 5
        else:
            self.energy = 10
        print(self.name + " took a nap and feels rested!")

    def play(self):
        # Playing uses energy, increases happiness and hunger
        if self.energy >= 2:
            self.energy -= 2
            if self.happiness <= 8:
                self.happiness += 2
            else:
                self.happiness = 10
            if self.hunger < 10:
                self.hunger += 1
            print(self.name + " played and had fun!")
        else:
            print(self.name + " is too tired to play.")

    def train(self, trick):
        # Teach the pet a new trick
        self.tricks.append(trick)
        if self.happiness < 10:
            self.happiness += 1
        if self.energy > 0:
            self.energy -= 1
        print(self.name + " learned a new trick: " + trick)

    def show_tricks(self):
        # Show all learned tricks
        if len(self.tricks) == 0:
            print(self.name + " hasn't learned any tricks yet.")
        else:
            print(self.name + " knows these tricks: ")
            for trick in self.tricks:
                print("- " + trick)

    def get_status(self):
        # Print the current state of the pet
        print("\n--- " + self.name + "'s Status ---")
        print("Hunger: " + str(self.hunger) + "/10")
        print("Energy: " + str(self.energy) + "/10")
        print("Happiness: " + str(self.happiness) + "/10")
        print("-----------------------------\n")
