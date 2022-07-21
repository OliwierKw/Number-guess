import random

granica = input("Do ilu liczb chcesz zgadywać?: ")

if granica.isdigit(): #czy jest cyfra
    granica = int(granica)
    if granica <= 0:
        print("Wybierz liczbę większą od zera następnym razem.")
        quit()
else:
    print("Wybierz liczbę zamiast textu następnym razem.")
    quit()

wylosowany_numer = random.randint(1,granica) # czemu w randrange(11) daje do 10
# losuje liczbe z przedzialu od 0 do granicy ustalonej
proby = 0


while True: # true zawsze true
    proby += 1
    liczba_gracza = input("Jaka liczba?: ")
    if liczba_gracza.isdigit():  # czy jest cyfra
        liczba_gracza = int(liczba_gracza)
    else:
        print("Wybierz liczbę zamiast textu następnym razem.")
        continue

    if liczba_gracza == wylosowany_numer:
        print("Wygrałeś!!! Brawo ty!")
        break
    else:
        if liczba_gracza > wylosowany_numer:
            print("Trochę niższa liczba :)")
        else:
            print("Trochę większa liczba :)")

print("Udało ci się za",proby,"próbą!")