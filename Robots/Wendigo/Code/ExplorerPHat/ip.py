#!/usr/bin/env python

#run at boot
#crontab -e
#@reboot python /home/pi/ip.py

import socket
from pushbullet import Pushbullet

api_key = open('/home/pi/APIConfigs/Pushbulletkey.config', 'r').read() #read Pushbullet Key from /home/pi/Pushbulletkey.config file
api_key = api_key.replace("\n", "") #Remove Whitespace
#print api_key
pb = Pushbullet(api_key) 

ipaddress = ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', $

#print ipaddress

ippush = "Wendigo IP: %s" % ipaddress
#print ippush

push = pb.push_note(ippush,ippush)
