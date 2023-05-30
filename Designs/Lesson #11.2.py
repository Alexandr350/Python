import collections
import sys


def get_suffix(age):
    if 10 <= age <= 14:
        return "лет"
    else:
        tmp = age/10
        y = int(age/10)
        year = int((tmp - y + 0.01) * 10)
        if year == 1:
            return "год"
        if 5 > year > 1:
            return "года"
        if 4 < year < 10:
            return "лет"


pets = {}
last = 1


def create(slo, ID):
    NAME = input('Кличка питомца: ')
    KIND = input('Вид питомца: ')
    AGE = int(input('Возраст: '))
    OWNER = input('Имя владельца: ')
    slo[ID] = {'Name': NAME, 'Kind': KIND, 'Age': AGE, 'Owner': OWNER}
    return slo


def read(ID):
    pet = pets[ID]
    print('Это {1} по кличке "{0}". Возраст питомца: {2} {3}.'
          ' Имя владельца: {4}'.format(pet['Name'], pet['Kind'], pet['Age'],
                                       get_suffix(pet['Age']), pet['Owner']))


def update(ID):
    tmp = {}
    new_pet = create(tmp, ID)
    read(ID)
    pets.update(new_pet)
    print('Обновлена запись {0}: '.format(ID))
    read(ID)


def delete(ID):
    pet = pets[ID]
    print('Удален: {0} {1}'.format(pet['Kind'], pet['Name']))
    pets.pop(ID)


def pets_list():
    for id, name in pets.items():
        print('{5}) {1}. Kличка: "{0}". Возраст: {2} {3}.'
              ' Владелец: {4}'.format(name['Name'], name['Kind'], name['Age'],
                                           get_suffix(name['Age']), name['Owner'], id))


def get_pet(ID):
    return ID if ID in pets.keys() else False


def user_vvod():
    while True:
        command = input('Команда: ').lower()
        if command == 'создать':
            global last
            create(pets, last)
            last = collections.deque(pets, maxlen=1)[0] + 1
        if command == 'найти':
            ID = int(input('ID питомца: '))
            if not get_pet(ID):
                print('Нет в списке')
                continue
            else:
                read(get_pet(ID))
                continue
        if command == 'список':
            if len(pets) == 0:
                print('Список пуст')
                continue
            else:
                pets_list()
                continue
        if command == 'удалить':
            ID = int(input('ID питомца: '))
            if not get_pet(ID):
                print('Нет в списке')
                continue
            else:
                delete(get_pet(ID))
                continue
        if command == 'обновить':
            ID = int(input('ID питомца: '))
            if not get_pet(ID):
                print('Нет в списке')
                continue
            else:
                update(get_pet(ID))
                continue
        if command == 'выход':
            break


user_vvod()


print(sys.stdin.readline())