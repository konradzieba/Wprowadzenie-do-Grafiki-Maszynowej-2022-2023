from PIL import Image, ImageOps, ImageChops
import numpy as np
import matplotlib.pyplot as plt

# Zadanie 1
obraz = Image.open('obraz.jpg')
inicjaly = Image.open('inicjaly.bmp')


# Zadanie 2.1
def wstaw_inicjaly(obraz, inicjaly, m, n, kolor):
    color_white = (255, 255, 255)
    for i in range(0, inicjaly.size[0]):
        for j in range(0, inicjaly.size[1]):
            if (m + i) < obraz.size[0] and (n + j) < obraz.size[1]:
                if inicjaly.getpixel((i, j)) == 0:
                    obraz.putpixel((m + i, n + j), kolor)
                else:
                    obraz.putpixel((m + i, n + j), color_white)
            else:
                if inicjaly.getpixel((i, j)) == 0:
                    obraz.putpixel((m + i - obraz.size[0], (n + j) - obraz.size[1]), kolor)
                else:
                    obraz.putpixel((m + i, n + j), color_white)


obraz_width, obraz_height = obraz.size
inicjaly_width, inicjaly_height = inicjaly.size
color_red = (255, 0, 0)
place_to_put = (obraz_width-inicjaly_width, obraz_height-inicjaly_height)

print(f'Rozmiar obrazu: {obraz_width}, {obraz_height}')
print(f'Rozmiar inicjalow: {inicjaly_width}, {inicjaly_height} \n')
print(f'Miejsce do wstawienia: {place_to_put}')

inicjaly_copy = inicjaly.copy()
obraz1 = obraz.copy()
wstaw_inicjaly(obraz1, inicjaly_copy, place_to_put[0], place_to_put[1], color_red)
obraz1.save('obraz1.png')
obraz1.show()

# Zadanie 2.2
def wstaw_inicjaly_maska(obraz, inicjaly, m, n, x, y, z):
    inicjaly_w, inicjaly_h = inicjaly.size
    for i in range(0, inicjaly_w):
        for j in range(0, inicjaly_h):
            if inicjaly.getpixel((i, j)) == 0:
                if m + i < obraz.size[0] and n + j < obraz.size[1]:
                    pixel = obraz.getpixel((i + m, j+n))
                    obraz.putpixel((i + m, j + n), (pixel[0] + x, pixel[1] + y, pixel[2] + z))
                else:
                    pixel = obraz.getpixel((i + (m - obraz.size[0]), j + (n - obraz.size[1])))
                    obraz.putpixel((i + (m - obraz.size[0]), j + (n - obraz.size[1])), (pixel[0] + x, pixel[1] + y, pixel[2] + z))
#
obraz_width_center = int((obraz_width / 2) - (inicjaly_width / 2))
obraz_height_center = int((obraz_height / 2) - (inicjaly_height / 2))

print(f'Środek obrazka: {obraz_width_center}, {obraz_height_center}')

obraz2 = obraz.copy()
wstaw_inicjaly_maska(obraz2, inicjaly_copy, obraz_width_center, obraz_height_center, 50, 70, -50)
obraz2.save('obraz2.png')
obraz2.show()



# Zadanie 3

def wstaw_inicjaly_load(obraz, inicjaly, m, n, kolor):
    obraz_load = obraz.load()
    inicjaly_load = inicjaly.load()
    color_white = (255, 255, 255)
    for i in range(0, inicjaly.size[0]):
        for j in range(0, inicjaly.size[1]):
            if (m+i) < obraz.size[0] and (n+j) < obraz.size[1]:
                if inicjaly_load[i, j] == 0:
                    obraz_load[m+i, n+j] = kolor
                else:
                    obraz_load[m+i, n+j] = color_white
            else:
                if inicjaly_load[i, j] == 0:
                    obraz_load[m + (i - obraz.size[0]), n+(j - obraz.size[1])] = kolor
                else:
                    obraz_load[m + (i - obraz.size[0]), n+(j - obraz.size[1])] = color_white

wstaw_inicjaly_load_check = obraz.copy()
wstaw_inicjaly_load(wstaw_inicjaly_load_check, inicjaly_copy, place_to_put[0], place_to_put[1], color_red)
wstaw_inicjaly_load_check.save('zadanie3_1.png')
wstaw_inicjaly_load_check.show()

