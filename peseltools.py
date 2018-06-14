def validate(pesel):
    """
    validate(pesel)
    Checks if given PESEL number is correct or not.
    Args: PESEL number
    Return: True if PESEL number is validate,False otherwise
    """
    pesel = str(pesel)
    if len(str(pesel)) != 11:
        return False
    data = str(9 * int(pesel[0]) + 7 * int(pesel[1]) + 3 * int(pesel[2]) + int(pesel[3]) + 9 * int(pesel[4])
               + 7 * int(pesel[5]) + 3 * int(pesel[6]) + int(pesel[7]) + 9 * int(pesel[8]) + 7 * int(pesel[9]))
    if data[-1] != str(pesel[-1]):
        return False
    return True

def extract_personal_data(pesel):
    """Returns birth date and sex from given PESEL number."""
    personal_data = {}
    pesel = str(pesel)
    if int(pesel[-2]) % 2 == 0:
        personal_data['sex'] = 'Kobieta'
    else:
        personal_data['sex'] = 'Mężczyzna'

    day = pesel[4:6]
    month = pesel[2:4]

    if month[0] == '8' or month[0] == '9':
        year = '18' + pesel[0:2]
    elif month[0] == '0'  or month[0] == '1':
        year = '19' + pesel[0:2]
    elif month[0] == '2' or month[0] == '3':
        year = '20' + pesel[0:2]
    elif month[0] == '4' or month[0] == '5':
        year = '21' + pesel[0:2]
    elif month[0] == '6' or month[0] == '7':
        year = '22' + pesel[0:2]
    personal_data['day'] = day
    personal_data['month'] = month
    personal_data['year'] = year

    return personal_data