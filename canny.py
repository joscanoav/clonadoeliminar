#Bibliotecas
import cv2
img =import cv2

# Inicializar la cámara
cap = cv2.VideoCapture(0)

# Comprobar si la cámara se ha iniciado correctamente
if not cap.isOpened():
    print("Error al abrir la cámara.")
    exit()

# Bucle principal
while True:
    # Leer un fotograma de la cámara
    ret, frame = cap.read()

    # Mostrar el fotograma en una ventana
    cv2.imshow('Cámara Web', frame)

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar la ventana
cap.release()
cv2.destroyAllWindows()

