import os, sys
n=0
for i in range(1,5) :
    fils_pid = os.fork() #1
    if (fils_pid > 0) : #2 dans le père, algo déterministe il affichera n = 0 ; n = 8; n = 6; n = 4; n = 2;
        os.wait() #3 il est encore déterministe mais il ne s'execute pas dans le meme ordre
        n = i*2
        break;
print("n = ", n) #4
sys.exit(0)