#!/usr/bin/env python
import time
import binascii
import sys
import itertools
import csv
import struct
import socket

frame = int(sys.argv[1])
#Attention: frames are numbered starting with 1, as in Dragonframe.


fileName = "/home/opit/Desktop/hackerspace/projects/Staubli/test/robot_axes.csv"
TCP_IP = ''
TCP_PORT = 11000
BUFFER_SIZE = 64
PREFIX = 8 
HEADER1 = 11
HEADER2 = 2
HEADER3 = 0
SEQUENCE = 0
dummy_joint = 0 
vel = 1.
dur = 999

DFControl = True
manualControl = False
demoLoop = False

def setPos():
	#return [10, 10, 15, 30, 60, 50]
	return [1, 2, 3, 4, 5, 6]

def from_binary(msg):
	#print("size", struct.calcsize(msg))
	print(repr(msg))
	return struct.unpack('I', msg)

def float_to_hex(f):
	#print(f)
	return hex(struct.unpack('<L', struct.pack('<f', f))[0])

def getDFPos(frame):
	with open(fileName, 'r') as f:
		print " frame no. ",frame
		s = next(itertools.islice(csv.reader(f, delimiter ='\t'), frame-1, None))
		return [float(joint) for joint in s]
		
def getFileLength(fileName):
	input_file = open(fileName,"r+")
	reader_file = csv.reader(input_file)
	return len(list(reader_file))
	input_file.close()
		



#https://pymotw.com/2/socket/binary.html
coordLength = getFileLength(fileName)

def sendMsg(joint_pos, dummy_joint, PREFIX, HEADER1, HEADER2, HEADER3, SEQUENCE, vel, dur):
	msg = (PREFIX, HEADER1, HEADER2, HEADER3, SEQUENCE, joint_pos[0], joint_pos[1], joint_pos[2], joint_pos[3], joint_pos[4], joint_pos[5], dummy_joint, dummy_joint, dummy_joint, dummy_joint, vel, dur)
	packer = struct.Struct('I I I I I f f f f f f f f f f f f')
	packed_data = packer.pack(*msg)
	#print('sending "%s"' % binascii.hexlify(packed_data), msg)
	print(msg)
	a.sendall(packed_data)


def setZeroPos():
	return [0, 0, 0, 0, 0, 0]

def makeDemoLoop(times):
 for i in range(0, times):
 	joint_pos = setZeroPos()
 	sendMsg(joint_pos, dummy_joint, PREFIX, HEADER1, HEADER2, HEADER3, SEQUENCE, vel, dur)
 	time.sleep(1)
 	joint_pos = setPos()
 	sendMsg(joint_pos, dummy_joint, PREFIX, HEADER1, HEADER2, HEADER3, SEQUENCE, vel, dur)
 	time.sleep(1)
	

# log_file = open("/home/opit/Desktop/hackerspace/projects/Staubli/test/messages.log","a")
# log_file.write(str(frame)+"\n")
# log_file.write("Not connected\n")
# log_file.close()


time.sleep(3) #time to run to the robot 
a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
a.connect((TCP_IP, TCP_PORT))


if DFControl:
	if (frame > 0 & frame < coordLength+1):
		for i in range(1, frame+1):
			joint_pos = getDFPos(i)
			print(joint_pos)
			sendMsg(joint_pos, dummy_joint, PREFIX, HEADER1, HEADER2, HEADER3, SEQUENCE, vel, dur)
			
			for i in range(0, 4):
				data = a.recv(BUFFER_SIZE)
			#	print(data)
			#	print("ack")
				print(from_binary(data)) #unpack() always returns a tuple
			#	print("ack")
			time.sleep(0.2)
		
elif manualControl:
	#joint_pos = getDFPos(frame)
	#joint_pos = setPos()
	joint_pos = setZeroPos()
	sendMsg(joint_pos, dummy_joint, PREFIX, HEADER1, HEADER2, HEADER3, SEQUENCE, vel, dur)

elif demoLoop:
	makeDemoLoop(frame)
else:
	print("Select motion control method!")	


time.sleep(2)
a.close()




