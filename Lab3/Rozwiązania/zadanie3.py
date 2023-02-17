import numpy as np
from PIL import Image
import random


def kolorowe_pasy_inicjaly(tab):
    h, w = tab.shape
    colored_tab = np.ones((h, w, 3), dtype=np.uint8)
    for i in range(h):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        for j in range(w):
            if tab[i][j] == False:
                colored_tab[i][j] = [r, g, b]
            else:
                colored_tab[i][j] = [255, 255, 255]
    return colored_tab

obrazek = Image.open('inicjaly.bmp')
obrazek_tab = np.asarray(obrazek)

kolorowe_pasy_tab = kolorowe_pasy_inicjaly(obrazek_tab)

obrazek_rgb = Image.fromarray(kolorowe_pasy_tab)
obrazek_rgb.show()

obrazek_rgb.save('obraz3.jpg', mode='RGB')
obrazek_rgb.save('obraz3.png', mode='RGB')