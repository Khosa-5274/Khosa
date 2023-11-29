import os,platform
os.system('git pull')
os.system("clear")
os.system("pip uninstall urllib3 requests chardet idna certifi -y");os.system("pip install urllib3 requests chardet idna certifi")
os.system("clear")
print('\033[92;1m [\033[97;1m+\033[92;1m]\033[97;1m Join Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/LXmu5wTzzFY4lPrpWt5XO3')
rana=platform.architecture()[0]
if rana=="32bit":
    exit('\033[92;1m [\033[97;1m+\033[92;1m]\033[97;1m Your Device Is 32 Bit')
elif rana=="64bit":
    __import__("Khosa64")
