#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.nxtdevices import LightSensor 

# General constantss
DRIVE_SPEED = 400#300       # Base driving speed
stopwatch = StopWatch() # Timer for differential part

# Create EV3 brick object
ev3 = EV3Brick()

# Initialize motors
left_motor = Motor(Port.A) 
right_motor = Motor(Port.D)

#INITIALISE DRIVEBASE
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=150)

# Initialize touch sensor
touch_sensor = TouchSensor(Port.S1)

# Signal start of the program
ev3.speaker.beep()

# Start the stopwatch
stopwatch.reset()

#While the touch sensor is not pressed, drive forward
while not touch_sensor.pressed() and stopwatch.time() < 15000:
    robot.drive(DRIVE_SPEED, 0)
    #left_motor.run(DRIVE_SPEED)
    #right_motor.run(DRIVE_SPEED)

# Stop the motors when we reach the end of the line
robot.stop()
#left_motor.stop()
#right_motor.stop()

# Stop the stopwatch
time = stopwatch.time()

# Print the time it took
if time >= 15000:
    print("Time limit reached. DNF!")
else:
    print("Completion time: ", time)