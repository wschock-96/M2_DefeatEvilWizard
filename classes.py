from character import Character

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def special_ability(self, opponent):
        print(f"{self.name} used 'Titans Wrath' against {opponent.name} for {self.attack_power*2} damage!")
        print(f"{self.name} used 'Iron Vambrace' to absorb the Wizard's attack!")
        return super().special_ability(opponent)

    def health_regen(self):
        return super().health_regen()

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def special_ability(self, opponent):
        print(f"{self.name} used 'Spectral Explosion' against {opponent.name} for {self.attack_power*2} damage!")
        print(f"{self.name} used 'Vortex of Protection' to slow the Wizard's attack!")
        return super().special_ability(opponent)
    
    def health_regen(self):
        return super().health_regen()

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=25)

    def special_ability(self, opponent):
        print(f"{self.name} used 'Quick Shot' against {opponent.name} for {self.attack_power*2} damage!")
        print(f"{self.name} used 'Evade' to escape the Wizard's attack!")
        return super().special_ability(opponent)

    def health_regen(self):
        return super().health_regen()

class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=135, attack_power=30)

    def special_ability(self, opponent):
        print(f"{self.name} used 'Holy Strike' against {opponent.name} for {self.attack_power*2} damage!")
        print(f"{self.name} used 'Divine Shield' to block the Wizard's attack!")
        return super().special_ability(opponent)

    def health_regen(self):
        return super().health_regen()
