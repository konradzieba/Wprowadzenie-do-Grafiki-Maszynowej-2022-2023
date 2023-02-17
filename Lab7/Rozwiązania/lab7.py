from PIL import Image, ImageChops, ImageFilter
from matplotlib import pyplot as plt

img = Image.open('obraz.jpg')
img_copy = img.copy()

#Zadanie 1
def filtruj(image, kernel, scale):
    w, h = image.size
    kernel_len = len(kernel)
    image_copy = image.copy()
    t = image_copy.load()
    obraz_tab = image.load()
    half_kernel_len = int(kernel_len / 2)
    for i in range(half_kernel_len, w - half_kernel_len):
        for j in range(half_kernel_len, h - half_kernel_len):
            tmp = [0, 0, 0]
            for k in range(kernel_len):
                for l in range(kernel_len):
                    pix_x = i + k - half_kernel_len
                    pix_y = j + l - half_kernel_len
                    frame = obraz_tab[pix_x, pix_y]
                    for m in range(3):
                        tmp[m] += frame[m] * kernel[k][l]
            t[i, j] = (int(tmp[0] / scale), int(tmp[1] / scale), int(tmp[2] / scale))
    return image_copy

zadanie1 = filtruj(img_copy, ((-1, -2, -1),(-1, 8, -1),(-1, -2, -1)),1)
zadanie1.show()

#Zadanie 2.1
print(ImageFilter.BLUR.filterargs)
blur = filtruj(img_copy, [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]],
               ImageFilter.BLUR.filterargs[1])
blur.save('blur.png')
blur.show()

blur1 = img_copy.filter(ImageFilter.BLUR)
blur1.save('blur1.png')
blur1.show()

#Zadanie 2.2

font = {
        'family': 'serif',
        'color':  'darkred',
        'weight': 'bold',
        'size': 28,
        }

blur_diff = ImageChops.difference(blur, blur1)
blur_diff.save('blur_diff.png')

plt.figure(figsize=(35, 20))
plt.subplot(1, 3, 1)  # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.imshow(blur)
plt.axis('off')
plt.title('blur', fontdict=font)
plt.subplot(1, 3, 2)
plt.imshow(blur1)
plt.axis('off')
plt.title('blur1', fontdict=font)
plt.subplot(1, 3, 3)
plt.imshow(blur_diff)
plt.axis('off')
plt.title('blur and blur1 diff', fontdict=font)
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig1.png')
plt.show()

#Zadanie 3

print(ImageFilter.EMBOSS.filterargs)
img_L = img_copy.convert('L')

#Zadanie 3 a)
ImageFilter.EMBOSS.filterargs = ((3, 3), 1, 128, (-1,  0,  1, -2,  0,  2, -1,  0,  1))
sobel1 = img_L.filter(ImageFilter.EMBOSS)
sobel1.save('sobel1.png')
sobel1.show()

#Zadanie 3 b)
ImageFilter.EMBOSS.filterargs = ((3, 3), 1, 128, (-1, -2, -1, 0,  0, 0, 1, 2, 1))
sobel2 = img_L.filter(ImageFilter.EMBOSS)
sobel2.save('sobel2.png')
sobel2.show()

#Zadanie 3 c)

plt.figure(figsize=(35, 20))
plt.subplot(1, 3, 1)  # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.imshow(img_L, 'gray')
plt.axis('off')
plt.title('Image convert L', fontdict=font)
plt.subplot(1, 3, 2)
plt.imshow(sobel1, 'gray')
plt.axis('off')
plt.title('Sobel 1', fontdict=font)
plt.subplot(1, 3, 3)
plt.imshow(sobel2, 'gray')
plt.axis('off')
plt.title('Sobel 2', fontdict=font)
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig2.png')
plt.show()

#Zadanie 4

