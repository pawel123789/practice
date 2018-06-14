number = 0
total = 0
count = 0
while number >= 0:
    number = float(input('Podaj liczbę: '))
    if number >= 0:
        count += 1
        total += number
print('Podałeś tyle nieujemnych iczb: ', count)
