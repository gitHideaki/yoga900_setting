#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import subprocess
from subprocess import PIPE, STDOUT, TimeoutExpired

# get input id
def get_input_id(monitor_name):
    cmd = "xinput list | grep '{}' | awk -F'[\t=]' '{{print $3}}'".format(monitor_name)
    proc = subprocess.Popen(cmd, shell=True, stdout=PIPE, stderr=STDOUT,text=True)
    outs,err = proc.communicate()
    id = outs.rstrip()
    return id

# check monitor-sensor and monitor rotate
def monitor_rotate(monitor_name):

    # check word of monitor-sensor
    check_word = "Accelerometer orientation changed:"
  
    # monitor_rotate
    cmd = "/usr/bin/monitor-sensor"
    proc = subprocess.Popen(cmd, shell=True, stdout=PIPE, stderr=STDOUT,text=True)
    
    while True:
        monitor_status = proc.stdout.readline()
        
        if "normal" in monitor_status:
            id = get_input_id(monitor_name)
            monitor_rotate_cmd = \
            "/usr/bin/xrandr -o normal " \
            "&& " \
            "xinput set-prop {} 'Coordinate Transformation Matrix' 1 0 0 0 1 0 0 0 1".format(id)
            subprocess.Popen(monitor_rotate_cmd, shell=True, stdout=PIPE, stderr=STDOUT,text=True)
        elif "bottom-up" in monitor_status:
            id = get_input_id(monitor_name)
            monitor_rotate_cmd = \
            "/usr/bin/xrandr -o inverted " \
            "&& " \
            "xinput set-prop {} 'Coordinate Transformation Matrix' -1 0 1 0 -1 1 0 0 1".format(id)
            subprocess.Popen(monitor_rotate_cmd, shell=True, stdout=PIPE, stderr=STDOUT,text=True)
            
if __name__ == '__main__':
    monitor_name = "<input_id>"
    monitor_rotate(monitor_name)
