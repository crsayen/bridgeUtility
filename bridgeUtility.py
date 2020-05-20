try:
    import os
    import tkinter as tk
    from tkinter import messagebox
    import tkinter.ttk as ttk
    from tkinter import filedialog
except ImportError as e:
    print(e)
    import Tkinter as tk
    import ttk
    import tkFileDialog as filedialog
from paramiko import SSHClient, AutoAddPolicy
import sys
from paramiko.py3compat import u
try:
    import termios
    import tty
    has_termios = True
except ImportError:
    has_termios = False

ssh_uname = "ubuntu"
ssh_pass = 'temppwd'
ssh_ip = "192.168.7.2" if sys.platform == "win32" else "192.168.6.2"

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x100")
        self.root.title('bridge utility')
        self.startCarBtn = tk.Button(self.root, text="start with car config", command=self.startCar)
        self.startCarBtn.pack()
        self.startToolBtn = tk.Button(self.root, text="start with tool config", command=self.startTool)
        self.startToolBtn.pack()
        self.stopBtn = tk.Button(self.root, text="start", command=self.stop)
        self.stopBtn['state'] = 'disabled'
        self.stopBtn.pack()
        self.ssh = SSHClient()
        self.ssh.set_missing_host_key_policy(AutoAddPolicy)


    def startCar(self):
        self.ssh.connect(hostname=ssh_ip, username=ssh_uname, password=ssh_pass)
        self.ssh.exec_command('/usr/bin/python3.8 dev/node-can-bridge/enable_can.py')
        self.ssh.exec_command(f'/home/ubuntu/.nvm/versions/node/v10.20.1/bin/node dev/node-can-bridge/client.js car', get_pty=True)
        self.stopBtn['state'] = 'enabled'
        self.startCarBtn['state'] = 'disabled'
        self.startToolBtn['state'] = 'disabled'

    def startTool(self):
        self.ssh.connect(hostname=ssh_ip, username=ssh_uname, password=ssh_pass)
        self.ssh.exec_command('/usr/bin/python3.8 dev/node-can-bridge/enable_can.py')
        self.ssh.exec_command(f'/home/ubuntu/.nvm/versions/node/v10.20.1/bin/node dev/node-can-bridge/client.js tool', get_pty=True)
        self.stopBtn['state'] = 'enabled'
        self.startCarBtn['state'] = 'disabled'
        self.startToolBtn['state'] = 'disabled'
    
    def stop(self):
        self.ssh.close()
        self.ssh = SSHClient()
        self.stopBtn['state'] = 'disabled'
        self.startCarBtn['state'] = 'enabled'
        self.startToolBtn['state'] = 'enabled'

if __name__ == "__main__":
    App().root.mainloop()