from PIL import Image  # Python Imaging Library
import numpy as np




inicjaly = Image.open('inicjaly.bmp')
print(f' Tryb: {inicjaly.mode}')
print(f' Format: {inicjaly.format}')
print(f' Rozmiar: {inicjaly.size}')

#inicjaly.show()

dane_obrazka = np.asarray(inicjaly) *1

plik_tekstowy = open('inicjaly.txt', 'w')
for rows in dane_obrazka:
    for item in rows:
        plik_tekstowy.write(str(item) + ' ')
    plik_tekstowy.write('\n')
