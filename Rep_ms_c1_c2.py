def bits_sizing(local_list, n):
    """
    #Add 0 to the list until it has the required
    size like 4,8,16... and so on
    :return:
    """
    while len(local_list) < n:
        local_list.append(0)
    return local_list


def bits_checking(number_):
    """
    Checking how many bits
    do wee need
    :return: int
    """
    n = 4
    while abs(number_) > 2 ** (n - 1):
        n *= 2
    return n


def base10_to_base2(number_):
    """
    Convert from base10
    to base2
    :return: list
    """
    local_list = []
    num = abs(number_)
    while num:
        local_list.append(num % 2)
        num //= 2
    return bits_sizing(local_list, bits_checking(number_))


def list_to_string(this_list):
    """
    We are converting from
    one list to a string
    and also we are reversing
    the result
    :param this_list: list
    :return: string
    """
    this_list.reverse()
    return ''.join(map(str, this_list))


def c1_rep(local_list):
    """
    Representation in C1
    :param local_list:list
    :return:list
    """
    for i in range(len(local_list)):
        local_list[i] = (local_list[i] + 1) % 2
    return local_list



def c2_rep(num1, n):
    """
    Representation in C2
    :return: c2_result int
    """
    x = 1
    num2 = [1 for _ in range(n + 1)]
    c2_result = [num2[i] - num1[i] for i in range(n)]
    for i in range(n):
        c2_result[i] += x
        if c2_result[i] != 2:
            x = 0
        c2_result[i] %= 2
    return c2_result


def transform(number_, form='MS'):
    number_ = str(number_)
    negative_zero = number_ == '-0'
    number_ = int(number_)
    nbr_bits = bits_checking(number_)
    number_in_b2 = base10_to_base2(number_)
    if number_ < 0 or negative_zero:
        c1 = c1_rep(number_in_b2.copy())
        c2 = c2_rep(number_in_b2.copy(), nbr_bits)
        # set the last element to one for bit sign
        number_in_b2[len(number_in_b2) - 1] = 1
    else:
        # bcs they are not negative numbers they have the same rep. in C1 and C2
        c1 = number_in_b2.copy()
        c2 = number_in_b2.copy()
    ms = number_in_b2
    represent_ms = list_to_string(ms)
    represent_c1 = list_to_string(c1)
    represent_c2 = list_to_string(c2)
    if form == "C1":
        return represent_c1
    elif form == "C2":
        return represent_c2
    elif form == "MS":
        return represent_ms


# bcs we are using this in other programs as well
if __name__ == "__main__":
    print("Introduceți numărul dorit: ", end="")
    number = input()
    print(f'In mărime si stare (MS)  {transform(number, "MS")}')
    print(f'In reprezentare fată de complement 1 (C1): {transform(number, "C1")}')
    print(f'In reprezentare fată de complement 2 (C2): {transform(number, "C2")}')
