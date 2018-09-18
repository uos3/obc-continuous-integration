#!/usr/bin/env bash

#if new one exists, git pull
cd ..
cd obc-firmware
git pull

#build
./build uos3-proto main >> log.txt

#flash
./flash >> log.txt

# move log
mv log.txt ../obc-continuous-integration/logs/log-toolchain.txt

# open screen and record
timeout 5s "screen -L /dev/ttyACM1 9600"
mv screenlog.0 ../obc-continuous-integration/logs/log-simulation.txt

# call front-end with log file
cd ../obc-continuous-integration
python front-end/main.py