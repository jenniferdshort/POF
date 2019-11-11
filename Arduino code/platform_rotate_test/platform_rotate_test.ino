// defines pins numbers
const int stepPin = 52;      //Stepper driver step pin
const int dirPin = 50;       //Stepper driver direction pin, HIGH=up, LOW=down
const int enPin = 48;        //Stepper driver enable pin (keeping enabled = LOW)

const int centerStop = 46;  //Sensor input for when platform is 0deg rotated

//Motor wiring
// Blue + Green, Black + Yellow
//Red + Gray, Yellow + Green

const int stepsPerRev = 32 * 360 / float(1.8);
int RPM;
float revs;
int dir;
// ************************************************************************//

void setup() {

  Serial.begin(9600);

  //*** Sets outputs as output
  //Stepper Driver
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  pinMode(enPin, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(enPin, LOW);   //Enable Stepper motor

  //End Stops
  pinMode(centerStop, INPUT_PULLUP);

  //*** Startup sequence
  /*
    //Go down until hitting end stop at high speed
    digitalWrite(dirPin, LOW);  //Set stepper to go down
    while (debounceSignal(bottomStopPin) == HIGH) {
      //Serial.println("here");
      for (int x = 0; x < 10; x++) {
        runStepper(highSpeed);
      }
    }

    //Go up a little
    digitalWrite(dirPin, HIGH);  //Set stepper to go UP
    for (int x = 0; x < 5000; x++) {
      runStepper(highSpeed);
    }


    //Go down until hitting end stop at low speed
    digitalWrite(dirPin, LOW);  //Set stepper to go down
    while (debounceSignal(bottomStopPin) == HIGH) {
      for (int x = 0; x < 10; x++) {
        runStepper(highSpeed);
      }
    }

  */



}
void loop() {
  revs = 1;           // # of revs to go
  RPM = 10;  // RPM
  // 125 RPM is good for base linear slide
  // 10 RPM is good for lifting mechanism

  // ***** Stepper test *****
  dir = 0;
  Serial.println("******** New run*****");
  runStepper(RPM, revs, dir);
  delay(2000); // Delays before new run
  dir = 1;
  Serial.println("******** New run*****");
  runStepper(RPM, revs, dir);
  delay(2000); // Delays before new run

  /*
    // ***** Sensor Test *****
    if (digitalRead(centerStop)) {
    digitalWrite(LED_BUILTIN, HIGH);
    Serial.println("LED ON");
    }
    else {
    digitalWrite(LED_BUILTIN, LOW);
    //Serial.println("LED OFF");
    }
  */
  //delay(10);


}


// Debounce noisey signal
/* int debounceSignal(int pin) {

  // Take 5 readings, 70ms apart.
  for (int x = 0; x < 5; x++) {
    readings += digitalRead(pin);
    delayMicroseconds(70);
  }

  //Sum readings. If sum is over 1,
  if (readings > 1) {
    average = HIGH;
  }
  else {
    average = LOW;
  }

  //Reset readings variable to zero
  readings = 0;

  return average;

  }
*/

// Function for running stepper
int runStepper (int RPM, float revs, int dir) {

  long steps = revs * stepsPerRev; // Calculates how many steps to move
  float stepDelay = stepsPerRev / (2 * float(RPM) / 60) / 100; // Delay in microseconds
  int accelSteps = stepsPerRev / 10; // Takes 36deg of rotation to accelerate/deceleration
  int accelDelay;

  Serial.println("revs");
  Serial.println(revs);
  Serial.println("stepsPerRev");
  Serial.println(stepsPerRev);
  Serial.println("Steps");
  Serial.println(steps);
  Serial.println("Step delay");
  Serial.println(stepDelay);
  Serial.println("Direction");
  Serial.println(dir);

  // Picks direction
  if (dir == 0) {
    digitalWrite(dirPin, LOW);
  }
  if (dir == 1) {
    digitalWrite(dirPin, HIGH);
  }
  //digitalWrite(dirPin, LOW);

  // Acceleration Zone
  // Make exception for when too short to accel/decc
  accelDelay = stepDelay * 5;
  for (int i = 0; i < accelSteps; i++) {
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(accelDelay);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(accelDelay);

    // Whenever 1/5 of steps done, decrease delay
    if ((i % int(stepDelay)) == 0) {
      accelDelay -=  stepDelay;
    }

  }

  // Constant velocity Zone
  for (int i = accelSteps; i < (steps - accelSteps); i++) {
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(stepDelay);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(stepDelay);
  }

  // Decelleration Zone
  accelDelay = stepDelay * 5;
  for (int i = (steps - accelSteps); i < steps; i++) {
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(accelDelay);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(accelDelay);

    // Whenever 1/5 of steps done, increase delay
    if ((i % int(stepDelay)) == 0) {
      accelDelay += stepDelay;
    }

  }

}
