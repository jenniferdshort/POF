// defines pins numbers
const int stepPin = 5; 
const int dirPin = 2; 
const int enPin = 8;
const int speed_via_delay = 50;

void setup() {
  
  // Sets the two pins as Outputs
  pinMode(stepPin,OUTPUT); 
  pinMode(dirPin,OUTPUT);

  pinMode(enPin,OUTPUT);
  digitalWrite(enPin,LOW);
  
}
void loop() {
  
  digitalWrite(dirPin,HIGH); // Enables the motor to move in a particular direction
  // Makes 200 pulses for making one full cycle rotation
  for(int x = 0; x < 1500; x++) {
    digitalWrite(stepPin,HIGH); 
    delayMicroseconds(speed_via_delay); 
    digitalWrite(stepPin,LOW); 
    delayMicroseconds(speed_via_delay); 
  }
  delay(1000); // One second delay

  digitalWrite(dirPin,LOW); //Changes the rotations direction
  // Makes 400 pulses for making two full cycle rotation
  for(int x = 0; x < 1500; x++) {
    digitalWrite(stepPin,HIGH);
    delayMicroseconds(speed_via_delay);
    digitalWrite(stepPin,LOW);
    delayMicroseconds(speed_via_delay);
  }
  delay(1000);
  
}
