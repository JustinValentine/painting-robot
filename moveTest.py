from robot import Robot
from time import *
from kinematics import ForwardKinematics, InverseKinematics
from inverse_kin import pose_for_location
import numpy as np


arm = Robot()

origin = [-8.35, 0, 2.4] 

joints = [[4.05, 0, 6], [9, 0, 0], [-0.85, 0, 2.165],
        [15.8, 0, 0], [1.825, 0, 0.85], [1, -6.75, 0]]

kin = ForwardKinematics(joints, origin)


physical_angles = [90, 150, 140, 98, 75, 0] # true acuator angles used to drive the model 
physical_angles = [90, 117, 105, 98, 73, 85] # 105

physical_angles = [90, 117, 105, 98, 73, 85] # 105



physical_angles = [np.radians(i) for i in physical_angles]


B = kin.jointLimitsPhysical(physical_angles)

print(B)


# physical_angles = [np.radians(i) for i in [90, 100, 170, 98, 75, 0]]


logical_angles = kin.physicalToLogicalAngles(physical_angles) # the angles used in the serial linkage model

arm.move2pose(logical_angles)

def goto_phys(angles):
    angles = [np.radians(i) for i in angles]
    logical_angles = kin.physicalToLogicalAngles(angles)
    arm.move2pose(logical_angles)
    sleep(1)
    arm.print_status()

def goto_logical(angles):
    angles = [np.radians(i) for i in angles]
    arm.move2pose(angles)
    sleep(1)
    arm.print_status()

# goto_phys([90, 100, 170, 98, 75, 0])

# moves = [[160, 116, 132, 90, 75, 95], [157, 120, 170, 90, 120, 95], [157, 90, 180, 90, 120, 95], [20, 116, 132, 90, 75, 95], [17, 120, 170, 90, 120, 95], [17, 90, 180, 90, 120, 95]]
# moves = []

# sleep(1)
# arm.dipPaint()

# for move in moves:
#         physical_angles = [np.radians(i) for i in move]

#         logical_angles = kin.physicalToLogicalAngles(physical_angles) # the angles used in the serial linkage model

#         arm.move2pose(logical_angles)
#         print(move)
#         sleep(0.3)
# physical_angles = [90, 100, 90, 98, 68, 0] # true acuator angles used to drive the model 

# physical_angles = [np.radians(i) for i in physical_angles]

# arm.move2pose(physical_angles, physical=True)

# arm = Robot()

# physical_angles = [1.570, 2.443, 2.094, 1.570, 2.792, 3.141] # ture acuator angles used to drive the model 
# logical_angles = kin.physicalToLogicalAngles(physical_angles)

# Output = ["%.2f" % np.degrees(elem) for elem in physical_angles]
# print("start_logical: ", Output)

# physical = kin.logicalToPhysicalAngles(logical_angles)

# Output = ["%.2f" % np.degrees(elem) for elem in physical]
# print("start_physical: ", Output)

# Output = ["%.2f" % np.degrees(elem) for elem in physical_angles]
# print("start_physical_real: ", Output)


# start_pose = logical_angles
# goal = np.array([-3, 14.5, 3])


# logical = pose_for_location(kin, start_pose, goal)

# physical = kin.logicalToPhysicalAngles(logical)


# # Output = ["%.2f" % np.degrees(elem) for elem in logical]
# # print("move to: ", Output)

# Output = ["%.2f" % np.degrees(elem) for elem in physical]
# print("move to: ", Output)

# user = input("start: ")

# arm.move2pose(physical)

#      #116.4
# # pose = [1.571, 1.571, 1.571, 1.571, 2.793, 1.571]

# pose = [np.radians(pose[i]) for i in range(6)]


# arm.move2pose(pose)

# origin = [-8.35, 0, 2.6] 

# # cheack [4.05, 0, 6.25]

# # joints = [[4.05, 0, 6.25], [0, 0, 9], [-0.85, 0, 2.165],
# #           [15.8, 0, 0], [1.825, 0, 0.85], [0, 0, 0]]

# joints = [[4.05, 0, 6.75], [9, 0, 0], [-2.165, 0, 0.85],
#           [15.8, 0, 0], [1.825, 0, 0.85], [1.55, 0, -6.75]]


# kin = ForwardKinematics(joints, origin)

# logical = kin.physicalToLogicalAngles(pose)
# Output = ["%.2f" % np.degrees(elem) for elem in logical]
# print("logical: ", Output)


# physical = kin.logicalToPhysicalAngles(logical)
# Output = ["%.2f" % np.degrees(elem) for elem in physical]
# print("physical: ", Output)

# pos = kin.getPos(logical)
# print("cord: ", pos[0:3])


# physical = kin.logicalToPhysicalAngles(logical)
# Output = ["%.2f" % np.degrees(elem) for elem in physical]
# print(Output)

# test_pose = kin.logicalToPhysicalAngles(pose_new)


# user = input("stop: ")

# arm.stopRobot()
