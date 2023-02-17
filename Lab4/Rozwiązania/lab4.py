from PIL import Image, ImageOps, ImageChops
import numpy as np
import matplotlib.pyplot as plt
import random


#Zadanie 1
im1 = Image.open('obraz.jpg')
# im1.show()

#Zadanie 2 a)
# tablica obrazu
T = np.array(im1)
#tablica kanału r
t_r = T[:, :, 0]
im_r = Image.fromarray(t_r) # obraz w odcieniuach szarości kanału r
# im_r.show()
#tablica kanału g
t_g = T[:, :, 1]
im_g = Image.fromarray(t_g) # obraz w odcieniuach szarości kanału g
# im_g.show()
#tablica kanału b
t_b = T[:, :, 2]
im_b = Image.fromarray(t_b) # obraz w odcieniuach szarości kanału b
# im_b.show()

#Zadanie 2 b)

im2 = Image.merge('RGB', (im_r, im_g, im_b))
# im2.show()
im_diff = ImageChops.difference(im1, im2)

# im_diff.show()

#Zadanie 2 c)
im1_tab = np.asarray(im1)
im2_tab = np.asarray(im2)

compare = im1_tab == im2_tab
is_equal = compare.all()
if is_equal:
    print("Zadanie 2 c) : Obrazy są takie same")
else:
    print("Zadanie 2 c): Obrazy RÓŻNIĄ się")

#Zadanie 3
r, g, b = im1.split()
im3 = Image.merge('RGB', (b,g,r))
# im3.show()

#Zadanie 3 a)
im3.save('im3.jpg')
im3.save('im3.png')

#Zadanie 3 b)
im3_jpg = Image.open('im3.jpg')
im3_png = Image.open('im3.png')

im3_diff = ImageChops.difference(im3_jpg, im3_png)
# im3_diff.show()
# im3_diff jest czarny

im3_jpg_tab = np.asarray(im3_jpg)
im3_png_tab = np.asarray(im3_png)
compare2  = im3_jpg_tab == im3_png_tab
is_equal2 = compare2.all()
if is_equal2:
    print("Zadanie 3 b): Obrazy są takie same")
else:
    print("Zadanie 3 b): Obrazy RÓŻNIĄ się")


#Zadanie 3 c)
obraz1_1_jpg = Image.open('obraz1_1.jpg')
obraz1_1_png = Image.open('obraz1_1.png')
obraz1_1N_jpg = Image.open('obraz1_1N.jpg')
obraz1_1N_png = Image.open('obraz1_1N.png')
obraz1_2_jpg = Image.open('obraz1_2.jpg')
obraz1_2_png = Image.open('obraz1_2.png')
obraz1_2_N_jpg = Image.open('obraz1_2_N.jpg')
obraz1_2_N_png = Image.open('obraz1_2_N.png')

obraz1_1_jpg_tab = np.asarray(obraz1_1_jpg)
obraz1_1_png_tab = np.asarray(obraz1_1_png)
compare3 = obraz1_1_jpg_tab == obraz1_1_png_tab
is_equal3 = compare3.all()
print("Obraz1_1", is_equal3)

font = {
        'family': 'serif',
        'color':  'darkred',
        'weight': 'bold',
        'size': 28,
        }

plt.figure(figsize=(20, 16))
plt.subplot(2, 2, 1)  # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.imshow(ImageChops.difference(obraz1_1_jpg, obraz1_1_png), "gray")
plt.axis('off')
plt.title('obraz1_1: jpg-png difference', fontdict=font)
plt.subplot(2, 2, 2)
plt.imshow(ImageChops.difference(obraz1_1N_jpg, obraz1_1N_png), "gray")
plt.axis('off')
plt.title('obraz1_1N: jpg-png difference', fontdict=font)
plt.subplot(2, 2, 3)
plt.imshow(ImageChops.difference(obraz1_2_jpg, obraz1_2_png), "gray")
plt.axis('off')
plt.title('obraz1_2: jpg-png difference', fontdict=font)
plt.subplot(2, 2, 4)
plt.imshow(ImageChops.difference(obraz1_2_N_jpg, obraz1_2_N_png), "gray")
plt.axis('off')
plt.title('obraz1_2_N: jpg-png difference', fontdict=font)
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig1.png')
# plt.show()


#Zadanie4
#funkcja z wczesniejszego laba
gray_lines = random.randint(35, 220)
gray_background = random.randint(35, 220)

# print(gray_lines, gray_background)

while gray_background <= gray_lines or abs(gray_lines - gray_background) < 50:
    gray_lines = random.randint(35, 220)
    gray_background = random.randint(35, 220)

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

im4_tab = wlasne(1920, 1080)
im4 = Image.fromarray(im4_tab)
# im4.show()
print(im4.size==im1.size)

#Zadanie 4 a)
ch_r, ch_g, ch_b = im1.split()
obrazek1 = Image.merge('RGB', (im4, ch_b, ch_b))
obrazek2 = Image.merge('RGB', (ch_r, im4, ch_b))
obrazek3 = Image.merge('RGB', (ch_r, ch_b, im4))
# obrazek1.show()
# obrazek2.show()
# obrazek3.show()


#Zadanie 4 b)
plt.figure(figsize=(20, 16))
plt.subplot(1, 3, 1)  # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.imshow(obrazek1)
plt.axis('off')
plt.title('replaced R channel', fontdict=font)
plt.subplot(1, 3, 2)
plt.imshow(obrazek2)
plt.axis('off')
plt.title('replaced G channel', fontdict=font)
plt.subplot(1, 3, 3)
plt.imshow(obrazek3)
plt.axis('off')
plt.title('replaced B channel', fontdict=font)
plt.savefig('fig2.png')
# plt.show()

#Zadanie 5
#Bitmapy monochromatyczne (mode='1')
test = Image.open('okrag.bmp')
print(f'Tryb: {test.mode}')
okrag = Image.open('okrag.bmp').convert('L') #.convert('L') zamienia obraz na skale szarości
prostokat = Image.open('prostokat.bmp').convert('L') #brak .convert('L') skutkuje błędem trybów
trojkat = Image.open('trojkat.bmp').convert('L')
print(f'Tryb: {okrag.mode}')

#Zadanie 5 a
perm1 = Image.merge('RGB', (trojkat, prostokat, okrag))
perm2 = Image.merge('RGB', (trojkat, okrag, prostokat))
perm3 = Image.merge('RGB', (okrag, prostokat, trojkat))
perm4 = Image.merge('RGB', (okrag, trojkat, prostokat))
perm5 = Image.merge('RGB', (prostokat, trojkat, okrag))
perm6 = Image.merge('RGB', (prostokat, okrag, trojkat))

#Zadanie 5 b
plt.figure(figsize=(35, 20))
plt.subplot(2, 3, 1)  # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.imshow(perm1)
plt.axis('off')
plt.title('Permutation 1', fontdict=font)
plt.subplot(2, 3, 2)
plt.imshow(perm2)
plt.axis('off')
plt.title('Permutation 2', fontdict=font)
plt.subplot(2, 3, 3)
plt.imshow(perm3)
plt.axis('off')
plt.title('Permutation 3', fontdict=font)
plt.subplot(2, 3, 4)
plt.imshow(perm4)
plt.axis('off')
plt.title('Permutation 4', fontdict=font)
plt.subplot(2, 3, 5)
plt.imshow(perm5)
plt.axis('off')
plt.title('Permutation 5', fontdict=font)
plt.subplot(2, 3, 6)
plt.imshow(perm6)
plt.axis('off')
plt.title('Permutation 6', fontdict=font)
plt.savefig('fig3.png')
# plt.show()




