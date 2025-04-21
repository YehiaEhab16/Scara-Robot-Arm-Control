/***************************************************************************************/
/*********************** Project: Scara Robot Arm                ***********************/
/*********************** Version: 1.3                            ***********************/
/*********************** Authors: Yehia Ehab                     ***********************/
/*********************** Date : 19/04/2025                       ***********************/
/***************************************************************************************/

#ifndef SCARA_ROBOT_H
#define SCARA_ROBOT_H

#include <Arduino.h>
#include <math.h>
#include <Servo.h>
#include <AccelStepper.h>

// Motor Pins
#define STEPPER_DRIVER      1
#define STEPPER_1_STEP      2
#define STEPPER_2_STEP      3 
#define STEPPER_3_STEP      4
#define STEPPER_4_STEP      12
#define STEPPER_1_DIR       5
#define STEPPER_2_DIR       6
#define STEPPER_3_DIR       7
#define STEPPER_4_DIR       13
#define GRIPPER_PIN         A1

// Limit Switches
#define LIMIT_SWITCH_1      11
#define LIMIT_SWITCH_2      10
#define LIMIT_SWITCH_3      9
#define LIMIT_SWITCH_4      A3

// Baud Rate
#define BAUD_RATE           115200

// Communication Variables
#define COM_JOINT_1         'A'
#define COM_JOINT_2         'B'
#define COM_JOINT_3         'C'
#define COM_JOINT_Z         'D'
#define COM_GRIPPER         'E'
#define COM_GRIPPER_MOVE    'e'
#define COM_SPEED           'F'
#define COM_ACCELERATION    'G'
#define COM_DELETE          'H'
#define COM_INDEX           'I'
#define COM_INDEX_CHANGE    'J'
#define COM_EDIT            'K'
#define COM_START_MOTION    'S'
#define COM_START_LOOP      's'
#define COM_END_LOOP        'X'
#define COM_CLEAR           'Z'
#define COM_NULL            '#'  

// Joint Argument 
#define JOINT_1              0
#define JOINT_2              1
#define JOINT_3              2
#define JOINT_Z              3
#define GRIPPER              4
#define GRIPPER_MOVE         5
#define SPEED                6
#define ACCELERATION         7

// Angle to step conversion
#define ANGLE_1_TO_STEPS     44.88888f
#define ANGLE_2_TO_STEPS     36.0f
#define PHI_TO_STEPS         9.333322f
#define Z_POS_TO_STEPS       96.5f

// Initial Positions
#define JOINT1_INIT_POS      0 * ANGLE_1_TO_STEPS    
#define JOINT2_INIT_POS      0 * ANGLE_2_TO_STEPS    
#define JOINT3_INIT_POS      0 * PHI_TO_STEPS        
#define JOINTZ_INIT_POS      100 * Z_POS_TO_STEPS   
#define GRIPPER_INIT_POS     0
#define SPEED_INIT_VALUE     500
#define ACCEL_INIT_VALUE     500

// Home Positons
#define JOINT1_HOME_POS      -80 * ANGLE_1_TO_STEPS     
#define JOINT2_HOME_POS      -160 * ANGLE_2_TO_STEPS     
#define JOINT3_HOME_POS      -175 * PHI_TO_STEPS     
#define JOINTZ_HOME_POS      150 * Z_POS_TO_STEPS
#define JOINT1_HOME_SPEED    -1000
#define JOINT2_HOME_SPEED    -1300
#define JOINT3_HOME_SPEED    -1100
#define JOINTZ_HOME_SPEED    2000

// Maximum Values
#define MAX_SPEED           4000
#define MAX_ACC             2000
#define MAX_POSITIONS       10

// Positions Struct
struct Positions
{
    bool active  = false;               int gripper      = GRIPPER_INIT_POS;
    int stepper1 =  JOINT1_INIT_POS;    int stepper2     = JOINT2_INIT_POS;
    int stepper3 =  JOINT3_INIT_POS;    int stepper4     = JOINTZ_INIT_POS;
    int speed    =  SPEED_INIT_VALUE;   int acceleration = ACCEL_INIT_VALUE;
};

// Scara Class
class Scara
{
    // Motor Positions
    Positions positions[MAX_POSITIONS];

    // Stepper Motors
    AccelStepper stepper1 = {STEPPER_DRIVER, STEPPER_1_STEP, STEPPER_1_DIR};
    AccelStepper stepper2 = {STEPPER_DRIVER, STEPPER_2_STEP, STEPPER_2_DIR};
    AccelStepper stepper3 = {STEPPER_DRIVER, STEPPER_3_STEP, STEPPER_3_DIR};
    AccelStepper stepper4 = {STEPPER_DRIVER, STEPPER_4_STEP, STEPPER_4_DIR};

    // Servo Motor
    Servo gripperServo;

    /**
    *@def set motors speed
    *@param speed required speed
    */
    void setSpeed(int speed);    

    /**
    *@def set motors acceleration
    *@param acceleration required acceleration
    */
    void setAcceleration(int acceleration);  

    /**
    *@def set gripper angle
    *@param angle required angle
    */
    void setGripperAngle(int angle); 

    public:
        /**
        *@def init scara arm
        */
        void init(void);

        /**
        *@def move to home position
        */
        void homePostion(void); 
        
        /**
        *@def save positions
        *@param jointIndex joint index
        *@param position required position
        *@param order motion iteration
        */
        void savePositions(int jointIndex, int order, int position);

        /**
        *@def edit position
        *@param oldOrder old order / index
        *@param newOrder new order / index
        */
        void editPosition(int oldOrder, int newOrder);

        /**
        *@def delete positions
        *@param order motion iteration
        */
        void deletePosition(int order);

        /**
        *@def delete positions
        */
        void deletePositions(void);

        /**
        *@def move arm to required position
        *@param index required index
        */
        void moveArm(int index=0);
};


#endif
