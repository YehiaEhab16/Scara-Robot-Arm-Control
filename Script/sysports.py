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
import serial.tools.list_ports as serial

# Serial handler class
class PortHandler(QThread):
    # Signal to notify about arduino connection
    ConnectedPort = Signal(str)
    # Connection feedback
    NoDeviceFound = 'N/A'
    
    # Class constructor
    def __init__(self):
        super().__init__()
        self.threadActive = False
        self.previousPort = self.NoDeviceFound
        self.start()

    # Main thread loop
    def run(self):
        self.threadActive = True
        while self.threadActive:
            port = self.listen()
            if port != self.previousPort:
                self.ConnectedPort.emit(port)
                self.previousPort = port

    # Listen to connected ports
    def listen(self) -> str:
        # Read connected serial ports
        ports = serial.comports()
        # Loop on all ports
        for port in ports:
            port = str(port)
            port = port.split(' - ')
            if 'ch340' in port[1].lower() or 'arduino' in port[1].lower():
                return port[0][3:]
        # In case of no devices found
        return self.NoDeviceFound
    
    # Terminate thread
    def terminate(self):
        self.threadActive = False
        self.wait()
        super().terminate()