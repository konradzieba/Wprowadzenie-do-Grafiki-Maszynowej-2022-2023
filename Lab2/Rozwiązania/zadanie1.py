from PIL import Image
import numpy as np

inicjaly = Image.open("inicjaly.bmp")
print("tryb", inicjaly.mode)
print("format", inicjaly.format)
print("rozmiar", inicjaly.size)

obraz_wstawiany = np.asarray(inicjaly)
print("typ danych tablicy", obraz_wstawiany.dtype)
print("rozmiar tablicy", obraz_wstawiany.shape)


def wstaw_obraz(obraz_wstawiany, w_m, h_m, wsp):
    h0, w0 = obraz_wstawiany.shape
    print(h0,w0)
    t = (int(wsp*h0), int(wsp*w0))
    height_border = t[0]
    width_border = t[1]
    tab = np.zeros(t, dtype=np.uint8)

    if wsp <= 1:
        raise ValueError("Wspolczynnik powinien wynosić więcej niż 1")

    if h_m + h0 < height_border:
        height_border = h_m + h0
    if w_m + w0 < width_border:
        width_border = w_m + w0

    for i in range(h_m, height_border):
        for j in range(w_m, width_border):
            tab[i][j] = obraz_wstawiany[i - h_m][j - w_m]
    tab = tab.astype(bool)
    done = Image.fromarray(tab)
    return done

# obrazek1 = wstaw_obraz(obraz_wstawiany,180,0,2)
# obrazek1.save('obrazek_zadanie1.bmp', mode='1')
# obrazek1.show()

