#!/usr/bin/sh
pkill -f avatar.py
sleep 3
nohup python3.10 avatar.py > logs/nohup.log &
