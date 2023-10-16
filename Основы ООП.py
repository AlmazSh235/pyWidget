# у объекта есть
#    тип - type()
#    идентификатор - id()
#    значение - value
#    имя - name
class Pistol:
    damage = 10
    bullet_speed = 100


deagle = Pistol()
m1911 = Pistol()

deagle.damage = Pistol.damage * 6
deagle.bullet_speed = Pistol.bullet_speed * 5

m1911.damage = Pistol.damage * 3.4
m1911.bullet_speed = Pistol.bullet_speed * 3

print('PICK YOUR GUN', f'{"Deagle:"} {deagle.__dict__}', f'{"M1911:"} {m1911.__dict__}', sep='\n')