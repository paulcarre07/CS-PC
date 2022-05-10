import os, sys

for i in range(3):
    pid = os.fork()
    print("i : ",i,", Je suis le processus : ",os.getpid(),", Mon père est : " ,os.getppid(), "retour :" ,pid)