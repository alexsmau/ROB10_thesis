#!/usr/bin/env python3

from locomotion_modes import LocomotionMode
from rover import Rover
from rover_2 import Rover2
import math


rover = Rover()
rover.setLocomotionMode(1)

rover2 = Rover2()
rover2.setLocomotionMode(1)

driving_command = 50
steering_command = 12
print (rover.joystickToSteeringAngle(driving_command, steering_command))

print (rover.joystickToVelocity(driving_command, steering_command))