# Type help("robolink") or help("robodk") for more information
# Press F5 to run the script
# Documentation: https://robodk.com/doc/en/RoboDK-API.html
# Reference:     https://robodk.com/doc/en/PythonAPI/index.html
# Note: It is not required to keep a copy of this file, your python script is saved with the station
from robolink import *    # RoboDK API
from robodk import *      # Robot toolbox
RDK = Robolink()
#RDK.setRunMode(RUNMODE_MAKE_ROBOTPROG)

import csv

PROGRAM_NAME = "Simas"


# Get the robot item by name:
robot = RDK.Item('Staubli-RX160', ITEM_TYPE_ROBOT)
RDK.ProgramStart(PROGRAM_NAME, "", "", robot)
robot.setSpeedJoints(200)
robot.setSpeed(200)
#robot.ConnectSafe(robot_ip='192.168.0.254', max_attempts=5, wait_connection=4, callback_abort=None)
# state = robot.Connect()
# print(state)   
robot.setJoints([0,0,0,0,0,0])
# joints = robot.Joints().list()
# print(joints)
# # Check the connection status and message
# state, msg = robot.ConnectedState()
# print(state)
# print(msg)
#pose_ref = robot.Pose()
# Get the reference target by name:
#target = RDK.Item('Target 1')
#target_pose = target.Pose()
#xyz_ref = target_pose.Pos()

# Move the robot to the reference point:
#robot.MoveJ(target)

# Draw a hexagon around the reference target:
# strfile = "/home/opit/Desktop/hackerspace/projects/Staubli/Simo kadrai/robot_axes.csv"

# csvdata = LoadList(strfile, ',')
# values = []
# for i in range(len(csvdata)):
#     print(csvdata[i])
#     values.append(csvdata[i])
#     robot.setJoints(csvdata[i]) 
# exit()   

with open("/home/opit/Desktop/hackerspace/projects/Staubli/Simo kadrai/robot_axes.csv", "r") as f:
     reader = csv.reader(f, delimiter="\t")
     for i, line in enumerate(reader):
          #robot.waitDI(1,1)
          #robot.Pause(500)
          print([float(joint) for joint in line])
          robot.MoveJ([float(joint) for joint in line])
			#joints = robot.Joints().list()
			#print(joints)
