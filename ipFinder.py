'''
ipFinder.py - prints local (internal) & public (external) IP address
By: Matt Conforti
06/10/21
'''


# imports -------
import subprocess


# main code -------
local_cmd = 'ipconfig getifaddr en0'  # en0 for wireless connection
public_cmd = 'curl -s ifconfig.me'
print(f"\nLocal IP: {subprocess.check_output(local_cmd, shell=True).decode('ascii')}")
print(f"Public IP: {subprocess.check_output(public_cmd, shell=True).decode('ascii')}\n")
