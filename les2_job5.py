my_list = [7, 5, 3, 3, 2]

k = 1
while k == 1:
    i_nteger = input('Введи целое число от 0 до 9')
    if i_nteger.isdigit() and 0 <= int(i_nteger) <= 9:
        i_nteger = int(i_nteger)
        k = -1
    else:
        print("Повнимательнее. Ещё разок")
        k = 1
my_listrat = []
k = 1
for el in my_list:
    if el >= i_nteger and k == 1:
        my_listrat.append(el)
    elif k == -1:
        my_listrat.append(el)
    else:
        k = -1
        my_listrat.append(i_nteger)
        my_listrat.append(el)
print('\n\nНабор натуральных чисел -    ', ', '.join(map(str, my_list)))
print('\n\nВы ввели ', i_nteger, '. Результат - ', ', '.join(map(str, my_listrat)))