REM @echo off
set target=%1
set username=%2
set password=%3

REM ssh %2@%1
%~dp0plink.exe -batch -pw password username@target sudo su - < mkdir /home/pi/sense

%~dp0plink.exe %2@%1 -batch -pw -t %3 "echo %3 | sudo -S rm -r /home/pi/sense"
%~dp0plink.exe %2@%1 -batch -pw -t %3 "echo %3 | sudo -S mkdir /home/pi/sense"
REM Now we are in linux scope

REM Now back in windows scope

REM start /d "" .\pscp.exe -pw %3 %2"@"%1
%~dp0pscp.exe -r -pw %3 %~dp0* %2@%1:/home/pi/sense/