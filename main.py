import argparse
import kalkulator

def parse_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode")
    parser.add_argument("--name")

    return parser.parse_args()


def dodawanie():
    print("Jakie liczby chcesz dodać?")

    a = int(input("Pierwsza liczba"))
    b = int(input("Druga liczba"))

    result = a + b
    return f"Wynik działania {a} + {b}  = {result}"


def odejmowanie():
    print("Jakie liczby chcesz odjąć?")

    a = int(input("Pierwsza liczba"))
    b = int(input("Druga liczba"))

    result = a - b
    return f"Wynik działania {a} - {b} = {result}"


def glowna(mode):

    if mode == '1':
        print(dodawanie())
    elif mode == '2':
        print(odejmowanie())
    else:
        print("Źle podany parametr")


if '__main__' == __name__:

    nasze_parametry = parse_argument()
    kalkulator.menu(nasze_parametry.name)
    mode = nasze_parametry.mode
    glowna(mode)