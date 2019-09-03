#include <mathstronauts_arduino_library.h>
int S0 = 2;
int S1 = 3;
int S2 = 4;
int S3 = 5;
int OUT = 6;
int echo = 10;
int trig = 9;

float distance;
float duration;//float distance;

void setup() {
  // put your setup code here, to run once:
  // Set up sensor
  pinMode(S0,OUTPUT);
  pinMode(S1,OUTPUT);
  pinMode(S2,OUTPUT);
  pinMode(S3,OUTPUT);
  pinMode(OUT,INPUT);

 // Setting frequency-scaling to 20%
  digitalWrite(S0,HIGH);
  digitalWrite(S1,LOW);
  
  // Set up Ultrasonic
  pinMode(trig,OUTPUT);
  pinMode(echo,INPUT);

  // Set up serial communication
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  colourDetection(S2,S3, OUT);
  distance = ultrasonicDistance(trig,echo);

  
  
  
//  //With each iteration print RED,GREEN,BLUE and distance on the same line
  Serial.print(RED);
  Serial.print(",");
  Serial.print(GREEN);
  Serial.print(",");
  Serial.print(BLUE);
  Serial.print(",");
  Serial.println(distance); // next line will be on a newline after this
  delay(100);
}
