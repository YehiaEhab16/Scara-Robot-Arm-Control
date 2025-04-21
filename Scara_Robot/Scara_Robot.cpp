/***************************************************************************************/
/*********************** Project: Scara Robot Arm                ***********************/
/*********************** Version: 1.3                            ***********************/
/*********************** Authors: Yehia Ehab                     ***********************/
/*********************** Date : 19/04/2025                       ***********************/
/***************************************************************************************/


#include "Scara_Robot.hpp"

// Set Motors Speed
void Scara::setSpeed(int speed)
{
    stepper1.setSpeed(speed); stepper2.setSpeed(speed); stepper3.setSpeed(speed); stepper4.setSpeed(speed);
}    

// Set Motors Acceleration
void Scara::setAcceleration(int acceleration)
{
    stepper1.setAcceleration(acceleration); stepper2.setAcceleration(acceleration); stepper3.setAcceleration(acceleration); stepper4.setAcceleration(acceleration);
}

// Set gripper angle
void Scara::setGripperAngle(int angle)
{
    gripperServo.write(angle);
}

// Init Scara Arm
void Scara::init(void)
{
    // Make index 0 active
    positions[0].active = true;

    // Limit Switches
    pinMode(LIMIT_SWITCH_1, INPUT_PULLUP); pinMode(LIMIT_SWITCH_2, INPUT_PULLUP);
    pinMode(LIMIT_SWITCH_3, INPUT_PULLUP); pinMode(LIMIT_SWITCH_4, INPUT_PULLUP);

    // Set Maximum Speed and Acceleration
    stepper1.setMaxSpeed(MAX_SPEED);  stepper1.setAcceleration(MAX_ACC);
    stepper2.setMaxSpeed(MAX_SPEED);  stepper2.setAcceleration(MAX_ACC);
    stepper3.setMaxSpeed(MAX_SPEED);  stepper3.setAcceleration(MAX_ACC);
    stepper4.setMaxSpeed(MAX_SPEED);  stepper4.setAcceleration(MAX_ACC);
    // Init Servo
    gripperServo.attach(GRIPPER_PIN); setGripperAngle(GRIPPER_INIT_POS);
    // Move to home position
    homePostion();
}

// Move to home position
void Scara::homePostion() 
{
    // Indicate Start of Motion
    Serial.println(COM_START_MOTION);

    // Homing Stepper4
    while (!digitalRead(LIMIT_SWITCH_4)) { stepper4.setSpeed(JOINTZ_HOME_SPEED); stepper4.runSpeed(); stepper4.setCurrentPosition(JOINTZ_HOME_POS); }
    stepper4.moveTo(JOINTZ_INIT_POS); while (stepper4.currentPosition() != JOINTZ_INIT_POS) stepper4.run();  

    // Homing Stepper3
    while (!digitalRead(LIMIT_SWITCH_3)) { stepper3.setSpeed(JOINT3_HOME_SPEED); stepper3.runSpeed(); stepper3.setCurrentPosition(JOINT3_HOME_POS); }
    stepper3.moveTo(JOINT3_INIT_POS); while (stepper3.currentPosition() != JOINT3_INIT_POS) stepper3.run();

    // Homing Stepper2
    while (!digitalRead(LIMIT_SWITCH_2)) { stepper2.setSpeed(JOINT2_HOME_SPEED); stepper2.runSpeed(); stepper2.setCurrentPosition(JOINT2_HOME_POS); }
    stepper2.moveTo(JOINT2_INIT_POS); while (stepper2.currentPosition() != JOINT2_INIT_POS) stepper2.run();

    // Homing Stepper1
    while (!digitalRead(LIMIT_SWITCH_1)) { stepper1.setSpeed(JOINT1_HOME_SPEED); stepper1.runSpeed(); stepper1.setCurrentPosition(JOINT1_HOME_POS); }
    stepper1.moveTo(JOINT1_INIT_POS); while (stepper1.currentPosition() != JOINT1_INIT_POS) stepper1.run();
    
    // Indicate End of Motion
    Serial.println(COM_END_LOOP);
}

// Save postions
void Scara::savePositions(int jointIndex, int order, int position)
{
    switch (jointIndex)
    {
        case JOINT_1:      positions[order].stepper1     = position * ANGLE_1_TO_STEPS;              break;
        case JOINT_2:      positions[order].stepper2     = position * ANGLE_2_TO_STEPS;              break;
        case JOINT_3:      positions[order].stepper3     = position * PHI_TO_STEPS;                  break;
        case JOINT_Z:      positions[order].stepper4     = position * Z_POS_TO_STEPS;                break;
        case GRIPPER:      positions[order].gripper      = position;                                 break;
        case GRIPPER_MOVE: positions[order].gripper      = position; setGripperAngle(position);      break;
        case SPEED:        positions[order].speed        = position;                                 break;
        case ACCELERATION: positions[order].acceleration = position; positions[order].active = true; break;
    }
}

// Edit position
void Scara::editPosition(int oldOrder, int newOrder)
{
    // Swap if new order is already active
    if(positions[newOrder].active)
    {
        Positions tempPos = positions[oldOrder];
        positions[oldOrder] = positions[newOrder];
        positions[newOrder] = tempPos;
    }
    else
    {
        positions[newOrder] = positions[oldOrder];
        positions[oldOrder].active = false;
    }
}

// Delete positions
void Scara::deletePosition(int order)
{
    positions[order].active = false;
}

// Delete positions
void Scara::deletePositions(void)
{
    for(int i=1;i<MAX_POSITIONS;i++) positions[i].active = false;
}

// Move Arm to required position
void Scara::moveArm(int index=0)
{  
    if(positions[index].active)
    {
        // Print index position
        if(index) { Serial.print(index); Serial.println(COM_INDEX); }

        // Indicate Start of Motion
        Serial.println(COM_START_LOOP);

        // Set speed and acceleration
        setSpeed(positions[index].speed);
        setAcceleration(positions[index].acceleration);

        // Move to required positions
        stepper1.moveTo(positions[index].stepper1); stepper2.moveTo(positions[index].stepper2); stepper3.moveTo(positions[index].stepper3); stepper4.moveTo(positions[index].stepper4);

        // Loop until required position is reached
        while (stepper1.currentPosition() != positions[index].stepper1 || stepper2.currentPosition() != positions[index].stepper2 || stepper3.currentPosition() != positions[index].stepper3 || stepper4.currentPosition() != positions[index].stepper4)
        { stepper1.run(); stepper2.run(); stepper3.run(); stepper4.run(); }

        // Move servo motor
        setGripperAngle(positions[index].gripper);

        // Indicate End of Motion
        Serial.println(COM_END_LOOP);
    }
}
