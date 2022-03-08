import PyInstaller.__main__
import shutil
import os

filename= "malicious.py"
exename= "begin.exe"
icon= "Firefox.ico"
pwd= os.getcwd
usbdir=os.path.join(pwd,"USB")

if os.path.isfile(exename):
    os.remove(exename)
#Create excutable from Python script
PyInstaller._main_.run([
    "malicious.py",
    "--onefile",
    "--clean",
    "--log-level-ERROR",
    "--name="+exename,
    "--icon="+icon
])
#Clean up after Pyinstaller
shutil.move(os.path.join(pwd,"dist",exename),pwd)
shutil.rmtree("dist")
shutil.rmtree("build")
shutil.rmtree("__pycache__")
os.remove(exename+".spec")