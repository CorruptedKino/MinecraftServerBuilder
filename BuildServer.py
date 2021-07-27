# Libraries
import os
import time
from pathlib import Path
# Variables
eula_found = 0

# Function
if os.path.isfile("server.jar") == False:
    input('Server file not found if the file is in make sure its named "server.jar"\nRestart the program once its been added or renamed')

if os.path.isfile("server.jar") == True:
    start = open("start.bat", "x")
    print("Creating Start File")
    time.sleep(1)
    start.write("java -Xmx1024M -Xms1024M -jar server.jar nogui")
    start.close()

    os.startfile("start.bat")
    print("Running start")

    while os.path.isfile("eula.txt") == False:
        time.sleep(3)
        eula_found += 1

    if eula_found < 5:
        print("EULA found")

    allow_eula = input("Do you accept the Minecraft server eula?\nType yes if you want to proceed and type anything else if you want to cancel\nhttps://account.mojang.com/documents/minecraft_eula\n")
    
    if allow_eula == "yes":
        eula = open("eula.txt", "w")
        eula.write("eula=true")
        eula.close
        input("Please run the start file again so that the rest of the files can be created\nOnce its run, your server should start up. Have fun!\n")    