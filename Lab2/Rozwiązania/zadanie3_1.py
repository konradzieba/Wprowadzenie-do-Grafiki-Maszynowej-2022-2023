from PIL import Image
import numpy as np


def rysuj_ramke(w, h, dzielnik):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    grubosc = int(min(w, h) / dzielnik)
    return _recursive(tab, h, w, grubosc, 0)


def _recursive(tablica, h, w, grubosc, wsp):
    #warunek konczacy
    if wsp > int(w / 2) and wsp > int(h / 2):
        return tablica
    #rekurencja
    else:
        tablica[wsp:h, wsp:w] = 0
        for i in range(0 + wsp, h):
            for j in range(0 + wsp, w):
                if i >= grubosc + wsp and i < h - grubosc and j >= grubosc + wsp and j < w - grubosc:
                    tablica[i, j] = 255
        return _recursive(tablica, h - (2*grubosc), w - (2*grubosc), grubosc, wsp + (2 * grubosc))

tab = rysuj_ramke(480, 320, 8)
obrazek = Image.fromarray(tab)
obrazek.show()
obrazek.save('zadanie3_1.bmp', mode='1')