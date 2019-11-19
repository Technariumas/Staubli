#!/usr/bin/env python
import time
import binascii
import sys
import itertools
import csv
import struct
import socket
import config

frame = int(sys.argv[1])
scene = sys.argv[3]
prod = sys.argv[2]
#Attention: frames are numbered starting with 1, as in Dragonframe.

TCP_IP = config.properties['IP']
TCP_PORT = int(config.properties['TCP_PORT'])
PROJECT_PATH = config.properties['PROJECT_PATH']
PROJECT_PREFIX = str(prod)
fileName = PROJECT_PATH+prod+"_"+scene+".csv"
print(fileName)
BUFFER_SIZE = 4
PREFIX = 8 
HEADER1 = 11
HEADER2 = 2
HEADER3 = 0
SEQUENCE = 0
dummy_joint = 0 
vel = 1.
dur = 999
move_delay = 0.5
DFControl = True
manualControl = False
demoLoop = False

def setPos():
	#return [10, 10, 15, 30, 60, 50]
	return [1, 2, 3, 4, 5, 6]

def from_binary(msg):
	#print("size", struct.calcsize(msg))
	#print(repr(msg))
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
			



#https://pymotw.com/2/socket/binary.html
coordLength = getFileLength(fileName)
#coordLength = 2 #for testing safety

def sendMsg(joint_pos, dummy_joint, PREFIX, HEADER1, HEADER2, HEADER3, SEQUENCE, vel, dur):
	msg = (PREFIX, HEADER1, HEADER2, HEADER3, SEQUENCE, joint_pos[0], joint_pos[1], joint_pos[2], joint_pos[3], joint_pos[4], joint_pos[5], dummy_joint, dummy_joint, dummy_joint, dummy_joint, vel, dur)
	packer = struct.Struct('I I I I I f f f f f f f f f f f f')
	packed_data = packer.pack(*msg)
	print('sending "%s"' % binascii.hexlify(packed_data), msg)
	#print(msg)
	a.sendall(packed_data)

f = open(PROJECT_PATH+"current_pos.csv", "r")
start = int(f.read())
f.close()
#time.sleep(3) #time to run to the robot 
a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
a.connect((TCP_IP, TCP_PORT))


def goto(frame):
	print("goto ", frame)
	if (frame > 0 & frame < coordLength+1):
		joint_pos = getDFPos(frame)
		print("joints: ",joint_pos)
		sendMsg(joint_pos, dummy_joint, PREFIX, HEADER1, HEADER2, HEADER3, SEQUENCE, vel, dur)	
		ret = 0
		msg = [0]*17
		for i in range(0, 17):
		 	data = a.recv(BUFFER_SIZE)
		 	msg[i] = from_binary(data)[0]
		print("msg: ", msg) 	
	 	ret = msg[3]
	 	#print(ret)
	 	#print(msg)
	 	#exit()
		if (ret == 1):
		 	print("Robot has arrived to a point")
		 	time.sleep(0.1)
			with open(PROJECT_PATH+'current_pos.csv','wb') as f:
				f.write(str(frame))  #saving the set frame, TODO: move after robot ack
				f.close()
			with open('/home/opit/Desktop/hackerspace/projects/Staubli/Staubli/log.txt','ab') as f:
				f.write("Step to: "+str(frame)+"\n")  #saving the set frame
				f.close()
		
		else:
			print("Robot is stuck, ret = ", ret)
			with open('/home/opit/Desktop/hackerspace/projects/Staubli/Staubli/log.txt','ab') as f:
				f.write("Robot is stuck at: "+str(frame)+"\n")  #saving the set frame
				f.close()
 	
		return ret		


if DFControl:
	end = frame
	curr_frame = start
	print(end, curr_frame)
	
	if (abs(start - end) >= coordLength+1):
		print("Wrong trajectory or file, trajectory length: ", abs(start - end))
	else:
		if (start < end):
			while (curr_frame < end):
				curr_frame = curr_frame + 1
				ret = goto(curr_frame)
				print(curr_frame)
				time.sleep(move_delay)
				if (ret!=1):
					break
		elif (start > end):
			while (curr_frame > end):
				curr_frame = curr_frame - 1
				ret = goto(curr_frame)	
				print(curr_frame)
				time.sleep(move_delay)				
				if (ret!=1):
					break
		elif (start == end):
			print("Same point")
			ret = goto(curr_frame)
			time.sleep(move_delay)				

		
elif manualControl:
	#joint_pos = getDFPos(frame)
	#joint_pos = setPos()
	joint_pos = setZeroPos()
	sendMsg(joint_pos, dummy_joint, PREFIX, HEADER1, HEADER2, HEADER3, SEQUENCE, vel, dur)

elif demoLoop:
	makeDemoLoop(frame)
else:
	print("Select motion control method!")	
#time.sleep(0.5)
a.shutdown(socket.SHUT_WR)
a.close()




