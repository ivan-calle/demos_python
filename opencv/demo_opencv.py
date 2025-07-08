import sys
import numpy
import cv2
import matplotlib.pyplot as plt # Plotear
plt.ion()
print("version opencv:", cv2.__version__)
print("version numpy:", numpy.__version__)
# LEEMOS UNA IMAGEN
img = cv2.imread('lena.png', cv2.IMREAD_GRAYSCALE)
if img is None:
    print('La imagen no existe. Revise el path')
    sys.exit()  # Finaliza python
# MOSTRAMOS PROPIEDADES
print("---")
print("Propiedades de la imagen")
print("  tipo de variable:", type(img))
print("  tipo de pixel:", img.dtype)
print("  tamaño:", img.shape)  # (rows,cols)
# MOSTRAMOS LA IMAGEN USANDO "plt"
plt.figure()
plt.imshow(img, cmap='gray')
# PONEMOS LA SIGUIENTE LINEA EN CASO SE INVOQUE DESDE EL TERMINAL
input('press any key to finish')
