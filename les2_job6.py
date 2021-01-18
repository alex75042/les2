k = 1
while k != 0:
    qua = input('Напишите кол-во позиций\n вводимого товара')
    if qua.isdigit():
        qua = int(qua)
        k = 0
    else:
        print("Вы ввели не целое число больше 1. Ещё разок")
        k = 1
k = 1
pos = []
val_1 = []
val_2 = []
val_3 = []
val_4 = []
pos_tabl = {'название': val_1, 'цена': val_2,
            'кол-во': val_3, 'ед': val_4}
while k <= qua:
    print('\nпозиция', k)
    value_1 = input('название')

    value_2 = input('цена')

    value_3 = input('количество товара')

    value_4 = input('ед. измерения')
    position = {'название': value_1, 'цена': value_2,
                'кол-во': value_3, 'ед': value_4}

    posit = (k, position)
    pos.append(posit)

    val_1.append(value_1)
    val_2.append(value_2)
    val_3.append(value_3)
    val_4.append(value_4)

    k += 1
print('\n', pos, '\n')
print(pos_tabl)