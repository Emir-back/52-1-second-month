from random import randint, choice
from xml.sax.handler import property_xml_string


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health}, damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes: list):
        random_hero: Hero = choice(heroes)
        self.__defence = random_hero.ability

    def attack(self, heroes: list):
        for hero in heroes:
            if hero.health > 0:
                if type(hero) == Berserk and self.defence != hero.ability:
                    hero.blocked_damage = choice([5, 10])
                    hero.health -= self.damage - hero.blocked_damage
                else:
                    hero.health -= self.damage

    def __str__(self):
        return 'BOSS ' + super().__str__() + ' defence: ' + str(self.__defence)


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def attack(self, boss: Boss):
        boss.health -= self.damage

    def apply_super_power(self, boss: Boss, heroes: list):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'CRITICAL_DAMAGE')

    def apply_super_power(self, boss: Boss, heroes: list):
        crit = self.damage * randint(2, 5)
        boss.health -= crit
        print(f'Warrior {self.name} hit critically: {crit}')

class Witcher(Hero):
    def __init__(self, name, health, damage=0):
        super().__init__(name, health, damage, "REVIVE")
        self.__revive_used = False

    def apply_super_power(self, boss: Boss, heroes: list):
        if not self.__revive_used:
            for hero in heroes:
                if hero.health == 0:
                    hero.health = self.health
                    self.health = 0
                    self.__revive_used = True
                    print(f'Witcher {self.name} sacrificed himself to revive {hero.name}')
                    break

    @property
    def health(self):
        return self._GameEntity__health

    @health.setter
    def health(self, value):
        self._GameEntity__health = value  # Теперь сеттер работает правильно


class Magic(Hero):
    def __init__(self, name, health, damage, boost_amount):
        super().__init__(name, health, damage, 'BOOSTING')
        self.boost_amount = boost_amount
        self.rounds_boosted = 0

    def apply_super_power(self, boss: Boss, heroes: list):
        if self.rounds_boosted < 4:
            for hero in heroes:
                if hero.health > 0 and hero != self:
                    hero.damage += self.boost_amount
            self.rounds_boosted += 1
            print(f'Magic {self.name} boosted all heroes by {self.boost_amount}')

class Hacker(Hero):
    def __init__(self, name, health, damage, steal_amount):
        super().__init__(name, health, damage, 'HEALTH_STEAL')
        self.steal_amount = steal_amount
        self.round_counter = 0

    def apply_super_power(self, boss: Boss, heroes: list):
        self.round_counter += 1
        if self.round_counter % 2 == 0 and boss.health > self.steal_amount:
            hero_to_heal = choice([h for h in heroes if h.health > 0 and h != self])
            boss.health -= self.steal_amount
            hero_to_heal.health += self.steal_amount
            print(f'Hacker {self.name} stole {self.steal_amount} health from Boss and gave it to {hero_to_heal.name}')

class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, 'HEAL')
        self.__heal_points = heal_points

    def apply_super_power(self, boss: Boss, heroes: list):
        for hero in heroes:
            if hero.health > 0 and self != hero:
                hero.health += self.__heal_points


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'BLOCK_REVERT')
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    def apply_super_power(self, boss: Boss, heroes: list):
        boss.health -= self.__blocked_damage
        print(f'Berserk {self.name} reverted: {self.__blocked_damage}')


round_number = 0


def show_statistics(boss: Boss, heroes: list):
    print(f'ROUND {round_number} ----------------')
    print(boss)
    for hero in heroes:
        print(hero)


def is_game_over(boss: Boss, heroes: list):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
        return True
    return False


def play_round(boss: Boss, heroes: list):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if hero.health > 0 and boss.health > 0 and boss.defence != hero.ability:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)
    show_statistics(boss, heroes)


def start_game():
    boss = Boss('Splinter', 1000, 50)

    warrior_1 = Warrior('Django', 280, 10)
    warrior_2 = Warrior('Billy', 270, 15)
    magic = Magic('Dulittle', 290, 10,5)
    doc = Medic('James', 250, 5, 15)
    assistant = Medic('Marty', 300, 5, 5)
    berserk = Berserk('William', 260, 10)
    hacker = Hacker('Anonimus',250,10,30)
    witcher = Witcher('Gerakl',300,0)


    heroes_list = [warrior_1, doc, warrior_2, magic, berserk, assistant,hacker, witcher]

    show_statistics(boss, heroes_list)
    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)


start_game()
