echo off
set target=%1
set username=%2
set password=%3


%~dp0plink.exe %2@%1 -batch -pw %3 -m %~dp0commands.txt
%~dp0pscp.exe -r -pw %3 %~dp0* %2@%1:/home/pi/SenseHatPatterns

echo Deployment complete.