# / 2 - 10 ввод целого числа
k = 1
while k != 0:
    qua = input('Напишите кол-во элементов\n вводимого списка')
    if qua.isdigit():
        qua = int(qua)
        k = 0
    else:
        print("Вы ввели не целое число больше 1. Ещё разок")
        k = 1
# /ввод списка
rost = []
while k < qua:
    answer_1 = input('Введи эл-т списка')
    k += 1
    rost.append(answer_1)
print(rost)
k = 0
rost_new =[]
while k + 1 < qua:
    #/f_rost = rost[k:k+1:]
    #/l_rost = rost[k+1:k+2:]
    #/rost_new.append(l_rost)
    #/rost_new.append(f_rost)
    rost[k], rost[k+1] = rost[k+1], rost[k]
    k+=2
print(rost)
