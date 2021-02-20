#!/usr/bin/env python3

from datetime import datetime
import subprocess
import socket


username = 'blah'
UDP_IP = "192.168.0.43"
UDP_PORT = 3333
endpoints = ["192.168.0.2", "192.168.0.43"]
 
 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
 
while True:
    data, addr = sock.recvfrom(1024)
    print(f'Knock received at {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    for endpoint in endpoints:
        print('Ringing on machine {endpoint}...')
        subprocess.call(['ssh', f'{username}@{endpoint}', 'espeak', '"Ding dong, someone at the door!"'])
    

