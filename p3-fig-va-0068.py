import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

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

    # 3. Mostrar la imagen original
    plt.imshow(mi_imagen_rgb)
    plt.title("semana y Christian Garcia Jimenez 0068")
    plt.axis("off")
    plt.show()

    # 4. Graficar puntos sobre la imagen
    print("+-+-+-+-+- puntos en la imagen -+-+-+-+-+-+-+-")
    
    # Se usa mi_imagen_rgb para conservar los colores correctos
    plt.imshow(mi_imagen_rgb)
    
    # Coordenadas X e Y de los puntos
    x = [100, 100, 300,]
    y = [100, 400, 500,]
    
    # Graficar los puntos en color rojo (c='red') con tamaño 50 (s=50)
    plt.scatter(x, y, c='red', s=50, marker='o', label='Puntos')
    
    plt.title("Puntos colocados sobre la imagen 0068")
    plt.show()