import os

# execution en parallèle

pid1 = os.fork()
pid2 = os.fork()

if pid1 == 0:
    os.execlp("who","who")
if pid2 == 0:
    os.execlp("ps","ps")

os.execlp("ls","ls","-l")