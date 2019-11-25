#!/usr/bin/env python
import time
import binascii
import sys, errno
import itertools
import csv
import struct
import socket
import config
import signal


frame = int(sys.argv[1])
prod = sys.argv[2]
scene = sys.argv[3]
#Attention: frames are numbered starting with 1, as in Dragonframe.

TCP_IP = '0.0.0.0' #config.properties['IP']
TCP_PORT = int(config.properties['TCP_PORT'])
PROJECT_PATH = config.properties['PROJECT_PATH']
PROJECT_PREFIX = str(prod)
fileName = PROJECT_PATH+prod+"_"+scene+".csv"
BUFFER_SIZE = 16
PREFIX = 8 
HEADER1 = 11
HEADER2 = 2
HEADER3 = 0
SEQUENCE = 0
dummy_joint = 0 
vel = 1.
dur = 999
move_delay = 0.6 	
DFControl = True


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


#https://pymotw.com/2/socket/binary.html



class GracefulKiller:
  kill_now = False
  def __init__(self):
    # register the signals to be caught
    signal.signal(signal.SIGHUP, self.exit_gracefully)
    #signal.signal(signal.SIGINT, self.exit_gracefully)
    signal.signal(signal.SIGQUIT, self.exit_gracefully)
    signal.signal(signal.SIGILL, self.exit_gracefully)
    signal.signal(signal.SIGTRAP, self.exit_gracefully)
    signal.signal(signal.SIGABRT, self.exit_gracefully)
    signal.signal(signal.SIGBUS, self.exit_gracefully)
    signal.signal(signal.SIGFPE, signal.SIG_IGN)
    #signal.signal(signal.SIGKILL, receiveSignal)
    signal.signal(signal.SIGUSR1, self.exit_gracefully)
    signal.signal(signal.SIGSEGV, self.exit_gracefully)
    signal.signal(signal.SIGUSR2, self.exit_gracefully)
    signal.signal(signal.SIGPIPE, self.exit_gracefully)
    signal.signal(signal.SIGALRM, self.exit_gracefully)
    signal.signal(signal.SIGTERM, self.exit_gracefully)
    

  def exit_gracefully(self,signum, frame):
    #self.kill_now = True
    with open(PROJECT_PATH+'log.txt','ab') as f:
    	f.write("Sig: "+str(signum)+"\n")  #saving the set frame
    	f.close()	


#time.sleep(3) #time to run to the robot 
a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
a.connect((TCP_IP, TCP_PORT))
			

			

def log(msg):
	with open(PROJECT_PATH+'log.txt','ab') as f:				
		f.write(str(msg)+"\n") 
		f.close()

def getCurrPos():
	f = open(PROJECT_PATH+"current_pos.csv", "r")
	start = int(f.read())
	f.close()
	return start

def setCurrPos(frame):
	with open(PROJECT_PATH+'current_pos.csv','wb') as f:
		f.write(str(frame))  #saving the set frame
		f.close()


def sendMsg(joint_pos, dummy_joint, PREFIX, HEADER1, HEADER2, HEADER3, SEQUENCE, vel, dur):
	msg = [PREFIX, HEADER1, HEADER2, HEADER3, SEQUENCE, joint_pos[0], joint_pos[1], joint_pos[2], joint_pos[3], joint_pos[4], joint_pos[5], dummy_joint, dummy_joint, dummy_joint, dummy_joint, vel, dur]
	#packer = struct.Struct('I I I I I f f f f f f f f f f f f')
	#packed_data = packer.pack(*msg)
	#print('sending "%s"' % binascii.hexlify(packed_data), msg)
	out = ''.join(map(str, msg))
	print(out, "msg")
	return out #packed_data

if __name__ == "__main__":
		state = 'init'
		killer = GracefulKiller()
		coordLength = getFileLength(fileName)
		end = frame
		start = getCurrPos()
		curr_frame = start		
		if (abs(start - end) >= coordLength+1):
			log("Wrong trajectory or file, trajectory length: "+ str(abs(start - end)) + " File length: "+str(coordLength))
			state = 'fail'
		else:
			state = 'initMotion'
		log("DF cmd received")	
		if state == 'initMotion':
			time.sleep(30)				
			while (curr_frame<>end):
				print("current frame: ", curr_frame)
				if (start < end):
						if (curr_frame < end):
							curr_frame = curr_frame + 1
				elif (start > end):
						if (curr_frame > end):
							curr_frame = curr_frame - 1
				state = "getDFPos"		
				if state == 'getDFPos':
					if (curr_frame > 0 & curr_frame < coordLength+1):
						joint_pos = getDFPos(curr_frame) #TODO: handle IOError
						print("joints: ",joint_pos)



						state = 'sendCommand'
					else:
						log("Frame outside bounds")
						state == 'fail'				
				if state == 'sendCommand':
					try:
						a.sendall("goto "+str(curr_frame))
						state = 'recvCommand'
					except IOError as e:
						state='fail'
						log(str(e))
				if state == 'recvCommand':
					try:
						data = a.recv(BUFFER_SIZE) #TODO: handle robot error message
						print("Robot has arrived to a point")
						setCurrPos(str(curr_frame))
						state = 'initMotion'
						#a.close()						
					except IOError as e:
						state='fail'
						log(str(e))
			if state == 'fail':
				log("failed state")			

	


	



