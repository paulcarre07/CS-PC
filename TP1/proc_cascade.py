import imp


import os,sys

N=10
i =2
while os.fork()==0 and i<=N: #Création du fils
    i+=1
    print("je suis",os.getpid(), "et mon père est",os.getppid())
sys.exit(0)
