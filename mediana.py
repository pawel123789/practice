a = float(input('Podaj pierwszą liczbę: '))
b = float(input('Wprowadź drugą iczbę: '))
c = float(input('Wprowadź trzecią liczbę: '))

if a != b and b != c:
    if a < b and b < c:
        print('Mediana to:', b)
    elif a < b and b > c and a < c:
        print('Mediana to: ', c)
    else: print('Mediana to: ', a)
else:
    print('Należy wprowadzić rónże liczby.')