import os,sys

(dfr,dfw) = os.pipe()
pid = os.fork()

if pid == 0:
    os.close(dfr)
    os.dup2(dfw,1)
    os.close(dfw)
    os.execlp("cat","cat","exercice1.py")


else:
    os.close(dfw)
    os.dup2(dfr,0)
    os.close(dfr)
    os.execlp( "wc","wc")

sys.exit(0)