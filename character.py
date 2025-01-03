import random
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  
        self.defense_active = False  
        
    def attack(self, opponent):
        random_damage = random.randrange(self.attack_power, 40)        
        opponent.health -= random_damage
        print(f"{self.name} attacks {opponent.name} for {random_damage} damage!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def health_regen(self):
        if 0 < self.health < self.max_health:
            self.health += 30
            print(f"{self.name} regenerates health. Current health {self.health}")
        else:
            print(f'{self.name} is at max health.')

    def special_ability(self, opponent):
        opponent.health -= self.attack_power * 2
        self.defense_active = True

        if opponent.health <= 0:
            print(f'{opponent.name} has been defeated!')
