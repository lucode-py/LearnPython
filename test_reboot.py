import os
import signal
import subprocess

def reboot():
    command = "pgrep Python"
    pid = subprocess.check_output(command, shell=True)

    os.kill(int(pid), signal.SIGTERM)
    with open('mac/sortie.txt', 'w') as fichier_sortie:
        subprocess.Popen(['python3', "playground_windows.py"], stdout=fichier_sortie, stderr=subprocess.STDOUT)

while True:
    cmd = input(">>> ")
    if cmd == "reboot":
        reboot()
