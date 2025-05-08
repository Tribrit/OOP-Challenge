class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5        # 0 = full, 10 = very hungry
        self.energy = 5        # 0 = tired, 10 = fully rested
        self.happiness = 5     # 0 to 10
        self.tricks = []

    def eat(self):
        print(f"{self.name} is eating...")
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        print(f"{self.name} is sleeping...")
        self.energy = min(10, self.energy + 5)

    def play(self):
        if self.energy <= 0:
            print(f"{self.name} is too tired to play.")
            return
        print(f"{self.name} is playing...")
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)

    def train(self, trick):
        print(f"{self.name} is learning a new trick: {trick}!")
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)
        self.energy = max(0, self.energy - 1)

    def show_tricks(self):
        if not self.tricks:
            print(f"{self.name} hasn't learned any tricks yet.")
        else:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")

    def get_status(self):
        print(f"{self.name}'s current status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        print(f"Tricks: {self.tricks if self.tricks else 'None'}")
