n = int(input('Введите кол-во заказов: '))

res = {}
for i in range(n):
    l_name, pizza, c = input(f'{i + 1} заказ').split()
    
