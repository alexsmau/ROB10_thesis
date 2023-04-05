#!/usr/bin/env python3

import math

"""
    Compute the steering angles and angular velocities for the wheels.

    lin_vel: linear velocity in meters per second
    ang_vel: angular velocity in radians per second
"""
def Ackerman_drive(lin_vel, ang_vel):
    # Define the static variables
    wheel_radius = 0.1
    wheel_diameter = 2 * math.pi * wheel_radius

    # The offset is defined as pairs of dX and dY
    wheel_offsets = [[-0.385, 0.438],   # FL
                    [0.385, 0.438],     # FR
                    [-0.447, 0.0],      # ML
                    [0.447, 0.0],       # MR
                    [-0.385, -0.411],   # RL
                    [0.385, -0.411]]    # RR

    steering_angles = [0] * len(wheel_offsets)
    angular_velocity = [0] * len(wheel_offsets)

    if ang_vel != 0:
        # Calculate the turning radius
        turn_radius = abs(lin_vel / ang_vel)

        sign = 1 
        if ang_vel < 0: 
            sign = -1

        index = 0
        for offset_pair in wheel_offsets:
            dX = turn_radius - offset_pair[0]
            steering_angles[index] = math.atan2(offset_pair[1], dX) * sign
            index = index + 1

        # Calculate the linar velocity of the wheels.

        # Calculate the amount of time to turn 45 degrees based on the anglar
        # velocity.
        t = math.pi / (2 * abs(ang_vel))

        direction = 1      # forward
        if lin_vel < 0:
            direction = -1 # backwards

        index = 0
        for offset_pair in wheel_offsets:
            radius = math.sqrt((turn_radius - offset_pair[0])**2 + (offset_pair[1])**2)
            wheel_vel = (math.pi * radius) / (2 * t)
            angular_velocity[index] = (wheel_vel / wheel_diameter) * direction
            index = index + 1
    else:
        # No angular velocity. Go stragit ahead.
        index = 0
        for offset_pair in wheel_offsets:
            angular_velocity[index] = lin_vel / wheel_diameter
            index = index + 1

    return steering_angles, angular_velocity



steering_angles, angular_velocity = Ackerman_drive(-1, -0.3)

print(steering_angles)
steering_angles_deg = list(map(lambda x: math.degrees(x), steering_angles))
print(steering_angles_deg)

indexes = [0,1,4,5]
steering_angles_deg = list(map(lambda x: steering_angles_deg[x], indexes))
print(steering_angles_deg)

print(angular_velocity)

    



