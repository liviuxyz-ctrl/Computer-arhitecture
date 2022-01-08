import time

mini_calculator = True


class Au(ZeroDivisionError):
    def __init__(self, m):
        self.m = m

    def __str__(self):
        return self.m


# main function which calculate every operation
def simple_trans(nr1, nr2, gen_base, op, decimal_1, no_decimal_1, decimal_2, no_decimal_2):
    # calc + operation
    match op:
        case "+":
            if gen_base == '10':
                return float(base_10_to_any_d(convertor(nr1, gen_base, 10, decimal_1, no_decimal_1), gen_base, decimal_1,
                                              no_decimal_1)) + float(
                    base_10_to_any_d(convertor(nr2, gen_base, 10, decimal_2, no_decimal_2), gen_base, decimal_2,
                                     no_decimal_2))
            else:
                return float(base_n_to_10_d(convertor(nr1, gen_base, 10, decimal_1, no_decimal_1), gen_base, decimal_1,
                                            no_decimal_1)) + float(
                    base_n_to_10_d(convertor(nr2, gen_base, 10, decimal_2, no_decimal_2), gen_base, decimal_2,
                                   no_decimal_2))

        case "-":
            if gen_base == '10':
                return float(base_10_to_any_d(convertor(nr1, gen_base, 10, decimal_1, no_decimal_1), gen_base, decimal_1,
                                              no_decimal_1)) - float(
                    base_10_to_any_d(convertor(nr2, gen_base, 10, decimal_2, no_decimal_2), gen_base, decimal_2,
                                     no_decimal_2))
            else:
                return float(base_n_to_10_d(convertor(nr1, gen_base, 10, decimal_1, no_decimal_1), gen_base, decimal_1,
                                            no_decimal_1)) - float(
                    base_n_to_10_d(convertor(nr2, gen_base, 10, decimal_2, no_decimal_2), gen_base, decimal_2,
                                   no_decimal_2))
        case "/":
            if gen_base == '10':
                return float(base_10_to_any_d(convertor(nr1, gen_base, 10, decimal_1, no_decimal_1), gen_base, decimal_1,
                                              no_decimal_1)) / float(
                    base_10_to_any_d(convertor(nr2, gen_base, 10, decimal_2, no_decimal_2), gen_base, decimal_2,
                                     no_decimal_2))
            else:
                return float(base_n_to_10_d(convertor(nr1, gen_base, 10, decimal_1, no_decimal_1), gen_base, decimal_1,
                                            no_decimal_1)) / float(
                    base_n_to_10_d(convertor(nr2, gen_base, 10, decimal_2, no_decimal_2), gen_base, decimal_2,
                                   no_decimal_2))
        case "*":
            if gen_base == '10':
                return float(base_10_to_any_d(convertor(nr1, gen_base, 10, decimal_1, no_decimal_1), gen_base, decimal_1,
                                              no_decimal_1)) * float(
                    base_10_to_any_d(convertor(nr2, gen_base, 10, decimal_2, no_decimal_2), gen_base, decimal_2,
                                     no_decimal_2))
            else:
                return float(base_n_to_10_d(convertor(nr1, gen_base, 10, decimal_1, no_decimal_1), gen_base, decimal_1,
                                            no_decimal_1)) * float(
                    base_n_to_10_d(convertor(nr2, gen_base, 10, decimal_2, no_decimal_2), gen_base, decimal_2,
                                   no_decimal_2))


numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
# REMEMBER TO CHANGE THIS AS WELL
precision = 4
nr = '22'
base_nr = 10
base_convert = 10
# There is the place if I check is the nr has any decimals

if "." in nr:
    no_decimal, decimal = str(nr).split(".")
else:
    no_decimal = nr
    decimal = '0'


def base_n_to_10(nr_, base_of_nr_):
    rez = 0
    ct = (len(str(nr_)) - 1)
    for i in str(nr_):
        rez += int(numbers.index(i)) * (int(base_of_nr_) ** int(ct))
        ct -= 1

    return rez


def base_n_to_10_d(nr_, base_of_nr_, decimal_, no_decimal_):
    output = str(base_n_to_10(no_decimal_, base_of_nr_)) + "."
    rez = 0
    ct = 1
    for i in str(decimal_):
        if ct == 0:
            break
        rez += int(numbers.index(i)) * (int(base_of_nr_) ** int(-ct))
        ct += 1

    return float(output) + rez