test_zad_2_1 = obraz1.copy()
test_zad_3_1 = wstaw_inicjaly_load_check.copy()
load_put_diff = ImageChops.difference(test_zad_2_1, test_zad_3_1)
load_put_diff.save('zadanie3_1_2_1_diff.png')
load_put_diff.show()

#
def wstaw_inicjaly_maska2(obraz, inicjaly, m, n, x, y, z):
    obraz_load = obraz.load()
    inicjaly_load = inicjaly.load()
    inicjaly_w, inicjaly_h = inicjaly.size
    for i in range(0, inicjaly_w):
        for j in range(0, inicjaly_h):
            if inicjaly_load[i, j] == 0:
                if (m+i) < obraz.size[0] and (n+j) < obraz.size[1]:
                    pixel = obraz_load[i + m, j + n]
                    obraz_load[i + m, j + n] = (pixel[0] + x, pixel[1] + y, pixel[2] + z)
                else:
                    pixel = obraz_load[(i + m) - obraz.size[0], (j+n) - obraz.size[1]]
                    obraz_load[(i + m) - obraz.size[0], (j + n) - obraz.size[1]] = (pixel[0] + x, pixel[1] + y, pixel[2] + z)
#

wstaw_inicjaly_load(wstaw_inicjaly_load_check, inicjaly_copy, place_to_put[0], place_to_put[1], color_red)
wstaw_inicjaly_load_check.show()
wstaw_inicjaly_maska2_check = obraz.copy()
wstaw_inicjaly_maska2(wstaw_inicjaly_maska2_check, inicjaly_copy, obraz_width_center, obraz_height_center, 50, 70, -50)
wstaw_inicjaly_maska2_check.save('maska2.png')
wstaw_inicjaly_maska2_check.show()
zadanie3_2_2_2_diff = ImageChops.difference(obraz2, wstaw_inicjaly_maska2_check)
zadanie3_2_2_2_diff.save('zadanie3_2_2_2_diff.png')
zadanie3_2_2_2_diff.show()


# # Zadanie 4.1

def kontrast(obraz, wsp_kontrastu):
    if wsp_kontrastu >= 0 and wsp_kontrastu <= 100:
        mn = ((255 + wsp_kontrastu) / 255) ** 2
        return obraz.point(lambda i: 128 + (i - 128) * mn)
    else:
        raise ValueError('Współczynnik wartości musi być w zakresie <0, 100>')

# # kontrast_validation_test = kontrast(obraz, 101)
kontrast_test1 = kontrast(obraz, 0)
kontrast_test2 = kontrast(obraz, 20)
kontrast_test3 = kontrast(obraz, 40)
kontrast_test4 = kontrast(obraz, 60)
kontrast_test5 = kontrast(obraz, 80)
kontrast_test6 = kontrast(obraz, 100)
# kontrast_test1.show()
# kontrast_test2.show()
# kontrast_test3.show()
#
font = {
        'family': 'serif',
        'color':  'darkred',
        'weight': 'bold',
        'size': 28,
        }

plt.figure(figsize=(35, 20))
plt.subplot(2, 3, 1)  # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.imshow(kontrast_test1)
plt.axis('off')
plt.title('Wsp_kontrastu = 0', fontdict=font)
plt.subplot(2, 3, 2)
plt.imshow(kontrast_test2)
plt.axis('off')
plt.title('Wsp_kontrastu = 20', fontdict=font)
plt.subplot(2, 3, 3)
plt.imshow(kontrast_test3)
plt.axis('off')
plt.title('Wsp_kontrastu = 40', fontdict=font)
plt.subplot(2, 3, 4)
plt.imshow(kontrast_test4)
plt.axis('off')
plt.title('Wsp_kontrastu = 60', fontdict=font)
plt.subplot(2, 3, 5)
plt.imshow(kontrast_test5)
plt.axis('off')
plt.title('Wsp_kontrastu = 80', fontdict=font)
plt.subplot(2, 3, 6)
plt.imshow(kontrast_test6)
plt.axis('off')
plt.title('Wsp_kontrastu = 100', fontdict=font)
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('kontrast_obrazek.png')
plt.show()

#
# # Zadanie 4.3
#
def transformacja_logarytmiczna(obraz):
    return obraz.point(lambda i: 255 * np.log(1 + i / 255))


transformacja_logarytmicznatest = transformacja_logarytmiczna(obraz)
transformacja_logarytmicznatest.save('transformacja_logarytmiczna.png')
transformacja_logarytmicznatest.show()

