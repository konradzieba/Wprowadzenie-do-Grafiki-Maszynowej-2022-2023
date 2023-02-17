import time
from PIL import Image, ImageChops
import numpy as np

st = time.time()


# 2.1
def mirror_top_bottom(img):
    img_copy = img.copy()
    img_t = img.load()
    img_copy_t = img_copy.load()
    k = 0
    for i in range(img.size[0])[::-1]:
        l = 0
        for j in range(img.size[1])[::-1]:
            img_t[k, l] = img_copy_t[i, j]
            l += 1
        k += 1
    return img


# 2.1 - inne rozwiązanie - szybsze
def mirror_top_bottom_np(img):
    tmp = np.asarray(img)
    reverse = tmp[::-1, ::-1]
    return Image.fromarray(reverse)


# 2.2
def mirror_bottom_to_top(img):
    tab = np.asarray(img)
    # w, h = img.size
    # w2 = int(w / 2)
    # h2 = int(h / 2)
    tab_split = np.array_split(tab, 2)
    reverse = tab[::-1, ::]
    reverse_split = np.array_split(reverse, 2)
    result = np.concatenate((reverse_split[0], tab_split[1]), axis=0)
    return Image.fromarray(result)


# 2.3
def mirror_top_to_bottom(img):
    tab = np.asarray(img)
    # w, h = img.size
    # w2 = int(w / 2)
    # h2 = int(h / 2)
    tab_split = np.array_split(tab, 2)
    reverse = tab[::-1, ::]
    reverse_split = np.array_split(reverse, 2)
    result = np.concatenate((tab_split[0], reverse_split[1]), axis=0)
    return Image.fromarray(result)

# 2.4
# Trzeba miec 2 tablice bo inaczej to przypisujemy wartosci tej samej tablicy to tej samej


def zakres(w, h):
    return [(i, j) for i in range(w) for j in range(h)]


# 3.0
def rysuj_kolo(obraz, m_s, n_s, r, innym_s, innyn_s):
    obraz1 = obraz.copy()
    w, h = obraz.size
    px = []
    k = 0
    for i, j in zakres(w, h):
        if (i - innym_s) ** 2 + (j - innyn_s) ** 2 < r ** 2:
            px.append(obraz1.getpixel((i, j)))
    for i, j in zakres(w, h):
        if (i - m_s)**2 + (j - n_s)**2 < r**2:
            obraz1.putpixel((i, j), px[k])
    return obraz1

# 3.1
# Na ten sam obraz musimy wielokronie uzyć funkcji z 3 za kazdym razem podając inne współrzędne


img = Image.open('baby_yoda.jpg')
img_copy = img.copy()
img_copy2 = img.copy()

# porównanie szybkości kodu
et = time.time()
final = et - st
print(final * 1000)
