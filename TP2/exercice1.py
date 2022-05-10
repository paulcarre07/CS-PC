import os,sys

pid = os.fork()

if pid == 0:
    os.execlp("python","python","/fs03/share/users/paul.carre/home/Documents/CS-PC/TP1/miroir.py", "DNA")

os.execlp("python","python","/fs03/share/users/paul.carre/home/Documents/CS-PC/TP1/miroir2.py", "troubadoure" , "trace")