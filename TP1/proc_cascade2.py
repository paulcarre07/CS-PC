import os,sys

N=4
for i in range(N):
    pid =os.fork()
    if pid == 0: 
        print("je suis",os.getpid(),"mon père est",os.getppid())
        break
sys.exit(0)