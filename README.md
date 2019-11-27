# Staubli
Python scripts for Staubli RX160

Hack and Tell talk: https://github.com/Technariumas/Staubli/blob/master/hnt.pdf

Robot simulation: https://vimeo.com/364303191
Real motion: https://vimeo.com/364303376

Instrukcijos, kaip dirbti su robotu ir Dragonframe'u: https://github.com/Technariumas/Staubli/blob/master/DF_instructions.md

Uploading a VAL3 code directory recursively: 

ncftp -u maintenance <IP>
  
  
mput -r <dir>  

TODOs:
+ check timestamps b/ween adjacent positions

-- adjust socket timeout robot-side

+ safe trajectory 

+ filename check: filenames are corresponding (AFAIK) to Dragonframe project settings as PROJECT_PREFIX+"SC"+scene+"SH"+take+".csv".

+ read robot message

+ send ack from robot to Dragonframe when movement is finished
