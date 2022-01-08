import time
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
precision = 4
nr = '54323.465'
base_nr = 16
base_convert = 10
#There is the place if I check if the nr has any decimals
if "." in nr:
    no_decimal, decimal = str(nr).split(".")
else:
    no_decimal = nr
    decimal = '0'

#base n to base 10 without decimals

def base_n_to_10(nr_, base_of_nr_):
    rez = 0
    ct = (len(str(nr_)) - 1)
    for i in str(nr_):
        rez += numbers.index(i) * (base_of_nr_ ** ct)
        ct -= 1

    return rez

#base n to base 10 with decimals

def base_n_to_10_d(nr_, base_of_nr_):
    output = str(base_n_to_10(no_decimal, base_of_nr_)) + "."
    rez = 0
    ct = 1
    for i in str(decimal):
        if ct == 0:
            break
        rez += numbers.index(i) * (base_of_nr_ ** -ct)
        ct += 1

    return float(output) + rez

#base 10 to base n without decimals
def base_10_to_any(nr_, base_):
    digits = []
    # Algorithm to transform from base 10 to any base lower than 16
    while nr_ != 0:
        digit = nr_ % base_
        digits.insert(0, numbers[int(digit)])
        nr_ = nr_ // base_
    # output str instead of list
    return ''.join(map(str, digits))

#base 10 to base n with decimals
def base_10_to_any_d(nr_, base_):
    no_decimal, decimal = str(nr_).split(".")
    no_decimal = int(no_decimal)
    output = base_10_to_any(no_decimal, base_) + "."

    for _ in range(precision):
        decimal = str('0.') + str(decimal)
        temp = '%1.16f' % (float(decimal) * base_)
        no_decimal, decimal = temp.split(".")
        output += numbers[int(no_decimal)]

    if no_decimal == 0:
        return '0' + output

    return output


def convertor(nr, base_nr, base_convert):
    if base_nr == 10:
        return (base_10_to_any_d(nr, base_convert))
    else:
        return (base_10_to_any_d(base_n_to_10_d(nr, base_nr), base_convert))

print("╔══════════════════════════════════════════════╗")
print(f"║INPUT in base {base_nr}, NR={nr}")
print(f"║Loading",end='')
time.sleep(0.3)
print(f".",end='')
time.sleep(0.4)
print(f".",end='')
time.sleep(0.4)
print(f".",end='')
time.sleep(0.4)
print("DONE :)")
for i in f"║OUTPUT in base {base_convert} => ", convertor(nr, base_nr, base_convert):
    time.sleep(0.7)
    print(i,end="")
print("")
print("╚══════════════════════════════════════════════╝")