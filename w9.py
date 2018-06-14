data1 = (2014, 7, 2)
data2 = (2014, 7, 11)

if data1[1] == data2[1] and data1[0] ==data2[0]:
    if data1[2] > data2[2]:
        print('Różnica wynosi ',(data1[2]) - (data2[2]), 'dni.')
    elif data2[2] > data1[2]:
        print('Różnica wynosi ',(data2[2]) - (data1[2]), 'dni.')
    else: print('Podane daty są takie same!')
