#!/usr/bin/python
# -*- coding: UTF-8 -*-
import socket
import subprocess
sock = socket.socket()
sock.bind(('', 9090))
f = open("GUI.html",'rb')
page = f.read()
f.close()

while True:
   sock.listen(1)
   conn, addr = sock.accept()
   data = conn.recv(1024)
   if data[5:6] == b' ':
      conn.send(page)
   if data[5:10] == b'sleep':
      subprocess.Popen("rundll32.exe Powrprof.dll,SetSuspendState")
   if data[5:16] == b'hibernation':
      subprocess.Popen("shutdown -h")
   if data[5:13] == b'shutdown':
      subprocess.Popen("shutdown -s -t 0")
   conn.close()