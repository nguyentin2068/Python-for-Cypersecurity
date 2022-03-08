import os, winreg

def readPathValue (reghive, regpath) :
    reg = winreg.connectRegistry (None, reghive)
    key = winreg.Openkey (reg, regpath, access=winreg.KEY_READ)
    index = 0
    while True:
        val = winreg. Enumvalue (key, index)
        if val [0] == "Path":
            return val[1]
        index += 1
def editPathvalue (reghive, regpath, targetdir):
    path = readPathValue (reghive, regpath)
    newpath = targetdir + ";" + path
    reg = winreg.ConnectRegistry (None, reghive)
    key = winreg.Openkey (reg, regpath, access=winreg. KEY_SET_VALUE)
    winreg.SetvalueEx (key, "Path",0,winreg.REG_EXPAND_SZ,newpath)

# Modify user path
reghive = winreg.HKEY_CURRENT_USER
regpath = "Environment"
targetdir = os.getcwd ()
editPathvalue (reghive, regpath, targetdir)


# Modify SYSTEM path
#treghive= winreg.HKEY LOCAL MACHINE
#regpath = "SYSTEM\Currentcontrolset\Control\Session Manager\Environment"
#editPathvalue (reghive, regpath, targetdir)