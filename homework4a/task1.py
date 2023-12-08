k = int(input('Кол-во стран: '))

res = {}

for i in range(1, k+1):
    a, *b = input(f'{i} страна: ').split()
    for j in b:
        res[j] = a

for i in range(3):
    city = input(f'{i + 1} город: ')
    land = res.get(city)
    if land:
        print(f'Город {city} расположен в стране {land}.')
    else:
        print(f'По городу {city} данных нет.')
