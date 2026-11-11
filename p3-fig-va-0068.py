import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

# Limpiar pantalla de la consola
os.system('cls' if os.name == 'nt' else 'clear')

# Christian Garcia Jimenez Nc = 0068 
print(" Christian Garcia Jimenez Nc = 0068 ")
print("Fecha : 10/11/2026")
print("UIII Act3 colocar puntos a una imagen en blanco y negro VA")

# 1. Cargar la imagen
mi_imagen = cv2.imread("semana.jpg")

# Validación por si la imagen no se encuentra en la ruta
if mi_imagen is None:
    print("Error: No se encontró la imagen 'semana.jpg'. Verifica la ruta.")
else:
    # 2. Convertir BGR a RGB para Matplotlib
    mi_imagen_rgb = cv2.cvtColor(mi_imagen, cv2.COLOR_BGR2RGB)

    # 3. Mostrar la imagen original con ejes visibles
    plt.imshow(mi_imagen_rgb)
    plt.title("semana y Christian Garcia Jimenez 0068")
    plt.show()

    # 4. Graficar puntos sobre la imagen
    print("+-+-+-+-+- puntos en la imagen -+-+-+-+-+-+-+-")
    plt.imshow(mi_imagen_rgb)
    
    # Coordenadas X e Y de los puntos
    x = [100, 100, 300]
    y = [100, 400, 500]
    
    # Graficar los puntos en color rojo
    plt.scatter(x, y, c='red', s=50, marker='o', label='Puntos')
    plt.title("Puntos colocados sobre la imagen 0068")
    plt.show()

    # 5. Graficar cuadro rojo sobre la imagen
    print("+-+-+-+-+-+-+- cuadros en la imagen -+-+-+-+-+-+--+")
    plt.imshow(mi_imagen_rgb)
    
    # Cuadro reducido al 75% (225 px) y movido +50 unidades a la derecha
    x = [150, 375, 375, 150, 150]
    y = [100, 100, 325, 325, 100]
    
    plt.plot(x, y, c="red", linewidth=2)
    plt.title("semana cuadro y Christian Garcia Jimenez 0068")
    plt.show()

    # 6. Graficar segundo cuadro (azul)
    print("+-+-+-+-+-+-+- cuadros en la imagen -+-+-+-+-+-+--+")
    plt.imshow(mi_imagen_rgb)
    
    x_azul = [150, 375, 375, 150, 150]
    y_azul = [450, 150, 150, 450, 450]
    
    plt.plot(x_azul, y_azul, c='blue', linewidth=2)
    plt.show()

# 7. Graficar círculo verde sobre otra imagen
print("+--+--+ circulo verde en la imagen +--+--+")
I = cv2.imread('semana.jpg')

if I is None:
    print("Error: No se encontró la imagen 'JohnLennon.jpg'. Verifica la ruta.")
else:
    I = cv2.cvtColor(I, cv2.COLOR_BGR2RGB)
    plt.imshow(I)

    N = 30  # Lados del polígono
    x = np.zeros((N + 1))
    y = np.zeros((N + 1))
    (xc, yc) = (340, 320)
    r = 150  # Radio

    for i in range(N + 1):
        t = 2 * np.pi / N * i
        x[i] = xc + r * np.cos(t)
        y[i] = yc + r * np.sin(t)

    plt.plot(x, y, c='green')
    plt.show()

