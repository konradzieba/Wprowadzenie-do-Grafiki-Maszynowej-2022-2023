from PIL import Image
import numpy as np
import random

'''Losowanie koloru pierwszego z zakresu <34..220>, aby uniknąć wylosowania kolorów
bardzo zbliżonych do białego czy czarnego'''
gray_type1 = random.randint(35, 220)
gray_type2 = random.randint(35, 220)

# print(gray_type1, gray_type2)

'''Upewnienie się, że kolor pierwszego kwadratu (najbardziej zewnętrznego) będzie ciemniejszy od drugiego w kolejności, 
oraz pomiędzy wylosowanymi kolorami będzie 50 jednostek różnicy, w każdym innym przypadku losuje liczbę na nowo'''
while gray_type2 >= gray_type1 or abs(gray_type1 - gray_type2) < 50:
    gray_type1 = random.randint(35, 220)
    gray_type2 = random.randint(35, 220)

# print(gray_type1,gray_type2)

def rysuj_ramke(w, h, dzielnik):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    grubosc = int(min(w, h) / dzielnik)
    return _recursive(tab, h, w, grubosc, 0)

def rysuj_ramke_negative(w, h, dzielnik):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    grubosc = int(min(w, h) / dzielnik)
    return _recursive_negative(tab, h, w, grubosc, 0)


def _recursive(tablica, h, w, grubosc, wsp):
    #warunek konczacy
    if wsp > int(w / 2) and wsp > int(h / 2):
        return tablica
    #rekurencja
    else:
        tablica[wsp:h, wsp:w] = gray_type2
        for i in range(0 + wsp, h):
            for j in range(0 + wsp, w):
                if i >= grubosc + wsp and i < h - grubosc and j >= grubosc + wsp and j < w - grubosc:
                    tablica[i, j] = gray_type1
        return _recursive(tablica, h - (2*grubosc), w - (2*grubosc), grubosc, wsp + (2 * grubosc))

def _recursive_negative(tablica, h, w, grubosc, wsp):
    #warunek konczacy
    if wsp > int(w / 2) and wsp > int(h / 2):
        return tablica
    #rekurencja
    else:
        tablica[wsp:h, wsp:w] = (255 - gray_type2)
        for i in range(0 + wsp, h):
            for j in range(0 + wsp, w):
                if i >= grubosc + wsp and i < h - grubosc and j >= grubosc + wsp and j < w - grubosc:
                    tablica[i, j] = (255 - gray_type1)
        return _recursive_negative(tablica, h - (2*grubosc), w - (2*grubosc), grubosc, wsp + (2 * grubosc))

tab = rysuj_ramke(1366, 768, 10)
obrazek = Image.fromarray(tab)

tab_negative = rysuj_ramke_negative(1366,768,10)
obrazek_negative = Image.fromarray(tab_negative)


obrazek.show()
obrazek_negative.show()
obrazek.save('obraz1_1.jpg', mode='L')
obrazek.save('obraz1_1.png', mode='L')

obrazek_negative.save('obraz1_1N.jpg', mode='L')
obrazek_negative.save('obraz1_1N.png', mode='L')
