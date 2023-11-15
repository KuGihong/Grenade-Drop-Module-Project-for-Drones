#include <Arduino.h>
#include <Servo.h>

Servo sv1;
Servo sv2;
Servo sv3;
Servo sv4;


void setup()
{
  Serial.begin(9600);
  sv1.attach(7);
  sv2.attach(6);  
  sv3.attach(5);
  sv4.attach(4); 
   
  sv1.write(82);  //82, 113
  sv2.write(114); //114, 145
  sv3.write(100); //100, 150
  sv4.write(60);  //60, 110
}

void loop()
{
  if (Serial.available())
  {
    String receivedData = Serial.readString();
    Serial.println(receivedData);
    if (receivedData == "mode1_a"){
      Serial.println("succes");
      sv1.write(113);
    }
    if (receivedData == "mode1_b"){
      Serial.println("succes");
      sv3.write(150);
    }
    if (receivedData == "mode1_c"){
      Serial.println("succes");
      sv2.write(145);
    }
    if (receivedData == "mode1_d"){
      Serial.println("succes");
      sv4.write(110);
    }
    if (receivedData == "mode2"){
      Serial.println("succes");
      sv1.write(113);
      sv2.write(145);
      sv3.write(150);
      sv4.write(110);
    }
  }
}
