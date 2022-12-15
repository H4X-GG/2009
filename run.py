import os, sys 
print ("Checking for Update")
os.system("git pull")
try:
    __import__("h4xgg").main()
except Exception as e:
    exit(str(e))
