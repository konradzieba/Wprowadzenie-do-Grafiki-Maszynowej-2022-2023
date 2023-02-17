from PIL import Image
import numpy as np
import random

gray_lines = random.randint(35, 220)
gray_background = random.randint(35, 220)

# print(gray_lines, gray_background)

while gray_background <= gray_lines or abs(gray_lines - gray_background) < 50:
    gray_lines = random.randint(35, 220)
    gray_background = random.randint(35, 220)

# print(gray_lines, gray_background)


def wlasne(w, h):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    srodek_h = int(h/2)
    srodek_w = int(w/2)
    tab[0:h, 0:w] = gray_background
    tab[0:srodek_h, srodek_w-3:srodek_w+3] = gray_lines
    tab[srodek_h:h, srodek_w-3:srodek_w + 3] = gray_lines
    tab[srodek_h-3:srodek_h+3, srodek_w::] = gray_lines
    return tab

def wlasne_negative(w, h):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    srodek_h = int(h/2)
    srodek_w = int(w/2)
    tab[0:h, 0:w] = (255 - gray_background)
    tab[0:srodek_h, srodek_w-3:srodek_w+3] = (255 - gray_lines)
    tab[srodek_h:h, srodek_w-3:srodek_w + 3] = (255 - gray_lines)
    tab[srodek_h-3:srodek_h+3, srodek_w::] = (255 - gray_lines)
    return tab

zadanie1_2_tab = wlasne(1366, 768)
zadanie1_2 = Image.fromarray(zadanie1_2_tab)
zadanie1_2.show()

zadanie1_2_tab_negative = wlasne_negative(1366, 768)
zadanie1_2_negative = Image.fromarray(zadanie1_2_tab_negative)
zadanie1_2_negative.show()

zadanie1_2.save('obraz1_2.jpg', mode='L')
zadanie1_2.save('obraz1_2.png', mode='L')

zadanie1_2_negative.save('obraz1_2_N.jpg', mode='L')
zadanie1_2_negative.save('obraz1_2_N.png', mode='L')