def base_10_to_any(nr_, base_):
    digits = []
    # Algorithm to transform from base 10 to any base lower than 16
    while nr_ != 0:
        digit = float(nr_) % float(base_)
        digits.insert(0, numbers[int(digit)])
        nr_ = float(nr_) // float(base_)
    # output str instead of list
    return ''.join(map(str, digits))


def base_10_to_any_d(nr_, base_, decimal_, no_decimal_):
    nr_ = str(nr_)
    if "." in nr_:
        no_decimal, decimal = str(nr_).split(".")
    else:
        decimal = 0
        no_decimal = int(nr_)
    no_decimal = no_decimal
    output = base_10_to_any(no_decimal, base_) + "."

    for _ in range(precision):
        decimal = str('0.') + str(decimal)
        temp = '%1.16f' % (float(decimal) * float(base_))
        no_decimal, decimal = temp.split(".")
        output += numbers[int(no_decimal)]

    if no_decimal == 0:
        return '0' + output

    return output


def convertor(nr, base_nr, base_convert, decimal_, no_decimal):
    base_nr = int(base_nr)
    if base_nr == 10:
        return (base_10_to_any_d(nr, base_convert, decimal_, no_decimal))
    else:
        return (base_10_to_any_d(base_n_to_10_d(nr, base_nr, decimal_, no_decimal), base_convert, decimal_, no_decimal))


if mini_calculator is False:
    print("╔══════════════════════════════════════════════╗")
    print(f"║INPUT in base {base_nr}, NR={nr}")
    print(f"║Loading", end='')
    time.sleep(0.3)
    print(f".", end='')
    time.sleep(0.4)
    print(f".", end='')
    time.sleep(0.4)
    print(f".", end='')
    time.sleep(0.4)
    print("DONE :)")
    decimal_ = 0
    no_decimal_ = nr
    for i in f"║OUTPUT in base {base_convert} => ", convertor(nr, base_nr, base_convert, decimal_, no_decimal_),:
        time.sleep(0.3)
        print(i, end="")
    print("")
    print("╚══════════════════════════════════════════════╝")

elif mini_calculator is True:
    print("Enter the numbers you want to use.")
    nr1 = input()
    nr2 = input()
    print("Enter the base of the respective numbers")
    gen_base = input()
    base_nr = int(gen_base)
    print('Choose one of the following operations: "+", "-" "/" "*"')
    op = input()
    if op == "/" and nr2 == '0':
        raise Au("Can't divide by zero :(")
    if "." in nr1:
        no_decimal_1, decimal_1 = str(nr1).split(".")
    else:
        no_decimal_1 = nr1
        decimal_1 = '0'

    if "." in nr2:
        no_decimal_2, decimal_2 = str(nr2).split(".")
    else:
        no_decimal_2 = nr2
        decimal_2 = '0'
    # print(calc(nr1, nr2, gen_base, op))

    print("╔══════════════════════════════════════════════╗")
    print(f"║INPUT one in base {gen_base}, NR={nr1}")
    print(f"║INPUT two in base {gen_base}, NR={nr2}")
    print(f"║Calculating")
    print(f".", end='')
    time.sleep(0.4)
    print(f".", end='')
    time.sleep(0.4)
    print(f".", end='')
    time.sleep(0.4)
    print("DONE :)")
    print(nr1.rjust(35))
    print(nr2.rjust(35))
    print("".rjust(35 - max(len(nr1), len(nr2))), end="")
    for i in range(max(len(nr1), len(nr2))):
        print("═", end="")
    print(op)
    nr_final = simple_trans(nr1, nr2, gen_base, op, decimal_1, no_decimal_1, decimal_2, no_decimal_2)
    nr_final = str(nr_final)

    if "." in nr_final:
        no_decimal_z, decimal_z = nr_final.split(".")
    else:
        no_decimal_z = nr_final
        decimal_z = '0'

    nr_final_deci = convertor(nr_final, 10, gen_base, decimal_z, no_decimal_z)  # nr_final conv in baza b
    print(str(nr_final_deci).rjust(30 + precision))
    print("╚══════════════════════════════════════════════╝")
