/* Includes */
#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"
#include <TimerOne.h>  // library: https://code.google.com/archive/p/arduino-timerone/downloads

/* Adafruit_motor initialization */
Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_DCMotor *myMotorR = AFMS.getMotor(1);
Adafruit_DCMotor *myMotorL = AFMS.getMotor(2);

int encoder_pinRight = 2;
int encoder_pinLeft = 3;
volatile int counter = 0;

/* Constantes pour les broches */
const byte TRIGGER_PIN_R = 6; // Broche TRIGGER
const byte ECHO_PIN_R = 4; // Broche ECHO
const byte TRIGGER_PIN_L = 9; // Broche TRIGGER
const byte ECHO_PIN_L = 8; // Broche ECHO

/* Constantes pour IR */
const byte IR_PIN_AV = 10; //IR Avant
const byte IR_PIN_AR = 11; //IR Arrière

/* Constantes pour le timeout */
const unsigned long MEASURE_TIMEOUT = 25000UL; // 25ms = ~8m à 340m/s

/* Vitesse du son dans l'air en mm/us */
const float SOUND_SPEED = 340.0 / 1000;

/* constante générale */
int dir=1;
int MurGauche;
int MurDroit;
int MurAvant;
int MurArriere;
int RP;


void setup() {
  /* set up Serial library at 9600 bps */
  Serial.begin(9600);           
  /* Setup Motor */
  AFMS.begin();
  myMotorR->setSpeed(255);
  myMotorL->setSpeed(255);
  pinMode(encoder_pinRight, INPUT);
  pinMode(encoder_pinLeft, INPUT);
  Timer1.initialize(1000000);  // set for 1 sec
  attachInterrupt(digitalPinToInterrupt(2), do_count, RISING);
  Timer1.attachInterrupt(timerIsr);

  /* Set up right sensor */
  pinMode(TRIGGER_PIN_R, OUTPUT);
  digitalWrite(TRIGGER_PIN_R, LOW); // La broche TRIGGER doit être à LOW au repos
  pinMode(ECHO_PIN_R, INPUT);
  /* Set up left sensor */
  pinMode(TRIGGER_PIN_L, OUTPUT);
  digitalWrite(TRIGGER_PIN_L, LOW); // La broche TRIGGER doit être à LOW au repos
  pinMode(ECHO_PIN_L, INPUT);

  /*Set up IR sensors (front and bak) */
  pinMode(IR_PIN_AV, INPUT);
  pinMode(IR_PIN_AR, INPUT);
  
}

void loop() {
  MurGauche=MurCote(-1);
  MurDroit=MurCote(1);
  MurAvant=digitalRead(IR_PIN_AV);  //si 1 --> obstacle
  MurArriere=digitalRead(IR_PIN_AR);  //si -1 --> obstacle
  RP=readSerialPort();
  if (dir==1){ // si dir==1 move_forward
    if (MurGauche<30 & MurDroit<30) {
      if (MurAvant == 1){
        Serial.print(1);
        delay(100);
        dir=-1;
        RP=readSerialPort();
      }
    } else if (MurGauche>30) {
      if (MurDroit<30) {
        if (MurAvant == 1) {
          Serial.print(2);
          delay(100);
          RP=readSerialPort();
        } else if (MurAvant ==0){
          Serial.print(3);
          delay(100);
          RP=readSerialPort();
        }
      } else {
        if (MurAvant == 1) {
          Serial.print(4);
          delay(100);
          RP=readSerialPort();
        } else if (MurAvant ==0){
          Serial.print(5);
          delay(100);
          RP=readSerialPort();
        }
      }
    } else if (MurDroit>30 && MurGauche<30){
      if (MurAvant == 1) {
          Serial.print(6);
          delay(100);
          RP=readSerialPort();
        } else if (MurAvant ==0){
          Serial.print(7);
          delay(100);
          RP=readSerialPort();
        }
    }
      
  } else if (dir==-1) { //if dir==- move_backward
    if (MurGauche<30 & MurDroit<30) {
      if (MurArriere == 1){
        Serial.print(-1);
        delay(100);
        dir=1;
        RP=readSerialPort();
      }
    } else if (MurGauche>30) {
      if (MurDroit<30) {
        if (MurArriere == 1) {
          Serial.print(-2);
          delay(100);
          RP=readSerialPort();
        } else if (MurArriere ==0){
          Serial.print(-3);
          delay(100);
          RP=readSerialPort();
        }
      } else {
        if (MurArriere == 1) {
          Serial.print(-4);
          delay(100);
          RP=readSerialPort();
        } else if (MurArriere ==0){
          Serial.print(-5);
          delay(100);
          RP=readSerialPort();
        }
      }
    } else if (MurDroit>30 && MurGauche<30){
      if (MurArriere == 1) {
          Serial.print(-6);
          delay(100);
          RP=readSerialPort();
        } else if (MurArriere ==0){
          Serial.print(-7);
          delay(100);
          RP=readSerialPort();
        }
    }
  }

  switch (RP) {
    case 0:
      MoveForward();
      break;
    case 1:
      TurnLeft();
      break;
    case 2:
      TurnRight();
      break;
    case 3:
      MoveBackward();
      break;
  }
}

