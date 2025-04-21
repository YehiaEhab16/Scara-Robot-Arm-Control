/***************************************************************************************/
/*********************** Project: Scara Robot Arm                ***********************/
/*********************** Version: 1.3                            ***********************/
/*********************** Authors: Yehia Ehab                     ***********************/
/*********************** Date : 19/04/2025                       ***********************/
/***************************************************************************************/

#include "Scara_Robot.hpp"

// Global variables 
bool loopFlag;
int order;
int iterator = 1;

// volatile flags
volatile char data; 
volatile int recievedNumber;
volatile String recievedString;

// Scara Bot instance
Scara scaraArm;

// Setup Code
void setup() {
  Serial.begin(BAUD_RATE);
  scaraArm.init();
}

// Main Loop
void loop(){
  
  if(loopFlag && iterator < MAX_POSITIONS) scaraArm.moveArm(iterator++);
  else if (iterator==MAX_POSITIONS) iterator = 1;

  switch(data)
  {
    case COM_JOINT_1:      scaraArm.savePositions(JOINT_1,      order, recievedNumber); data = COM_NULL; break;
    case COM_JOINT_2:      scaraArm.savePositions(JOINT_2,      order, recievedNumber); data = COM_NULL; break;
    case COM_JOINT_3:      scaraArm.savePositions(JOINT_3,      order, recievedNumber); data = COM_NULL; break;
    case COM_JOINT_Z:      scaraArm.savePositions(JOINT_Z,      order, recievedNumber); data = COM_NULL; break;
    case COM_GRIPPER:      scaraArm.savePositions(GRIPPER,      order, recievedNumber); data = COM_NULL; break;
    case COM_GRIPPER_MOVE: scaraArm.savePositions(GRIPPER_MOVE, order, recievedNumber); data = COM_NULL; break;
    case COM_SPEED:        scaraArm.savePositions(SPEED,        order, recievedNumber); data = COM_NULL; break;
    case COM_ACCELERATION: scaraArm.savePositions(ACCELERATION, order, recievedNumber); data = COM_EDIT; break;
    case COM_EDIT:         order = 0;                                                   data = COM_NULL; break; 
    case COM_INDEX:        order = recievedNumber;                                      data = COM_NULL; break; 
    case COM_INDEX_CHANGE: scaraArm.editPosition(order, recievedNumber);                data = COM_EDIT; break; 
    case COM_DELETE:       scaraArm.deletePosition(recievedNumber);                     data = COM_EDIT; break; 
    case COM_CLEAR:        scaraArm.deletePositions();                                  data = COM_NULL; break; 
    case COM_START_MOTION: scaraArm.moveArm();                                          data = COM_NULL; break;
    case COM_START_LOOP:   loopFlag = true;                                             data = COM_NULL; break;
    case COM_END_LOOP:     loopFlag = false;                                            data = COM_NULL; break; 
  }
}

// Serial Interrupt
void serialEvent() {
  char recievedChar = Serial.read();
  if((recievedChar >= '0' && recievedChar <= '9') || recievedChar == '-') { recievedString += recievedChar; }
  else{recievedNumber = atoi(recievedString.c_str()); recievedString=""; data=recievedChar; } 
}
