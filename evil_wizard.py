from character import Character
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        if 0 < self.health < self.max_health:
            self.health += 5
        print(f"{self.name} regenerates 5 health! Wizard's health: {self.health}")
