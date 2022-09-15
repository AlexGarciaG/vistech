// Motor 1
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

int mode = 0;

void setup() {
  Serial.begin(9600);  
  
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
  if(Serial.available() != 0){
    mode = Serial.parseInt();
    switch (mode) {
    case 1:
      moveForward(127);
      break;
    case 2:
      moveBackwards(127);
      break;
    case 3:
      moveLeft(127);
      break;
    case 4:
      moveRight(127);
      break;
    default:
      stopMoving();
    }
  }
}

void moveForward(int vel){
  analogWrite(IN1, vel);
  analogWrite(IN3, vel);
  analogWrite(IN5, vel);
  analogWrite(IN7, vel);
}

void moveLeft(int vel){
  analogWrite(IN1, 0);
  analogWrite(IN3, 0);
  analogWrite(IN5, vel);
  analogWrite(IN7, vel);
}

void moveRight(int vel){
  analogWrite(IN1, vel);
  analogWrite(IN3, vel);
  analogWrite(IN5, 0);
  analogWrite(IN7, 0);
}

void moveBackwards(int vel){
  analogWrite(IN2, vel);
  analogWrite(IN4, vel);
  analogWrite(IN6, vel);
  analogWrite(IN8, vel);
}

void stopMoving(){
  analogWrite(IN1, 0);
  analogWrite(IN2, 0);
  analogWrite(IN3, 0);
  analogWrite(IN4, 0);
  analogWrite(IN5, 0);
  analogWrite(IN6, 0);
  analogWrite(IN7, 0);
  analogWrite(IN8, 0);
}
