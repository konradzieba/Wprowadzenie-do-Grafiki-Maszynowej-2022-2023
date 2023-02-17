from PIL import Image, ImageChops


# 1.1
def draw_rectangle(img, m, n, a, b, color):
    if m + a > img.size[0] or n + b > img.size[1] or m < 0 or n < 0:
        raise ValueError('Prostokąt wychodzi poza granice obrazka')
    else:
        for i in range(m, m + a + 1):
            img.putpixel((i, n), color)
            img.putpixel((i, n + b), color)
        # pasy pionowe
        for j in range(n, n + b + 1):
            img.putpixel((m, j), color)
            img.putpixel((m + a, j), color)


# 1.2
def draw_square(img, m, n, a, color):
    if a % 2 == 0:
        raise ValueError('A musi być parzyste')
    if m < 0 or n < 0 or m + a > img.size[0] or n + a > img.size[1]:
        raise ValueError('Kwadrat wychodzi poza granice obrazka')
    else:
        for i in range(m, m + a + 1):
            img.putpixel((i, n), color)
            img.putpixel((i, n + a), color)
            img.putpixel((m, i), color)
            img.putpixel((m + a, i), color)


# 1.3
def draw_square1(img, m, n, a, color, thickness):
    if a % 2 == 0:
        raise ValueError('A musi być parzyste')
    corner_m = int(m - (a / 2))
    corner_n = int(n - (a / 2))
    if corner_m < 0 or corner_n < 0 or corner_m + a > img.size[0] or corner_n + a > img.size[1]:
        raise ValueError('Kwadrat wychodzi poza granice obrazka')
    else:
        for i in range(corner_m, corner_m + a + thickness):
            for j in range(0, thickness):
                img.putpixel((i, corner_n + j), color)
                img.putpixel((i, corner_n + a + j), color)
                img.putpixel((corner_m + j, i), color)
                img.putpixel((corner_m + a + j, i), color)


img = Image.open('baby_yoda.jpg')
img_copy = img.copy()
img_copy2 = img.copy()
img_copy3 = img.copy()
img_copy4 = img.copy()

draw_rectangle(img_copy, 0, 0, 50, 150, (255, 255, 255))
# img_copy.show()

draw_square(img_copy2, 0, 0, 51, (255, 255, 255))
# img_copy2.show()

draw_square1(img_copy3, 200, 200, 105, (255, 255, 255), 5)
draw_square1(img_copy4, 200, 200, 305, (255, 255, 255), 5)
# img_copy3.show()

# Porównanie obrazów
# ImageChops.difference(img_copy3, img_copy4).show()
