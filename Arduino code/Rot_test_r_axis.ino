//Define pins
int driverPUL = 14;
int driverDIR = 16;
int boardLight = 13;

//Variables

int pdMin = 1000; //Highest Speed
int pdMax = 7000; //Slowest speed
int pd = pdMax; //pulse duration. The higher the number, the slower the spin.
int spr = 800; //Steps per revolution


double numDegrees = 360 * 3.1; //Desired angle (will need to be multiplied by the gear ratio)


int currentLocation = 0;
//int endLocation = float(numDegrees / 360 * spr); //calculates end location in steps
int endLocation = spr * numDegrees / 360; //calculates end location in steps

//int jerk = 1;
int acceleration = 95;
int cruiseSteps = 0; //Coast phase steps in case motor gets to max speed before path midpoint.

int distance = endLocation - currentLocation;

//Functions
void pulse();


void setup() {
  // put your setup code here, to run once:
 pinMode (driverPUL, OUTPUT);
 pinMode (driverDIR, OUTPUT);
 pinMode (boardLight, OUTPUT);

 digitalWrite(driverDIR, HIGH); //DIRECTION. HIGH = Right. LOW = LEFT.
}

void pulse(){
  digitalWrite(driverPUL,HIGH);
  delayMicroseconds(pd);
  digitalWrite(driverPUL,LOW);
  delayMicroseconds(pd);
}

void loop() {
  // put your main code here, to run repeatedly:

while(currentLocation != endLocation){
  
  if(currentLocation < (distance / 2)){
  //Accelerating
    if(pd >= pdMin){
      pulse();
      currentLocation += 1;
      pd -= acceleration;
      //acceleration += jerk;
    }

    //cruise building
    else{ 
      pulse();
      currentLocation += 1;
      cruiseSteps += 1;
    }
  }

  else{
    //cruise consuming
    if(cruiseSteps){
      pulse();
      currentLocation += 1;
      cruiseSteps -= 1;
    }

    //Decelerating
    else{
      pulse();
      currentLocation += 1;
      pd += (acceleration * 1.25); //Not sure why increasing accel works, but it works!
      //acceleration -= jerk;
    }
  }
}
}
