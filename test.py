from data.clothes import Clothes
from data.functionality import Functionality
from data.looks import Looks
from data.season import Season
from data.sex import Sex
from data.style import Style
from data.type import Type
from data.users import Users

s1 = Sex(sex='Мужской')
session.add(s1)
s2 = Sex(sex='Женский')
session.add(s2)

season1 = Season(id=1, season='Лето', look_season='Летний')
session.add(season1)
season2 = Season(id=2, season='Зима', look_season='Зимний')
session.add(season2)
season3 = Season(id=3, season='Всесезонная', look_season='Всесезонный')
session.add(season3)
season4 = Season(id=4, season='Демисезонная', look_season='Демисезонный')
session.add(season4)

functionality1 = Functionality(id=1, functionality='Верхняя')
session.add(functionality1)
functionality2 = Functionality(id=2, functionality='Верхняя лёгкая')
session.add(functionality2)

style1 = Style(id=1, style='Деловой')
session.add(style1)
style2 = Style(id=2, style='Казуальный')
session.add(style2)
style3 = Style(id=3, style='Спортивный')
session.add(style3)

type1 = Type(id=1, type='Плечевая')
session.add(type1)
type2 = Type(id=2, type='Поясная')
session.add(type2)

c1 = Clothes(id=1, name='Пальто', type=1, func=1, season=4)
c2 = Clothes(id=2, name='Пуховик', type=1, func=1, season=2)
c3 = Clothes(id=3, name='Плащ', type=1, func=1, season=4)
c4 = Clothes(id=4, name='Бомбер', type=1, func=1, season=4)
c5 = Clothes(id=5, name='Ветровка', type=1, func=1, season=1)
c6 = Clothes(id=6, name='Косуха', type=1, func=1, season=4)
c7 = Clothes(id=7, name='Парка', type=1, func=1, season=4)
c8 = Clothes(id=8, name='Блуза', type=1, func=2, season=3)
c9 = Clothes(id=9, name='Классические брюки', type=2, func=1, season=4)
c10 = Clothes(id=10, name='Джемпер', type=1, func=2, season=4)
c11 = Clothes(id=11, name='Жилет', type=1, func=2, season=3)
c12 = Clothes(id=12, name='Кардиган', type=1, func=2, season=4)
c13 = Clothes(id=13, name='Кофта', type=1, func=2, season=2)
c14 = Clothes(id=14, name='Пиджак', type=1, func=2, season=4)
c15 = Clothes(id=15, name='Рубашка', type=1, func=2, season=3)
c16 = Clothes(id=16, name='Свитер', type=1, func=2, season=2)
c17 = Clothes(id=17, name='Шорты', type=2, func=1, season=1)
c18 = Clothes(id=18, name='Юбка', type=2, func=1, season=1)
c19 = Clothes(id=19, name='Майка', type=1, func=2, season=1)
c20 = Clothes(id=20, name='Футболка', type=1, func=2, season=1)
c21 = Clothes(id=21, name='Водолазка', type=1, func=2, season=3)
c22 = Clothes(id=22, name='Пуловер', type=1, func=2, season=4)
c23 = Clothes(id=23, name='Милитари', type=2, func=1, season=4)
c24 = Clothes(id=24, name='Джинсы', type=2, func=1, season=3)
c25 = Clothes(id=25, name='Лыжная куртка', type=1, func=1, season=2)
c26 = Clothes(id=26, name='Бушлат', type=1, func=1, season=2)
c27 = Clothes(id=27, name='Стеганая куртка', type=1, func=1, season=2)
c28 = Clothes(id=28, name='Комбинезон', type=2, func=1, season=2)
c29 = Clothes(id=29, name='Джоггеры', type=2, func=1, season=4)
c30 = Clothes(id=30, name='Карго', type=2, func=1, season=4)
c31 = Clothes(id=31, name='Спортивные штаны', type=2, func=1, season=1)
c32 = Clothes(id=32, name='Джинсовка', type=1, func=1, season=1)
c33 = Clothes(id=33, name='Кожаная куртка', type=1, func=1, season=4)
c34 = Clothes(id=34, name='Дублёнка', type=1, func=1, season=2)
c35 = Clothes(id=35, name='Рубашка(короткий рукав)', type=1, func=2, season=1)
c36 = Clothes(id=36, name='Брюки', type=2, func=1, season=4)
c37 = Clothes(id=37, name='Джинсы(утеплённые)', type=2, func=1, season=2)
for i in range(1, 38):
    session.add(eval(f'c{i}'))

l1 = Looks(id=1, style=2, season=1)
l2 = Looks(id=2, style=2, season=1)
l3 = Looks(id=3, style=2, season=1)
l4 = Looks(id=4, style=2, season=1)
l5 = Looks(id=5, style=1, season=1)
l6 = Looks(id=6, style=3, season=1)
l7 = Looks(id=7, style=1, season=1)
l8 = Looks(id=8, style=2, season=1)
l9 = Looks(id=9, style=2, season=1)
l10 = Looks(id=10, style=3, season=1)
l11 = Looks(id=11, style=3, season=1)
l12 = Looks(id=12, style=2, season=2)
l13 = Looks(id=13, style=2, season=2)
l14 = Looks(id=14, style=2, season=2)
l15 = Looks(id=15, style=2, season=2)
l16 = Looks(id=16, style=1, season=2)
l17 = Looks(id=17, style=2, season=2)
l18 = Looks(id=18, style=1, season=2)
l19 = Looks(id=19, style=2, season=2)
l20 = Looks(id=20, style=3, season=2)
l21 = Looks(id=21, style=1, season=4)
l22 = Looks(id=22, style=3, season=4)
l23 = Looks(id=23, style=2, season=4)
l24 = Looks(id=24, style=2, season=4)
l25 = Looks(id=25, style=2, season=4)
l26 = Looks(id=26, style=2, season=4)
l27 = Looks(id=27, style=2, season=4)
l28 = Looks(id=28, style=1, season=4)
for i in range(1, 29):
    session.add(eval(f'l{i}'))

user1 = Users(sex=1, nickname='test', email='test', hashed_password='test')
session.add(user1)