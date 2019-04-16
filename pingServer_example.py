import os
hostname = "dir.bg" #example
response = os.system("ping -n 1 " + hostname)

#and then check the response...
if response == 0:
  print(hostname, 'is up!')
else:
  print(hostname, 'is down!')
# -----------------------------------------------
import pyping

r = pyping.ping('dir.bg')

if r.ret_code == 0:
    print("Success")
else:
    print("Failed with {}".format(r.ret_code))
# -----------------------------------------------
import subprocess

host = "dir.bg"

ping = subprocess.Popen(
    ["ping", "-n", "1", host],
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE
)

out, error = ping.communicate()
print(out)
# -----------------------------------------------

import platform    # For getting the operating system name
import subprocess  # For executing a shell command

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """
# Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

# Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0 
# -----------------------------------------------

# -----------------------------------------------