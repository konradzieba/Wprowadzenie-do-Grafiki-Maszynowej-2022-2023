from PIL import Image
import numpy as np
import random

lista_kolorow = np.arange(0, 256, 1)
lista_kolorow = [int(element) for element in lista_kolorow]


def rysuj_pasy_pionowe_kolor(w, h, dzielnik, kolor):
    t = (h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    tab[:] = kolor
    grub = int(w / dzielnik)
    for k in range(dzielnik):
        r = (kolor[0] + random.choice(lista_kolorow)) % 256
        g = (kolor[1] + random.choice(lista_kolorow)) % 256
        b = (kolor[2] + random.choice(lista_kolorow)) % 256
        for gr in range(grub):
            i = k * grub + gr
            for j in range(h):
                tab[j, i] = [r, g, b]
    return tab

def negatyw_tablicy_kolor(tab):
    tab_n = tab.copy()
    for i in range(0, tab_n.shape[0]):
        for j in range(0, tab_n.shape[1]):
            pixel = tab_n[i][j]
            negative_pixel = [255 - pixel[0], 255 - pixel[1], 255 - pixel[2]]
            tab_n[i][j] = negative_pixel
    return tab_n



#
zadanie2_tab = rysuj_pasy_pionowe_kolor(720, 480, 8, [0,0,0])
zadanie2_tab_negative = negatyw_tablicy_kolor(zadanie2_tab)
zadanie2 = Image.fromarray(zadanie2_tab)
zadanie2_negative = Image.fromarray(zadanie2_tab_negative)
zadanie2.show()
zadanie2_negative.show()

zadanie2.save('obraz2.jpg', mode='RGB')
zadanie2.save('obraz2.png', mode='RGB')
zadanie2_negative.save('obraz2N.jpg', mode='RGB')
zadanie2_negative.save('obraz2N.png', mode='RGB')