plt.figure(figsize=(35, 20))
plt.subplot(1, 2, 1)  # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.imshow(obraz)
plt.axis('off')
plt.title('Before log transformation', fontdict=font)
plt.subplot(1, 2, 2)
plt.imshow(transformacja_logarytmicznatest)
plt.axis('off')
plt.title('After log transformation', fontdict=font)
plt.savefig('transformacja_logarytmiczna.png')
plt.show()

#
# # Zadanie 4.4
#
def transformacja_gamma(obraz, gamma): #gamma > 0
    if gamma > 0:
        return obraz.point(lambda i: (i / 255) ** (1 / gamma) * 255)
    else:
        raise ValueError('Parametr gamma musi być większy od 0')
#
transformacja_gamma_test1 = transformacja_gamma(obraz, 0.25)
transformacja_gamma_test2 = transformacja_gamma(obraz, 0.5)
transformacja_gamma_test3 = transformacja_gamma(obraz, 1)
transformacja_gamma_test4 = transformacja_gamma(obraz, 2)
transformacja_gamma_test5 = transformacja_gamma(obraz, 10)

plt.figure(figsize=(35, 20))
plt.subplot(2, 3, 1)  # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.imshow(obraz)
plt.axis('off')
plt.title('Without Gamma', fontdict=font)
plt.subplot(2, 3, 2)
plt.imshow(transformacja_gamma_test1)
plt.axis('off')
plt.title('Gamma = 0.25', fontdict=font)
plt.subplot(2, 3, 3)
plt.imshow(transformacja_gamma_test2)
plt.axis('off')
plt.title('Gamma = 0.5', fontdict=font)
plt.subplot(2, 3, 4)
plt.imshow(transformacja_gamma_test3)
plt.axis('off')
plt.title('Gamma = 1 (No changes)', fontdict=font)
plt.subplot(2, 3, 5)
plt.imshow(transformacja_gamma_test4)
plt.axis('off')
plt.title('Gamma = 2', fontdict=font)
plt.subplot(2, 3, 6)
plt.imshow(transformacja_gamma_test5)
plt.axis('off')
plt.title('Gamma = 10', fontdict=font)
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('gamma_obrazek.png')
plt.show()

test_gamma = ImageChops.difference(obraz,transformacja_gamma_test3)
test_gamma.show()
#
#
# Zadanie 5
T = np.array(obraz, dtype='uint8')
print(f'Wartości przed zwiększeniem o 100 : {T[0, 0]}')
T += 100
print(f'Wartości po zwiększeniu o  100 : {T[0, 0]}')
obraz_wynik = Image.fromarray(T, "RGB")
obraz_wynik.show()

#
lambda_test_img = obraz.copy()

def lambda_test(image, value):
    return image.point(lambda i: i + value)

lambda_test_img = lambda_test(lambda_test_img, 100)
lambda_test_img.show()

#
# # Zadanie 6
def similar_to_point_lambda(img, value):
    tab = np.array(img, dtype='uint8')
    for i in range(0, img.size[1]):
        for j in range(0, img.size[0]):
            pixel = tab[i, j]
            if pixel[0] + value > 255:
                pixel[0] = 255
            else:
                pixel[0] = pixel[0] + value
            if pixel[1] + value > 255:
                pixel[1] = 255
            else:
                pixel[1] = pixel[1] + value
            if pixel[2] + value > 255:
                pixel[2] = 255
            else:
                pixel[2] = pixel[2] + value
            tab[i, j] = (pixel[0], pixel[1], pixel[2])
    return Image.fromarray(tab, "RGB")


test11 = similar_to_point_lambda(obraz, 100)
test11.show()
test12 = lambda_test(obraz, 100)

diff = ImageChops.difference(test11, test12)
diff.show()


zadanie6_1 = similar_to_point_lambda(obraz, 100)

plt.figure(figsize=(35, 20))
plt.subplot(2, 2, 1)  # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.imshow(obraz_wynik)
plt.axis('off')
plt.title('T += 100', fontdict=font)
plt.subplot(2, 2, 2)
plt.imshow(test12)
plt.axis('off')
plt.title('Point Lambda i: i + 100', fontdict=font)
plt.subplot(2, 2, 3)
plt.imshow(test11)
plt.axis('off')
plt.title('Similar_to_point_lambda(img, 100)', fontdict=font)
plt.subplot(2, 2, 4)
plt.imshow(diff)
plt.axis('off')
plt.title('Diff between Point Lambda and Similar_to_lambda (+100)', fontdict=font)
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('zadanie6.png')
plt.show()









