from PIL import Image
import numpy as np

def prostokaty(w, h, m, n):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    tab[0:n, 0:m] = 0
    tab[n:h, m:w] = 0
    tab = tab * 255
    return tab



zadanie3_3_tab1 = prostokaty(480, 320, 100, 50)
zadanie3_3_obrazek1 = Image.fromarray(zadanie3_3_tab1)
zadanie3_3_obrazek1.show()
zadanie3_3_obrazek1.save('zadanie3_3_obrazek1.bmp', mode='1')

