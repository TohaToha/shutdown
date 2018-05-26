import socket
import subprocess
sock = socket.socket()
sock.bind(('', 9090))
f = open("test.html",'rb')
page = f.read()
f.close()

while True:
   sock.listen(1)
   conn, addr = sock.accept()
   data = conn.recv(1024)
   if data[5:10] == b'sleep':#sleep
      subprocess.Popen("rundll32.exe Powrprof.dll,SetSuspendState")
   if data[5:16] == b'hibernation':#hibernation
      subprocess.Popen("shutdown -h")
   if data[5:13] == b'shutdown':
      subprocess.Popen("shutdown -s -t 0")
   if data[5:9] == b'help':
      text = b'Available commands >>> sleep, hibernation, shutdown'
      conn.send(text + b' ' * (1024-len(text)))
   if data[5:9] == b'test':
      conn.send(page)
   conn.close()