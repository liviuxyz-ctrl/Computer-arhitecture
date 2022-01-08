import math
def trans_in_b10(nbr):
    nbr_list = []
    for i in nbr:
        if i != ' ':
            nbr_list.append(int(i))
    while len(nbr_list) <= 32:
        nbr_list.append(0)
    caract = 0 #caract => caracteristici
    mantisa = 0
    semn = nbr_list[0]
    for i in range(8, 0, -1):
        caract += nbr_list[i]*(2**(8-i))
    for i in range(9, 33):
        mantisa += nbr_list[i]*((2**(i-8))**(-1))
    valoare = 0
    # valoare normala
    if 0 < caract < 255:
        valoare = (-1)**semn * (1 + mantisa) * 2**(caract - 127)
    # valoare denormalizata
    elif caract == 0 and mantisa != 0:
        valoare = (-1)**semn * mantisa * 2**( -126)
    # reprezentarea lui 0
    elif caract == 0 and mantisa == 0 and semn == 0:
        valoare = '0'
    # reprezentarea lui -0
    elif caract == 0 and mantisa == 0 and semn == 1:
        valoare = '-0'
    # reprezentarea lui ∞
    elif caract == 255 and mantisa == 0 and semn == 0:
        valoare = 'Infinit'
    # reprezentarea lui -∞
    elif caract == 255 and mantisa == 0 and semn == 1:
        valoare = 'Minus Infinit'
    # reprezentarea Nan(not an nbr)
    elif caract == 255 and mantisa != 0:
        valoare = 'NaN'
    print(valoare)
    return valoare


def trans_in_b2(decimal_nbr): #transformarea nbrului in binar
    nbr = []
    decimal_nbr = float(decimal_nbr)
    real_nbr = math.floor(decimal_nbr)
    fractional_nbr = decimal_nbr - real_nbr
    while real_nbr != 0:
        nbr.append(real_nbr % 2)
        real_nbr = real_nbr // 2
    final_nbr = ''
    while nbr:
        final_nbr = final_nbr + str(nbr.pop())
    nbr.clear()
    while fractional_nbr != 0:
        fractional_nbr *= 2
        aux = 0
        if fractional_nbr >= 1:
            aux = math.floor(fractional_nbr)
        nbr.append(aux)
        fractional_nbr -= aux
    str(final_nbr)
    new_aux = ''
    nbr.reverse()
    while nbr:
        new_aux += str(nbr.pop())
    if final_nbr == '':
        final_nbr = '0'
    if new_aux != '':
        final_nbr = final_nbr + '.' + new_aux
    return final_nbr


def trans_from_b10(nbr_zecimal):
    if nbr_zecimal[0] == '-':
        semn = 1
        nbr_zecimal = nbr_zecimal.replace('-','')
    else:
        semn = 0
    nbr_zecimal2 = ''
    for i in nbr_zecimal:
        if i != ' ':
            nbr_zecimal2 += i
    nbr_zecimal = nbr_zecimal2
    nbr_binar = float(trans_in_b2(nbr_zecimal))
    i = 0
    while nbr_binar < 1:
        nbr_binar *= 10
        i -= 1
    caract = str(trans_in_b2(i+127))
    mantisa = nbr_binar - math.floor(nbr_binar)
    mantisa = str("{:.10f}".format(float(mantisa)))
    mantisa = mantisa.replace('0.','')
    nbr_in_pr_simplelista = []
    caract_list = []
    for i in caract:
        caract_list.append(i)
    while len(caract_list) < 8:
        caract_list.insert(0,'0')
    nbr_in_pr_simplelista.append(semn)
    nbr_in_pr_simplelista.append(' ')
    for i in caract_list:
        nbr_in_pr_simplelista.append(i)
    nbr_in_pr_simplelista.append(' ')
    for i in mantisa:
        nbr_in_pr_simplelista.append(i)
    nbr_in_precizie_simpla = ''
    for i in nbr_in_pr_simplelista:
        nbr_in_precizie_simpla += str(i)
    return nbr_in_precizie_simpla

#nbr_zecimal = '-0.75'
nbr_binar = '1 1000 0001 01 '

#nbr_binar = str(trans_from_b10(nbr_zecimal))

nbr_zecimal = str(trans_in_b10(nbr_binar))
nbr_zecimal = f"{float(nbr_zecimal):.2f}"

print(f'Number in zecimal: {nbr_zecimal}')
print(f'Number in binar: {nbr_binar}')