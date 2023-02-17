import zadanie1
import numpy as np
from PIL import Image

inicjaly = Image.open("inicjaly.bmp")
obraz_wstawiany = np.asarray(inicjaly)

przyklad1 = zadanie1.wstaw_obraz(obraz_wstawiany, 50, 0, 2)
przyklad2 = zadanie1.wstaw_obraz(obraz_wstawiany, 180, 30, 3)
przyklad3 = zadanie1.wstaw_obraz(obraz_wstawiany, 120, 80, 4)
# przyklad1.show()
# przyklad2.show()
przyklad3.show()