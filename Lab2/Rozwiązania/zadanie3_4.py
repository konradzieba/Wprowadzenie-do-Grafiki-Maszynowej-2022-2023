from PIL import Image
import numpy as np




#Funkcja dzieląca obrazek czarna kreska pionowo na pół, gdzie druga połówka jest dodatkowo podzielona poziomo na pół
#grubość kresek dzielących to 6px

def wlasne(w, h):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    srodek_h = int(h/2)
    srodek_w = int(w/2)
    tab[0:h, 0:w] = 255
    tab[0:srodek_h, srodek_w-3:srodek_w+3] = 0
    tab[srodek_h:h, srodek_w-3:srodek_w + 3] = 0
    tab[srodek_h-3:srodek_h+3, srodek_w::] = 0
    return tab


zadanie3_4_tab = wlasne(480, 320)
zadanie3_4_obrazek = Image.fromarray(zadanie3_4_tab)
zadanie3_4_obrazek.show()
zadanie3_4_obrazek.save('zadanie3_4_obrazek.bmp', mode='1')
