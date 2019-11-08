#!/bin/bash
#
# Rename file from dragonframe_script.sh.txt to dragonframe_script.sh
# then run 'chmod u+x dragonframe_script.sh' to make it executable.
#
# In Dragonframe, go to the Advanced tab of Preferences
# and choose this file for Action Script.
#
# Example script showing input arguments
#  arguments should be obvious, except "Action"
#  which can be one of the following:
#
# "POSITION" is sent whenever Dragonframe moves to a new frame.
#   This is probably what you want to use. After shooting 
#   frame 10, when Dragonframe is ready to capture frame 11, it
#   sends "POSITION 11".
#
# "SHOOT" happens immediately before shooting.
#
# "DELETE" happens immediately before deleting.
#
# "CC" is capture complete. There is an additional argument,
#   the file name of the main downloaded image.
#
# "FC" is frame complete. There is an additional argument,
#   the file name of the main downloaded image.
#
# "TEST" is test shot complete. There is an additional argument,
#   the file name of the main downloaded image.

# "EDIT" means a timeline edit (cut/copy/paste frames) is
#   complete.
#
# "CONFORM" means a conform edits is complete.
#

echo "Dragonframe Script"

#echo "Production : $1" >> /home/opit/Desktop/hackerspace/projects/Staubli/test/dragonframe_script_log.txt
#echo "Scene      : $2" >> /home/opit/Desktop/hackerspace/projects/Staubli/test/dragonframe_script_log.txt
#echo "Take       : $3" >> /home/opit/Desktop/hackerspace/projects/Staubli/test/dragonframe_script_log.txt
#echo "Action     : $4" >> /home/opit/Desktop/hackerspace/projects/Staubli/test/dragonframe_script_log.txt
#echo "Frame      : $5" >> /home/opit/Desktop/hackerspace/projects/Staubli/test/dragonframe_script_log.txt
#echo "Exposure   : $6" >> /home/opit/Desktop/hackerspace/projects/Staubli/test/dragonframe_script_log.txt
#echo "Exp. Name  : $7" >> /home/opit/Desktop/hackerspace/projects/Staubli/test/dragonframe_script_log.txt
#echo "Filename   : $8" >> /home/opit/Desktop/hackerspace/projects/Staubli/test/dragonframe_script_log.txt


if [ "$4" == "POSITION" ]
then
echo "$5" >> /home/opit/Desktop/hackerspace/projects/Staubli/test/log.txt
#SCRIPT_PATH="/home/opit/Desktop/hackerspace/projects/Staubli/test/DF.py" 
#PYTHON="/usr/bin/python" 
#$PYTHON $SCRIPT_PATH $5
fi


if [ "$4" == "EDIT" ]
then

echo "EDIT $5-$6-$7-$8" >> ~/dragonframe_script_log_edit.txt

fi

#
#if [ "$4" == "CC" ]
#then

#echo "CC $5-$6 -> $8" >> /home/opit/Desktop/hackerspace/projects/Staubli/test/dragonframe_script_log.txt

#fi

#if [ "$4" == "FC" ]
#then

#echo "FC $5-$6" >> /home/opit/Desktop/hackerspace/projects/Staubli/test/dragonframe_script_log.txt

#fi

#if [ "$4" == "EDIT" ]
#then

#echo "EDIT $5-$6" >> /home/opit/Desktop/hackerspace/projects/Staubli/test/dragonframe_script_log.txt

#fi


