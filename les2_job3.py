monat_l = ['зима', 'весна', 'лето', 'осень', 'много снега - хорошо', 'всё расцветает', 'тепло, солнце', 'опадает листва']
monat_d = {'зима': [12, 1, 2],
           'весна': [3, 4, 5],
           'лето': [6, 7, 8],
           'осень': [9, 10, 11]}
k = 0
while k < 1 or k > 12:
    k = input('напиши номер любимого времени года\n (целое число от 1 до 12)')

    if k.isdigit() and 0 < int(k) <= 12:
        k = int(k)
        break
    else:
        k = 0
        print('Внимательнее вводи число. Ещё разок')
k_dict = int(k)
if 8 < k <= 11:
    k = 3
elif 2 < k < 6:
    k = 1
elif 5 < k < 9:
    k = 2
else:
    k = 0
print('Ваше любимое время года ' + monat_l[k] + ' когда ' + monat_l[k + 4])
for key, value in monat_d.items():
    monat_dd = key
    numer_monat = value
    ei =0
    while ei < 3:
        if  k_dict == numer_monat[ei]:
            print('dict. \nВаше любимое время года - ' + monat_dd + ' - когда ' + monat_l[k + 4])
            break
        ei += 1

