import os



cmd = 'vncserver -kill :1'

os.system(cmd)

cmd = 'vncserver -kill :2'  

os.system(cmd)

cmd = 'rm -rf /tmp/.X1-lock'

os.system(cmd)

cmd = 'rm -rf /tmp/.X11-unix/X1'  

os.system(cmd)
