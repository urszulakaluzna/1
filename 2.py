a = int(input("Podaj liczbę: "))

if a % 2 == 0:
    print("Wybrana liczba jest parzysta!")
    if a % 4 == 0:
        print("Wybrana liczba jest podzielna przez 4.")
    else:
        print("Wybrana liczba jest nie podzielna przez 4.")
else:
    print("Wybrana liczba jest nieparzysta.")