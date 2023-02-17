# from PIL import Image
# import numpy as np
#
# inicjaly = Image.open('inicjaly.bmp')
# tablica_obrazka = np.asarray(inicjaly)
# # print(tablica_obrazka)
#
# zad6 = np.loadtxt('inicjaly.txt', dtype=np.int_)
#
# print(f'Czy elementy są takie same? -> {tablica_obrazka.all() == zad6.all()}')
# print(f'Czy typ danych jest taki sam? -> {tablica_obrazka.dtype == zad6.dtype}')
# print(f'Czy rozmiar jest taki sam? -> {tablica_obrazka.shape == zad6.shape}')
# print(f'Czy liczba elementow jest taka sama? -> {tablica_obrazka.size == zad6.size}')
# print(f'Czy wymiar taki jest sam? -> {tablica_obrazka.ndim == zad6.ndim}')
# print(f'Czy rozmiar wyrazu jest taki sam? -> {tablica_obrazka.itemsize == zad6.itemsize}')
#
# obrazek = Image.fromarray(zad6)
# print(obrazek.mode)
# obrazek.show()

def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))

print(increment_string('ala123'))
