import cv2

def capturar_video():
    # Inicializar la captura de video desde la cámara (0 indica la cámara predeterminada)
    cap = cv2.VideoCapture(0)

    # Comprobar si la cámara se ha iniciado correctamente
    if not cap.isOpened():
        print("Error al abrir la cámara.")
        exit()

    # Bucle principal para capturar video
    while True:
        # Leer un fotograma de la cámara
        ret, frame = cap.read()

        # Mostrar el fotograma en una ventana
        cv2.imshow('Captura de Video', frame)

        # Salir del bucle si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar la cámara y cerrar la ventana
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Llamar a la función para capturar video desde la cámara
    capturar_video()