void do_count() {
  noInterrupts();
  counter += 1;
  interrupts();
}
void TurnRight() {
   counter = 0;
   myMotorR->setSpeed(150);
   myMotorL->setSpeed(150);
  while (counter <= 55) {
    
      myMotorR->run(BACKWARD);
      myMotorL->run(FORWARD);
  }
  myMotorR->setSpeed(0);
  myMotorL->setSpeed(0);

}
void TurnLeft() {

  counter = 0;
  myMotorR->setSpeed(150);
  myMotorL->setSpeed(150);
  while (counter <= 55) {
   
      myMotorR->run(FORWARD);
      myMotorL->run(BACKWARD);
  }
  myMotorR->setSpeed(0);
  myMotorL->setSpeed(0);
}

void MoveForward(){
  counter = 0;
  myMotorR->setSpeed(255);
  myMotorL->setSpeed(255);
  while (counter <= 55) {
    
      myMotorR->run(FORWARD);
      myMotorL->run(FORWARD);
  }
  myMotorR->setSpeed(0);
  myMotorL->setSpeed(0);
}
void MoveBackward(){
  counter = 0;
  myMotorR->setSpeed(255);
  myMotorL->setSpeed(255);
  while (counter <= 55) {
    
      myMotorR->run(BACKWARD);
      myMotorL->run(BACKWARD);
  }
  myMotorR->setSpeed(0);
  myMotorL->setSpeed(0);
  
}

void timerIsr() {
  Timer1.detachInterrupt();
  //Serial.print("Motor Speed: ");
  int rotation = (counter / 20);
  //Serial.print(rotation, DEC);
  //Serial.println(" RPS");
  counter = 0;
  Timer1.attachInterrupt(timerIsr);
}

float MurCote(int i){
float distance;   
  if (i==1){
    /* 1. Lance une mesure de distance en envoyant une impulsion HIGH de 10µs sur la broche TRIGGER */
    digitalWrite(TRIGGER_PIN_R, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIGGER_PIN_R, LOW);
  
    /* 2. Mesure le temps entre l'envoi de l'impulsion ultrasonique et son écho (si il existe) */
    long measure_R = pulseIn(ECHO_PIN_R, HIGH, MEASURE_TIMEOUT);
    distance = measure_R / 2.0 * SOUND_SPEED;
    //Serial.print(F("Distance Droite: "));
  }

  else if (i==-1) {
    /*même chose pour le capteur à gauche*/
    digitalWrite(TRIGGER_PIN_L, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIGGER_PIN_L, LOW);
    
    long measure_L = pulseIn(ECHO_PIN_L, HIGH, MEASURE_TIMEOUT);
    distance = measure_L / 2.0 * SOUND_SPEED;
    //Serial.print(F("Distance Gauche: "));  
  }
  //Serial.println(distance/ 10.0, 2);
  return distance/10.0;
}

int readSerialPort() {
  if (Serial.available()) {
    delay(10);
      return (int)Serial.readStringUntil('\n');;
  } 
  else {
    return 0;
  }
}


/* 
 *  Communication sur le RPI:
 *  Si le Rpi lit quelque chose sur son Serial, en fonction de la valeur :
 *  Exécute l'action puis renvoie en continu 
 */
