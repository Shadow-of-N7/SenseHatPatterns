#!/bin/bash

for entry in "/home/pi/SenseHatPatterns/sensehat"/*
do
  pkill -f "$entry"
done

