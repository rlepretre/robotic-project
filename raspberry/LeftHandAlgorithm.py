import serial
import time 

ser = serial.Serial('/dev/ttyACM0')  # open serial port
print(ser.name) 

while(True):
    case = int(ser.read_until())
    print("looping")
    print(case)
    if case == 1: #Cul-de-sac
        ser.write(3)
        print("case 1")
    if case == 2: #Mur droit et avant
        ser.write(1)
        print("case 2")
    if case == 3: #Mur droit mais pas avant
        ser.write(0)
        print("case 3")
    if case == 4: #Mur avant
        ser.write(1)
        print("case 4")
    if case == 5: #Pas de mur
        ser.write(0)
        print("case 5")
    if case == 6: #Mur gauche et avant
        ser.write(2)
        print("case 6")
    if case == 7: #Mur gauche mais pas avant
        ser.write(0)
        print("case 7")

    if case == -1: #Cul-de-sac
        ser.write(0)
        print("case -1")
    if case == -2: #Mur droit et arrière
        ser.write(1)
        print("case -2")
    if case == -3: #Mur droit mais pas arrière
        ser.write(3)
        print("case -3")
    if case == -4: #Mur arrière
        ser.write(1)
        print("case -4")
    if case == -5: #Pas de mur
        ser.write(3)
        print("case -5")
    if case == -6: #Mur gauche et arrière
        ser.write(2)
        print("case -6")
    if case == -7: #Mur gauche mais pas arrière
        ser.write(3)
        print("case -7")

    time.sleep(1)

ser.close() 