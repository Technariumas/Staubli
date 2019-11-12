# Staubli
Python scripts for Staubli RX160

Hack and Tell talk: https://github.com/Technariumas/Staubli/blob/master/hnt.pdf

Robot simulation: https://vimeo.com/364303191
Real motion: https://vimeo.com/364303376

Uploading a VAL3 code directory recursively: 


ncftp -u maintenance <IP>
  
  
mput -r <dir>  

TODOs:
+ check timestamps b/ween adjacent positions

-- adjust socket timeout robot-side

+ safe trajectory 

-- filename check if needed

+ read robot message

+ send ack from robot to Dragonframe when movement is finished
