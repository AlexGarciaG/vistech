// Motor 1, 
int IN1 = 3;
int IN2 = 4;

// Motor 2
int IN3 = 6;
int IN4 = 5;

// Motor 3
int IN5 = 8;
int IN6 = 9;

// Motor 4
int IN7 = 11;
int IN8 = 10;

// Joystick
int mode = 0;
int VRx = A0;
int VRy = A1;
int SW = 2;

int xPosition = 0;
int yPosition = 0;
int SW_state = 0;
int mapX = 0;
int mapY = 0;

void setup() {
  Serial.begin(9600); 
  
  pinMode(VRx, INPUT);
  pinMode(VRy, INPUT);
  pinMode(SW, INPUT_PULLUP); 

  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(IN5, OUTPUT);
  pinMode(IN6, OUTPUT);
  pinMode(IN7, OUTPUT);
  pinMode(IN8, OUTPUT);
}

void loop() {
  xPosition = analogRead(VRx);
  yPosition = analogRead(VRy);
  SW_state = digitalRead(SW);
  mapX = map(xPosition, 0, 1023, -512, 512);
  mapY = map(yPosition, 0, 1023, -512, 512);
  
  if(mapY < -250){
    moveForward(mapY * -0.498046875);  
  } else if(mapY > 210){
    moveBackwards(mapY * 0.498046875);
  } else if(mapX < -230){
    moveLeft(mapX * -0.498046875);
  } else if(mapX > 230){
    moveRight(mapX * 0.498046875);
  } else if(SW_state == 0){
    stopMoving(); 
  } else{
    stopMoving(); 
  }
  Serial.print(" | X: ");
  Serial.print(mapX);
  Serial.print(" | Y: ");
  Serial.print(mapY);
  Serial.print(" | Button: ");
  Serial.println(SW_state);

  delay(100); 
}

void moveForward(int vel){
  Serial.print("Enfrente");
  analogWrite(IN1, vel);
  analogWrite(IN3, vel);
  analogWrite(IN5, vel);
  analogWrite(IN7, vel);
}

void moveLeft(int vel){
  Serial.print("Izquierda");
  analogWrite(IN2, vel);
  analogWrite(IN4, vel);
  analogWrite(IN5, vel);
  analogWrite(IN7, vel);
}

void moveRight(int vel){
  Serial.print("Derecha");
  analogWrite(IN1, vel);
  analogWrite(IN3, vel);
  analogWrite(IN6, vel);
  analogWrite(IN8, vel);
}

void moveBackwards(int vel){
  Serial.print("Atrás");
  analogWrite(IN2, vel);
  analogWrite(IN4, vel);
  analogWrite(IN6, vel);
  analogWrite(IN8, vel);
}

void stopMoving(){
  Serial.print("Alto");
  analogWrite(IN1, 0);
  analogWrite(IN2, 0);
  analogWrite(IN3, 0);
  analogWrite(IN4, 0);
  analogWrite(IN5, 0);
  analogWrite(IN6, 0);
  analogWrite(IN7, 0);
  analogWrite(IN8, 0);
}
