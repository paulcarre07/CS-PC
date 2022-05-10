import os,sys,time

for i in range(len(sys.argv[1:])):
    os.fork()
    if os.fork() == 0:
        
        pid = os.getpid()
        ppid = os.getppid()
        if 1 == 1:
            os.execlp("python","python",sys.argv[i+1])
        time.sleep(2*i)
        sys.exit(i)
    pid_fils, etat = os.wait()
    


