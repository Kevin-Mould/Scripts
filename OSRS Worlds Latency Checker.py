import os, subprocess, re
for i in range(1, 195):
    hostname = "oldschool"+ str(i)+".runescape.com"
    ping = subprocess.Popen(["ping", hostname, "-n", "1"], stdout = subprocess.PIPE,stderr = subprocess.PIPE, shell=True)
    output = ping.communicate()
    pattern = r"Average = (\d+\S+)"
    world = i+300
    print("World: " + str(world) + " " + re.findall(pattern, output[0].decode())[0])
