"""
IN1 = 26
IN2 = 18
IN3 = 19
IN4 = 23
"""

from machine import Pin
import time

class SteppingMotor():
    # Defining the constants
    _PIN1 = 26
    _PIN2 = 18
    _PIN3 = 19
    _PIN4 = 23
    
    SINGLE_PHASE_FORWARD  = 0
    SINGLE_PHASE_BACKWARD = 1
    DOUBLE_PHASE_FORWARD  = 2
    DOUBLE_PHASE_BACKWARD = 3
    HALF_STEP_FORWARD     = 4
    HALF_STEP_BACKWARD    = 5
    
    def __init__(self, p1=_PIN1, p2=_PIN2, p3=_PIN3, p4=_PIN4):
        self.pin_1 = Pin(p1, Pin.OUT)
        self.pin_2 = Pin(p2, Pin.OUT)
        self.pin_3 = Pin(p3, Pin.OUT)
        self.pin_4 = Pin(p4, Pin.OUT)
        self._mode = 0
        
    def _clrAll(self):
        self.pin_1.value(0)
        self.pin_2.value(0)
        self.pin_3.value(0)
        self.pin_4.value(0)
        
    def _singlePhaseForward(self, steps):
        # Single phase pattern        
        pattern = [
            [1,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
            [0,0,0,1]
            ]
        for i in range(steps):
            for j in range(4):
                for k in range(4):
                    self.pin_1.value(pattern[j][0])
                    self.pin_2.value(pattern[j][1])
                    self.pin_3.value(pattern[j][2])
                    self.pin_4.value(pattern[j][3])
                    time.sleep_ms(1)
        self._clrAll()
        
    def _singlePhaseBackward(self, steps):
        # Single phase pattern        
        pattern = [
            [0,0,0,1],
            [0,0,1,0],
            [0,1,0,0],
            [1,0,0,0]    
            ]
        for i in range(steps):
            for j in range(4):
                for k in range(4):
                    self.pin_1.value(pattern[j][0])
                    self.pin_2.value(pattern[j][1])
                    self.pin_3.value(pattern[j][2])
                    self.pin_4.value(pattern[j][3])
                    time.sleep_ms(1)
        self._clrAll()
        
    def _doublePhaseForward(self, steps):
        # Single phase pattern        
        pattern = [
            [1,1,0,0],
            [0,1,1,0],
            [0,0,1,1],
            [1,0,0,1]
            ]
        for i in range(steps):
            for j in range(4):
                for k in range(4):
                    self.pin_1.value(pattern[j][0])
                    self.pin_2.value(pattern[j][1])
                    self.pin_3.value(pattern[j][2])
                    self.pin_4.value(pattern[j][3])
                    time.sleep_ms(1)
        self._clrAll()
        
    def _doublePhaseBackward(self, steps):
        # Single phase pattern        
        pattern = [
            [0,0,1,1],
            [0,1,1,0],
            [1,1,0,0],
            [1,0,0,1]
            ]
        for i in range(steps):
            for j in range(4):
                for k in range(4):
                    self.pin_1.value(pattern[j][0])
                    self.pin_2.value(pattern[j][1])
                    self.pin_3.value(pattern[j][2])
                    self.pin_4.value(pattern[j][3])
                    time.sleep_ms(1)
        self._clrAll()
        
    def _halfStepForward(self, steps):
        # Single phase pattern        
        pattern = [
            [1,0,0,0],
            [1,1,0,0],
            [0,1,0,0],
            [0,1,1,0],
            [0,0,1,0],
            [0,0,1,1],
            [0,0,0,1],
            [1,0,0,1]
            ]
        for i in range(steps):
            for j in range(8):
                for k in range(4):
                    self.pin_1.value(pattern[j][0])
                    self.pin_2.value(pattern[j][1])
                    self.pin_3.value(pattern[j][2])
                    self.pin_4.value(pattern[j][3])
                    time.sleep_ms(1)
        self._clrAll()
        
    def _halfStepBackward(self, steps):
        # Single phase pattern        
        pattern = [
            [0,0,0,1],
            [0,0,1,1],
            [0,0,1,0],
            [0,1,1,0],
            [0,1,0,0],
            [1,1,0,0],
            [1,0,0,0],            
            [1,0,0,1]
            ]
        for i in range(steps):
            for j in range(8):
                for k in range(4):
                    self.pin_1.value(pattern[j][0])
                    self.pin_2.value(pattern[j][1])
                    self.pin_3.value(pattern[j][2])
                    self.pin_4.value(pattern[j][3])
                    time.sleep_ms(1)
        self._clrAll()
        
    def stepMode(self, mode=None):
        if not mode:
            if self._mode == 0:
                return "(0) Motor is in single phase forward mode"
            if self._mode == 1:
                return "(1) Motor is in single phase backward mode"
            if self._mode == 2:
                return "(2) Motor is in double phase forward mode"
            if self._mode == 3:
                return "(3) Motor is in double phase backward mode"
            if self._mode == 4:
                return "(4) Motor is in half step forward mode"
            if self._mode == 5:
                return "(5) Motor is in half step backward mode"
        elif ((mode < 0) or (mode > 5)):
            return "Mode range is 0 to 5"
        elif (type(mode) != int):
            return "Mode must be an integer (From 0 to 5)"
        else:
            self._mode = mode
            
    def move(self, noOfSteps):
        print ("Moving", noOfSteps, "steps...")
        if self._mode == 0:
            self._singlePhaseForward(noOfSteps)
        if self._mode == 1:
            self._singlePhaseBackward(noOfSteps)
        if self._mode == 2:
            self._doublePhaseForward(noOfSteps)
        if self._mode == 3:
            self._doublePhaseBackward(noOfSteps)
        if self._mode == 4:
            self._halfStepForward(noOfSteps)
        if self._mode == 5:
            self._halfStepBackward(noOfSteps)
            
        
motor = SteppingMotor()
print(motor.stepMode(5))
motor.move(400)

