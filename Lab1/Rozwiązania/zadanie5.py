from PIL import Image
import numpy as np

inicjaly = Image.open('inicjaly.bmp')

tablica_obrazka = np.asarray(inicjaly)
# print(tablica_obrazka)

zad5 = np.loadtxt('inicjaly.txt', dtype=np.bool_)

print(f'Czy elementy są takie same? ->" {tablica_obrazka.all() == zad5.all()}')
print(f'Czy typ danych jest taki sam? -> {tablica_obrazka.dtype == zad5.dtype}')
print(f'Czy rozmiar jest taki sam? -> {tablica_obrazka.shape == zad5.shape}')
print(f'Czy liczba elementow jest taka sama? -> {tablica_obrazka.size == zad5.size}')
print(f'Czy wymiar taki jest sam? -> {tablica_obrazka.ndim == zad5.ndim}')
print(f'Czy rozmiar wyrazu jest taki sam? -> {tablica_obrazka.itemsize == zad5.itemsize}')