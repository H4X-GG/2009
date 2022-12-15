import os, sys 
print ("\t\033[1:35mChecking for Update")
os.system("git pull")
try:
    __import__("h4xgg").main()
except Exception as e:
    exit(str(e))
