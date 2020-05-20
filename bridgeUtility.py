from paramiko import SSHClient, AutoAddPolicy
import sys
import socket
import threading
import sys
import time
from paramiko.py3compat import u

# windows does not have termios...
try:
    import termios
    import tty

    has_termios = True
except ImportError:
    has_termios = False


ssh_uname = "ubuntu"
ssh_pass = 'temppwd'
ssh_ip = "192.168.7.2" if sys.platform == "win32" else "192.168.6.2"
print(ssh_ip)

ssh = SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy)
ssh.load_system_host_keys('./keys')
ssh.connect(hostname=ssh_ip, username=ssh_uname, password=ssh_pass)

# ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('/home/ubuntu/.nvm/versions/node/v10.20.1/bin/node dev/node-can-bridge/client.js car')
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ls')
for line in ssh_stdout:
   print(line.strip('\n'))
for line in ssh_stderr:
   print(line.strip('\n'))

while True:
    time.sleep(0.2)
    pass