plt.figure(figsize=(35, 20))
plt.subplot(4, 2, 1)
plt.imshow(img_copy.filter(ImageFilter.DETAIL))
plt.axis('off')
plt.title('Image Detail filter', fontdict=font, wrap=True)
plt.subplot(4, 2, 2)
plt.imshow(ImageChops.difference(img_copy, img_copy.filter(ImageFilter.DETAIL)))
plt.axis('off')
plt.title('Before and after DETAIL filter', fontdict=font, wrap=True)
plt.subplot(4, 2, 3)
plt.imshow(img_copy.filter(ImageFilter.EDGE_ENHANCE_MORE))
plt.axis('off')
plt.title('Image EDGE_ENHANCE_MORE filter', fontdict=font, wrap=True)
plt.subplot(4, 2, 4)
plt.imshow(ImageChops.difference(img, img_copy.filter(ImageFilter.EDGE_ENHANCE_MORE)))
plt.axis('off')
plt.title('Before and after ENHANCE_MORE filter', fontdict=font, wrap=True)
plt.subplot(4, 2, 5)
plt.imshow(img_copy.filter(ImageFilter.SHARPEN))
plt.axis('off')
plt.title('Image SHARPEN filter', fontdict=font, wrap=True)
plt.subplot(4, 2, 6)
plt.imshow(ImageChops.difference(img, img_copy.filter(ImageFilter.SHARPEN)))
plt.axis('off')
plt.title('Before and after SHARPEN filter', fontdict=font, wrap=True)
plt.subplot(4, 2, 7)
plt.imshow(img_copy.filter(ImageFilter.SMOOTH_MORE))
plt.axis('off')
plt.title('Image SMOOTH_MORE filter', fontdict=font, wrap=True)
plt.subplot(4, 2, 8)
plt.imshow(ImageChops.difference(img, img_copy.filter(ImageFilter.SMOOTH_MORE)))
plt.axis('off')
plt.title('Before and after SMOOTH_MORE filter', fontdict=font, wrap=True)
plt.subplots_adjust(wspace=0.05)
plt.savefig('fig3.png')
plt.show()

#Zadanie 4 b)

plt.figure(figsize=(35, 20))
plt.subplot(5, 2, 1)  # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.imshow(img_copy.filter(ImageFilter.GaussianBlur(radius=2)))
plt.axis('off')
plt.title('Gaussian blur(radius=2)', fontdict=font, wrap=True)
plt.subplot(5, 2, 2)
plt.imshow(ImageChops.difference(img, img_copy.filter(ImageFilter.GaussianBlur(radius=2))))
plt.axis('off')
plt.title('Gaussian blur(radius=2) - original diff', fontdict=font, wrap=True)
plt.subplot(5, 2, 3)
plt.imshow(img_copy.filter(ImageFilter.UnsharpMask(radius=3, percent=200, threshold=5)))
plt.axis('off')
plt.title('Unsharp mask(radius=3, percent=200, threshold=5)', fontdict=font, wrap=True)
plt.subplot(5, 2, 4)
plt.imshow(ImageChops.difference(img, img_copy.filter(ImageFilter.UnsharpMask(radius=3, percent=200, threshold=5))))
plt.axis('off')
plt.title('Unsharp mask(radius=3, percent=200, threshold=5) - original diff', fontdict=font, wrap=True)
plt.subplot(5, 2, 5)
plt.imshow(img_copy.filter(ImageFilter.MedianFilter(size=3)))
plt.axis('off')
plt.title('Median filter(size=3)', fontdict=font, wrap=True)
plt.subplot(5, 2, 6)
plt.imshow(ImageChops.difference(img, img_copy.filter(ImageFilter.MedianFilter(size=3))))
plt.axis('off')
plt.title('Median filter(size=3) - original diff', fontdict=font, wrap=True)
plt.subplot(5, 2, 7)
plt.imshow(img_copy.filter(ImageFilter.MinFilter(size=3)))
plt.axis('off')
plt.title('Min filter(size=3)', fontdict=font, wrap=True)
plt.subplot(5, 2, 8)  # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.imshow(ImageChops.difference(img, img_copy.filter(ImageFilter.MinFilter(size=3))))
plt.axis('off')
plt.title('Min filter(size=3) - original diff', fontdict=font, wrap=True)
plt.subplot(5, 2, 9)  # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.imshow(img_copy.filter(ImageFilter.MaxFilter(size=3)))
plt.axis('off')
plt.title('Max filter(size=3)', fontdict=font, wrap=True)
plt.subplot(5, 2, 10)  # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.imshow(ImageChops.difference(img, img_copy.filter(ImageFilter.MaxFilter(size=3))))
plt.axis('off')
plt.title('Max filter(size=3) - original diff', fontdict=font, wrap=True)
plt.subplots_adjust(wspace=0.05)
plt.savefig('fig4.png')
plt.show()







