import time,signal,sys,os

def fin(s , frame) :
    print("SIGINT pour processus %d" %os.getpid() )
    sys.exit(1)

#signal.signal(signal.SIGQUIT,signal.SIG_IGN)
signal.signal(signal.SIGINT,fin)

while True:
    time.sleep(2)
    print("Hello World")
