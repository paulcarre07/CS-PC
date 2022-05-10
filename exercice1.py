import os , sys # Communication par tube anonyme os.pipe()
msg = "messagePERE"
(dfr,dfw) = os.pipe()
pid = os.fork()
if pid != 0 : #Processus Père
    os.close(dfr)
    n = os.write(dfw , msg.encode())
    print ("Le processus %d:%d octets, message transmis est %s \n" %(os.getpid() , n , msg))
    os.close(dfw)
else : #Processus fils
    os.close(dfw)
    msgReception = os.read(dfr , len(msg))
    n = len(msgReception)
    print ("Le processus %d:%d octets, message recu est %s \n" %(os.getpid(), n, msgReception.decode()))
    os.close(dfr)
sys.exit(0)