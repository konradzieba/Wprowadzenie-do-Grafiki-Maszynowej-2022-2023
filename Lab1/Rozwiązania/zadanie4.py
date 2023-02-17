from PIL import Image
import numpy as np

zad4 = np.loadtxt('inicjaly.txt', dtype=np.int_)
# print(f'Typ danych tablicy: {zad4.dtype}')
# print(f'Rozmiar tablicy: {zad4.shape}')
# print(f'Liczba elementów tablicy: {zad4.size}')
# print(f'Wymiar tablicy: {zad4.ndim}')
# print(f'Rozmiar wyrazu tablicy: {zad4.itemsize}')


print(f'Wartość pikseli o adresach (50,30): {zad4[30][50]}')
# print(f'Wartość pikseli o adresach (90,30): {zad4[40][90]}')
# print(f'Wartość pikseli o adresach (99,0): {zad4[0][99]}')


