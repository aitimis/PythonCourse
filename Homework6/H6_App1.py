""" Homework 6 - needs to be presented before exam day
O fabrica de masini are nevoie de un obiect iterabil care sa contina seriile si loturile masinilor produse in ziua respectiva.
Seriile si loturile sunt numere intregi de tip int
Un lot este alcatuit din 20 de masini jumatate din lot sunt cu volan pe dreapta si jumatate cu volan pe stanga
Numerotarea loturilor incepe de la prima masina produsa cu seria 1 si lot 1
Ziua de lucru stocata in obiectul contruit de voi poate incepe cu orice numar de serie si numarul de bucati produse in acea zi poate avea orice valoare
Obiectul iterat va returna numerele loturilor din care fac parte masinile din acea zi, numerotarea lor a inceput de la prima masina produsa cu seria 0 si lot 0
Masinile cu serii pare sunt cu volan pe dreapta iar cele cu serii impare cu volan pe stanga
1)Definire: 40p
  - Creati o clasa pentru un obiect iterabil
   a) constructorul primeste doua argumente de tip int, seria de inceput si numarul de bucati. ex: (101, 41) 10p
   b) obiectul are doua metode: prima returneaza o lista cu seriile cu volan pe dreapta si a doua o lista cu seriile cu volan pe stanga 15p
   c) iterator-ul returnat de object va comtine loturile din care fac parte seriile din obiectul curent  15p
2) Executie: 40p
- Creati o instanta a clasei de mai sus dand ca argumente: serie_inceput 314, bucati 90. 10p
- Iterati obiectul creat si salvati fiecare valoare din iteratie in acelas fisier pe linie noua. 30p
3) Documentatie: 20p
   a) adaugati type hints 5p
   a) documentati modulul 5p
   b) documentati clasele 5p
   c) documentati metodele 5p
"""

class CarsFactory:
    """ main factory """
    def __init__(self, series: int,  lot_nr: int):
        """ contructor """
        self.series = series
        self.lot_nr = lot_nr

    def left_hand(self):
      """ left hand cars method """
        left_hand_list = []
        for i in range(series, lot_nr):
            if i % 2 != 0:
                left_hand_list.append(i)
        return left_hand_list

    def right_hand(self):
      """ right hand cars method """
        right_hard_list = []
        for i in range(series, lot_nr):
            if i % 2 == 0:
                right_hard_list.append(i)
        return right_hard_list

    def __iter__(self):
        return CarsIterator


class CarsIterator:
    """ class for iteration """
    def __init__(self, data: list):
        """ constructor """
        self.data = data

    def __next__(self):
        if not self.data:
            raise StopIteration
        return self.data.pop()

    def __iter__(self):
        return self


car_result = CarsFactory(314, 90)

with open('Datafile.txt', 'w') as file:
    for i in car_result:
        file.write(str(i) + '\n')
