##########################################################################################
####################### Project: Scara Robot Arm                   #######################
####################### Version: 1.3                               #######################
####################### Author: Yehia Ehab                         #######################
####################### Date : 19/04/2025                          #######################
##########################################################################################

# GUI Main #

# Importing PySide packages
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QButtonGroup, QTableWidgetItem
from PySide6.QtCore import QPropertyAnimation, Qt, QTimer
from PySide6.QtGui import QCloseEvent, QMovie, QIcon

# Importing defined modules
from syscom import Communication as Com
from sysports import PortHandler
from path import PathManager
from gui import ScaraUi

# Importing required modules
from functools import partial
import math, sys, re

# Define main window
class ScaraRobot(QWidget):
    def __init__(self):
        super().__init__()

        # Load UI
        self.ui = ScaraUi()
        self.ui.setupUi(self)
        window = self.frameGeometry()
        window.moveCenter(self.screen().availableGeometry().center())
        self.move(window.topLeft())

        # Handle unexpected errors
        sys.excepthook = lambda excType, excValue, _ : QMessageBox.critical(self, "Error", f"An unexpected error occurred:\n{excType.__name__}: {excValue}")

        # Initial Values
        self.firstJointInitialValue   = 0    # Joint 1 Value (from -45 to 260)
        self.secondJointInitialValue  = 0    # Joint 2 Value (from -150 to 150) 
        self.thirdJointInitialValue   = 0    # Joint 3 Value (from -170 to 170)
        self.zPositionInitialValue    = 100  # Z Position Value (from 0 to 150)
        self.gripperInitialValue      = 0    # Gripper Value (from 0 to 180)
        self.speedInitialValue        = 500  # Speed Value (from 500 to 4000)
        self.accelerationInitialValue = 500  # Acceleration Value (from 500 to 2000)

        # Previous Line Edit, Table and Slider Values
        self.previousX = self.ui.xPositionLineEdit.text() 
        self.previousY = self.ui.yPositionLineEdit.text()
        self.previousZ = self.ui.zPositionLineEdit.text() 
        self.previousTableItem = None
        self.previousSliderValue = None
        self.previousPressedSlider = None

        # Create Feedback Animation
        self.feedbackAnimation = QPropertyAnimation(self.ui.animationFrame, b'maximumHeight')
        self.ui.animationFrame.setMaximumHeight(0)
        self.feedbackAnimation.setDuration(500)
        
        # Create Communication Animation
        self.comAnimation = QPropertyAnimation(self.ui.portFrame, b'maximumWidth')
        self.comAnimation.setDuration(500)

        # Create Forward Values Animation
        self.forwardAnimation = QPropertyAnimation(self.ui.forwadValuesFrame, b'maximumWidth')
        self.ui.forwadValuesFrame.setMaximumWidth(0)
        self.comAnimation.setDuration(500)

        # Create Slider Buttons Animations
        self.firstSliderAnimation = QPropertyAnimation(self.ui.firstJointButtonsFrame, b'maximumWidth')
        self.secondSliderAnimation = QPropertyAnimation(self.ui.secondJointButtonsFrame, b'maximumWidth')
        self.thirdSliderAnimation = QPropertyAnimation(self.ui.thirdJointButtonsFrame, b'maximumWidth')
        self.zPositionSliderAnimation = QPropertyAnimation(self.ui.zPositionButtonsFrame, b'maximumWidth')
        self.ui.firstJointButtonsFrame.setMaximumWidth(0)
        self.ui.secondJointButtonsFrame.setMaximumWidth(0)
        self.ui.thirdJointButtonsFrame.setMaximumWidth(0)
        self.ui.zPositionButtonsFrame.setMaximumWidth(0)
        self.firstSliderAnimation.setDuration(500)
        self.secondSliderAnimation.setDuration(500)
        self.thirdSliderAnimation.setDuration(500)
        self.zPositionSliderAnimation.setDuration(500)

        # Show GIF Loading Animation
        animatedIcon = QMovie(PathManager.LoadingGifPath)
        animatedIcon.setScaledSize(self.ui.animationLabel.size())
        self.ui.animationLabel.setMovie(animatedIcon)
        animatedIcon.start()

        # Show GIF Rnd Animation
        animatedIcon = QMovie(PathManager.RndGifPath)
        animatedIcon.setScaledSize(self.ui.rndLabel.size())
        self.ui.rndLabel.setMovie(animatedIcon)
        animatedIcon.start()

        # Timer for sending data to arduino
        self.sendTimer = QTimer(self)
        self.sendTimer.timeout.connect(self.Handle_Hold)
        
        # Port Handler
        self.portThread = PortHandler()
        self.isConnected = False
        self.portThread.ConnectedPort.connect(self.Handle_Port)

        # Communication Thread
        self.serialThread = Com()
        self.inLoop = False
        self.inProgress = False
        self.serialThread.MotionStatus.connect(self.Handle_Animation)
        self.serialThread.PositonUpdate.connect(self.Handle_Position)

        # Handle GUI Buttons
        self.Handle_Buttons()

    # GUI buttons
    def Handle_Buttons(self):
        # Communication Button                  
        self.ui.comButton.clicked.connect(self.Handle_Com)                                          # Start Communication Button

        # Sliders
        self.ui.firstJointSlider.sliderPressed.connect(lambda: self.Handle_JointSlider(1, True))    # Joint 1 Slider Press
        self.ui.firstJointSlider.sliderReleased.connect(lambda: self.Handle_JointSlider(1, False))  # Joint 1 Slider Release
        self.ui.firstJointSlider.sliderMoved.connect(partial(self.Handle_JointValue, 1, True))      # Joint 1 Slider Move
        self.ui.firstJointSlider.valueChanged.connect(partial(self.Handle_JointValue, 1, False))    # Joint 1 Slider Value Change
        self.ui.secondJointSlider.sliderPressed.connect(lambda: self.Handle_JointSlider(2, True))   # Joint 2 Slider Press
        self.ui.secondJointSlider.sliderReleased.connect(lambda: self.Handle_JointSlider(2, False)) # Joint 2 Slider Release
        self.ui.secondJointSlider.sliderMoved.connect(partial(self.Handle_JointValue, 2, True))     # Joint 2 Slider Move
        self.ui.secondJointSlider.valueChanged.connect(partial(self.Handle_JointValue, 2, False))   # Joint 2 Slider Value Change
        self.ui.thirdJointSlider.sliderPressed.connect(lambda: self.Handle_JointSlider(3, True))    # Joint 3 Slider Press
        self.ui.thirdJointSlider.sliderReleased.connect(lambda: self.Handle_JointSlider(3, False))  # Joint 3 Slider Release
        self.ui.thirdJointSlider.sliderMoved.connect(partial(self.Handle_JointValue, 3, True))      # Joint 3 Slider Move
        self.ui.thirdJointSlider.valueChanged.connect(partial(self.Handle_JointValue, 3, False))    # Joint 3 Slider Value Change
        self.ui.zPositionSlider.sliderPressed.connect(lambda: self.Handle_JointSlider(4, True))     # Z Position Slider Press
        self.ui.zPositionSlider.sliderReleased.connect(lambda: self.Handle_JointSlider(4, False))   # Z Position Slider Release
        self.ui.zPositionSlider.sliderMoved.connect(partial(self.Handle_JointValue, 4, True))       # Z Position Slider Move
        self.ui.zPositionSlider.valueChanged.connect(partial(self.Handle_JointValue, 4, False))     # Z Position Slider Value Change
        self.ui.gripperSlider.sliderMoved.connect(partial(self.Handle_JointValue, 5, True))         # Gripper Slider Move
        self.ui.gripperSlider.valueChanged.connect(partial(self.Handle_JointValue, 5, False))       # Gripper Slider Value Change   
        self.ui.speedSlider.sliderMoved.connect(partial(self.Handle_JointValue, 6, True))           # Speed Slider Move
        self.ui.speedSlider.valueChanged.connect(partial(self.Handle_JointValue, 6, False))         # Speed Slider Value Change   
        self.ui.accelerationSlider.sliderMoved.connect(partial(self.Handle_JointValue, 7, True))    # Acceleration Slider Move
        self.ui.accelerationSlider.valueChanged.connect(partial(self.Handle_JointValue, 7, False))  # Acceleration Slider Value Change

        # Sliders Initial Value
        self.ui.firstJointSlider.setValue(self.firstJointInitialValue)
        self.ui.secondJointSlider.setValue(self.secondJointInitialValue)
        self.ui.thirdJointSlider.setValue(self.thirdJointInitialValue)
        self.ui.zPositionSlider.setValue(self.zPositionInitialValue)
        self.ui.gripperSlider.setValue(self.gripperInitialValue)
        self.ui.speedSlider.setValue(self.speedInitialValue)
        self.ui.accelerationSlider.setValue(self.accelerationInitialValue)

        # Slider Buttons
        self.ui.firstJointMoveButton.clicked.connect(lambda: self.Handle_JointMove(1, True))        # Joint 1 Move Button
        self.ui.firstJointCancelButton.clicked.connect(lambda: self.Handle_JointMove(1, False))     # Joint 1 Cancel Button
        self.ui.secondJointMoveButton.clicked.connect(lambda: self.Handle_JointMove(2, True))       # Joint 2 Move Button
        self.ui.secondJointCancelButton.clicked.connect(lambda: self.Handle_JointMove(2, False))    # Joint 2 Cancel Button
        self.ui.thirdJointMoveButton.clicked.connect(lambda: self.Handle_JointMove(3, True))        # Joint 3 Move Button
        self.ui.thirdJointCancelButton.clicked.connect(lambda: self.Handle_JointMove(3, False))     # Joint 3 Cancel Button
        self.ui.zPositionMoveButton.clicked.connect(lambda: self.Handle_JointMove(4, True))         # Z Position Move Button
        self.ui.zPositionCancelButton.clicked.connect(lambda: self.Handle_JointMove(4, False))      # Z Position Cancel Button

        # Add / Subtract Buttons
        self.ui.addButton.pressed.connect(lambda: self.Handle_Add(True))                            # Add Button Pressed
        self.ui.subtractButton.pressed.connect(lambda: self.Handle_Add(False))                      # Subtract Button Pressed
        self.ui.addButton.released.connect(self.Handle_Stop)                                        # Add Button Released
        self.ui.subtractButton.released.connect(self.Handle_Stop)                                   # Subtract Button Released

        # X / Y / Z Line Edit 
        self.ui.xPositionLineEdit.editingFinished.connect(self.Handle_XposEdit)                     # X Position Line Edit
        self.ui.yPositionLineEdit.editingFinished.connect(self.Handle_YposEdit)                     # Y Position Line Edit
        self.ui.zPositionLineEdit.editingFinished.connect(self.Handle_ZposEdit)                     # Z Position Line Edit
        
        # Sending Buttons
        self.ui.moveButton.clicked.connect(self.Handle_Move)                                        # Move to Position Button
        self.ui.homeButton.clicked.connect(self.Handle_Home)                                        # Home Position Button
        self.ui.saveButton.clicked.connect(self.Handle_Save)                                        # Save Position Button
        self.ui.loopButton.clicked.connect(self.Handle_Loop)                                        # Loop through Positions Button
        self.ui.clearButton.clicked.connect(self.Handle_Clear)                                      # Clear Positions Button

        # Position Table
        self.ui.positionsTable.cellDoubleClicked.connect(self.Handle_Remove)                        # Remove Item from table
        self.ui.positionsTable.itemClicked.connect(self.Handle_Item)                                # Item Clicked in table
        self.ui.positionsTable.itemChanged.connect(self.Handle_Change)                              # Edit Item in table

        # Control Radio Group
        self.radioGroup = QButtonGroup()
        self.radioGroup.addButton(self.ui.firstJointRadio)                                          # First Joint Radio
        self.radioGroup.addButton(self.ui.secondJointRadio)                                         # Second Joint Radio
        self.radioGroup.addButton(self.ui.thirdJointRadio)                                          # Third Joint Radio
        self.radioGroup.addButton(self.ui.zPositionRadio)                                           # Z Position Radio
        self.radioGroup.addButton(self.ui.gripperRadio)                                             # Gripper Radio
        self.radioGroup.addButton(self.ui.speedRadio)                                               # Speed Radio
        self.radioGroup.addButton(self.ui.accelerationRadio)                                        # Acceleration Radio
        self.radioGroup.setExclusive(True) 

    # Handle Timer Function
    def Handle_Hold(self):
        # Temporarily clear connection flag
        isConnected = self.isConnected
        self.isConnected = False
        
        # Joint 1 Checked 
        if self.ui.firstJointRadio.isChecked():
            firstJointPosition = max(self.ui.firstJointSlider.minimum(), min(self.ui.firstJointSlider.maximum(), int(self.ui.actualFirstJointValueLabel.text()) + (1 if self.operation else -1)))
            self.ui.firstJointSlider.setValue(firstJointPosition)
            self.forwardKinematics()
            self.data = str(firstJointPosition) + Com.FirstJointPosition + Com.StartMotion
        
        # Joint 2 Checked 
        elif self.ui.secondJointRadio.isChecked():
            secondJointPosition = max(self.ui.secondJointSlider.minimum(), min(self.ui.secondJointSlider.maximum(), int(self.ui.actualSecondJointValueLabel.text()) + (1 if self.operation else -1)))
            self.ui.secondJointSlider.setValue(secondJointPosition)
            self.forwardKinematics()
            self.data = str(secondJointPosition) + Com.SecondJointPosition + Com.StartMotion

        # Joint 3 Checked 
        elif self.ui.thirdJointRadio.isChecked():
            thirdJointPosition = max(self.ui.thirdJointSlider.minimum(), min(self.ui.thirdJointSlider.maximum(), int(self.ui.actualThirdJointValueLabel.text()) + (1 if self.operation else -1)))
            self.ui.thirdJointSlider.setValue(thirdJointPosition)
            self.data = str(thirdJointPosition) + Com.ThirdJointPosition + Com.StartMotion

        # Z Position Checked 
        elif self.ui.zPositionRadio.isChecked():
            zPosition = max(self.ui.zPositionSlider.minimum(), min(self.ui.zPositionSlider.maximum(), int(self.ui.actualZPositionValueLabel.text()) + (1 if self.operation else -1)))
            self.ui.zPositionSlider.setValue(zPosition)        
            self.data = str(zPosition) + Com.Zposition + Com.StartMotion

        # Gripper Checked 
        elif self.ui.gripperRadio.isChecked():
            gripper = max(self.ui.gripperSlider.minimum(), min(self.ui.gripperSlider.maximum(), self.ui.gripperSlider.value() + (5 if self.operation else -1)))
            self.ui.gripperSlider.setValue(gripper)        
            self.serialThread.sendData(str(gripper) + Com.GripperMove)

        # Speed Checked
        elif self.ui.speedRadio.isChecked():
            speed = max(self.ui.speedSlider.minimum(), min(self.ui.speedSlider.maximum(), self.ui.speedSlider.value() + (10 if self.operation else -1)))
            self.ui.speedSlider.setValue(speed)
            self.data = str(speed) + Com.SpeedValue   

        # Acceleration Checked
        elif self.ui.accelerationRadio.isChecked():
            acceleration = max(self.ui.accelerationSlider.minimum(), min(self.ui.accelerationSlider.maximum(), self.ui.accelerationSlider.value() + (10 if self.operation else -1)))
            self.ui.accelerationSlider.setValue(acceleration)
            self.data = str(acceleration) + Com.AccelerationValue
        
        # Restore Connection Flag 
        self.isConnected = isConnected

    # Handle Port Changes
    def Handle_Port(self, port: str):
        if port == PortHandler.NoDeviceFound:
            # Stop Thread and show disconnect animation
            self.serialThread.stop()
            self.ui.portLineEdit.setText('')
            self.showFeedbackAnimation(False, 'Communication Interrupted')
            self.showComAnimation(False)
        else:
            # Update Port Line Edit
            self.ui.portLineEdit.setText(port)  

    # Handle Animation
    def Handle_Animation(self, motionStatus: int):
        if not self.inLoop:
            if motionStatus == Com.HomingInProgress:
                # Clear Table and set home position
                self.ui.positionsTable.setRowCount(0)
                self.homePosition()
                self.showFeedbackAnimation(True, 'Moving to home position ...')
            elif motionStatus == Com.MotionInProgress:
                self.showFeedbackAnimation(True, 'Moving to desired position ...')
            elif motionStatus == Com.MotionComplete:
                self.showFeedbackAnimation(False, 'Motion Complete')

    # Handle Posiiton Update from serial thread
    def Handle_Position(self, index: int):
        for row in range(self.ui.positionsTable.rowCount()):
            if index == int(self.ui.positionsTable.item(row, 0).text()):
                self.ui.positionsTable.selectRow(row)
                # Temporarily clear connection flag
                isConnected = self.isConnected
                self.isConnected = False
                # Update all positions
                self.ui.xPositionLineEdit.setText(self.ui.positionsTable.item(row, 1).text())
                self.ui.yPositionLineEdit.setText(self.ui.positionsTable.item(row, 2).text())
                self.ui.zPositionLineEdit.setText(self.ui.positionsTable.item(row, 3).text())
                self.ui.gripperSlider.setValue(int(self.ui.positionsTable.item(row, 4).text()))
                self.ui.speedSlider.setValue(int(self.ui.positionsTable.item(row, 5).text()))
                self.ui.accelerationSlider.setValue(int(self.ui.positionsTable.item(row, 6).text()))
                self.inverseKinematics(True)
                # Restore Connection Flag 
                self.isConnected = isConnected
                return

    # Start Communication
    def Handle_Com(self):
        if not self.isConnected:
            port = self.ui.portLineEdit.text() # Read Com Port
            if port.isdigit():
                # Try to initialize connection
                comStatus = self.serialThread.init(port)
                if comStatus == Com.ComInitSuccess:
                    # Success initializing serial communication
                    self.showComAnimation(True)
                elif comStatus == Com.ComAlreadyInitialized:
                    # Already initialized
                    QMessageBox.warning(self, 'Communication Error', 'Serial communication already initialized')
                else:
                    # Error connecting
                    QMessageBox.warning(self, 'Communication Error', "Couldn't start serial communication")
            else:
                # Error connecting
                QMessageBox.warning(self, 'Communication Error', 'Please select available com port')

        else:
            comStatus = self.serialThread.stop()
            if comStatus == Com.ComStopSuccess:
                # Succeess ending serial communication
                self.showComAnimation(False)
                self.showFeedbackAnimation(False, 'Communication Interrupted')
            elif comStatus == Com.ComAlreadyStopped:
                # Already Stopped
                QMessageBox.warning(self, 'Communication Error', 'No serial communication available')
            else:
                # No serial communication available 
                QMessageBox.warning(self, 'Communication Error', "Couldn't end serial communication")

    # Joint Slider Press / Release
    def Handle_JointSlider(self, sliderIndex:int, isPressed: bool):
        sliderValue = { 1: self.ui.firstJointSlider.value(), 2: self.ui.secondJointSlider.value(), 3: self.ui.thirdJointSlider.value(), 4: self.ui.zPositionSlider.value() }.get(sliderIndex)
        # Update Previous Pressed Values and Clear Previous Animations
        if isPressed:
            if self.previousPressedSlider != sliderIndex:
                self.Handle_JointMove(self.previousPressedSlider, False)
                self.previousSliderValue = sliderValue
            self.previousPressedSlider = sliderIndex
        # Show Buttons Animation
        elif self.isConnected:
            if self.previousSliderValue != sliderValue:
                self.showSliderButtonsAnimation(sliderIndex, True)

    # Slider Value Changed
    def Handle_JointValue(self, sliderIndex: int, isPressed: bool, newValue:int):
        newValue = str(newValue)
        # Joint 1 Update (Update actual value only if not connected)
        if sliderIndex == 1:
            self.ui.firstJointValueLabel.setText(newValue)
            if self.isConnected:
                self.showForwardValuesAnimation(True)
            else:
                self.ui.actualFirstJointValueLabel.setText(newValue)
            if isPressed:
                self.forwardKinematics()
        # Joint 2 Update (Update actual value only if not connected)
        elif sliderIndex == 2:
            self.ui.secondJointValueLabel.setText(newValue)
            if self.isConnected:
                self.showForwardValuesAnimation(True)
            else:
                self.ui.actualSecondJointValueLabel.setText(newValue)
            if isPressed:
                self.forwardKinematics()
        # Joint 3 Update (Update actual value only if not connected)
        elif sliderIndex == 3:
            self.ui.thirdJointValueLabel.setText(newValue)
            if self.isConnected:
                self.showForwardValuesAnimation(True)
            else:
                self.ui.actualThirdJointValueLabel.setText(newValue)
        # Z Position (Update actual value only if not connected)
        elif sliderIndex == 4:
            self.ui.zPositionValueLabel.setText(newValue)
            if self.isConnected:
                self.showForwardValuesAnimation(True)
            else:
                self.ui.actualZPositionValueLabel.setText(newValue)
            if isPressed:
                self.ui.zPositionLineEdit.setText(newValue)
        # Gripper Update
        elif sliderIndex == 5:
            self.ui.gripperValueLabel.setText(newValue)
            if isPressed and not self.inProgress:
                self.serialThread.sendData(newValue + Com.GripperMove)
        # Speed Update
        elif sliderIndex == 6:
            self.ui.speedValueLabel.setText(newValue)
            if isPressed and not self.inProgress:
                self.serialThread.sendData(newValue + Com.SpeedValue)
        # Acceleration Update
        elif sliderIndex == 7:
            self.ui.accelerationValueLabel.setText(newValue)
            if isPressed and not self.inProgress:
                self.serialThread.sendData(newValue + Com.AccelerationValue)      

    # Joint Move / Cancel Button
    def Handle_JointMove(self, sliderIndex:int , requiredToMove: bool):
        if sliderIndex:
            # Get required data and sliderr
            data, slider = { 1: (self.ui.firstJointValueLabel.text() + Com.FirstJointPosition, self.ui.firstJointSlider), 2: (self.ui.secondJointValueLabel.text() + Com.SecondJointPosition, self.ui.secondJointSlider), 3: (self.ui.thirdJointValueLabel.text() + Com.ThirdJointPosition, self.ui.thirdJointSlider), 4: (self.ui.zPositionValueLabel.text() + Com.Zposition, self.ui.zPositionSlider) }.get(sliderIndex)
            # Hide Forward Values Frame 
            if requiredToMove:
                self.showForwardValuesAnimation(False)
                self.serialThread.sendData(data + Com.StartMotion)
            # Set Slider to previous value
            elif self.previousSliderValue:
                slider.setValue(self.previousSliderValue)
                self.forwardKinematics(True)
            # Hide Slider Buttons
            self.showSliderButtonsAnimation(sliderIndex, False)

    # Add / Subtract Button
    def Handle_Add(self, operation):
        self.data = None
        self.operation = operation
        if not self.inProgress:
            # Start Timer if any radio button is checked
            if self.radioGroup.checkedButton():
                self.sendTimer.start(Com.ManualTimeStep)
            else:
                QMessageBox.information(self, 'No Joint Selected', 'Please select one of the joints to control')
        else:
            QMessageBox.information(self, 'Scara in operation', 'Please wait until scara robot finishes current operation')
    
    # Stop Timer
    def Handle_Stop(self):
        # Send data to scara
        self.serialThread.sendData(self.data)
        # Stop timer
        self.sendTimer.stop()

    # X Postion Line Edit
    def Handle_XposEdit(self):
        xPosText = self.ui.xPositionLineEdit.text()
        # Check if input is valid
        if re.match(r"^-?\d+$", xPosText) and int(xPosText)>=-365 and int(xPosText)<=365:
            # Update previous value if valid
            if self.inverseKinematics():
                self.previousX = xPosText
                # Set to home position
            elif int(xPosText) == 365 and not int(self.ui.yPositionLineEdit.text()):
                self.homePosition()
            # Out of range
            else:
                QMessageBox.information(self, 'Range Error', 'Out of scara robot range')
                self.ui.xPositionLineEdit.setText(self.previousX)
        else:
            QMessageBox.information(self, 'Value Error', 'Please enter a valid value for X from -365 to 365')
            self.ui.xPositionLineEdit.setText(self.previousX)

    # Y Postion Line Edit
    def Handle_YposEdit(self):
        yPosText = self.ui.yPositionLineEdit.text()
        # Check if input is valid
        if re.match(r"^-?\d+$", yPosText) and int(yPosText)>=-365 and int(yPosText)<=365:
            # Update previous value if valid
            if self.inverseKinematics():
                self.previousY = yPosText
                # Set to home position
            elif not int(yPosText) and int(self.ui.xPositionLineEdit.text()) == 365:
                self.homePosition()
            # Out of range
            else:
                QMessageBox.information(self, 'Range Error', 'Out of scara robot range')
                self.ui.yPositionLineEdit.setText(self.previousY)
        else:
            QMessageBox.information(self, 'Value Error', 'Please enter a valid value for Y from -365 to 365')
            self.ui.yPositionLineEdit.setText(self.previousY)

    # Z Postion Line Edit
    def Handle_ZposEdit(self):
        zPosText = self.ui.zPositionLineEdit.text()
        # Check if input is valid
        if zPosText.isdigit() and int(zPosText)>=0 and int(zPosText)<=150:
            # Update previous value if valid
            self.previousZ = zPosText 
            # Set actual value only if not connected  
            if self.isConnected:
                self.ui.zPositionValueLabel.setText(zPosText)
                self.showForwardValuesAnimation(True)
            else:
                self.ui.zPositionSlider.setValue(int(zPosText))
        else:
            QMessageBox.information(self, 'Value Error', 'Please enter a valid value for Z from 0 to 150')
            self.ui.zPositionLineEdit.setText(self.previousZ)

    # Move Postion Button
    def Handle_Move(self):
        if not self.inProgress:
            # Temporarily clear connection flag
            isConnected = self.isConnected
            self.isConnected = False
            self.inverseKinematics(True)
            # Restore Connection Flag 
            self.isConnected = isConnected
            # Show Animations and send data
            self.showSliderButtonsAnimation(self.previousPressedSlider, False)
            self.showForwardValuesAnimation(False)
            self.serialThread.sendData(self.ui.firstJointValueLabel.text() + Com.FirstJointPosition + self.ui.secondJointValueLabel.text() + Com.SecondJointPosition + self.ui.thirdJointValueLabel.text() + Com.ThirdJointPosition + self.ui.zPositionValueLabel.text() + Com.Zposition + self.ui.gripperValueLabel.text() + Com.GripperValue + Com.StartMotion)
        else:
            QMessageBox.information(self, 'Scara in operation', 'Please wait until scara robot finishes current operation')

    # Home Postion Button
    def Handle_Home(self):
        if not self.inProgress:
            # Set home position then send data
            self.homePosition()
            self.Handle_Move()
        else:
            QMessageBox.information(self, 'Scara in operation', 'Please wait until scara robot finishes current operation')

    # Save Position Button
    def Handle_Save(self):
        if not self.inProgress:
            self.inProgress = True
            # Insert New Row
            newRow = self.ui.positionsTable.rowCount()
            self.ui.positionsTable.insertRow(newRow)

            # Get Order of new row
            previous = 1
            for indexRow in range(self.ui.positionsTable.rowCount()-1):
                tableItem = self.ui.positionsTable.item(indexRow, 0).text()
                if previous and int(tableItem) - previous:
                    break
                previous = int(tableItem) + 1
            
            # Set Order in current Row            
            item = QTableWidgetItem(str(previous))
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.positionsTable.setItem(newRow, 0, item)
            
            # Set X Position in current Row
            item = QTableWidgetItem(self.ui.xPositionLineEdit.text())
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.positionsTable.setItem(newRow, 1, item)
            
            # Set Y Position in current Row
            item = QTableWidgetItem(self.ui.yPositionLineEdit.text())
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.positionsTable.setItem(newRow, 2, item)
            
            # Set Z Position in current Row
            item = QTableWidgetItem(self.ui.zPositionLineEdit.text())
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.positionsTable.setItem(newRow, 3, item)
            
            # Set Gripper Value in current Row
            item = QTableWidgetItem(self.ui.gripperValueLabel.text())
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.positionsTable.setItem(newRow, 4, item)
            
            # Set Speed Value in current Row
            item = QTableWidgetItem(self.ui.speedValueLabel.text())
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.positionsTable.setItem(newRow, 5, item)
            
            # Set Accleration Value in current Row
            item = QTableWidgetItem(self.ui.accelerationValueLabel.text())
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.positionsTable.setItem(newRow, 6, item)

            # Sort Items according to order and send to Scara
            self.inProgress = False
            self.ui.positionsTable.sortItems(0, Qt.AscendingOrder)
            self.serialThread.sendData(str(newRow+1) + Com.Index + self.ui.firstJointValueLabel.text() + Com.FirstJointPosition + self.ui.secondJointValueLabel.text() + Com.SecondJointPosition + self.ui.thirdJointValueLabel.text() + Com.ThirdJointPosition + self.ui.zPositionValueLabel.text() + Com.Zposition + self.ui.gripperValueLabel.text() + Com.GripperValue + self.ui.speedValueLabel.text() + Com.SpeedValue + self.ui.accelerationValueLabel.text() + Com.AccelerationValue)
        else:
            QMessageBox.information(self, 'Scara in operation', 'Please wait until scara robot finishes current operation')

    # Loop Button
    def Handle_Loop(self):
        if self.inLoop:
            # Stop Loop
            self.inLoop = False
            self.serialThread.sendData(Com.StopMotion)               
            self.showFeedbackAnimation(True, 'Halting Motion ...')     
            self.ui.loopButton.setIcon(QIcon(PathManager.PlayPngPath))
        elif not self.ui.positionsTable.rowCount():
            QMessageBox.information(self, 'Positions Error', 'Please save positions to loop through')
        elif not self.isConnected:
            QMessageBox.warning(self, 'Communication Error', 'Please connect to scara robot first')
        elif not self.inProgress:
            # Start Loop and show animations
            self.inLoop = True
            self.serialThread.sendData(Com.LoopMotion)
            self.showSliderButtonsAnimation(self.previousPressedSlider, False)
            self.showFeedbackAnimation(True, 'Looping through positions ...')
            self.ui.loopButton.setIcon(QIcon(PathManager.PausePngPath))
        else:
            QMessageBox.information(self, 'Scara in operation', 'Please wait until scara robot finishes current operation')
        
    # Clear Positions Button
    def Handle_Clear(self):
        if not self.inProgress:
            # Clear Table items and send to Scara
            self.ui.positionsTable.setRowCount(0)
            self.serialThread.sendData(Com.Clear)
        else:
            QMessageBox.information(self, 'Scara in operation', 'Please wait until scara robot finishes current operation')

    # Remove Position Button
    def Handle_Remove(self, row: int, _: int):
        if not self.inProgress:
            if QMessageBox.information(self, 'Confirm Delete', 'Are you sure you want to remove this position ?', QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
                # Remove row and send to Scara
                self.serialThread.sendData(self.ui.positionsTable.item(row, 0).text() + Com.Index + Com.Delete)
                self.ui.positionsTable.removeRow(row)
        else:
            QMessageBox.information(self, 'Scara in operation', 'Please wait until scara robot finishes current operation')

    # Item Clicked in table
    def Handle_Item(self, item: QTableWidgetItem):
        # Update previous item
        self.previousTableItem = item.text()

    # Change item in table
    def Handle_Change(self, item: QTableWidgetItem):
        if not self.inProgress:
            # Get Item Data
            text, row, column = item.text(), item.row(), item.column()
            self.inProgress = True
            
            # Order Edit
            if column == 0:
                if text.isdigit() and int(text)>0 and int(text)<=9:
                    # Loop through all values in column 0
                    for indexRow in range(self.ui.positionsTable.rowCount()):
                        tableItem = self.ui.positionsTable.item(indexRow, column)
                        if indexRow != row and tableItem.text() == text:
                            tableItem.setText(self.previousTableItem)
                    # Sort table and send new index
                    self.ui.positionsTable.sortItems(0, Qt.AscendingOrder)
                    self.serialThread.sendData(self.previousTableItem + Com.Index + text + Com.IndexChange)
                    self.previousTableItem = text
                else:
                    QMessageBox.information(self, 'Value Error', 'Please enter a valid order from 1 to 9')
                    item.setText(self.previousTableItem)
            
            # X / Y Position Edit
            elif column == 1 or column ==2:
                if re.match(r"^-?\d+$", text) and int(text)>=-365 and int(text)<=365:
                    x, y = int(self.ui.positionsTable.item(row, 1).text()), int(self.ui.positionsTable.item(row, 2).text())
                    success, theta1, theta2, phi = self.inverseKinematicsCalc(x, y)
                    # Update Previous Item if valid
                    if success:
                        self.serialThread.sendData(self.ui.positionsTable.item(row, 0).text() + Com.Index + str(theta1) + Com.FirstJointPosition + str(theta2) + Com.SecondJointPosition + str(phi) + Com.ThirdJointPosition + Com.EditPosition)
                        self.previousTableItem = text
                    elif not (x==365 and y==0):
                        QMessageBox.information(self, 'Range Error', 'Out of scara robot range')
                        item.setText(self.previousTableItem)
                else:
                    QMessageBox.information(self, 'Value Error', 'Please enter a valid value for X/Y from -365 to 365')
                    item.setText(self.previousTableItem)
            
            # Z Position Edit
            elif column == 3:
                if text.isdigit() and int(text)>=0 and int(text)<=150:
                    # Update Previous Item if valid
                    self.serialThread.sendData(self.ui.positionsTable.item(row, 0).text() + Com.Index + text + Com.Zposition + Com.EditPosition)
                    self.previousTableItem = text
                else:
                    QMessageBox.information(self, 'Value Error', 'Please enter a valid value for Z from 0 to 150')
                    item.setText(self.previousTableItem)
            
            # Gripper Edit
            elif column == 4:
                if text.isdigit() and int(text)>=0 and int(text)<=180:
                    # Update Previous Item if valid
                    self.serialThread.sendData(self.ui.positionsTable.item(row, 0).text() + Com.Index + text + Com.GripperValue + Com.EditPosition)
                    self.previousTableItem = text
                else:
                    QMessageBox.information(self, 'Value Error', 'Please enter a valid value for gripper from 0 to 180')
                    item.setText(self.previousTableItem)
            
            # Speed Edit
            elif column == 5:
                if text.isdigit() and int(text)>=500 and int(text)<=4000:
                    # Update Previous Item if valid
                    self.serialThread.sendData(self.ui.positionsTable.item(row, 0).text() + Com.Index + text + Com.SpeedValue + Com.EditPosition)
                    self.previousTableItem = text
                else:
                    QMessageBox.information(self, 'Value Error', 'Please enter a valid value for speed from 500 to 4000')
                    item.setText(self.previousTableItem)
            
            # Acceleration Edit
            elif column == 6:
                if text.isdigit() and int(text)>=500 and int(text)<=2000:
                    # Update Previous Item if valid
                    self.serialThread.sendData(self.ui.positionsTable.item(row, 0).text() + Com.Index + text + Com.AccelerationValue)
                    self.previousTableItem = text
                else:
                    QMessageBox.information(self, 'Value Error', 'Please enter a valid value for acceleration from 500 to 2000')
                    item.setText(self.previousTableItem)
            self.inProgress = False

    # Forward Kinematics
    def forwardKinematics(self, zLabel: bool = False):
        # Convert degrees to radians
        theta1 = math.radians(self.ui.firstJointSlider.value()) 
        theta2 = math.radians(self.ui.secondJointSlider.value())

        # Update Labels        
        self.ui.xPositionLineEdit.setText(str(math.ceil(228 * math.cos(theta1) + 136.5 * math.cos(theta1 + theta2))))
        self.ui.yPositionLineEdit.setText(str(math.ceil(228 * math.sin(theta1) + 136.5 * math.sin(theta1 + theta2))))
        if zLabel:
            self.ui.zPositionLineEdit.setText(str(self.ui.zPositionSlider.value()))

    # Inverse Kinematics Calculation
    def inverseKinematicsCalc(self, x: int, y: int) -> tuple[bool, int, int, int]:
        try:
            # Calculate angles in radians
            theta2 = math.acos((x**2 + y**2 - 70616.25) / (62244))
            theta2 = -theta2 if x < 0 and y < 0 else theta2
            theta1 = math.atan(x / (y+1e-9)) - math.atan((136.5 * math.sin(theta2)) / (228 + 136.5 * math.cos(theta2)))

            # Convert angles from radians to degrees
            theta2 = -theta2 * 180 / math.pi
            theta1 = theta1 * 180 / math.pi
            
            # Adjust theta1 based on quadrant
            theta1 = 90 - theta1 if (x >= 0 and y >= 0) or (x < 0 and y > 0) else 270 - theta1 if x < 0 and y < 0 else -90 - theta1 if x > 0 and y < 0 else 270 + theta1 if x < 0 and y == 0 else theta1
            
            # Calculate phi angle
            phi = -((90 + theta1 + theta2) if not (x < 0 and y < 0) else (270 - theta1 - theta2))        
            phi = phi if abs(phi) <= 165 else 180 + phi

            return True, int(round(theta1)), int(round(theta2)), int(round(phi)) 
        
        except:
            return False, x, y, x+y
    
    # Inverse Kinematics
    def inverseKinematics(self, zLabel: bool = False) -> bool:
        success, theta1, theta2, phi = self.inverseKinematicsCalc(int(self.ui.xPositionLineEdit.text()), int(self.ui.yPositionLineEdit.text()))
        # Update Labels
        if success:
            if self.isConnected:
                self.ui.firstJointValueLabel.setText(str(theta1))
                self.ui.secondJointValueLabel.setText(str(theta2))
                self.ui.thirdJointValueLabel.setText(str(phi))
                if zLabel:
                    self.ui.zPositionValueLabel.setText(self.ui.zPositionLineEdit.text())
                self.showForwardValuesAnimation(True)
            else:
                self.ui.firstJointSlider.setValue(theta1)
                self.ui.secondJointSlider.setValue(theta2)
                self.ui.thirdJointSlider.setValue(phi)
                if zLabel:
                    self.ui.zPositionSlider.setValue(int(self.ui.zPositionLineEdit.text()))
                self.showForwardValuesAnimation(False)
            # Indicate successful operation
            return True
        # Indicate math error
        else:
            return False
        
    # Home Position
    def homePosition(self):
        # Temporarily clear connection flag
        isConnected = self.isConnected
        self.isConnected = False
        # Set all positions to initial values
        self.ui.firstJointSlider.setValue(self.firstJointInitialValue)
        self.ui.secondJointSlider.setValue(self.secondJointInitialValue)
        self.forwardKinematics()
        self.ui.thirdJointSlider.setValue(self.thirdJointInitialValue)
        self.ui.zPositionSlider.setValue(self.zPositionInitialValue)
        self.inProgress = True
        self.ui.gripperSlider.setValue(self.gripperInitialValue)
        self.inProgress = False
        self.ui.speedSlider.setValue(self.speedInitialValue)
        self.ui.accelerationSlider.setValue(self.accelerationInitialValue)
        self.showForwardValuesAnimation(False)
        # Restore Connection Flag 
        self.isConnected = isConnected

    # Communication Animation
    def showComAnimation(self, isConnected: bool):
        if isConnected:
            # Update Connection Flag
            self.isConnected = True
            self.ui.comButton.setIcon(QIcon(PathManager.GreenPngPath))
            # Hide Port Frame
            if self.ui.portFrame.width():
                self.comAnimation.setStartValue(self.ui.portFrame.width())
                self.comAnimation.setEndValue(0) 
                self.comAnimation.start()
        else:
            # Update Connection Flag
            self.isConnected = False
            self.ui.comButton.setIcon(QIcon(PathManager.RedPngPath))
            # Show Port Frame
            if not self.ui.portFrame.width():
                self.comAnimation.setStartValue(0)
                self.comAnimation.setEndValue(self.ui.logoLabel.width())
                self.comAnimation.start()

    # Feedback Animation
    def showFeedbackAnimation(self, inProgress: bool = False, feedbackText: str = 'Motion Complete'):
        self.ui.feedbackLabel.setText(feedbackText)
        if inProgress:
            # Update Progress Flag
            self.inProgress = True
            # Disable Sliders
            self.ui.gripperSlider.setEnabled(False)
            self.ui.speedSlider.setEnabled(False)
            self.ui.accelerationSlider.setEnabled(False)
            # Show Animation Frame
            if not self.ui.animationFrame.height():
                self.feedbackAnimation.setStartValue(0)
                self.feedbackAnimation.setEndValue(self.ui.positionsFrame.height())
                self.feedbackAnimation.start()
        else:
            # Update Progress Flag
            self.inProgress = False
            # Enable Sliders
            self.ui.gripperSlider.setEnabled(True)
            self.ui.speedSlider.setEnabled(True)
            self.ui.accelerationSlider.setEnabled(True)
            # Hide Animation Frame
            if self.ui.animationFrame.height():
                self.feedbackAnimation.setStartValue(self.ui.animationFrame.height())
                self.feedbackAnimation.setEndValue(0)
                self.feedbackAnimation.start()
            else:
                QTimer.singleShot(100, lambda: self.showFeedbackAnimation(inProgress, feedbackText))

    # Slider Animation
    def showSliderButtonsAnimation(self, sliderIndex: int, showButtons: bool):
        if sliderIndex:
            # Get Reuired frame and animation
            frame, animation = {1: (self.ui.firstJointButtonsFrame, self.firstSliderAnimation), 2: (self.ui.secondJointButtonsFrame, self.secondSliderAnimation), 3: (self.ui.thirdJointButtonsFrame, self.thirdSliderAnimation), 4: (self.ui.zPositionButtonsFrame, self.zPositionSliderAnimation)}.get(sliderIndex)
            # Show Slider Buttons
            if showButtons and not frame.width():
                animation.setStartValue(0)
                animation.setEndValue(self.ui.firstJointRadio.width())
                animation.start()
            # Hide Slider Buttons
            elif not showButtons and frame.width():
                animation.setStartValue(frame.width())
                animation.setEndValue(0)
                animation.start()

    # Forward Values Animation
    def showForwardValuesAnimation(self, showFrame: bool):
        # Hide Forward Values Frame if all actual and current values are equal
        if showFrame and self.ui.actualFirstJointValueLabel.text() == self.ui.firstJointValueLabel.text() and self.ui.actualSecondJointValueLabel.text() == self.ui.secondJointValueLabel.text() and self.ui.actualThirdJointValueLabel.text() == self.ui.thirdJointValueLabel.text() and self.ui.actualZPositionValueLabel.text() == self.ui.zPositionValueLabel.text():
            self.showForwardValuesAnimation(False)
        # Show Forward Values Frame
        elif showFrame and not self.ui.forwadValuesFrame.width():
            self.forwardAnimation.setStartValue(0)
            self.forwardAnimation.setEndValue(self.ui.actualForwardValuesFrame.width())
            self.forwardAnimation.start()
        # Hide Forward Values Frame and set all actual values to be equal current values
        elif not showFrame and self.ui.forwadValuesFrame.width():
            self.ui.actualFirstJointValueLabel.setText(self.ui.firstJointValueLabel.text())
            self.ui.actualSecondJointValueLabel.setText(self.ui.secondJointValueLabel.text())
            self.ui.actualThirdJointValueLabel.setText(self.ui.thirdJointValueLabel.text())
            self.ui.actualZPositionValueLabel.setText(self.ui.zPositionValueLabel.text())
            self.forwardAnimation.setStartValue(self.ui.forwadValuesFrame.width())
            self.forwardAnimation.setEndValue(0)
            self.forwardAnimation.start()

    # Overriding close event to dispose camera
    def closeEvent(self, event: QCloseEvent):
        # Kill all threads
        self.serialThread.sendData(Com.StopMotion)
        self.portThread.terminate()
        self.serialThread.terminate()
        event.accept()

# Executing GUI
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ScaraRobot().show()
    app.exec()
