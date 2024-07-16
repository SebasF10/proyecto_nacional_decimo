import cv2
import os
import imutils

persona1 = "sebas"
rutadata = "C:/Users/USER/Desktop/trabajos de python/proyecto_nacional_decimo/Data"
personadata = rutadata + '/' + persona1

#condicional para verificar si la capeta existe
if not os.path.exists(personadata):
    print("carpeta creada: ", personadata)
    os.makedirs(personadata)


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()

