void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int dist = 2340;
  int situation = 2;
  Serial.print(dist);
  Serial.print(";");
  Serial.println(situation);
  
  if(Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    if(data = '1'){
      Serial.print(dist);
      Serial.print(";");
      Serial.println(3);
    }
  }

  delay(1000);
}
