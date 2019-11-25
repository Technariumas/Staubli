@echo off

REM
REM In Dragonframe, go to the Advanced tab of Preferences
REM and choose this file for Action Script.
REM
REM Example script showing input arguments
REM  arguments should be obvious, except "Action"
REM  which can be one of the following:
REM
REM "POSITION" is sent whenever Dragonframe moves to a new frame.
REM   This is probably what you want to use. After shooting 
REM   frame 10, when Dragonframe is ready to capture frame 11, it
REM   sends "POSITION 11".
REM
REM "SHOOT" happens immediately before shooting.
REM
REM "DELETE" happens immediately before deleting.
REM
REM "CC" is capture complete. There is an additional argument,
REM   the file name of the main downloaded image.
REM
REM "FC" is frame complete. There is an additional argument,
REM   the file name of the main downloaded image.
REM
REM "TEST" is test shot complete. There is an additional argument,
REM   the file name of the main downloaded image.
REM
REM "EDIT" means a timeline edit (cut/copy/paste frames) is
REM   complete.
REM
REM "CONFORM" means a conform edits is complete.

echo Dragonframe Script

echo Production    : %1
echo Scene         : %2
echo Take          : %3
echo Action        : %4
echo Frame         : %5
echo Exposure      : %6
echo Exposure Name : %7
echo Image Path    : %8

if "%4" == "POSITION" (
    echo Move to frame %5 >> %HOMEPATH%\dragonframe_script_log.txt
)

if "%4" == "CC" (
    echo New image %5-%6 -> %8 >> %HOMEPATH%\dragonframe_script_log.txt
)

