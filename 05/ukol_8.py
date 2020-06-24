rodne_cislo = input("Jake je tvoje rodne cislo? ")

# (a)
def format_check(rodne_cislo):
    if len(rodne_cislo) != 11:
        return False
    if rodne_cislo[6] != '/':
        return False
    if not rodne_cislo[0:6].isdigit() or not rodne_cislo[7:11].isdigit():
        return False
    else:
        return True

# (b)
def division_by_eleven(rodne_cislo):
    rodne_cislo_withoutslash = rodne_cislo[:6] + rodne_cislo[7:]
    rodne_cislo_int = int(rodne_cislo_withoutslash)
    if rodne_cislo_int % 11 != 0:
        return False
    else:
        return True

# (c)
# rok
def year_check(rodne_cislo):
    year = int(rodne_cislo[0:2])
    if year < 85 and year > 20:
        return False
    else: 
        return True

# den
def day_check(rodne_cislo):
    day = int(rodne_cislo[4:6])
    if day > 31:
        return False
    else:
        return True

# mesic
def month_check(rodne_cislo):
    month = int(rodne_cislo[2:4])
    correct_month = list(range(1, 13)) + list(range(21, 33)) + list(range(51, 63)) + list(range(71, 83))
    if month in correct_month:
        return True
    else:
        return False

def check_rc(rodne_cislo):
    if (
        format_check(rodne_cislo) and 
        division_by_eleven(rodne_cislo) and 
        year_check(rodne_cislo) and 
        month_check(rodne_cislo) and 
        day_check(rodne_cislo)
        ):
        return 'Zadal jsi spravne rodne cislo'
    else:
        return 'Rodne cislo je nespravne nebo jsi prilis stary :)'

print(check_rc(rodne_cislo))

# (d)
def gender_check(rodne_cislo):
    try:
        month = int(rodne_cislo[2:4])
    except ValueError:
        print('Zadano nevalidni rodne cislo, nelze urcit pohlavi')
        return
    if month > 50:
        print('Jsi zena')
    else:
        print('Jsi muz')

gender_check(rodne_cislo)

