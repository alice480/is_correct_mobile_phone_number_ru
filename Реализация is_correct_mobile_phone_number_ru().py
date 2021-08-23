import sys


def is_correct_mobile_phone_ru(elem):
    count = 0
    if elem[0] == '8' or elem[0:2] == '+7':
        elem = elem.replace('+', '', 1)
        for letter in elem[1:]:
            if letter.isdigit():
                count += 1
        if count == 10:
            if '(' in elem or ')' in elem:
                if elem.count('(') == elem.count(')') == 1:
                    stroka = elem.replace(' ', '')
                    stroka = stroka.replace('-', '')
                    if stroka[1] != '(' and stroka[5] != ')':
                        return False
                else:
                    return False
            elem = elem.replace('(', '')
            elem = elem.replace(')', '')
            elem = elem.replace('-', ' ')
            indexes = [1, 5, 9, 12]
            stroka = elem.replace(' ', '')
            stroka = stroka[0] + ' ' + stroka[1:4] + ' ' + stroka[4:7] + ' ' + stroka[7:9] + ' ' + stroka[9:]

            if stroka != elem:
                return False
            return True
        else:
            return False
    else:
        return False



def test_is_correct_mobile_phone_number_ru():
    test_cases = (
        ('qwertyui', False),
        ('99243865073', False),
        ('+59324568194', False),
        ('81234', False),
        ('+78456', False),
        ('83717987894078217', False),
        ('+782948274297492', False),
        ('+7(7658721324', False),
        ('8918)0231435', False),
        ('+7()()8921927683', False),
        ('+ 7 9 3 2579072', False),
        ('+7*123*234*54*76', False),
        ('+79246531234', True),
        ('85648795348', True),
        ('8(785)2349503', True),
        ('+7(900)1234567', True),
        ('8 925 675-89-03', True),
        ('+7-(873)-634-12-45', True),
        ('8(921)325-98-12', True)
    )
    for input_s, correct_output_s in test_cases:
        if is_correct_mobile_phone_ru(input_s) != correct_output_s:
            print(input_s, correct_output_s)
            return False
    return True

if test_is_correct_mobile_phone_number_ru():
    print('YES')
else:
    print('NO')


data = list(map(str.strip, sys.stdin))
for elem in data:
    if is_correct_mobile_phone_ru(elem):
        print('YES')
    else:
        print('NO')
































































































































































































































