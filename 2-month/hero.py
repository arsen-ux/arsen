class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, healthypoints, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.healthypoints = healthypoints
        self.catchphrase = catchphrase

    def имя(self):
        return f'Имя героя: {self.name}'

    def удвоенное_здоровье(self):
        self.healthypoints *= 2
        print(f"Здоровье героя удвоено: {self.healthypoints}")

    def __str__(self):
        return f'Прозвище: {self.nickname}, Суперспособность: {self.superpower}, Здоровье: {self.healthypoints}'

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero('Тони Старк', 'Железный человек', 'костюм', 1000,
                 'Гений, миллиардер, плейбой, филантроп. Этот мир далёк от совершенства, но нам в нём жить.')


print(hero.имя())
hero.удвоенное_здоровье()
print(hero)
print(f"Длина коронной фразы: {len(hero)}")

# git add . :добавляет файлы
# git commit -m 'название'
# git push origin master/main
#
# удаление
# git rm --cached namefile: стирает файл
# git rm --cached -r удаляет файлы