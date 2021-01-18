my_list = ''
word_fin = ''

my_list = input('Введи строку из нескольких слов, разделённых пробелами')
print(my_list)
k = 1
el_my_list = my_list.split(' ')
print(el_my_list)
for el in el_my_list:
    if el == '':
        continue
    qw = 0
    while qw < len(el):

        if qw > 9:
            break
        word_fin += el[qw]
        qw += 1


    print(k, word_fin)
    k += 1
    word_fin = ''
