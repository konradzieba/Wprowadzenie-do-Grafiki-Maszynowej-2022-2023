from PIL import Image
import numpy as np

def rysuj_pasy_pionowe(w, h, dzielnik):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    grubosc = int(w / dzielnik)
    for k in range(dzielnik):
        for g in range(grubosc):
            i = k * grubosc + g
            for j in range(h):
                tab[j, i] = k % 2
    tab = tab * 255
    return tab


zadanie3_2_tab = rysuj_pasy_pionowe(480, 320, 8)
zadanie3_2_obraz = Image.fromarray(zadanie3_2_tab)
zadanie3_2_obraz.show()
zadanie3_2_obraz.save('zadanie3_2_obrazek.bmp', mode='1')


