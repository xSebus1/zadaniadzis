def utworz_samochod():
    pobrana_wartość = input("Wporwadz rocznik: ")
    pobrana_wartość2 = input("Wporwadz silnik: ")
    pobrana_wartość3 = input("Wporwadz marke: ")
    pobrana_wartość4 = input("Wprowadz kolor: ")
    samochody = {}
    samochody['rocznik'] = pobrana_wartość
    samochody['silnik'] = pobrana_wartość2
    samochody['marka'] = pobrana_wartość3
    samochody['kolor'] = pobrana_wartość4

    return samochody

print(utworz_samochod())