import serial
import time 
import struct
ser = serial.Serial('/dev/cu.usbmodem14301', 9600)
#ser = serial.Serial('/dev/ttyACM0')  # open serial port on arduino
print(ser.name) 

while(True):
    print("entered loop")
    if(ser.in_waiting > 0):
        line = ser.readline().decode('utf-8').rstrip()
        print("line is: " + line)
        line = line.split(";")
        dist = int(line[0])
        case = int(line[1])
        ser.write(3)
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
        if case == -2: #Mur droit et arriere
            ser.write(1)
            print("case -2")
        if case == -3: #Mur droit mais pas arriere
            ser.write(3)
            print("case -3")
        if case == -4: #Mur arriere
            ser.write(1)
            print("case -4")
        if case == -5: #Pas de mur
            ser.write(3)
            print("case -5")
        if case == -6: #Mur gauche et arriere
            ser.write(2)
            print("case -6")
        if case == -7: #Mur gauche mais pas arriere
            ser.write(3)
            print("case -7")

    time.sleep(1)

ser.close() 