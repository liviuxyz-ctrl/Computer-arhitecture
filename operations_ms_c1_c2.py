from Rep_ms_c1_c2 import list_to_string
from Rep_ms_c1_c2 import transform


def sum_nr(nr1, nr2, until=0):
    result_ = []
    excess = 0
    for i in range(len(nr1) - 1, until - 1, -1):
        temp = int(nr1[i]) + int(nr2[i]) + excess
        if temp > 1:
            temp %= 2
            excess = 1
        else:
            excess = 0
        result_.append(temp)
    return result_


def operation_ms(number1_, number2_, operator_):
    # transform numerele in binare in format C1
    nr1 = transform(number1_, 'MS')
    nr2 = transform(number2_, 'MS')
    print(f'Numerele in forma MS : {nr1} si {nr2}')
    nr1 = list(nr1)
    nr2 = list(nr2)
    memory_check = list(transform(str(int(number1_) + int(number2_)), 'MS'))
    if len(nr1) < len(memory_check):
        return "Out of memory :("
    #Verificam daca este vorba de adunare sau scadere si modificam calculul
    check_op = 0 if operator_ == "+" else 1
    option = (int(nr1[0]) + int(nr2[0]) + check_op) % 2
    #insemna ca fie ambele sunt pozitive "big_nr" e pozitiv
    if option == 0:
        sign = int(nr1[0])
        nr1[0], nr2[0] = 0, 0
        result = sum_nr(nr1, nr2, 1)
    else:
        big_nr = nr1.copy()
        low_nr = nr2.copy()
        for i in range(1, len(nr1)):
            if nr1[i] > nr2[i]:
                big_nr = nr1
                low_nr = nr2
                break
            elif nr1[i] < nr2[i]:
                big_nr = nr2
                low_nr = nr1
                break
        sign = int(big_nr[0])
        big_nr[0],low_nr[0] = 0,0
        result = []
        for i in range(len(big_nr) - 1, 0, -1):
            if int(big_nr[i]) - int(low_nr[i]) < 0:
                j = i - 1
                big_nr[i] = 2
                while True:
                    if int(big_nr[j]) == 1:
                        big_nr[j] = "0"
                        break
                    big_nr[j] = '1'
                    j -= 1
            result.append(int(big_nr[i]) - int(low_nr[i]))
        if check_op == 1 and int(sign) == 0 and number1_ < number2_:
            sign = 1
    result.append(sign)
    if len(result) > max(len(nr1), len(nr2)):
        return "Depasire de memorie"
    return list_to_string(result)


def operation_c1(number1, number2, operator):
    global result
    if operator == "-":
        number2 = str(int(number2) * (-1))
    if int(number1) < 0 and int(number2) >= 0:
        number1, number2 = number2, number1
    nr1 = transform(number1, 'C1')  # transform numerele in binare in format C1
    nr2 = transform(number2, 'C1')  #
    print(f'Numerele in forma C1 : {nr1} si {nr2}')
    nr1 = list(nr1)  # transform numerele in liste ca sa pot lucra cu ele
    nr2 = list(nr2)  #

    if (int(number1) >= 0 and int(number2) >= 0):
        if len(nr1) != len(list(transform(str(int(number1) + int(number2)), 'C1'))):
            return "Depasire, numere prea  mari"
        result = sum_nr(nr1, nr2)
    elif int(number1) >= 0 and int(number1) >= abs(int(number2)):
        result = sum_nr(nr1, nr2)
        result.reverse()
        result[0] = 0
        result = sum_nr(result, [0, 0, 0, 1])  # adaugarea bitului de corectie
    elif int(number1) >= 0:
        result = sum_nr(nr1, nr2)
    elif int(number2) < 0:
        if len(nr1) != len(list(transform(str(int(number1) + int(number2)), 'C1'))):
            return "Depasire, numere prea  mari"
        result = sum_nr(nr1, nr2)
        result.reverse()
        result[0] = 1
        result = sum_nr(result, [0, 0, 0, 1])  # adaugarea bitului de corectie

    return list_to_string(result)


def operation_c2(number1, number2, operator):
    if operator == "-":
        number2 = str(int(number2) * (-1))

    if int(number1) < 0 and int(number2) >= 0:
        #swaping
        number1, number2 = number2, number1
    nr1 = transform(number1, 'C2')  # transform numerele in binare in format C2
    nr2 = transform(number2, 'C2')  # transform numerele in binare in format C2
    print(f'Numerele in forma C2 : {nr1} si {nr2}')
    nr1 = list(nr1)  # transform numerele in liste ca sa pot lucra cu ele
    nr2 = list(nr2)  # transform numerele in liste ca sa pot lucra cu ele
    result = sum_nr(nr1, nr2)
    if (int(number1) >= 0 and int(number2) >= 0):
        if result[len(result) - 1] == 1:
            print('Calcul incorenct, marime depasita! ')
    elif int(number1) >= 0 and int(number1) >= abs(int(number2)):
        result[len(result) - 1] = 0
    elif int(number1) >= 0:
        result[len(result) - 1] = 1
    elif int(number2) < 0:
        if result[len(result) - 1] == 0:
            return ('Calcul incorenct, marime depasita! ')

    return list_to_string(result)


number1 = input('primul numar: ')
number2 = input('al doilea nr: ')
operator = input('operator : ')

print('Rezultat calul in MS : ' + operation_ms(number1, number2, operator))
print('Rezultat calul in C1 : ' + operation_c1(number1, number2, operator))
print('Rezultat calul in C2 : ' + operation_c2(number1, number2, operator))
