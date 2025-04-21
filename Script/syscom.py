##########################################################################################
####################### Project: Scara Robot Arm                   #######################
####################### Version: 1.3                               #######################
####################### Author: Yehia Ehab                         #######################
####################### Date : 19/04/2025                          #######################
##########################################################################################

# Serial Functions #

# Importing PySide packages
from PySide6.QtCore import QThread, Signal

# Importing Serial and Time modules
import serial

# Communication Thread
class Communication(QThread):
    # Signals to notify motion completion
    MotionStatus  = Signal(int)
    PositonUpdate = Signal(int)

    # Time Steps
    ManualTimeStep = 90

    # Error States
    ComInitSuccess        = 0
    ComStopSuccess        = 1
    ComInitFailure        = 2
    ComStopFailure        = 3
    ComAlreadyInitialized = 4
    ComAlreadyStopped     = 5

    HomingInProgress      = 0
    MotionInProgress      = 1
    MotionComplete        = 2

    FirstJointPosition    = 'A'
    SecondJointPosition   = 'B'
    ThirdJointPosition    = 'C'
    Zposition             = 'D'
    GripperValue          = 'E'
    GripperMove           = 'e'
    SpeedValue            = 'F'
    AccelerationValue     = 'G'
    Delete                = 'H'
    Index                 = 'I'
    IndexChange           = 'J'
    EditPosition          = 'K'
    Clear                 = 'Z'
    StartMotion           = 'S'
    LoopMotion            = 's'
    StopMotion            = 'X'

    # Initailize class variables
    def __init__(self):
        super().__init__()
        self.threadActive = False
        self.arduino = None

    # Connect to arduino
    def init(self, num: str) -> int:
        try:
            if self.arduino is None:
                self.arduino = serial.Serial(f'COM{num}', baudrate=115200, timeout=1) # Open serial port
                self.start()
                return self.ComInitSuccess
            else:
                return self.ComAlreadyInitialized
        except:
            return self.ComInitFailure

    # Send Data to Arduino
    def sendData(self, data: str) -> bool:
        try:
            if data and self.arduino is not None:
                self.arduino.write(bytes(data, 'utf-8')) # Write to serial port
                return True
            else:
                return False
        except:
            return False
        
    # Receive Data from Arduino
    def receiveData(self):
        try:
            if self.arduino is not None and self.arduino.in_waiting > 0:
                data = self.arduino.readline().decode('utf-8').strip()
                if data == self.StartMotion:
                    self.MotionStatus.emit(self.HomingInProgress)
                elif data == self.LoopMotion:
                    self.MotionStatus.emit(self.MotionInProgress)
                elif data == self.StopMotion:
                    self.MotionStatus.emit(self.MotionComplete)
                elif data.endswith(self.Index):
                    self.PositonUpdate.emit(int(data[:-1]))
        except:
            pass
    # Stop Communication
    def stop(self) -> int:
        try:
            if self.arduino is not None:
                self.arduino.close() # Close Serial Port
                self.arduino = None
                self.terminate()
                return self.ComStopSuccess
            else:
                return self.ComAlreadyStopped
        except:
            return self.ComStopFailure
        
    def run(self):
        self.threadActive = True
        while self.threadActive:
            self.receiveData()
    
    def terminate(self):
        self.threadActive = False
        self.wait()
        super().terminate()
