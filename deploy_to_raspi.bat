echo off
set target=%1
set username=%2
set password=%3

REM Cleanup and recreate project folder
%~dp0plink.exe %2@%1 -batch -pw %3 -m %~dp0commands_folder.txt
REM Transfer files
echo Starting file transfer...
%~dp0pscp.exe -r -pw %3 %~dp0* %2@%1:/home/pi/SenseHatPatterns
echo File transfer complete.
REM Make scripts executable and execute
%~dp0plink.exe %2@%1 -batch -pw %3 -m %~dp0commands_exec.txt
timeout /T 2  > nul
%~dp0plink.exe %2@%1 -batch -pw %3 -m %~dp0commands_start.txt

echo Deployment complete.