my_str = [23, '23', [2, '3'], (2, '3'), {'key_1': 2, 2: 'key_2'}]
qua = len(my_str)
print(qua)
k = 0

while k <= qua - 1:
    print(type(my_str[k]))
    k += 1
