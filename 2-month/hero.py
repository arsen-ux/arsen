class SuperHero:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.fly = False

    def multiply_hp(self):
        self.hp **= 2
        self.fly = True

    def true_phrase(self):
        print("True in the True_phrase")



class AirHero(SuperHero):
    def __init__(self, name, hp, damage, air_speed):
        super().__init__(name, hp, damage)
        self.air_speed = air_speed

class LandHero(SuperHero):
    def __init__(self, name, hp, damage, ground_speed):
        super().__init__(name, hp, damage)
        self.ground_speed = ground_speed


class SpaceHero(SuperHero):
    def __init__(self, name, hp, damage, space_speed):
        super().__init__(name, hp, damage)
        self.space_speed = space_speed



air_hero = AirHero("Wind Walker", 100, 15, 300)
land_hero = LandHero("Earth Shaker", 200, 25, 80)
space_hero = SpaceHero("Star Ranger", 150, 20, 500)

air_hero.multiply_hp()
land_hero.multiply_hp()
space_hero.multiply_hp()


print(air_hero.hp, air_hero.fly)  # 10000 True
print(land_hero.hp, land_hero.fly)  # 40000 True
print(space_hero.hp, space_hero.fly)  # 22500 True


air_hero.true_phrase()


class Villain(LandHero):
    def __init__(self, name, hp, damage, ground_speed):
        super().__init__(name, hp, damage, ground_speed)
        self.people = "monster"

    def gen_x(self):
        pass

    def crit(self, power):
        self.damage **= power



villain = Villain("Dark Lord", 300, 50, 60)
villain.crit(2)
print(villain.damage)


villain.crit(2)
print(land_hero.damage)
# git add . :добавляет файлы
# git commit -m 'название'
# git push origin master/main
#
# удаление
# git rm --cached namefile: стирает файл
# git rm --cached -r удаляет файлы